import sys
import os
import ast
from cmu_course_api import *

def convert():
    inputfile = open('master_data.txt','r')
    master = ast.literal_eval(inputfile.readline())
    mlist = []
    keys = master.keys()
    counter = 0
    for key in keys:
        mlist.append([key])
        course = master.get(key)
        coursekeys = course.keys()
        for item in coursekeys:
            mlist[counter].append(course[item])
        counter += 1
    newfile = open('converted.txt','w')
    newfile.write(str(mlist))
    return None

convert()
#import ast
#dict = ast.literal_eval(dictionary as string)
