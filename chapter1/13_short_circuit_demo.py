name = "Bob"

print("-----------or------------")
# None --> Falsy , or continues to "User" 
valid_user = None or "User"
print("Hello" , valid_user)

# name --> Truthy and prints name 
valid_user_1 = name or "User"
print("Hello Again" , valid_user_1)

print("-----------and------------")
email = "bob@example.com"
valid_email = email and email != ""
print(valid_email)
if(valid_email):
    print(f"Hello {valid_user}, your email is: {email}")
else:
    print(f"Hello {valid_user}, please give your email ")