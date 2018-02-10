import sys
import os
from cmu_course_api import *


#Saves data to given filename
def save_data(newfile,text):
    inputfile = open(os.path.join(data_folder,newfile),'w')
    inputfile.write(text)
    inputfile.close()
    return None

#fall = get_course_data('F')
