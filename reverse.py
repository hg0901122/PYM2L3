string = input("Enter a word or a sentence: ")
string2 = ""

for i in string:
    string2 = i + string2

print("original string: ",string)
print("reverse string: ",string2)
