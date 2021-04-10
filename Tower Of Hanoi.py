# 1. There are 3 towers. Tower 1 has n disks, where n is a positive number. Tower 2 and 3 are empty.
# 2. The disks are increasingly placed in terms of size such that the smallest disk is on top and largest disk is at bottom.
# 3. You are required to 
#     3.1. Print the instructions to move the disks.
#     3.2. from tower 1 to tower 2 using tower 3 
#     3.3. following the rules
#         3.3.1 move 1 disk at a time.
#         3.3.2 never place a smaller disk under a larger disk.
#         3.3.3 you can only move a disk at the top.
       
      
PROGRAM
def toh(n,d1,d2,d3):
    if(n==0):
        return
    toh(n-1,d1,d3,d2)
    print("{}[{} -> {}]".format(n,d1,d2))
    toh(n-1,d3,d2,d1)
    
n=int(input())
d1=int(input())
d2=int(input())
d3=int(input())
toh(n,d1,d2,d3)

OUTPUT:
1[10 -> 11]
2[10 -> 12]
1[11 -> 12]
3[10 -> 11]
1[12 -> 10]
2[12 -> 11]
1[10 -> 11]
