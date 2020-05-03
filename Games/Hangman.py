import random


class Hangman:

    HANGMAN_PIC = ""
    IS_RUNNING = False

    HANGMAN_WORD = ""

    CORRECT = []
    WRONG = []

    WORDLISTS = [
        "programming", "casual"
    ]

    @staticmethod
    def get_message(command):
        if "!start" in command.lower():
            if not Hangman.IS_RUNNING:
                wordlist = command.lower().split()[1]
                if wordlist not in Hangman.WORDLISTS:
                    return "I could not find the specified wordlist. Enter `!wordlists` to see all available wordlists"

                return Hangman.__start(wordlist)
            else:
                return "A game is currently running. Type `!restart` to restart the game."
        elif "!restart" in command.lower():
            if not Hangman.IS_RUNNING:
                return "No game is currently running. Type `!start` to start a new game."

            wordlist = command.lower().split()[1]
            if wordlist not in Hangman.WORDLISTS:
                return "I could not find the specified wordlist. Enter `!wordlists` to see all available wordlists"

            return Hangman.__start(wordlist)
        elif command == "!stop":
            Hangman.IS_RUNNING = False
            return "Game stopped."
        elif "!letter" in command.lower():
            if not Hangman.IS_RUNNING:
                return "The game is not running! Please start the game! (Command: `!start`)"

            letter = command.lower().split()[1]
            if len(letter) > 1:
                return "This is not a letter!"

            if letter in Hangman.HANGMAN_WORD:
                if letter not in Hangman.CORRECT:
                    Hangman.CORRECT.append(letter)
                    return Hangman.__status("Correct", letter)
                else:
                    return Hangman.__status("You already tried that letter! That letter was right!!", letter)
            else:
                if letter not in Hangman.WRONG:
                    Hangman.WRONG.append(letter)
                    return Hangman.__status("Incorrect", letter)
                else:
                    return Hangman.__status("You already tried that letter! That letter was wrong!!", letter)
        elif command.lower() == "!wordlists":
            msg = "```Available wordlists:\n\n"
            for w in Hangman.WORDLISTS:
                msg += w + "\n"

            msg += "\n```"

            return msg
        elif "!word" in command.lower():
            if not Hangman.IS_RUNNING:
                return "The game is not running! Please start the game! (Command: `!start`)"

            word = command.lower().split()[1]

            if word == Hangman.HANGMAN_WORD:
                for l in word:
                    Hangman.CORRECT.append(l)
                return Hangman.__status("You are amazing!", None)
            else:
                Hangman.WRONG.append(word)
                return Hangman.__status("Nice try, but it isn't right （；´д｀）ゞ", None)
        elif command.lower() == "!help":
            msg = "```The Hangman Game:\n\n"
            msg += "!start [wordlist]     Starts the game\n"
            msg += "!restart [wordlist]   Restarts a running game\n"
            msg += "!wordlists            Prints all available wordlists\n"
            msg += "!stop                 Stops a running game\n"
            msg += "!letter [char]        Type this during a running game if you want to try a letter\n"
            msg += "!word [word]          Type this during a running game if you want to try a word\n"

            msg += "```"

            return msg

    @staticmethod
    def __start(wordlist):
        Hangman.HANGMAN_PIC = ""
        Hangman.IS_RUNNING = True

        if wordlist == "programming":
            Hangman.HANGMAN_WORD = random.choice(programming_words)
        elif wordlist == "casual":
            Hangman.HANGMAN_WORD = random.choice(words)

        return Hangman.__status("Started game! GL HF!", None)

    @staticmethod
    def __status(status, letter):
        msg = f"```{status}!"

        if letter is not None:
            msg += f" (Letter: {letter})"

        msg += "\n"

        msg += "\n"
        if len(Hangman.WRONG) < len(HANGMAN_PICTURES):
            msg += HANGMAN_PICTURES[len(Hangman.WRONG)]
        else:
            msg += HANGMAN_PICTURES[-1]
        msg += "\n\n"
        msg += "Word:\n"

        for i in range(len(Hangman.HANGMAN_WORD)):
            word_letter = Hangman.HANGMAN_WORD[i]

            if word_letter in Hangman.CORRECT:
                msg += " " + word_letter + " "
            else:
                msg += " _ "

        msg += "\n\nWrong:\n"
        for w in Hangman.WRONG:
            msg += f" {w} "

        # Checking if won or game over
        if len(Hangman.CORRECT) >= len(set(Hangman.HANGMAN_WORD)):
            Hangman.IS_RUNNING = False
            msg += "\n\nYOU WON!"
        elif len(Hangman.WRONG) == len(HANGMAN_PICTURES):
            Hangman.IS_RUNNING = False
            msg += "\n\nGAME OVER!"
            msg += f"\nThe word was: {Hangman.HANGMAN_WORD}"

        msg += "```"

        return msg


# Got this from "https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c"
HANGMAN_PICTURES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

programming_words = [
    "algorithm", "program", "api", "argument", "ascii",
    "boolean", "bug", "char", "objects", "oop",
    "class", "code", "cli", "compilation", "compiler",
    "conditionals", "constants", "data", "array", "declaration",
    "exception", "expression", "framework", "hardcode", "loop",
    "loop", "iteration", "keyword", "null", "operand", "operator",
    "variable", "pointer", "language", "machine", "markup", "package",
    "runtime", "backend", "server", "source" , "statement", "syntax",
    "token", "java", "python", "c", "haskel", "flask", "django",
    "bash", "powershell", "devops", "uml", "linux", "docker", "yaml",
    "json", "hardware", "software", "computer"
]

