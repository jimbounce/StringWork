# Suppose we have this string
email = "user1001@somecoolsite.com"
print("The initial string is: ", email)

# Lets test some string functions out on it, to see what happens.

# returns occurrences of substring in string
print("Counting the @ symbols in the string: ", email.count('@'))

# Checks if String Ends with the Specified Suffix
print("Does the string end in .com?: ", email.endswith('.com'))

# Returns the index of first occurrence of substring
print("Find the index of first 'r' char in the string: ", email.find('r'))

# Checks Alphanumeric Character
print("Is the string alpha numeric?: ", email.isalnum())

# Checks if All Characters are Alphabets
print("Are all the characters in the string letters?: ", email.isalpha())

# Checks if all Alphabets in a String are Lowercase
print("Is the string lower case?: ", email.islower())

# Checks Numeric Characters
print("Is the string entirely numeric: ", email.isnumeric())

# returns if all characters are uppercase characters
print("Are all the characters uppercase?: ", email.isupper())

# Checks if String Starts with the Specified String
print("Does the string start with 'user'?: ", email.startswith('user'))


################     More string checking       ##################


# Let's create some data to test with. There are nine examples below.
users = ['0001@edgehill.Arts.ac.uk', '0002@edgehill.arts.ac.uk',
         '8000@edgehill.Sciences.ac.uk', '8001@edgehill.Administration.ac.uk',
         '8002@edgehill.arts.ac.uk', '8003@edgehill.arts.ac.uk',
         '8004@edgehill.Sciences.ac.uk', '8005@edgehill.arts.ac',
         '8006@edgehill.ac.uk', '']

# Look a the data above carefully. What are it's characteristics. First we need
# to check if the data is valid. We can use a loop to process this data.

# Count the users.
address_count = len(users)
print(address_count)
count = 0

while count < address_count:
    if '@' not in users[count]:
        print("Invalid Login - address: ", users[count], " is invalid - missing @ symbol.")

    # What about the number of . symbols?
    elif 3 > users[count].count(".") > 3:
        print("Invalid Login - address incorrect: ", users[count],
              " too many/few '.' symbols.")

    # What about the number of @ symbols?
    elif 1 > users[count].count("@") > 1:
        print("Invalid Login - address incorrect: ", users[count],
              " too many/few '@' symbols.")

    # Is the correct university in the address.
    elif "edgehill" not in users[count]:
        print("Invalid Login - incorrect university in address: ",
              users[count], " .")

    # Does it contain .ac.uk?
    elif ".ac.uk" not in users[count]:
        print("Invalid Login - incorrect address suffix: ", users[count], " .")

    # Is the department valid?
    elif "administration" not in users[count].lower() and \
            "arts" not in users[count].lower() and "sciences" \
            not in users[count].lower():
        print("Invalid Login - incorrect department: ", users[count], " .")
    else:
        # Account is valid.

        number = int(users[count][0:4])
        department = users[count].split(".")[1]  # Figure this out.

        # Now we can test on the number.
        if number <= 8000:

            print("Valid student account: ", users[count])
            print("Student department: ", department.capitalize())
            print("Student number: ", number)
            print("\n")  # Added this to make the output easier to read.

        elif number >= 8001:
            print("Valid staff account: ", users[count])
            print("Saff department: ", department.capitalize())
            print("Staff number: ", number)
            print("\n")  # Added this to make the output easier to read.

    # Update the counter...
    count += 1