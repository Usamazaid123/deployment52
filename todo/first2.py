mylist=[1,2,3]
print(mylist[2])
mylist[0]="new assignment"
print(mylist)
mylist.append("the last value")
print(mylist)
list2=[2,3]
mylist.extend(list2)
print(list2)
list3=[1,3,4,5,6]
list3.reverse()
print(list3)
list4=[13,22,11,33,55,134,21,44,55,41]
list4.sort()
print(list4)
list5=[1,2,3,[1,2,'a','b','c',[4,2,5]],[8,6]]
print(list5[3][2])

matrix=[[1,2,3,4 ],[5,6],[7,8,9]]
col= [row[0] for row in matrix]
print(col)
