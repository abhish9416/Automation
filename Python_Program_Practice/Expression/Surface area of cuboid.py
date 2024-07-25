def area_of_cuboid(length,breadth,height):
    area = 2*(length*height + length*breadth + breadth*height)
    return area


length = int(input("Enter the length of the cuboid : "))
breadth = int(input("Enter the breadth of the cuboid : "))
height = int(input("Enter the Height of the cuboid : "))

print(area_of_cuboid(length,breadth,height))