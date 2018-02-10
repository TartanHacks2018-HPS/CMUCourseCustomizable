import sys
import os
from cmu_course_api import *
import ast


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
