names=["alpha","bravo","charlie","delta","echo","foxtrot","hunter","tango","sierra","victor"] #cooncidering 10 students of (lpu)
marks=[6,5,7,5,8,4,5,7,4,5]         #concidering out of 10 of Mid terms
updates=[2,3,2,1,1,3,3,3,5,4]       #increment
newmarks=[]                         #updated marks
highindex=0
length=len(names)                      #size of list
for i in range(0,length):
    newmarks.append(marks[i]+updates[i])   #puting elemet list after updation

for i in range(0,length):
     if newmarks[highindex]<newmarks[i]:       #finding largest marks after update
        highindex=i
element=marks[highindex]                        #finding earlier marks at largest marks index after updation
marks.sort()                                    #sorting to find rank
for i in range(0,length):
    if element==marks[i]:                          #found rank
        before_rank=i+1

print(f"name of student with highest marks after updation is {names[highindex]}")
print(f"rank before updation {before_rank}")
print(f"new rank is 1 and diffrence in earlier and now is {before_rank-1}")
print(f"marks before updation {marks[highindex]}")
print(f"marks after updation {newmarks[highindex]}")