##Levels

class Intro:
    def __init__(self,game):
        self.game = game
        self.name = ""
        self.char = True
        self.stren = True
        self.intel = True
        self.const = True
        self.dext = True
        self.wisd = True

        self.ST = 0
        self.IN = 0
        self.DX = 0 
        self.CO = 0
        self.WI = 0
        self.CH = 0
        self.total_stat = 0

        self.CH_str = ""
        self.ST_str = ""
        self.IN_str = ""
        self.CO_str = ""
        self.DX_str = ""
        self.WI_str = ""
        
    def StartLevel(self):
        self.name = input("Welcome to TextGame! What's your name?\n")
        print(self.name + ", got it. Before we start, I'd like to ask you a few questions. \nAnswer them on a scale from 0-5.\n")

        while(self.char == True):
            self.CH = int(input("Are you good at making new friends? ")) #charisma
            if(self.CH < 0 or self.CH > 5):
                print("That isn't in the range, try again.\n")
            else:
                self.char = False
        self.total_stat = self.CH
            #CH = CH * .1

        while(self.stren == True):
            self.ST = int(input("Do you work out often? ")) #strength
            if(self.ST < 0 or self.ST> 5):
                print("That isn't in the range, try again.\n")
            else:
                self.stren = False
        self.total_stat = self.total_stat + self.ST
            #ST = ST * .1

        while(self.intel == True):
            self.IN = int(input("Do you enjoy acadamia? ")) #intellegence
            if(self.IN < 0 or self.IN> 5):
                print("That isn't in the range, try again.\n")
            else:
                self.intel = False
        self.total_stat = self.total_stat + self.IN
            #IN = IN * .1

        while(self.const == True):
            self.CO = int(input("Can you take a punch? ")) #constitution
            if(self.CO < 0 or self.CO> 5):
                print("That isn't in the range, try again.\n")
            else:
                self.const = False
        self.total_stat = self.total_stat + self.CO
            #CO = CO * .1

        while(self.dext == True):
            self.DX = int(input("Would you describe yourself as stealthy? ")) #dexterity
            if(self.DX < 0 or self.DX> 5):
                print("That isn't in the range, try again.\n")
            else:
                self.dext = False
        self.total_stat = self.total_stat + self.DX
            #DX = DX * .1

        while(self.wisd == True):
            self.WI = int(input("Do you find yourself to have good decision making skills? ")) #wisdom
            if(self.WI < 0 or self.WI> 5):
                print("That isn't in the range, try again.\n")
            else:
                self.wisd = False
        self.total_stat = self.total_stat + self.WI
            #WI = WI * .1


        self.CH = (self.CH / self.total_stat) * 100
        self.ST = (self.ST / self.total_stat) * 100
        self.IN = (self.IN / self.total_stat) * 100
        self.CO = (self.CO / self.total_stat) * 100
        self.DX = (self.DX / self.total_stat) * 100
        self.WI = (self.WI / self.total_stat) * 100

        self.CH_str = str(self.CH)
        self.ST_str = str(self.ST)
        self.IN_str = str(self.IN)
        self.CO_str = str(self.CO)
        self.DX_str = str(self.DX)
        self.WI_str = str(self.WI)

        #stat_idx = [CH,ST,IN,CO,DX,WI]

        print("Here are your stats:\n")
        print("Charisma: " + self.CH_str + "\nStrength: " + self.ST_str + "\nIntelligence: " + self.IN_str + "\nConstitution: " + self.CO_str + "\nDexterity: " + self.DX_str + "\nWisdom: " + self.WI_str)
        #print(stat_idx)

        print("Let's begin.\n")

        self.game.goTo("housetut")


