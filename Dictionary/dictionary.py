import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def word_finder(word):
    word = word.lower()                                 #This will convert all the entered word in lowercase so that all the posibilities entered by user is checked
    if word in data.keys():
        output = data[word]
        print("Here is your definition of %s:\n" % word)
        return output
    elif len(get_close_matches(word, data.keys(), cutoff=0.7)) > 0:
        user_option = input("Did you mean %s instead? Enter [Y] for yes, [N] for no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        new_word = get_close_matches(word, data.keys(), cutoff=0.8)[0]
        if user_option == "Y":
            return word_finder(new_word)
        elif user_option == "N":
            return "Word does not exist. Please double check."
    else:
        return "Word does not exist. Please double check."

user_input = input("Enter a word: ")
function_output = word_finder(user_input)

if isinstance(function_output,list):
    for item in function_output:
        print(item)
else:
    print(function_output)