str = "The ugly building stood in the city."
flag = False
print(str, len(str))
str = str.lower()
letters = str.count('a') + str.count('e') + str.count('i') + str.count('o')
print(letters)
str = str.replace('ugly ','beauty ')
if ("The" == str[0:2]) and ('end' == str[:-3]):
    flag = True
print(str, letters, flag)