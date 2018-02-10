import sys
import os
from cmu_course_api import *

def postReq_calc(master_file):
    inputfile = open(master_file,"r")
    master = ast.literal_eval(inputfile.readline())
    keys = master.keys()
    for key in keys:
        prereqs = master.get(key).get("prereqs")
        for entry in prereqs:
            master.get(entry).get("postreqs").append(key)
