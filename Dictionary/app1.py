import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
	    return data[w]
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	elif len(get_close_matches(w, data.keys())) >0:
		yn = raw_input("did you mean %s instead, press Y for yes or N for no" % get_close_matches(w, data.keys())[0])
		if yn == "Y":
		    return data[get_close_matches(w,data.keys())[0]]
		elif yn == "N":
		    return "Not sure if you entered the right word"
		else:
			return "Try again"
	else:
		return "exiting"

word = raw_input("enter the word: ")
output = translate(word)
if type(output) == list:
    for item in output:
	  print(item)
else:
	print(output)
	
	