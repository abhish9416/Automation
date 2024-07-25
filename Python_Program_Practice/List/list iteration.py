my_list = [1,2,3,4,5,6,7,8,9]

##for Loop
for i in my_list:
    print(i)

print('-------------------------')
##for Loop in range
for i in range(len(my_list)):
    print(my_list[i])

print('-----------reverse--------------')
for i in range(-1,-(len(my_list)+1),-1):
    print(my_list[i])
print('-------------------------')

i=0
while i < len(my_list):
    print(my_list[i])
    i +=1
