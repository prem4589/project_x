import re
import os
import sys
#defining a class

class Bag:
#intialisation of attributes

    def __init__(self,message):
        pass
#defining a function to pass any two text files and to read those files
    def list1(file1,file2):
        content=open(file1,"r")

        A=content.read()#read the file
#
        q=A.lower()#coverts all the characters to lower case
        q= re.sub('[^a-z\ \']+',"",q)#this method removes all the special characters
        l1=q.split(" ")#converts each and every string into characters of list
        content=open(file2,"r")#reads the file file2
        z=content.read()
        z=z.lower()
        z= re.sub('[^a-z\ \']+',"",z)
        l2=z.split(" ")
        return l1,l2
    def ListtoDict(l1,l2):#here,we create dictionaries using the contentds of the list
        vy={}#creating empty dictionary
        for i in range(len(l1)):#iterate upto the length of the characters  
            vy[l1[i]]=l1.count(l1[i]) #obtaining the frequency of each and every string
        vy1={}
        for i in range(len(l2)):
            vy1[l2[i]]=l2.count(l2[i])
        return vy,vy1#returning the obtained dictionaries
    def dotfunc(vy,vy1):#creating a dot function to multiply the key values in file
        dot=0#intialise a variable
        for k in vy:
            if k in vy1:
                dot=dot+vy.get(k)*vy1.get(k)#incrementing dot variable with the multiplication of key values
        return dot
    def vectorfunc(vy,vy1):#creating vector to obtain the vector product of key values
        vect1=0
        for k in vy:#use for loop to check in 1st file
            vect1=vect1+vy.get(k)**2#incrementing the value for each and every key
        vect1=vect1**(1/2)
        vect2=0
        for k in vy1:
            vect2=vect2+vy1.get(k)**2
        vect2=vect2**(1/2)
        return vect1*vect2#obtaining vector product of two lists
cwd = os.getcwd()#accesses the path of your file
files = os.listdir(cwd)
text = [i for i in files if i.endswith('.txt')]#checks for only .txt files
for s in text:
    for t in text:#this nested loop is to check for all files one with each other
        if (text.index(s)<=text.index(t)):#compares all files according to the  higher
                                            #index order,ignores if already compared

            pass
        else:#calling each and every function by assigning the variables if indexed files are not checked'''
            l1,l2=Bag.list1(s,t)
            vy,vy1=Bag.ListtoDict(l1,l2)
            dot=Bag.dotfunc(vy,vy1)
            e=Bag.vectorfunc(vy,vy1)
            f=(dot/e)*100#calculating percentage
            print("matching content of",s,"similar",t," is ",f,'%')
