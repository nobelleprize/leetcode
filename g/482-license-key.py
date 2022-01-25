# https://leetcode.com/problems/license-key-formatting/

def licenseKeyFormatting(s, k):
    s = s.replace('-', '').upper()
    head = len(s) % k
    groups = []
    if head:
        groups.append(s[:head])
    
    for i in range(head, len(s), k):
        groups.append(s[i:i+k])
    
    return '-'.join(groups)

print(licenseKeyFormatting("5F3Z-2e-9-w", k = 4))
print(licenseKeyFormatting("2-5g-3-J", k = 2))
