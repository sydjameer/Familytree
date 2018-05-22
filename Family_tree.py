# Developed By: Syed Jameer
# Date: 20-May-2018
# Purpose: To get the path from source and destination

from fn_family import find_parent
from fn_family import find_child_parent

# array=[(6,5),(6,1),(6,2),(6,15),(5,20),(5,8),(1,4),(1,16),(15,3),(15,10),(20,22),(20,28),(28,36),(28,42),(28,47),(42,54),(2,25)]
array=[(12,10),(12,1),(1,41),(10,11),(10,18),(18,54),(18,88),(88,20),(88,26),(26,34),(26,24),(54,60),(54,14),(60,72),(72,30),(72,66),(11,4),(11,32),(32,39),(39,61),(4,16),(16,50),(16,19)]
temp=0
start=int(input('Enter the source location:'))
end=int(input('Enter the destination location:'))

value_2=find_child_parent(start,end,array)

if len(value_2)!=0:
    if value_2[0]==start and value_2[-1]==end:
        print(value_2)
    else:
        tmp=value_2[-1]
        value_2.remove(value_2[-1])
        #print(value_2)
        value_1 = find_parent(end,tmp, array, temp)
        #To check if elements in value 2 is coinciding with value1
        #*********************************************************
        length = len(value_1)
        p1=None
        p2=None
        while True:
            if value_1[length - 1] in value_2:
                p1 = value_2.index(value_1[length - 1])
                p2 = (length - 1)
                break
            length = length - 1
            if length==-1:
                break

        #*********************************************************
        #If p1 and p2 value is non-zero then they are coinciding and need to find the shortest path

        if p1 or p2 is not None:
            temp_2 = value_2[0:p1]
            temp_1 = value_1[p2:]
            print(temp_2+temp_1)
        else:
            print(value_2+value_1)
else:
    value_1 = find_parent(end, start, array, temp)
    print(value_1)






