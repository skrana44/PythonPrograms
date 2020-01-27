def list_compre(value):
    result = sum([float(var) for var in value])
    return result

print(list_compre(['1.2','1.8','7.0']))