def mean(value):
    if type(value) == dict:
        mean_val = sum(value.values()) / len(value)
    elif type(value) == list:
        mean_val = sum(value) / len(value)
    else:
        print("The mean can not be calculated")
    return mean_val
   
    
    
#give "value" either a list or a dict
my_input = {"ear": 5,"nose": 10,"lip": 15}
print(mean(my_input))