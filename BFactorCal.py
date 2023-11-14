# Open file and search for the selected residues and calculate the sum of its atoms B-factor
print("Input file/path name: ")
filename = input()
try:
    file = open(filename,"r")
    lines = file.readlines()
    # Input the residues that you want to analyze
    residues = {}
    toStop = False
    while(not toStop):
        print("Input residues to analize Name(space)Chain(3spaces)Numb, (ex:LEU A   1), x to stop adding residues.")
        toAdd = input()
        if(toAdd == "x" or toAdd in residues.keys()):
            toStop = True
        else:
            residues[toAdd] = 0
    lastAtom = {}
    # Check if it is a residue like the ones we want
    for l in lines:
        for r in residues.keys():
            if(r in l):
                temp = l.split()
                residues[r] = residues[r] + float(temp[10])
                if(r in lastAtom.keys()):
                    lastAtom[r] = lastAtom[r] + 1
                else:
                    lastAtom[r] = 1
    # TEST: Make an avegrage. Need to check that the answer is correct
    for r in residues.keys():
        for a in lastAtom.keys():
            if(a == r):
                residues[r] = residues[r]/lastAtom[a]
                break
    print(residues)
except FileNotFoundError:
    print("Error, file not found! Incorrect name or path!")
