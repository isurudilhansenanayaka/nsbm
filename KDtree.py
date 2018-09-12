#Author: Isuru Dilhan Senanayake
#Subject: Data Structures and Algorithem
#Assignment: I
#Used Data Structure: K-D trees
#list,node

#Start of the Implementation of Tree
import math
class node:
    def __init__(self,data): #data is a list
        self.data=data
        self.color=0
        self.left=None
        self.right=None

#Node for tree Leaf
        
class leaf:
    def __init__(self):
        self.data=[]

    def insert(self,list1): #list1 is a list
        self.data.append(list1)

class tree:
    def __init__(self):
        self.head=None   #make head with non(root)
        self.dem=2       #abot 2D or 3D

    def insert(self,point,start=None): #Point is a list
        if start==None:
            start=self.head    #start equal to self.head
        if self.head==None:
            new=node(point)   #prepare new node and enter point
            new.color=0   #colr initialize for 2D or 3D
            self.head=new
            #print("None")
            self.insert(point,self.head)  #call recursive self function
        elif start.color==0:
            if start.data[0]<point[0]:   #compare point and data
                if start.right==None:    
                    new=node(point)
                    start.right=new
                    start.right.color=1
                    self.insert(point,start.right)
                else:
                    self.insert(point,start.right)
            else:
                if start.left==None:
                    new=node(point)
                    start.left=new
                    start.left.color=1
                    self.insert(point, start.left)
                else:
                    self.insert(point, start.left)

        elif start.color==1:
            if start.data[1]<point[1]:
                if start.right==None:
                    if self.dem==2:
                        new=leaf()
                        new.insert(point)
                        start.right=new
                    else:
                        new=node(point)
                        start.right=new
                        start.right.color=2
                        self.insert(point,start.right)
                else:
                    if self.dem==2:
                        #print(start.right.data)
                        start.right.insert(point)
                    else:
                        self.insert(point,start.right)
            else:
                if start.left==None:
                    if self.dem==2:
                        new=leaf()
                        new.insert(point)
                        start.left=new
                    else:
                        new=node(point)
                        start.left=new
                        start.left.color=2
                        self.insert(point,start.left)
                else:
                    if self.dem==2:
                        #print(start.left.data)
                        start.left.insert(point)
                    else:
                        self.insert(point,start.left)
        else:
            if start.data[2]<point[2]:
                if start.right==None:
                    new=leaf()
                    new.insert(point)
                    start.right=new
                else:
                    #print(start.right.data)
                    start.right.insert(point)
            else:
                if start.left==None:
                    new=leaf()
                    new.insert(point)
                    start.left=new
                else:
                    #print(start.left.data)
                    start.left.insert(point)

    def find(self,point,start=None):
        if start==None:
            start=self.head
        if start.color==0:
            if start.data[0]<point[0]:
                if start.right==None:
                    print("Not Found")
                else:
                    return self.find(point,start.right)
            else:
                if start.left==None:
                    print("Not Found")
                else:
                    return self.find(point, start.left)

        elif start.color==1:
            if start.data[1]<point[1]:
                if start.right==None:
                    print("Not Found")
                else:
                    if self.dem==2:
                        return start.right
                    else:
                        return self.find(point,start.right)
            else:
                if start.left==None:
                    print("Not Found")
                else:
                    if self.dem==2:
                        return start.left
                    else:
                        return self.find(point,start.left)
        else:
            if start.data[2]<point[2]:
                if start.right==None:
                    print("Not found")
                else:
                    return start.right
            else:
                if start.left==None:
                    print("Not Found")
                else:
                    return start.left

    def finder(self,point):
        a=self.find(point)
        return a

    def distance(self,point,start):
        d=math.sqrt(math.pow(int(point[0])-int(start[0]),2)+math.pow(int(point[1])+int(start[1]),2))
        return d

    def findmin(self,point,bucket,threshold):
        answers={}
        if bucket.data[0]!=point:
            min=self.distance(point,bucket.data[0])
            ans=bucket.data[0]
            answers[min]=ans
        else:
            min = self.distance(point, bucket.data[1])
            ans=bucket.data[1]
            answers[min] = ans
        for i in bucket.data:
            if i not in answers.values() and i!=point:
                dis=self.distance(point,i)
                if dis<min:
                    answers[dis]=(i)
        keys=answers.keys()
        count=0
        for i in sorted(keys):
            print(answers[i],end='')
            count+=1
            if count==threshold:
                break
        print()

    def findminimum(self,point,threshold):
        a=self.finder(point)
        self.findmin(point,a,threshold)




a=tree()  #cll to tree object

def inputfirst():  #for user input but not use all function hear
    x=input().split(' ')
    m=x[0]
    n=x[1]
    loop(m)
    x=getinput()
    a.findminimum(x,n)

def loop(m):     #not use this function
    for i in range(m):
        x=getinput()
        a.insert([x[0],x[1]])

def getinput():  #not use this function
    x=input().split(',')
    return x

a.insert([5,2])
a.insert([3,0])
a.insert([3,1])
a.insert([4,1])
a.insert([4,3])
a.insert([4,6])
a.insert([4,8])
a.insert([2,8])
a.insert([6,1])
a.insert([6,0])
a.insert([8,0])
a.insert([9,-5])
a.insert([6,5])
a.insert([9,12])
a.insert([15,18])
a.insert([-3,8])
a.insert([4,2])
a.insert([2,9])
a.insert([-3,1])
a.insert([0,0])
a.insert([8,0])
a.insert([4,-5])
a.insert([6,-1])
a.insert([9,-12])
a.insert([15,-18])
a.insert([7,8])

a.findminimum([5,0],4)



