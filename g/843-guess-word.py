from collections import defaultdict

secret = "anqomr"
guesses = 0

def guess(word: str) -> int:
    global guesses

    guesses += 1
    matches = 0
    for i in range(len(word)):
        if word[i] == secret[i]:
            matches += 1
    if matches != 0:
        print("MASTER: {p} matches".format(p = matches))
    else:
        print("-1")
    print("MASTER: Guess count: {g}".format(g=guesses))
    return matches

def findSecretWord(wordlist):
    matches = 0

    while matches < 6:
        popped = wordlist.pop()
        print("LOGGER: Guessing with word {w}".format(w = popped))
        matches = guess(popped)
        wordlist = helper_guess(wordlist, popped, matches)
        
    return popped

def helper_guess(wordlist, chosen, correct_matches):
    candidates = set()
    matches = 0
    for word in wordlist:
        if word != chosen:
            for i in range(len(word)):
                if word[i] == chosen[i]:
                    matches += 1
            if matches == correct_matches:
                candidates.add(word)
        matches = 0
    
    return candidates

print(findSecretWord([
                    "pzrooh","aaakrw","vgvkxb","ilaumf","snzsrz",
                    "qymapx","hhjgwz","mymxyu","jglmrs","yycsvl",
                    "fuyzco","ivfyfx","hzlhqt","ansstc","ujkfnr",
                    "jrekmp","himbkv","tjztqw","jmcapu","gwwwmd",
                    "ffpond","ytzssw","afyjnp","ttrfzi","xkwmsz",
                    "oavtsf","krwjwb","bkgjcs","vsigmc","qhpxxt",
                    "apzrtt","posjnv","zlatkz","zynlqc","czajmi",
                    "smmbhm","rvlxav","wkytta","dzkfer","urajfh",
                    "lsroct","gihvuu","qtnlhu","ucjgio","xyycvd",
                    "fsssoo","kdtmux","bxnppe","usucra","hvsmau",
                    "gstvvg","ypueay","qdlvod","djfbgs","mcufib",
                    "prohkc","dsqgms","eoasya","kzplbv","rcuevr",
                    "iwapqf","ucqdac","anqomr","msztnf","tppefv",
                    "mplbgz","xnskvo","euhxrh","xrqxzw","wraxvn",
                    "zjhlou","xwdvvl","dkbiys","zbtnuv","gxrhjh",
                    "ctrczk","iwylwn","wefuhr","enlcrg","eimtep",
                    "xzvntq","zvygyf","tbzmzk","xjptby","uxyacb",
                    "mbalze","bjosah","ckojzr","ihboso","ogxylw",
                    "cfnatk","zijwnl","eczmmc","uazfyo","apywnl",
                    "jiraqa","yjksyd","mrpczo","qqmhnb","xxvsbx"]))

