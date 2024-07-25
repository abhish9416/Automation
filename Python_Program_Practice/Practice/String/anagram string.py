s1 = input('Enter the string: ')
s2 = input("Enter the second string: ")

if len(s1) != len(s2):
    print("String is Not Anagram")
else:
    for x in s1:
        if x not in s2:
            print("Given Text Is not an Anagram")
    else:
        print("Text Is anagram")