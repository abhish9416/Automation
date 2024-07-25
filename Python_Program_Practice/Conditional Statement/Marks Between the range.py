def marksvalid(marks):
    if marks >= 0 and marks <= 100:
        print("Marks are Valid")
    else:
        print("Marks are invalid")


marks = int(input("Enter the Marks : "))
marksvalid(marks)