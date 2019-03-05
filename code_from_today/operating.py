import os
import sys
import subprocess
from urllib.request import urlopen
from urllib.error import HTTPError


try: 
    res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
    resultat = res.read().decode('utf-8')
    
     
    
    file = open('github.json', 'w')
    file.write(resultat)

    subprocess.run(['open', 'dr.html'])

except HTTPError as err:
    print(err)
except Exception as err:
    print(err)




sys.exit()





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





print('Hello from first line')
#os.mkdir('test')
os.chdir('test')

subprocess.run(['pwd'])
subprocess.run(['ls', '-a'])

subprocess.run(['git', 'clone', 'https://github.com/python-elective-1-spring-2019/Lesson-05-Python-Utilities-and-Modules.git'])

subprocess.run(['tree'])





print('Hello from 11 line')