def even_number(number):
    if number % 2 == 0:
        return True
    return False



for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

#Data Structures

#Strings is a data type.  " " or ' ' 

def double_word(word):
    return

print(double_word("hello" * 2 + "10")) # # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#print(double_word("hello" * 2 + "10")) # Should return hellohello10
#print(double_word("abc"))   # Should return abcabc6
#print(double_word(""))      # Should return 0