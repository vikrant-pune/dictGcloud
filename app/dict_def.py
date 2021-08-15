import sys


class dictCloud:

    def __init__(self):
        api_key = ""
        url = ""

    def getDefination(self, word: str) -> list:
        """

        :param word: Input string to get word definitions
        :return: array of string with multiple definitions
        """

        return [f"Getting defination of {word}"]


def getUserIp():
    myDict = dictCloud()
    exit = False
    while not exit:
        word = input("Enter word :")

        if word.strip() == "bye":
            # print("BBye!")
            sys.exit("BBye!")

        definitions = myDict.getDefination(word.strip())

        for definition in definitions:
            print(definition)


if __name__ == '__main__':

    getUserIp()