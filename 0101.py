import math
import numpy as np

class Game:

    ST = 0
    IN = 0
    DX = 0 
    CO = 0
    WI = 0
    CH = 0
    total_stat = 0
    location = 'none'
    inv_idx = []

    def __init__(self):
        self.value = 0


    def House(self, inventory_index):
        while True:
        #    location = input("type house")
        #    location = "house"
            location = "house"
            print("You wake up, coughing. Your throat is dry. As you open your eyes, you notice your surroundings. \n")
            print("Type 'Look' to look around. \n")
            Inputs_Ctrl(inventory_index, location)
            print("Type 'Take' and 'Keys' to take the keys.\n")
            print(inventory_index)
            Inputs_Ctrl(inventory_index, location)
            print(location)
            print("Type 'Inventory' to see what you're carrying.")
            print(inv_idx)
            Inputs_Ctrl(inv_idx, location)
            print("Good.")
        

    def Inputs_Ctrl(self, inventory_index, location_string):
    #    print("Hit input control")
        inputs = input(": ")
        if (inputs == "Look"):
    #        print("Going to look")
            Look(location_string)
        elif (inputs == 'Take'):
            Take(inventory_index, location_string)
        elif (inputs == 'Inventory'):
            Inventory(inventory_index)
    #    elif inputs = "

    def Look(self, location_string):
        print("Looking")
        if (location_string == "house"):
            print("looked")
            print("You are in a derelict house. There is peeling wallpaper on each wall. A dresser sits in the corner, photo frames lined upon it, as well as a keyring. The door is cracked.")

    def Take(self, inventory_index, location_string):
    #    print("Taking")
        input_take = input("Take what?\n: ")
        if (location_string == 'house'):
            if (input_take == ('Keys' or 'keys')):
                Add(inventory_index,"Keys")
                
                
                

    def Inventory(self, inventory_index):
        print(inventory_index)

    def Add(inventory_index,add_string):
        print("adding")
        inventory_index = np.append(inventory_index,add_string)
    #    inv_idx = inv_idx2
        print(inventory_index)


    def Stat_List(self):
        CH_str = str(CH)
        ST_str = str(ST)
        IN_str = str(IN)
        CO_str = str(CO)
        DX_str = str(DX)
        WI_str = str(WI)
        print("Here are your stats:\n")
        print("Charisma: " + CH_str + "\nStrength: " + ST_str + "\nIntelligence: " + IN_str + "\nConstitution: " + CO_str + "\nDexterity: " + DX_str + "\nWisdom: " + WI_str)
        
    if __name__ == "__main__":
        while True:
            char = True
            stren = True
            intel = True
            const = True
            dext = True
            wisd = True
            location = "intro"
            inputs = "intro"


            name = input("Welcome to TextGame! What's your name?\n")
            print(name + ", got it. Before we start, I'd like to ask you a few questions. \nAnswer them on a scale from 0-5.\n")

            while(char == True):
                CH = int(input("Are you good at making new friends? ")) #charisma
                if(CH < 0 or CH > 5):
                    print("That isn't in the range, try again.\n")
                else:
                    char = False
            total_stat = CH
                #CH = CH * .1

            while(stren == True):
                ST = int(input("Do you work out often? ")) #strength
                if(ST < 0 or ST> 5):
                    print("That isn't in the range, try again.\n")
                else:
                    stren = False
            total_stat = total_stat + ST
                #ST = ST * .1

            while(intel == True):
                IN = int(input("Do you enjoy acadamia? ")) #intellegence
                if(IN < 0 or IN> 5):
                    print("That isn't in the range, try again.\n")
                else:
                    intel = False
            total_stat = total_stat + IN
                #IN = IN * .1

            while(const == True):
                CO = int(input("Can you take a punch? ")) #constitution
                if(CO < 0 or CO> 5):
                    print("That isn't in the range, try again.\n")
                else:
                    const = False
            total_stat = total_stat + CO
                #CO = CO * .1

            while(dext == True):
                DX = int(input("Would you describe yourself as stealthy? ")) #dexterity
                if(DX < 0 or DX> 5):
                    print("That isn't in the range, try again.\n")
                else:
                    dext = False
            total_stat = total_stat + DX
                #DX = DX * .1

            while(wisd == True):
                WI = int(input("Do you find yourself to have good decision making skills? ")) #wisdom
                if(WI < 0 or WI> 5):
                    print("That isn't in the range, try again.\n")
                else:
                    wisd = False
            total_stat = total_stat + WI
                #WI = WI * .1


            CH = (CH / total_stat) * 100
            ST = (ST / total_stat) * 100
            IN = (IN / total_stat) * 100
            CO = (CO / total_stat) * 100
            DX = (DX / total_stat) * 100
            WI = (WI / total_stat) * 100

            CH_str = str(CH)
            ST_str = str(ST)
            IN_str = str(IN)
            CO_str = str(CO)
            DX_str = str(DX)
            WI_str = str(WI)

            #stat_idx = [CH,ST,IN,CO,DX,WI]

            print("Here are your stats:\n")
            print("Charisma: " + CH_str + "\nStrength: " + ST_str + "\nIntelligence: " + IN_str + "\nConstitution: " + CO_str + "\nDexterity: " + DX_str + "\nWisdom: " + WI_str)
            #print(stat_idx)

            print("Let's begin.\n")

            
        #    inv_idx = []
        #    location = "house"
            Test2 = House(inv_idx)
            Test2.House(inv_idx)

Test = Game()
Test.House()