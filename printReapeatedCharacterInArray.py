# chars = "abcdefghijklmnopqrstuvwxyz"
# check_string = "i am checking this string to see how many times each character appears"
# 
# for char in chars:
#   count = check_string.count(char)
#   if count > 1:
#     print (char,":" ,count)


def printduplicatesCharacter(string):
    duplicates = {}
    for char in string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
    for key, value in duplicates.items():
        if value > 1 and key != " ":
            print(key, end=", ")


string = "santosh kumar gouda"
printduplicatesCharacter(string)
