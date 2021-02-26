
def findWord(dict, str, out=""):

    # The end of string is reached, print output string from dict
    if not str:
        print(out)
        return

    for i in range(1, len(str) + 1):
        # Looping every possibility of combination
        word = str[:i]

        # if the word is in the dictionary, add it to the output string and call the method again
        # to print the out number
        if word in dict:
            findWord(dict, str[i:], out + " " + word)


if __name__ == '__main__':

    dict = [
        'pro', 'gram', 'merit',
        'program', 'it', 'programmer'
    ]

    str = "programmerit"

    findWord(dict, str)
