def weather(temp):
    if temp <= 10:
        result = "COLD"
    elif temp > 10 and temp <= 25:
        result = "WARM"
    else:
        result = "HOT"
    return result

user_input = float(input("Please enter a temperature: "))
print("The weather is",weather(user_input))