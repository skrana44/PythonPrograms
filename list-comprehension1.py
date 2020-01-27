def list_compre(value):
    result = [var for var in value if not isinstance(var,str)]
    return result
#def foo(lst):
 #   return [i for i in lst if not isinstance(i, str)]

print(list_compre(["aa",12,34,"r"]))

