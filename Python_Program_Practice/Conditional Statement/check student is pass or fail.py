def passorfail(math,physics,chemistry):
    if math >= 45 and physics >= 45 and chemistry >= 45:
        print("Student is Passed")
    else:
        print("Student is Failed")


math = int(input("Enter the Marks obtained in the Maths Subject : "))
physics = int(input("Enter the Marks obtained in the physics Subject : "))
chemistry = int(input("Enter the Marks obtained in the chemistry Subject : "))

passorfail(math,physics,chemistry)