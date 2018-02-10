import sys
import os
from cmu_course_api import *

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
