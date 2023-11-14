def filtre():
    #Open text file with the results
    print("Please, enter file name or path:")
    filename = input()
    try:
        file = open(filename,"r")
        lines = file.readlines()
        relevant = []
        #Using the index search for this line and then read all the following lines that can have information until a blank line
        for i in range(0,len(lines)):
            x = i
            if ("Cation	AA #	Chain	Pi	AA #	Chain	E(es)		E(vdw)" in lines[i]):
                x = x+3
                while ("Number" not in lines[x] and len(lines[x])>2):
                    relevant.append(lines[x])
                    x = x + 1
            #Then keep going from this point
            i = x
        #For each line in relevant print Chain:ResidueNumber-Chain:... if the chains are NOT equal
        for r in relevant:
            temp = r.split("\t") 
            if(temp[2] != temp[5]):
                print(temp[2]+":"+temp[0]+temp[1]+"-"+temp[5]+":"+temp[3]+temp[4])
        #Close files
        file.close()
    except FileNotFoundError:
        print("The file name or path is incorrect!")