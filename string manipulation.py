#String Revision


my_string = "This is the string. "
# print("m" in my_string)
# print("S" in my_string)   ## case-sensitive
# print("s" in my_string)
print(my_string*3)

#String indexing   (and i in range)
print(my_string[4:9])


for i in range(len(my_string)):         # prints each character on separate lines
    print(my_string[i])

print(my_string.isascii()) # returns True if all ascii chars I guesse

# Replacing any part of string
my_string = my_string.replace("i", "a")
print(my_string)

#extracting the first character in the strings
#that are part of the column '0'
#if the character is a number then it will return
#the number, else it will return NaN
#extr is the datafarme where we saved all the values
extr = df['0'].str.extract(r'^(\d{1})', expand=False)
print(extr.head(10))