def getCoord ():
    print("Please, enter file name or path:")
    filename = input()
    try:
        #open file and take the range/s of aa and put them on a new file
        file = open(filename,"r")
        lines = file.readlines()
        #Take as a input the chain you want to take from and the range or multiple ranges of atoms, example: chain, then ask range, write x once you put all the ranges
        print("Enter chain letter (example: A )...")
        chain = input()
        currentRanges = []
        isXPressed = False
        toSave = []
        while(not isXPressed):
            print("Enter range, if you want to stop entering ranges write x... (example: 156-167) || Current ranges: "+ currentRanges)
            result = input()
            if(result == "x" or result == ""):
                isXPressed = True
            elif(result not in currentRanges):
                currentRanges.append(result) 
        for l  in lines:
            if("ATOM" in l or "TER" in l):
                #For each current range check if it is between the range and is from the chain
                templine = l.split()
                for r in currentRanges:
                    temp = r.split("-")
                    if(templine[4] == chain and templine[5] >= temp[0] and templine[5] <= temp[1]):
                        toSave.append(l)
        print("Add a suffix for your file so the name is difererent (example: A1)")
        sufx = input()
        filenew = open(filename+"_"+sufx, "w")
        filenew.writelines(toSave)
        filenew.close()
        file.close()
    except FileNotFoundError:
        print("File name not correct!")