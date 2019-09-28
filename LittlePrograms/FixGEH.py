# based on https://www.reddit.com/r/beginnerprojects/comments/1i6sax/challenge_count_and_fix_green_eggs_and_ham/
# By Pete Baus 9/27/2019

from pathlib import Path  # file path don't realy work well with out pathlib
Path = Path('GitHub Files/PythonPrograms/LittlePrograms/')
FileOpenPath = Path / 'GreenEggsAndHam.txt'
FileSavePath = Path / 'GreenEggsAndHamFixed.txt'
File = open(FileOpenPath, 'rt')
OutFile = open(FileSavePath, 'wt')
Count = 0
for line in File:
    Text = line
    if 'i ' in line or '-i-' in line:
        Count += (Text.count('i '))
        Text = (Text.replace('i ', 'I '))
        Count += (Text.count('-i-'))
        Text = (Text.replace('-i-', '-I-'))
    print(Text.rstrip(), file=OutFile)
    print('', end='', flush=True)  # keep the buffer clean
OutFile.close()
print('There where {} errors'.format(Count))
