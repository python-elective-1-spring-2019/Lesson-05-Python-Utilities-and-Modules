import os
import sys
import subprocess
from urllib.request import urlopen
from urllib.error import HTTPError

import url_Clbo





url_Clbo.open_url()




sys.exit()

"""
    This is reading a url and puts it into a file
"""
def open_file():
    while True:
        try: 
            result = int(input('please tell me the file you want to open:: '))
            file = open(result, 'r')
            break
        except FileNotFoundError:
            print('no no no')
            continue
        except ValueError as err:
            print('you typed in a wroon value', err)
            continue

    print ('Bravo')

open_file()

"""




print('Hello from first line')
#os.mkdir('test')
os.chdir('test')

subprocess.run(['pwd'])
subprocess.run(['ls', '-a'])

subprocess.run(['git', 'clone', 'https://github.com/python-elective-1-spring-2019/Lesson-05-Python-Utilities-and-Modules.git'])

subprocess.run(['tree'])





print('Hello from 11 line')