# Assuming that we have some email addresses in the
# "username@companyname.com (mailto:username@companyname.com)" format,
# please write program to print the user name of a given email address. Both user
# names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com (mailto:john@google.com)
# Then, the output of the program should be:
# john

def Extract_Email(email):
    parts=email.split('@')

    if len(parts)==2:
        return parts[0]
    else:
        return "Invalid email forsmat"
    
try:
    email=input("Enter an email address:")
    username=Extract_Email(email)
    print(username)
except ValueError:
    print("Invalid input. Please enter a valid email address.")