# https://leetcode.com/problems/unique-morse-code-words/

def uniqueMorseRepresentations(words):
    morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    morse_dict = {i:j for i,j in zip(alphabet, morse_codes)}
    
    set_result = set()
    for word in words:
        morse_str = ""
        for char in word:
            morse_str += morse_dict[char]
        set_result.add(morse_str)
    return len(set_result)


# print(uniqueMorseRepresentations(words = ["a"]))