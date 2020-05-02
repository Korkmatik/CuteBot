import random

from mySpecials import compliments # List of strings compliments


def read_secrets():
    """
    File format:
        - First Line contains the bot token
        - Second Line contains the server ID
    """

    with open("token.txt", "r") as f:
        lines = f.readlines()
        bot_token = str(lines[0].strip())
        server_id = int(lines[1].strip())

    return bot_token, server_id


def get_random_compliment():
    index = random.randint(0, len(compliments)-1)
    return compliments[index]
