class Info:
    def detailSet(self,name,id):
        self._name=name
        self._id=id
    def detailGet(self):
        print(self._name,self._id)
    print(id)
obj=Info()
obj.detailSet("rahul",100)
obj.detailGet(); 

#lambda funtion
f=lambda x,y:x+y

print(f(5,6))

n=2
m=4
arr=[[1]*m]*n
print(arr)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j]=arr[i][j]+1
print(arr)


arr=[1,2,3,4,5]
arr.reverse()
arr.sort(reverse=True)
print(arr)