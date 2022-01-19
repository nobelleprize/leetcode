# https://leetcode.com/problems/unique-email-addresses/

def numUniqueEmails(emails):
    email_set = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        email = local + '@' + domain
        email_set.add(email)
    return len(email_set)

print(numUniqueEmails(["test.email+alex@leetcode.com",
"test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))