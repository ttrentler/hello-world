#Variables
message = "Hello world!!"
print(message)

#String Methods

#USe Title to Capitalize
name = "ted trentler"
print(name.title())

name = "John Smith"
print(name.upper())
print(name.lower())

#Concantonate Strings

first_name = "jane"
last_name = "smith"
full_name = first_name + " " + last_name 

print(full_name)


newmessage = "Hello, " + full_name.title() + "!"
print(newmessage)

#Add Lines and Tabs to Strings with \n and \t
print("Line1\nLine2")
print("Line1\tLine2")

#Remove whitespace CAn use strip, rstrip or lstrip
some_text = " space "
some_text = some_text.rstrip()
print (some_text + "stuff")

#import this  print (this)