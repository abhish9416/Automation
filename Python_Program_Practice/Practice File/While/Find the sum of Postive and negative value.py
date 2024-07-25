def psumnsum(total):
    psum = 0
    nsum = 0
    count = 0

    while count < total:
        num = int(input("Enter the Number : "))
        if num > 0:
            psum = psum + num
        else:
            nsum = nsum + num
        count = count +1

    return psum,nsum

total = int(input("Enter the total Number :"))
print(psumnsum(total))
