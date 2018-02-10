import sys
import os
from cmu_course_api import *
import ast

def postReq_calc(master_file):
    inputfile = open(master_file,"r")
    master = ast.literal_eval(inputfile.readline())
    keys = master.keys()
    for key in keys:
        print(key)
        prereqs = master.get(key).get("prereqs")
        print(prereqs)
        if(prereqs != None):
            for entry in prereqs:
                print (entry)
                print (master.get(entry).get("postreqs"))
                master.get(entry).get("postreqs").append(key)

postReq_calc("master_data.txt")
