import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter
import collections
import sys
import os.path
#Dylan Chu
#5/24/16
#CMSC471
#Project3

#takes the command line args
def processCommandLineArgs():
    filePath = sys.argv[1]

    return filePath

#creates a txt file of the image arrays
def createExamples():
    
    examples = open('Data/imgexamples.txt','a')
    imgswehave = ['01','02','03','04','05']
    smileyrange = range(10,25)
    hatrange = range(10,25)
    poundrange = range(10,25)
    heartrange = range(10,25)
    dollarrange = range(10,25)
    for x in imgswehave:
        if x == imgswehave[0]:
            for y in smileyrange:
                imgFilePath = 'Data/01/'+str(y)+'.jpg'
                ei = Image.open(imgFilePath)
                eiar = np.array(ei)
                eiarl = str(eiar.tolist())

                lineToWrite = str(x)+'::'+eiarl+'\n'
                examples.write(lineToWrite)    
        if x == imgswehave[1]:
            for y in hatrange:
                imgFilePath = 'Data/02/'+str(y)+'.jpg'
                ei = Image.open(imgFilePath)
                eiar = np.array(ei)
                eiarl = str(eiar.tolist())

                lineToWrite = str(x)+'::'+eiarl+'\n'
                examples.write(lineToWrite)   
        if x == imgswehave[2]:
            for y in poundrange:
                imgFilePath = 'Data/03/'+str(y)+'.jpg'
                ei = Image.open(imgFilePath)
                eiar = np.array(ei)
                eiarl = str(eiar.tolist())

                lineToWrite = str(x)+'::'+eiarl+'\n'
                examples.write(lineToWrite)      
        if x == imgswehave[3]:
            for y in heartrange:
                imgFilePath = 'Data/04/'+str(y)+'.jpg'
                ei = Image.open(imgFilePath)
                eiar = np.array(ei)
                eiarl = str(eiar.tolist())

                lineToWrite = str(x)+'::'+eiarl+'\n'
                examples.write(lineToWrite)                
        if x == imgswehave[4]:
            for y in dollarrange:
                imgFilePath = 'Data/05/'+str(y)+'.jpg'
                ei = Image.open(imgFilePath)
                eiar = np.array(ei)
                eiarl = str(eiar.tolist())

                lineToWrite = str(x)+'::'+eiarl+'\n'
                examples.write(lineToWrite)                

#function to check against our datafile to see what type of image we have
def whatImgIsThis(filePath):
    #load up the examples
    matchedAr = []
    loadExamps = open('Data/imgexamples.txt','r').read()
    loadExamps = loadExamps.split('\n')
    
    #open the image given
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)
    
    #check against each example
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print('')
    
    #create a dictionary of all the matches and print the most common match
    #print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    imgtype = x.most_common(1)[0][0]
    if imgtype == 1:
        print("Smiley")
    elif imgtype ==2:
        print("Hat")
    elif imgtype ==3:
        print("Hash")
    elif imgtype ==4:
        print("Heart")
    elif imgtype ==5:
        print("Dollar")
    
    

def main():
    #check if the example file is there
    if(os.path.isfile("Data/imgexamples.txt") == False):
        createExamples()
        
    #whatImgIsThis("Data/01/15.jpg")
    filePath = processCommandLineArgs()
    whatImgIsThis(filePath)


main()