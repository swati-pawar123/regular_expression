import re
string= "This is pune, pune is in maharashtra"
print(re.search("pune",string))

#findall returns a list containing all matches/object
print(re.findall("pune",string))

#split returns a list where the string has been split at each match
phrase = "what is your email,is it hello@gmail.com"
split_term="@"
print(re.split("@",phrase))

#substitute method replace white space with "g"
text= "The rain in pune"
x=re.sub("\s","g",text)
print(x)

# \A returns a match if specified character at the begining of string
str="The rain in pune"
print(re.findall("\AThe",str))


# \Z returns a match if specified character at the end of string
str="The rain in pune"
x=re.findall("pune\Z",str)
if(x):
    print("Yes string ends with specified character")
else:
    print("not ends with specified character")

# \b returns a match if specified character at the beginning or end of string
str="The rain in pune"
x=re.findall(r"ain\b",str)   # ends with ain
#x=re.findall(r"\bain",str)         # starts with ain
if(x):
    print("Yes there is match")
else:
    print("no match")

# \d returns a match where string contain number or digits
y= "This is a string with some numbers 1233 & a symbol # hashtag"
z=re.findall(r"\d+",y)
print(z)

# \D returns a match where string contain non digits
str= "This is a string with some numbers 1233 & a symbol # hashtag"
x=re.findall(r"\D+",str)
print(x)

