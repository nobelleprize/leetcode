# String Compression: return compressed string, if the string does not become smaller than original string, return original string
from collections import OrderedDict


def compress_string(string: str) -> str: 

    result = ""

    count = 1

    #Add in first character
    result += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            result += str(count)
            result += string[i+1]
            count = 1
    #print last one
    result += str(count)
    return result

    # for i in range(len(string)):
    #     if string[i] !
    # od = OrderedDict()
    # for
        
# print(compress_string("abc"))
print(compress_string("aabcccccaaa"))