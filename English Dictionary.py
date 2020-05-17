import json             # json is a built in package in Python
from difflib import get_close_matches   #difflib is a module which provides classes & function for comparing two sequence
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]  #if the first letter of the word is Capital
    elif w.upper() in data:
        return data[w.upper()]    #if all the letter are capital letter ex:USA
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? If yes enter 'Y' or if no enter 'N' : "%get_close_matches(w,data.keys()[0]))
        if yn == "Y":
            return get_close_matches(w,data.keys()[0])
        elif yn == "N":
            return "The word doesn't exist.Please double check it "
        else:
            return "Sorry! we didn't understand your entry "
    else:
        return "The word doesn't exist.Please double check it "
word = input("Enter your word : ")
output = translate(word)
print(output)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
