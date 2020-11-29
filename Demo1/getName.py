def getName(str_name):
    name1 = 'the name is'
    name2 = str_name.split(name1)[1].split(',')[0]
    print(name2)


name = "A old lady come in, the name is Mary, level '94454'"
getName(name)
