my_list=[]
with open('My_File', 'r') as f:   # we can use r:- read or w:- write 
 Lines = f.readlines()
 for line in Lines:
   my_list.append(line.strip())
print(my_list)
