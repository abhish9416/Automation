s1 = input("Enter the First String: ")
s2 = input("Enter the Second String: ")

if len(s1) != len(s2):
    print("Not an Anagram")
else:
    for x in s1:
        if x not in s2:
            print("Given String is not anagram")
            break
    else:
        print("String is Anagram")