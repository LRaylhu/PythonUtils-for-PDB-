def printRes():
    #Get the file name you want to process
    print("Please, enter file name (with extension) or relative path from the .exe:")
    fileName = input()
    try:
        file = open(fileName, 'r')
        #Get a list of all lines (NOTE: May be better to use something else, this might be the performance bottleneck)
        lines = file.readlines()
        number = "NULL"
        for l in lines:
            if("ATOM" in l):
                #Split into a list the line, using spaces as separator
                temp = l.split()
                #If the previous number is not the number of this residue print: Chain:ResiduNumber, Chain...
                if(number != temp[5]):
                    print(temp[4]+":"+temp[3]+temp[5]+", ", end="")
                    #Set the new number as current to check for in next interation
                    number = temp[5]
            #If it is a HETATM or a SPDBVT line it means there are no more ATOM lines
            elif ("SPDBVT" in l):
                break
        file.close()
    except FileNotFoundError:
        print("The file name is not correct!")
    close = input()