import pathlib
import os

#list(pathlib.Path('your_directory').glob('*.txt'))
for txt_file in pathlib.Path('E:').glob('**/*(?)*.mp3'):
    try:
        print (txt_file)
        os.remove(txt_file)
    except OSError:
        pass

for txt_file in pathlib.Path('E:').glob('**/*(??)*.mp3'):
    try:
        print (txt_file)
        os.remove(txt_file)
    except OSError:
        pass
    
