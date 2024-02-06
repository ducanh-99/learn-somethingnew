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
    synonyms: str
    ipa: str


# Load environment variables from .env file
# Get the Notion integration token from environment variables
token = os.getenv('NOTION_TOKEN')


def main():
    print("Please input your word")
    word = input()
    word = word.lower()
    print("Your word", word)
    endpoint_dictionary = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(endpoint_dictionary)

    if response.status_code != 200:
        print(f"Error, can not get this word ${word} , {response.text}")
        return
    word_response: List[Word] = response.json()
    for i in range(0, len(word_response)):
        w = word_response[i]
        word_response[i] = Word.model_validate(w)

    word_notion: List[NotionField] = []
    for w in word_response:
        new_word = NotionField(
            name=w.word,
            type_of_word=[meaning.partOfSpeech for meaning in w.meanings],
            definition="\n".join(["\n".join(
                [definition.definition for definition in meaning.definitions]) for meaning in w.meanings]),
            synonyms="\n".join(["\n".join(meaning.synonyms)
                               for meaning in w.meanings]),
            ipa="\n".join([phonetic.text for phonetic in w.phonetics])
        )
        word_notion.append(new_word)

    print(word_notion)

    # Database ID where you want to create a new record (page)
    database_id = '63eefad1dd0f49f280cfe46bee8858e2'

    # Notion API endpoint for creating a new page (record)
    endpoint = 'https://api.notion.com/v1/pages'

    # JSON data for the new record (page) you want to create
    for notion_field in word_notion:
        # JSON data for the new page (record) you want to create
        new_record_data = {
            "parent": {
                "database_id": database_id
            },
            "properties": {
                "name": {
                    "title": [
                        {
                            "text": {
                                "content": notion_field.name
                            }
                        }
                    ]
                },
                "Type Of word": {
                    "multi_select": [{"name": type_of_word} for type_of_word in notion_field.type_of_word]
                },
                "Definition": {
                    "rich_text": [
                        {
                            "text": {
                                "content": notion_field.definition
                            }
                        }
                    ]
                },
                "Synonyms": {
                    "rich_text": [
                        {
                            "text": {
                                "content": notion_field.synonyms
                            }
                        }
                    ]
                },
                "IPA": {
                    "rich_text": [
                        {
                            "text": {
                                "content": notion_field.ipa
                            }
                        }
                    ]
                }
            }
        }

        # Headers including the integration token
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Notion-Version': '2021-05-13'
        }

        # Make a POST request to create the new record (page)
        response = requests.post(
            endpoint, headers=headers, json=new_record_data)

        # Check if the request was successful
        if response.status_code == 200:
            print("New record (page) created successfully.")
        else:
            print("Error:", response.text)


if __name__ == "__main__":
    main()
