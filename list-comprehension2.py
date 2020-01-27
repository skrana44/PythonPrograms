def list_compre(value):
    result = [var if not isinstance(var,str) else 0 for var in value]
    return result

print(list_compre(["aa","bb",67,99]))