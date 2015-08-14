#!/usr/bin/python3

import json
from sys import argv
from os import environ, path, makedirs
from random import randint
WIDTH = 42

def main():
    if not environ.get('XDG_DATA_HOME'):
        dataPath = path.expanduser('~/.local/share/conky-notes/')
    else:
        dataPath = path.expanduser(environ['XDG_DATA_HOME'] + 'conky-notes/')

    if not path.exists(dataPath):
        makedirs(dataPath)

    finPath = dataPath + 'data.json'

    if path.exists(finPath):
        data = json.load(open(finPath,'r'))
    else:
        data = []

    if len(argv) < 2:
        print("\nInvalid command")
        printHelp()
        return False

    if argv[1] == 'conky':
        outputConky(data)
    elif argv[1] == 'random':
        outputRandom(data)
    elif argv[1] == '-':
        if argv[2] and argv[2].isnumeric():
            removeNote(data, finPath)
        else:
            print("\nInvalid command")
            printHelp()
    elif argv[1] == '+':
        if argv[2]:
            addNote(data, finPath)
        else:
            print("\nInvalid command")
            printHelp()
    elif argv[1] == 'list':
        listNotes(data)
    elif argv[1] == 'help':
        printHelp()
    else:
        print("\nInvalid command")
        printHelp()

def printHelp():
    print("\nUsage: notes [operation] [arguments]")
    print("Operations:")
    print("  +                 Add note                           notes + [note]")
    print("  -                 Remove note                        notes - [note index]")
    print("  list              Lists notes                        notes list")
    print("  help              Prints out this help               notes help")
    print("  conky             Print out conky output             notes conky")
    print("  random            Print out a random note            notes random\n")

def outputRandom(data):
    print(data[randint(0, len(data)-1)])

def outputConky(data):
    for string in data:
        print('\n' + string + '\n')

def writeToFile(data, fpath):
    json.dump(data, open(fpath,'w'))

def addNote(data, fpath):
    data.append(argv[2])
    writeToFile(data, fpath)

def removeNote(data, fpath):
    del data[int(argv[2])]
    writeToFile(data, fpath)

def listNotes(data):
    for string in data:
        print('\n' + str(data.index(string)) + ": " + string + '\n')

main()
