import sys
import os
from cmu_course_api import *
import ast


def findfirst(lst, key):
    for idx in range(0,len(lst)):
        if lst[idx] == key:
            return idx
    return -1

def clear(string,left,right):
    #convert string to list
    strlist = []
    for i in range(0,len(string)):
        strlist.append(string[i:i+1])
    #while string contains a '<'
    while findfirst(strlist,left) != -1:
        #find first instance of left post
        idleft = findfirst(strlist,left)
        idright = findfirst(strlist,right)
        strlist = strlist[0:idleft] + strlist[idright+1:]
    text = ''
    for letter in strlist:
        text = text + letter
    return text

def builder(master_file):
    inputfile = open(master_file,"r")
    master = ast.literal_eval(inputfile.readline())
    inputfile.close()
    keys = master.keys()
    for key in keys:
        prereqs = master.get(key).get('prereqs')
        if prereqs != None:
            prereqs = prereqs[1:-1]
            aslist = prereqs.split(',')
            for i in range(0,len(aslist)):
                aslist[i] = clear(aslist[i],'\'','\'')
                print(aslist[i])
            print(aslist)
            for course in aslist:
                try:
                    #print(key,course)
                    #print(master.get(course).get('postreqs'))
                    master[course]['postreqs'].append(key)
                    #print(master.get(course).get('postreqs'))
                except:
                    donothing = ''
    newfile = open(master_file,'w')
    newfile.write(str(master))

builder("master_data.txt")
