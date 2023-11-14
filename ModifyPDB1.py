def modify():
    #Open PDB file with specified name
    print("Please, enter file name or path:")
    filename = input()
    try:
        rawfile = open(filename, "r")
        lines = rawfile.readlines()
        #Remove the lines that create problems (MODEL AND ENDMDL)
        toRemove = []
        for l in lines:
            if("MODEL" in l or "ENDMDL" in l):
                toRemove.append(l)
        for r in toRemove:
            lines.remove(r)
        #Create a new file with .pdb extension and write the lines to it
        newfile = open((filename[:-4]+"pdb"),"w")
        newfile.writelines(lines)
        #Closing all the files at the end of process
        newfile.close()
        rawfile.close()
    except FileNotFoundError:
        print("The file name is not correct!")