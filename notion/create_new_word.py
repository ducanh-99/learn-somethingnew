import os
import requests
from dotenv import load_dotenv
from typing import List, Optional
from pydantic import BaseModel

load_dotenv()


class License(BaseModel):
    name: str
    url: str


class Phonetic(BaseModel):
    text: Optional[str] = ''
    audio: Optional[str] = ''
    sourceUrl: Optional[str] = ''
    license: Optional[License] = ''


class Definition(BaseModel):
    definition: str
    synonyms: Optional[List[str]]
    antonyms: Optional[List[str]]
    example: Optional[str] = ''


class Meaning(BaseModel):
    partOfSpeech: str
    definitions: Optional[List[Definition]]
    synonyms: Optional[List[str]]
    antonyms: Optional[List[str]]


class Word(BaseModel):
    word: str
    phonetics: Optional[List[Phonetic]]
    meanings: Optional[List[Meaning]]
    license: Optional[License]
    sourceUrls: Optional[List[str]]


class NotionField(BaseModel):
    name: str
    type_of_word: List[str]
    definition: str
    synonyms: str = ''
    antonyms: str = ''
    ipa: str
    audio: Optional[str]
    examples: Optional[str]


# Load environment variables from .env file
# Get the Notion integration token from environment variables
token = os.getenv('NOTION_TOKEN')


def fetch_word_data(word: str) -> List[Word]:
    endpoint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(endpoint)

    if response.status_code == 200:
        return [Word(**w) for w in response.json()]
    else:
        print(f"Error, can not get this word {word}, {response.text}")
        return []


def create_notion_fields(word_response: List[Word]) -> List[NotionField]:
    notion_fields = []
    for word in word_response:
        definitions = "\n".join(
            ["\n".join([d.definition for d in m.definitions]) for m in word.meanings])
        examples = []
        for m in word.meanings:
            example = "\n".join(
                [d.example for d in m.definitions if d.example])
            if example:
                examples.append(example)
        examples = "\n".join(examples)
        synonyms = "\n".join(["\n".join(
            [synonym for synonym in m.synonyms if synonym != '']) for m in word.meanings if m.synonyms])

        antonyms = "\n".join(["\n".join(
            [antonym for antonym in m.antonyms if antonym != '']) for m in word.meanings if m.antonyms])
        ipa = "\n".join(
            list(set([p.text for p in word.phonetics if p.text != ''])))
        audio = [p.audio for p in word.phonetics if p.audio != '']
        notion_fields.append(NotionField(
            name=word.word,
            type_of_word=[m.partOfSpeech for m in word.meanings],
            definition=definitions,
            synonyms=synonyms,
            antonyms=antonyms,
            ipa=ipa,
            audio=audio[0] if len(audio) > 0 else '',
            examples=examples
        ))
    return notion_fields


def create_notion_record(notion_field: NotionField, database_id: str, endpoint: str, token: str) -> None:
    new_record_data = {
        "parent": {"database_id": database_id},
        "properties": {
            "name": {"title": [{"text":
                                {"content": notion_field.name},
                                "annotations": {
                                    "link": {
                                        "url": notion_field.audio
                                    }
                                }}
                               ]
                     },
            "Type Of word": {"multi_select": [{"name": type_of_word} for type_of_word in notion_field.type_of_word]},
            "Definition": {"rich_text": [{"text": {"content": notion_field.definition}}]},
            "Synonyms": {"rich_text": [{"text": {"content": notion_field.synonyms}}]},
            "Antonyms": {"rich_text": [{"text": {"content": notion_field.antonyms}}]},
            "IPA": {"rich_text": [{"text": {"content": notion_field.ipa}}]},
            "Example Sentence": {"rich_text": [{"text": {"content": notion_field.examples}}]},
        },
        "children": [
            {
                "object": "block",
                "type": "embed",
                        "embed": {
                            "url": notion_field.audio
                        }
            }
        ]
    }
    headers = {'Authorization': f'Bearer {token}',
               'Content-Type': 'application/json', 'Notion-Version': '2021-05-13'}
    response = requests.post(endpoint, headers=headers, json=new_record_data)
    if response.status_code == 200:
        print("New record (page) created successfully.")
    else:
        print("Error:", response.text)


def main():
    print("Please input your word")
    word = input().lower()
    print("Your word", word)
    word_response = fetch_word_data(word)
    if word_response:
        notion_fields = create_notion_fields(word_response)
        database_id = '63eefad1dd0f49f280cfe46bee8858e2'
        endpoint = 'https://api.notion.com/v1/pages'
        for notion_field in notion_fields:
            create_notion_record(notion_field, database_id, endpoint, token)
            pass


if __name__ == "__main__":
    main()