class Housetut:

    def __init__(self, game):
        self.game = game
        self.desc = "You are in a derelict house. There is peeling wallpaper on each wall. A dresser sits in the corner, photo frames lined upon it, as well as a keyring. There is a door on one wall."
        self.loot = ["key"]
        self.places_to_go = []
        self.things_to_see = {
            "wallpaper":"The wallpaper that was once ornate is now peeling off the wall, revealing the crumbling drywall behind.",
            "dresser":"The drawers are empty, though there is no dust inside.",
            "frames":"The photos in the frames are of a child, and a parent with their face burnt out.",
            "key":"The keys are on a ring. There is a large old key, seemingly to a chest, and a smaller door key.",
            "door" : "The door is locked"
        }
        self.interactables = {"key":"door"}

    def StartLevel(self):
        while True:
            print("You wake up, coughing. Your throat is dry. As you open your eyes, you notice your surroundings. \n")
            print("Type 'Look' to look around. \n")
            self.game.takeAction(self.desc, self.things_to_see, self.places_to_go, self.loot,self.interactables)
            print("Type 'Take' and 'Keys' to take the keys.\n")
            #print(game.self.inv) #how to print this?
            self.game.takeAction(self.desc, self.things_to_see, self.places_to_go, self.loot,self.interactables)
            print("Type 'Inventory' to see what you're carrying.")
            self.game.takeAction(self.desc, self.things_to_see, self.places_to_go, self.loot,self.interactables)
            print("Good.")
            print(self.game.inv)
            self.game.goTo("house")
            # x = input()
            # if x == 'Look'

            #print("You wake up, coughing. Your throat is dry. As you open your eyes, you notice your surroundings. \n")
            #print('you check your inventory')
            #cur_inv = self.game.Inventory()
            #print(cur_inv)

            #print('you pick up a key')
            #self.game.addItem('key')
            #print('you check your inventory')
            #cur_inv = self.game.Inventory()
            #print(cur_inv)


            # 
            # 
            # loot_taken, thing_used = takeaction(loot, places_to_go)
            # if thing_used == 'key' => places_to_go.append('other room'), loot = []

            # self.game.takeaction(loot, opalces)

            # x = input()
            # if x == run 


        # self.game.goTo('stairs')

class House:
    def __init__(self, game):
        self.game = game
        self.desc = "You are in a derelict house. There is peeling wallpaper on each wall. A dresser sits in the corner, photo frames lined upon it, as well as a keyring. The door to the north is locked."
        self.loot = []
        self.places_to_go = {}
        self.things_to_see = {
            "wallpaper":"The wallpaper that was once ornate is now peeling off the wall, revealing the crumbling drywall behind.",
            "dresser":"The drawers are empty, though there is no dust inside.",
            "frames":"The photos in the frames are of a child, and a parent with their face burnt out.",
            "keys":"The keys are on a ring. There is a large old key, seemingly to a chest, and a smaller door key.",
            "door" : "The door is locked"
        }
        self.interactables = {"key":"door"}

    def StartLevel(self):
        while True:
            #print(self.game.inv)
            self.game.takeAction(self.desc, self.things_to_see, self.places_to_go, self.loot,self.interactables)
            if self.game.message == "Used key on door.":
                self.places_to_go["north"] = 'livingroom'
                self.things_to_see["door"] = "The door is unlocked"
                self.desc = "You are in a derelict house. There is peeling wallpaper on each wall. A dresser sits in the corner, photo frames lined upon it, as well as a keyring. The door to the north is unlocked."

