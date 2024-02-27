import requests


query = {'san%20francisconTMqu': '', 'lang': 'ru'}


def weather(query):
    url = (f'http://wttr.in')
    response = requests.get(url, params=query)
    print(response.raise_for_status)
    print(response.text)


def main():
    weather(query)


if __name__ == '__main__':
    main() 