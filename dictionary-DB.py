import mysql.connector
from difflib import get_close_matches

#Connecting to database
my_DB = mysql.connector.connect(
user = "ardit700_student",
passwd = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

#Below 3 lines gets the keys from the DB and stores in keys variable
my_cursor = my_DB.cursor()
query_key = my_cursor.execute("SELECT Expression FROM Dictionary")
keys = my_cursor.fetchall()
#Below 3 lines gets the data from key(a list of tuples) and converts to key_list(a list of string)
keys_list = []

for data in keys:
    keys_list.append(data[0])

def word_finder(word):
    #This if block checks the DB for the word entered in any CASE(upper,lower,title etc)
    if word in keys_list:
        #Below 2 line code gets the definition for the searches word from DB
        query = my_cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = my_cursor.fetchall()
        output = []
        for data in results:
            output.append(data[0])
        return output
    #Below if block checks for the word in DB in lower case as most of the words are in lower case
    elif word.lower() in keys_list:
        word = word.lower()
        return word_finder(word)
    #Below if block checks and gives words suggestion if the enteres word seems similar to some word
    elif len(get_close_matches(word, keys_list, cutoff =0.8))>0:
        new_word = get_close_matches(word, keys_list, cutoff = 0.8)[0]
        user_option = input("Did you mean '%s'? Enter [Y] for yes, [N] for no: " % new_word)
        #Below line converts the user enter string to lower to cover all the format entered by user
        user_option = user_option.lower()
        if user_option in ["y","yes",]:
            return word_finder(new_word)
        elif user_option in ["n","no"]:
            return "Word does not exist"
        else:
            print("Error: You entered a option which the system could not understand, hence exiting . . ")
            return "Error"
    else:
        return "Word does not exist"
        

word = input("Please enter the word: ")
data_from_func = (word_finder(word))
final_output = []

#The below condition is needed. If we do not use this, when the word does not exist, the letters of the output "Word does not exist" is printed in each line
if isinstance(data_from_func,list):
    for data in data_from_func:
        print(data)
else:
    print(data_from_func)