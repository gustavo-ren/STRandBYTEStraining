if __name__ == '__main__':
    # Don't accept escape characters
    rawString = r"C:\\"
    rawString2 = r'C:\Users\n'
    sweet_home = "alabama"
    print("{0}\n{1}".format(rawString, rawString2))

    print("What's up ".__add__("world!!!"))
    print("Deadpool".__contains__("dead"))
    print("Deadpool".__contains__("Dead"))   # Case sensitive
    print("Blah".__eq__("Blah"))
    print("Voss".__ge__("Voss"))
    print("Voss".__getitem__(0))
    print("{0}, {1}".format(sweet_home.capitalize(),
                            sweet_home))  # Did not modify

    encode_string = "ç ü, à"
    print("{0}\n".format(encode_string.encode("utf-8")))

    list1 = []
    list1.append(1)
    list1.append(2)
    list1.append(3)

    list2 = list("The Simpsons")
    print("{0}\n{1}".format(list1, list2))

    dict1 = {'k1': 1, 'k2': 2}

    for i in list1:
        print(i+3)

    print("\n")
    for v in dict1:
        print(dict1[v]+3)
