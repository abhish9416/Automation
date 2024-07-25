def isvowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("Entered Letter is vowel")
    else:
        print("Entered Letter is constant")


char = input("Enter the Letter : ")
isvowel(char)