import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data=json.load(open("data.json"))

def translate(qry):
    if qry in data:
        return data[qry]
    elif len(get_close_matches(qry,data.keys())) > 0 :
        closest_word=get_close_matches(qry,data.keys(),1)[0]
        yn=input("do you mean %s ?\n Press 'Y' if yes or 'N' if it isn't \n" %closest_word)
        if yn.lower()=="y":
            return data[closest_word]
        else:
            return "Then this word doesnt exist sorry"
    else:
        return "The word doesnt exist, sorry"

qry=input("Enter the word you want to search? \n")
qry=qry.lower()
output=translate((qry))

if type(output) == list:
    for x in output:
        print(x)
else:
    print(output)
