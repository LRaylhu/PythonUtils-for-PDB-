#Open file and search for the selected residues and calculate the sum of its atoms B-factor
print("Input file/path name: ")
filename = input()
try:
    file = open(filename,"r")
    lines = file.readlines()
    #input the residues that you want to analyze
    residues = []
    toStop = False
    while(not toStop):
        print("Input residues to analize Name(space)Chain(3spaces)Numb, (ex:LEU A   1), x to stop adding residues.")
        toAdd = input()
        if(toAdd == "x" or toAdd in residues):
            toStop = True
        else:
            residues.append(toAdd)
    for l in lines:
        if("ATOM" in l):
            #Fer coses mirar si és un dels residues
except FileNotFoundError:
    print("Error, file not found! Incorrect name or path!")