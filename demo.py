import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif get_close_matches(w,data.keys())[0].title() == word:
        return data[w.title()]
    elif word.upper() in data:
        return data[w.upper()] 
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s, Enter Y/N for Yes or No respectively: " % get_close_matches(w,data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "The word doesn't exist, Please try agian"
        else:
            return "We didn't understand that!!"
    else:
        return "The word does not exist. Please retry!"

word = input("Enter a word: ")

output = find(word)

if type(output) == list:    
    for w in output:
        print(w)
else:
    print(output)