def converter(message):
    converted_string = message.capitalize()
    if message.startswith(("what","when","why","who","how","where")):
        return "{}? ".format(converted_string)
    else:
        return "{}. ".format(converted_string)
output = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        output.append(converter(user_input))
print(" ".join(output))
