import sys
import os
from cmu_course_api import *

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

def clean(reqs):
    if reqs != None:
        reqs = clear(reqs,'o','r')
        reqs = clear(reqs,'a','d')
        reqs = clear(reqs,'(','(')
        reqs = clear(reqs,')',')')
        for i in range(0,len(reqs)-2):
            if reqs[i:i+2]=='  ':
                reqs = reqs[0:i] + ',' + reqs[i+2:]
        reqs = '[' + reqs + ']'
    return reqs

def get_data():
    newfile = open('master_data.txt','w')
    fall = get_course_data('F').get('courses')
    spring = get_course_data('S').get('courses')
#   summer = get_course_data('M').get('courses')
#   listof = [fall, spring, summer]
    listof = [fall, spring]
    master = {}
    for item in listof:
        keys = item.keys()
        for key in keys:
            course = item.get(key)
            course['prereqs'] = clean(course.get('prereqs'))
            course['coreqs'] = clean(course.get('coreqs'))
            course.pop('prereqs_obj')
            course.pop('coreqs_obj')
            course.pop('lectures')
            course.pop('sections')
            course['postreqs'] = []
            master[key] = course
    newfile.write(str(master))
    return None

get_data()
#print('enter get_data() to get the data')

#import ast
#dict = ast.literal_eval(dictionary as string)
