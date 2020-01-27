def converter(message):
    converted_string = message.capitalize()
    if message.startswith(("what","when","why","who","how","where","is","are")):
        return "{}? ".format(converted_string)  
    else:
        return "{}. ".format(converted_string)

message = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        message.append(converter(user_input))    #this is equeals to message = message + title_maker(user_input)

print(" ".join(message))
