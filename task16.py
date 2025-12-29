def wholeStr(name): #Задача 1
    with open(name, 'r', encoding='utf-8') as f:
        return f.read()

def firstStr(name): #Задача 2
    with open(name, 'r', encoding='utf-8') as f:
        return f.readline()
    
def listStrAll(name): #Задача 3
    with open(name, 'r', encoding='utf-8') as f:
        return f.readlines()
    
def listStr(name): #Задача 4
    with open(name, 'r', encoding='utf-8') as f:
        return f.read().split('\n')
    
def printIterFile(name): #Задача 5
    with open(name, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')

def listStr(name): #Задача 6
    with open(name, 'r', encoding='utf-8') as f:
        return ' '.join(f.read().split('\n'))

def noMore(str): #Задача 7
    return str.strip()

def noMoreChar(str): #Задача 8
    return str.rstrip('!?.')

def writeToFile(name, a): #Задача 9
    with open(name, 'w', encoding='utf-8') as f:
        f.write(a)
        
def writeToFileWithEnter(name, a): #Задача 10
    with open(name, 'w', encoding='utf-8') as f:
        f.write(a+'\n')
        
def writeToFileWithEnter(name, a): #Задача 11
    with open(name, 'w', encoding='utf-8') as f:
        f.writelines(a)
        
def copyData(A, B): #Задача 12
    with open(A, 'r', encoding='utf-8') as f:
        with open(B, 'w', encoding='utf-8') as g:
            for i in f:
                print(i, file=g, end='')

def copyDataCheck(A, B): #Задача 13
    with open(A, 'r', encoding='utf-8') as f:
        with open(B, 'w', encoding='utf-8') as g:
            for i in f:
                s = i.strip()
                if s.startswith('hello') and s.endswith('world'):
                    print(s, file=g, end='')


def parseDict(name): #Задача 14
    d = {}
    with open(name, 'r', encoding='utf-8') as f:
        for i in f:
            s = i.strip().split()
            if s[2].isdigit():
                d[s[0]] = (s[1], s[2])
    return d
                
print(parseDict('hehe.txt'))