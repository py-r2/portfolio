import json
from difflib import get_close_matches

dict = json.load(open('.\\data_files\\data.json'))

def translate(w):

#    for item in dict:
        if w in dict.keys():
            return dict[w]
#            for elem in dict[w]:
#                print "-" + elem
#        elif w.title() in dict[w]:
#            for elem in dict[item]:
#                print "-" + elem
        elif len(get_close_matches(w, dict.keys())) > 0:
            resp = raw_input("Did you mean: %s. Please respond with Y or N:" % get_close_matches(w, dict.keys())[0])
            if resp.lower() == 'y':
                return dict[get_close_matches(w, dict.keys())[0]]
            else:
                print "This word doesn't exist1."
        else:
            print "This word doesn't exist2."

word = raw_input('Enter word:')
output = translate(word)

if type(output) == list:
    for elem in output:
        print "-" + elem
else:
    print output
