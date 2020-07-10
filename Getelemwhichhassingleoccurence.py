def getelemwhichhassingleoccurence(myarray):
    hashTable = {}
    for elem in myarray.lower():
        if elem in hashTable:
            hashTable[elem] += 1
        else:
            hashTable[elem] = 1

    for elem in myarray.lower():
        if hashTable[elem] == 1:
            return elem


print(getelemwhichhassingleoccurence("acceepp"))