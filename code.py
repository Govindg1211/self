import random

class Game:
    def __init__(self):
        self.rooms = {
            'Entrance': {'description': 'You are at the entrance of a dark cave.', 'exits': ['Hallway']},
            'Hallway': {'description': 'A long hallway with flickering lights.', 'exits': ['Entrance', 'Treasure Room']},
            'Treasure Room': {'description': 'A room filled with gold and jewels!', 'exits': ['Hallway'], 'item': 'treasure'},
        }
        self.current_room = 'Entrance'
        self.inventory = []

    def describe_room(self):
        room = self.rooms[self.current_room]
        print(room['description'])
        print("Exits:", ', '.join(room['exits']))
        if 'item' in room:
            print(f"You see a {room['item']} here.")

    def move(self, direction):
        if direction in self.rooms[self.current_room]['exits']:
            self.current_room = direction
            self.describe_room()
        else:
            print("You can't go that way!")

    def take_item(self):
        room = self.rooms[self.current_room]
        if 'item' in room:
            self.inventory.append(room['item'])
            print(f"You took the {room['item']}.")
            del room['item']
        else:
            print("There's nothing to take here.")

    def show_inventory(self):
        if self.inventory:
            print("You have:", ', '.join(self.inventory))
        else:
            print("Your inventory is empty.")

    def play(self):
        print("Welcome to the Adventure Game!")
        self.describe_room()
        
        while True:
            command = input("> ").strip().lower()
            
            if command in ['quit', 'exit']:
                print("Thanks for playing!")
                break
            elif command.startswith('go '):
                direction = command.split(' ', 1)[1]
                self.move(direction.capitalize())
            elif command == "take":
                self.take_item()
            elif command == "inventory":
                self.show_inventory()
            else:
                print("Invalid command. Try 'go [direction]', 'take', or 'inventory'.")

if __name__ == "__main__":
    game = Game()
    game.play()