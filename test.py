import requests


symbols = [
    'bsc_0x111111111117dc0aa78b770fa6a738034120c302',
    'bsc_0xc5f0f7b66764f6ec8c8dff7ba683102295e16409',
    'bsc_0x170c84e3b1d282f9628229836086716141995200',
    'bsc_0x4691937a7508860f876c9c0a2a617e7d9e945d4b',
    'bsc_0x4ace5cdb2aa47d1b2b8e4c4ca01bf6850a4b87b5',
    'bsc_0x76f3ce6af26de7a9854dbd153acd8f46a2cf5133',
    'bsc_0x912ce59144191c1204e64559fe8253a0e49e6548',
    'bsc_0xcc42724c6683b7e57334c4e856f4c9965ed682bd',
    'bsc_0x352cb5e19b12fc216548a2677bd0fce83bae434b',
    'bsc_0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63',
    'bsc_0x90c97f71e18723b0cf0dfa30ee176ab653e89f40',
    'bsc_0xb86abcb37c3a4b64f74f59301aff131a1becc787',
    'eth_0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0',
    'bsc_0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe',
    'bsc_0xd4ed60d8368a92b5f1ca33af61ef2a94714b2d46',
    'bsc_0x1ce0c2827e2ef14d5c4f29a091d735a204794041',
    'bsc_0xf307910a4c7bbc79691fd374889b36d8531b08e3',
    'bsc_0x55d398326f99059fF775485246999027B3197955',
    'bsc_0xce7de646e7208a4ef112cb6ed5038fa6cc6b12e3',
    'bsc_0xf8a0bf9cf54bb92f17374d9e9a321e6a111a51bd',
    'bsc_0x031b41e504677879370e9dbcf937283a8691fa7f',
    'bsc_0xd41fdb03ba84762dd66a0af1a6c8540ff1ba5dfb',
    'bsc_0x4b0f1812e5df2a09796481ff14017e6005508003',
    'bsc_0x55d398326f99059ff775485246999027b3197955',
    'bsc_0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c',
    'arbitrum_0xcafcd85d8ca7ad1e1c6f82f651fa15e33aefd07b',
    'bsc_0x76a797a59ba2c17726896976b7b3747bfd1d220f',
    'bsc_0xbda011d7f8ec00f66c1923b049b94c67d148d8b2',
    'eth_0x582d872a1b094fc48f5de31d3b73f2d9be47def1',
    'bsc_0x47bead2563dcbf3bf2c9407fea4dc236faba485a',
    'eth_0x4691937a7508860f876c9c0a2a617e7d9e945d4b',
    'bsc_0x92ed61fb8955cc4e392781cb8b7cd04aadc43d0c',
    'arbitrum_0x11f98c7e42a367dab4f200d2fdc460fb445ce9a8',
]
url = 'https://api-test2.attlas.io/api/v1/dexswap/token_info'
for symbol in symbols:
    params = {'symbol': symbol, 'baseCurrency': "VNDC"}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Process the 'data' variable containing the response JSON as needed
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
