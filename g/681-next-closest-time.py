# https://leetcode.com/problems/next-closest-time/
from collections import defaultdict

def nextClosestTime(time):
    hour, minute = time.split(":")
    
    nums = sorted(set(hour+minute))

    two_digit_values = [a + b for a in nums for b in nums]

    i = two_digit_values.index(minute)

    if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
        return hour + ":" + two_digit_values[i+1]

    i = two_digit_values.index(hour)
    if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
        return two_digit_values[i+1] + ':' + two_digit_values[0]

    return two_digit_values[0] + ':' + two_digit_values[0]

print(nextClosestTime("19:34"))
# print(nextClosestTime("02:42"))
# print(nextClosestTime("23:59"))