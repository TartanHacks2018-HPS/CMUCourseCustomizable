import sys
import os
import ast
from cmu_course_api import *

def convert():
    inputfile = open('master_data.txt','r')
    master = ast.literal_eval(inputfile.readline())
    dictionary = {}
    keys = master.keys()
    for key in keys:
        mlist = []
        course = master.get(key)
        coursekeys = course.keys()
        for item in coursekeys:
            mlist.append(course[item])
        dictionary[key] = mlist
    newfile = open('converted.txt','w')
    newfile.write(str(dictionary))
    return None

convert()
#import ast
#dict = ast.literal_eval(dictionary as string)
