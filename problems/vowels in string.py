def find_vowel(string):
    vowel = "aAeEiIoOuU"
    vowel_list = []
    for char in string:
        if char in vowel:
            vowel_list.append(char)
    return(vowel_list)

string = "nAvEEN"
result=find_vowel(string)
print(result)