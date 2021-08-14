#Advance Regex

#Capturing Groups

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
#re.Match object; span=(0, 9), match='Lovelace, Ada'))
print(result.groups())
#('Lovelace', 'Ada')

print(result[0])
#'Lovelace', 'Ada'

print(result[1])
#Lovelace

print(result[2])
#Ada

"{} {}".format(resul[2], result[1])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

# rearrange_name(taylor, Deshaon)
#'Deshaon taylor'

rearrange_name(taylor, Deshaon L.)
#'taylor, Deshaon'


def rearrange_name(name):
    result = re.search(r"^([\.-), ([\w.-$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

rearrange_name(taylor, Deshaon L.)
#'Deshaon L. Taylor







