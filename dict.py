
import json
from difflib import get_close_matches
data = json.loads(open('dictionary.json').read())


def definition(name):
    name = name.lower()

    if name in data:
        return data[name]

    elif len(get_close_matches(name, data.keys())) > 0:
        check = input("Did you mean %s instead? Enter Y if yes, otherwise N to exit: " %
                      get_close_matches(name, data.keys())[0])
        if check == "Y":
            return data[get_close_matches(name, data.keys())[0]]
        elif check == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "Sorry, this word is not an English word. Please double check your spelling."


word = input('Enter a name: ')
output = definition(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

