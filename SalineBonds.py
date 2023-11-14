def filtre():
    #Get the file name you want to process
    print("Please, enter file name (with extension) or relative path from the .exe:")
    fileName = input()
    try:
        file = open(fileName, 'r')
        #Get a list of all lines (NOTE: May be better to use something else, this might be the performance bottleneck)
        lines = file.readlines()
        linkSubunits = []
        for l in lines:
            if("You" not in l and "Date=" not in l):
                #Split into a list the line, using spaces as separator
                temp = l.split()
                #If the first chain is not the same chain in the second residue save them in a list with Chain:ResidueNAMENumber-Chain...
                if(temp[5] != temp[12]):
                    linkSubunits.append(str(temp[5].replace(")","")+":"+temp[2]+temp[1]+"-"+temp[12].replace(")","")+":"+temp[9]+temp[8]))
        file.close()
        #Check if there are repetitions before printing
        checker1 = "null"
        checker2 = "null"
        toRemove = []
        #For each in the list split and check if the first residue is the same as the last one: the "checker", the same with the second
        for r in linkSubunits:
            temp = r.split("-")
            if(temp[0] == checker1 and temp[1] == checker2):
                toRemove.append(r)
            #Set checkers as the current residues
            checker1 = temp[0]
            checker2 = temp[1]
        #Remove everything of the toRemove list
        for t in toRemove:
            linkSubunits.remove(t)
        #Print the final results
        print("Total: "+str(len(linkSubunits))+"; ", end="")
        for r in linkSubunits:
            print(r+", ",end="")
    except FileNotFoundError:
        print("The file name is not correct!")
    close = input()