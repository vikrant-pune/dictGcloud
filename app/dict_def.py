"""
 Get user input and call API to get defination
 """
import sys
import os
from dotenv import load_dotenv

import requests


class DictCloud:
    """
        Stores information about API keys and urls
    """

    def __init__(self):
        self.config = load_dotenv()
        self.api_key = os.environ.get("API_KEY")
        self.url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"

    def get_definition(self, word: str) -> list:
        """
            Get Definition from wordpress
        :param word: Input string to get word definitions
        :return: array of string with multiple definitions
        """

        response = requests.get(url=(self.url + word.strip()), params={"key": self.api_key})
        definitions = []

        resp = response.json()

        for word_ in resp:
            definitions = definitions + word_.get("shortdef")

        return definitions


def get_user_ip():
    """
    Get user word and shows it's definition
    :return:
    """
    my_dict = DictCloud()
    exit_val = False
    while not exit_val:
        word = input("Enter word :")

        if word.strip() == "bye":
            sys.exit("BBye!")

        definitions = my_dict.get_definition(word.strip())

        num = 1
        for definition in definitions:
            print(f"{num}. " + definition)
            num += 1


if __name__ == '__main__':
    get_user_ip()
