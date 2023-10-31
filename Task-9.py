#task 9
#question-1
''' data=[10,501,22,37,100,999,87,351]
    result=filter(lambda x: x>4,data)
    print(list(result)'''
#output
#[10,501,22,37,100,999,87,351]

#question-2
''' Write a python code using lambda function to check every element of a list is an integer
or string'''

given_list = [10, 501, 22, 37, 100, 999, 87, 351,"KING"]
check_type = lambda x: "Integer" if isinstance(x, int) else "String"    # Check int or string using lambda function
for i in given_list:
    result = check_type(i)            # Check type of each element in the list
    print(f"{i} is {result}")


#question3
''' using the lambda function create a fibonacci series from 1 to 50 elements'''
def fibonacci(num):
   l1 = [0, 1]
   any(map(lambda _:l1.append(sum(l1[-2:])),
         range(2, num)))
   return l1[:num]
print(fibonacci(50))


# question4
''' write a python function to validate the regular expression for the following
a)email address
b)Mobile numbers of bangladesh
c)Telephone numbers of USA
d) 16 charcter alpha-numeric password composed of
alphabets of upper case, Lower case , special characters, numbers'''


# EMAIL ADDRESS
def is_valid_email(email):
    if email.count('@') != 1:   # Counting '@' Symbol:
        return False
    local_part, domain_part = email.split('@')  #Splitting Local Part and Domain Part
    if not local_part or not domain_part:       #Checking Non-Empty Parts:
        return False
    domain, tld = domain_part.split('.')        #Splitting Domain and TLD(top level domain)
    if not domain or not tld:                   #Checking Non-Empty Domain and TLD
        return False
    return True
# Example usage
email1 = "user@example.com"
email2 = "invalid_email@.com"
email3 = "another.user@domain.co"
print(f"Is '{email1}' a valid email? {is_valid_email(email1)}")
print(f"Is '{email2}' a valid email? {is_valid_email(email2)}")
print(f"Is '{email3}' a valid email? {is_valid_email(email3)}")



# MOBILE NUMBER OF BANGLADESH
def mobile_number(number):
    valid_number = number.replace(" ", "").replace("-", "")  # Remove spaces or dashes
    if valid_number.startswith("+880") and len(valid_number) == 14 and valid_number[4:].isdigit(): # Check if the number starts with '+880' and has 11 digits after the prefix
        return True
    if valid_number.startswith("01") and len(valid_number) == 11 and valid_number.isdigit(): # Check if the number starts with '01' and has 11 digits
        return True
    return False
# Example usage
mobile_number1 = "+8801712345678"
mobile_number2 = "01954321"
mobile_number3 = "+8801112345678"
print(f"Is '{mobile_number1}' valid - {mobile_number(mobile_number1)}")
print(f"Is '{mobile_number2}' valid -{mobile_number(mobile_number2)}")
print(f"Is '{mobile_number3}' valid - {mobile_number(mobile_number3)}")



# TELEPHONE NUMBER OF USA
def us_phone_number(phone_number):
    valid_number = ''.join(filter(str.isdigit, phone_number)) # Remove all non-digit characters from the phone number
    if len(valid_number) == 10 and valid_number[0] in '23456789':  # Check if the cleaned number has 10 digits and starts with 2-9
        return True
    else:
        return False

# Example usage
phone_number1 = "(123) 456-7890"
phone_number2 = "555-1234"
phone_number3 = "2234567890"
print(f"Is '{phone_number1}' valid - {us_phone_number(phone_number1)}")
print(f"Is '{phone_number2}' valid - {us_phone_number(phone_number2)}")
print(f"Is '{phone_number3}' valid - {us_phone_number(phone_number3)}")


# Write a python fun which has 16 Characters alpha numeric password composed of alphabets of upper case , lower case , special characters , numbers.

def password(password):
    lowercase = any(char.islower() for char in password)
    uppercase = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in '!@#$%^&*()_+{}[]:;<>,.?~\\-/' for char in password)

    return lowercase and uppercase and digit and special_char and len(password) >= 8

password1 = "Soul@1234"
password2 = "passcode-123"

print(f"Is '{password1}' valid -  {password(password1)}")
print(f"Is '{password2}' valid - {password(password2)}")




