def solution(s, n):
    count = 0
    result = 0
    for char in s:
        if char == "a":
            count += 1
    multiples = n // len(s)

    missing = n % len(s)

    result += count * multiples

    for i in s[:missing]:
        if i == "a":
            result += 1

    return result

print(solution("aba", 10))