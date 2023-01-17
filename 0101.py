##Levels
class Housetut:

    def __init__(self, game):
        self.game = game
        self.desc = "You are in a derelict house. There is peeling wallpaper on each wall. A dresser sits in the corner, photo frames lined upon it, as well as a keyring. The door is cracked."
        self.loot = ["keys"]
        self.places_to_go = []
        self.things_to_see = ["wallpaper", "dresser","frames","keys"]
        self.interactables = {"keys":"door"}

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
        self.desc = "You are in a derelict house. There is peeling wallpaper on each wall. A dresser sits in the corner, photo frames lined upon it, as well as a keyring. The door is cracked."
        self.loot = []
        self.places_to_go = []
        self.things_to_see = {"wallpaper":"The wallpaper that was once ornate is now peeling off the wall, revealing the crumbling drywall behind.", "dresser":"The drawers are empty, though there is no dust inside.","frames":"The photos in the frames are of a child, and a parent with their face burnt out.","keys":"The keys are on a ring. There is a large old key, seemingly to a chest, and a smaller door key."}
        self.interactables = {"keys":"door"}

    def StartLevel(self):
        while True:
            #print(self.game.inv)
            game.takeAction(self.desc, self.things_to_see, self.places_to_go, self.loot,self.interactables)
            if self.game.message == "Used key on door.":
                self.places_to_go.append("door")

class OutsideHouse:

    def __init__(self, game):
        self.game = game
        self.loot = []
        self.places_to_go = []


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
        if player_input == "look" or player_input == "Look":
            print(desc)

        elif player_input == "inspect" or player_input == "Inspect":
            subject = input("Inspect what?\n: ")
            if subject in(things_to_see):
                #print(the item desc)
                print("yes")
            else:
                print("I don't see " +subject+ " in here...")

        elif player_input == "move" or player_input == "Move":
            destination = input("Move where?\n: ")
            if destination in(places_to_go):
                self.goTo(destination) #check this
            else:
                print("I can't go to " +destination+ "...")

        elif player_input == "take" or player_input == "Take":
            take_obj = input("Take what?\n: ")
            print(take_obj)
            if (take_obj.lower() in(loot)) or (take_obj.lower()+"s" in (loot)):
                self.addItem(take_obj.lower()) #check this
            else:
                print("I cant take " +take_obj+ "...")
        elif player_input == "Inventory" or player_input == "inventory":
            print(self.Inventory())
            
        elif player_input == "Use" or player_input == "use":
            use_obj = input("Use what?\n: ")
            if (use_obj.lower() in(self.inv)):
                use_on_obj = input("Use " +use_obj+ " on what?")
                if use_on_obj.lower() in(interactables[use_obj.lower()]):
                    self.message = "Used " +use_obj+ " on " +use_on_obj+ "."
                    print(self.message)
                else:
                    print("I cant use that here...")
            else:
                print("I don't seem to have " +use_obj+"...")

        else:
            print("I don't understand. Try 'Look,' 'Inspect,' 'Move,' 'Take,' 'Inventory,' or 'Use'")






if __name__ == "__main__":
    game = Game('housetut')

    housetut = Housetut(game)
    house = House(game)
    # stairs = Stairs(game)

    game.addLevel('housetut', housetut)
    game.addLevel('house',house)
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