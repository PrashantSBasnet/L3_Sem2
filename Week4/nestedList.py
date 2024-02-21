#traversing nested lists
marks = [[10,20],[20,30]]
print (len(marks))
print (marks[1][1])


#example
marks = [[10,20],[30,40],[50,60]]
k=0 
sum=0
for i in range(len(marks)):
    sum = sum+marks[i][0]
    average_marks=sum/len(marks)
print(average_marks)