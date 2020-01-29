import mysql.connector
from difflib import get_close_matches

my_DB = mysql.connector.connect(
user = "ardit700_student",
passwd = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

my_cursor = my_DB.cursor()

query_key = my_cursor.execute("SELECT Expression FROM Dictionary")
keys = my_cursor.fetchall()
#print(keys)

def word_finder(word):
    print(keys[0:10])
    if word in keys:
        query = my_cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = my_cursor.fetchall()
        for i in results:
            print(i[0])
        return ""
    else:
        return "Word does not exist"

word = input("Please enter the word: ")

print(word_finder(word))
