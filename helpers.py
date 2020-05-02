# MIT License
#
# Copyright (c) 2020 Korkmatik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import random

from mySpecials import compliments # List of strings with compliments
from mySpecials import itachi_quotes # List of strings with itachi's quotes

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


def get_random_itachi_quote():
    index = random.randint(0, len(itachi_quotes) - 1)
    return itachi_quotes[index]
