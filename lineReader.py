'''
Created on 16Jun.,2017

@author: vinicius
'''
def readLines(filename):
    with open(filename) as file:
        returnValue = file.read()
    file.close()
    returnValue.strip()
    return returnValue
