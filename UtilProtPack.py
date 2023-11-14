import CationPi
import SalineBonds
import ModifyPDB1
import PrintResidues
import GetCoordRange
import BFactorCal

# TODO: implement BFactorCal and TEST GetCoordRange
running = True
while(running):
    print("Please choose action:[1]-ModifyPDB1, [2]-PrintRes, [3]-CationPi, [4]-SalineBonds, [5]-GetRange, [0]-Help, [x]-Close")
    choice = input()
    if(choice == "1"):
        ModifyPDB1.modify()
    elif(choice == "2"):
        PrintResidues.printRes()
    elif(choice == "3"):
        CationPi.filtre()
    elif(choice == "4"):
        SalineBonds.filtre()
    elif(choice == "0"):
        print("There is no help now!")
    elif(choice =="5"):
        GetCoordRange.getCoord()
    else:
        running = False
