import re
result = re.search(r"aza", "plaza")
print(result)
#always use raw strings in regex
result = re.search(r"aza", "plaaaaza")
print(result)

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "Penguin", re.IGNORECASE))

print(re.search(r"[Pp]ython", "Python"))
#re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way", "THe end of the highyway"))
#re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go"))
#none

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
#re.Match object; span=(0, 6), match='cloudy'>

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
#re.Match object; span=(0, 6), match='cloud9'>

print(re.search(r"[^a-zA-Z]", "This is a sentence with a spaces."))
#re.Match object; span=(18, 22), match=' '>

print(re.search(r"[^a-zA-Z ]", "This is a sentence with a spaces."))
#re.Match object; span=(18, 22), match='.'>


print(re.search(r"cat|dog", "I like cats."))
#re.Match object; span=(18, 22), match='cat'>

print(re.search(r"cat|dog", "I like dogs."))
#re.Match object; span=(18, 22), match='dog'>

print(re.search(r"cat|dog", "I like dogs and cats."))
#re.Match object; span=(18, 22), match='dog'>


print(re.findall(r"cat|dog", "I like dogs and cats."))
['dog', 'cat']

print(re.search(r"Py.*n", "Pygmalion"))
#re.Match object; span=(0, 9), match='Pygmalion'>

print(re.search(r"Py.*n", "Python Programming"))
#re.Match object; span=(0, 9), match='Python Programmin'>

print(re.search(r"Py[a-z]*n", "Python Programming"))
#re.Match object; span=(0, 9), match='Python"))

print(re.search(r"Py[a-z]*n", "Pyn "))
#re.Match object; span=(0, 9), match='Pyn"))

# THe Plus ( + ) character matches one or more accurances before it for Python and egrep not grep.
print(re.search(r"0+l+", "goldfish "))
#re.Match object; span=(0, 9), match='ol"))

print(re.search(r"0+l+", "wolly "))
#re.Match object; span=(0, 9), match='ooll"))

print(re.search(r"0+l+", "boil "))
none

#The question Mark ( ? ) mean  0 or 1 occurance of the charater before it.


print(re.search(r"p?each", "To each their own"))
#re.Match object; span=(0, 9), match='each'))

print(re.search(r"p?each", "I like peaches"))
#re.Match object; span=(0, 9), match='peach'))


print(re.search(r".com", "welcome"))
#re.Match object; span=(0, 9), match='welcome'))

print(re.search(r"\.com", "welcome"))
none

print(re.search(r"\.com", "mydomain.com"))
#re.Match object; span=(0, 9), match='welcome'))


print(re.search(r"\w*", "And_his_is_another"))
#re.Match object; span=(0, 9), match='And_his_is_another'))

# \d = digits \s for white spaces \b for word boundries.  

#www.regex101.com


print(re.search(r"A.*a", "Argentina"))
#re.Match object; span=(0, 9), match='Argentina'))

print(re.search(r"A.*a", "Azerbaijan"))
#re.Match object; span=(0, 9), match='Azerbaijan'))

print(re.search(r"^A.*a$", "Azerbaijan"))
#none  THe $ stops the search with A

print(re.search(r"^A.*a$", "Austrailia"))
#re.Match object; span=(0, 9), match='Austrailia'))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid variable name))
#re.Match object; span=(0, 9), match='this_is_a_valid variable name'))

print(re.search(pattern, "_this is a valid variable name))
#none

print(re.search(pattern, "my_variable1"))
#re.Match object; span=(0, 9), match='my_variable1'))