class LivingRoom:

    def __init__(self, game):
        self.game = game
        self.desc = "You are in a living room. There is a couch with springs exposed, a locked trunk, and a door with light shining through the window to the west."
        self.loot = ["wallet","letter"]
        self.places_to_go = ["south","west"]
        self.things_to_see = {
            "couch":"This couch has seen better days.",
            "trunk":"The trunk is plain black, and missing wheels. It's locked.",
            "door":"The door is unlocked.",
        }
        self.interactables = {'key':'trunk'}
        self.trunktrigger = True


    def StartLevel(self):
        print(self.desc)
        while True:
            self.game.takeAction(self.desc, self.things_to_see, self.places_to_go, self.loot,self.interactables)
            if self.game.message == "Used key on trunk." and self.trunktrigger == True:
                self.things_to_see["trunk"] = "The trunk is open. It's nearly empty, save for a wallet and a letter."
                self.things_to_see["wallet"] = "There is an ID card, $6 cash, and a Bath & Bodyworks gift card."
                self.things_to_see["letter"] = "\nDear " +self.intro.name+ ",\nIf you found this, it means that XXX. If there's any hope, I'm at XXX."
                self.desc = "You are in a living room. There is a couch with springs exposed, an unlocked trunk, and a door with light shining through the window to the west."
                print(self.things_to_see["trunk"])
                self.trunktrigger = False
            #if self.game.message == ""





##Mechanics, Starting
class Game:

    def __init__(self, startingLoc):
        self.inv = []
        self.boards = {}
        self.startingLoc = startingLoc
        self.message = ''

    def Inventory(self):
        return self.inv

    def addItem(self, add_string):
        self.inv.append(add_string)

    def addLevel(self, loc_string, location):
        self.boards[loc_string] = location

    def goTo(self, loc_string):
        self.boards[loc_string].StartLevel()

    def StartGame(self):
        #get stats
        #print("Starting game\n")
        #print(self.startingLoc)
        #print(self.boards)
        self.goTo(self.startingLoc)

    def takeAction(self, desc, things_to_see, places_to_go,loot,interactables):
        player_input = input(": ")
        # print(player_input)
        # print(loot)
        if player_input.lower() == "look":
            print(desc)

        elif player_input.lower() == "inspect":
            subject = input("Inspect what?\n: ")
            if subject in(things_to_see):
                print(things_to_see[subject])
            else:
                print("I don't see " +subject+ " in here...")

        elif player_input.lower() == "move":
            direction = input("Move where?\n: ")
            if direction.lower() in(places_to_go):
                print("You move " +direction+ ".")
                self.goTo(places_to_go[direction]) 
            else:
                print("I can't go " +direction+ "...")

        elif player_input.lower() == "take":
            take_obj = input("Take what?\n: ")
            print(take_obj)
            if (take_obj.lower() in(loot)) or (take_obj.lower()+"s" in (loot)):
                self.addItem(take_obj.lower()) #check this
                loot.remove(take_obj.lower())
                print(things_to_see[take_obj])
            else:
                print("I cant take " +take_obj+ "...")
        elif player_input.lower() == "inventory":
            print(self.Inventory())
            
        elif player_input.lower() == "use":
            use_obj = input("Use what?\n: ")
            if (use_obj.lower() in(self.inv)):
                use_on_obj = input("Use " +use_obj+ " on what?")
                if use_on_obj.lower() in(interactables[use_obj.lower()]) or use_on_obj.lower() in(interactables[use_obj.lower()+"s"]):
                    self.message = "Used " +use_obj+ " on " +use_on_obj+ "."
                    print(self.message)
                else:
                    print("I cant use that here...")
            else:
                print("I don't seem to have " +use_obj+"...")

        else:
            print("I don't understand. Try 'Look,' 'Inspect,' 'Move,' 'Take,' 'Inventory,' or 'Use'")
        






if __name__ == "__main__":
    game = Game('intro')

    intro = Intro(game)
    housetut = Housetut(game)
    house = House(game)
    livingroom = LivingRoom(game)
    # stairs = Stairs(game)
    game.addLevel('intro',intro)
    game.addLevel('housetut', housetut)
    game.addLevel('house',house)
    game.addLevel('livingroom',livingroom)

    # game.addLevel(stairs, 'stairs')

    game.StartGame()



"""


def take_action(loot, places to go, things to see, description):
    input()

    if look => print description
    if inspect => if in things to see, print description (picking from dictionary)
    if move => if in places to go, self.goTo(place)
    if take => if in loot, add to inventory, then return thing taken
    if use => return thing used

    return action, loot_taken, things_used

"""