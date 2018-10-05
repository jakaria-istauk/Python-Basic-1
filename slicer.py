#get user email address

email = input("What is your email address?: ").strip()

#slice out user name

user = email[:email.index("@")]
#print(user)

#slice domain name

domain = email[email.index("@")+1:]
#print(domain)

#format message

message = "Your user name is {}. and your domain is {}."
output = message.format(user, domain)

#display output message

print(output)
