# https://leetcode.com/problems/longest-absolute-file-path/

def lengthLongestPath(input):
    result = 0
    pathLength = {0: 0}

    for line in input.split('\n'):
        name = line.lstrip('\t')
        level = len(line) - len(name)
        if '.' in name: # text file
            if pathLength[level] + len(name) > result:
                result = pathLength[level] + len(name)
        else:
            pathLength[level+1] = pathLength[level] + len(name) + 1 # +1 to account for / 
    
    return result

print(lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
