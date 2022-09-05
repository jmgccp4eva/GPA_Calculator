import os
import time

INVALID_ENTRY = 'INVALID ENTRY: PLEASE TRY AGAIN!'

def createFile(file):
    f = open(file,'w',encoding='utf-8')
    f.write('')
    f.close()

def readFile(file):
    univInfo = {}
    with open(file,'r',encoding='utf-8') as f:
        lines = f.readlines()
    tmp = ''
    for line in lines:
        line = line.strip()
        univ,info = line.split('\t')
        univInfo[univ]=info
    return univInfo

def writeData(data,file):
    f = open(file,'w',encoding='utf-8')
    for k,v in data.items():
        f.write(k+'\t'+v+'\n')
    f.close()

def getData(universities):
    data = {}
    selectionMade = False
    name = None
    while not selectionMade:
        if name is None:
            name = input('Please enter your first and last name:\t')
        if ' ' in name:
            file = name + '.tsv'
            if os.path.exists(file):
                selection = input(
                    '\nA file by that name is already in the system.\nWould you like to continue with this file?\n'
                    'Press Y for yes or N for No\t')
                if selection.upper() == 'Y':
                    data = readFile(file)
                    selectionMade = True
                elif selection.upper() == 'N':
                    os.remove(file)
                    createFile(file)
                    for u in universities:
                        data[u] = ''
                    selectionMade = True
                else:
                    print('\n',INVALID_ENTRY)
            else:
                selection = 'N'
                selectionMade = True
                createFile(file)
        else:
            name = None
            print('\n',INVALID_ENTRY)
    return  data,name,file

def addData(data,universities,file):
    save = 'N'
    while save=='N':
        print()
        statement = 'Which university is this information for?  Press:'
        print(statement)
        for i in range(0,len(universities)):
            statement=str(i+1)
            statement+=' for '
            statement+=universities[i]
            print(statement)
        school = input('Selection: ')
        found = False
        try:
            ischool = int(school)
            for i in range(0,len(universities)):
                if ischool==(i+1):
                    found=True
                    break
        except:found=False
        if found:
            schoolChoice = universities[ischool-1]
            courseNum = ''
            while len(courseNum)==0:
                courseNum = input('What was the course number?\t')
                if len(courseNum)==0:
                    print('\n',INVALID_ENTRY)
            courseName = ''
            while len(courseName)==0:
                courseName = input('What was the course description?\t')
                if len(courseName)==0:
                    print('\n',INVALID_ENTRY)
            hours = ''
            fhours = ''
            while len(hours)==0 or isinstance(fhours,str):
                hours = input('How many credit hours was this course?\t')
                try:
                    fhours = float(hours)
                except:
                    fhours = ''
                if not isinstance(fhours,float):
                    print('\n',INVALID_ENTRY)
            invalid = True
            validGrades = ['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
            while invalid:
                grade = input('What was your grade for this course?\t')
                if grade not in validGrades:
                    print('\n',INVALID_ENTRY)
                else:
                    invalid=False
            try:
                tmp = data[schoolChoice]
            except:
                tmp = ''
            if len(tmp)>0:
                tmp+='~~~'
            tmp += courseNum+'```'+courseName+'```'+str(fhours)+'```'+grade
            data[schoolChoice]=tmp
            writeData(data,file)
            save='Y'
        else:
            print(INVALID_ENTRY,'\n')
            addData(data,universities)
            return

def calculateGPAs(data):
    for k,v in data.items():
        print(k)
        print(v)
        print()

def main():
    universities = ['Mineral Area', 'SEMO', 'Metropolitan Community College', 'UMKC-Undergrad', 'UMKC-Graduate']
    data,name,file = getData(universities)
    print('Hello, ',name,'\n')
    poss = ['1','2','3']
    valid = False
    while not valid:
        inpt = input('\nPlease press 1 to view your current GPA, 2 to enter more classes, or 3 to quit:\t')
        print(type(inpt))
        if inpt not in poss:
            print(INVALID_ENTRY,'\n')
        elif inpt=='1':
            # CALCULATE GPA
            calculateGPAs(data)
            pass
        elif inpt=="2":
            # GET INFORMATION
            addData(data,universities,file)
        else:
            print('Goodbye, ',name)
            valid=True

if __name__=='__main__':
    main()


