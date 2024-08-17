#Tanmayee Kolli

import TK_game_DataBase
from TK_game_Objects import Character, Hero, Monster, CharacterList

'''
This is the user interface which uses the methods from the Business class to
add, delete, or show the list of characters a player can play with. The player can
also play with the characters, which consists of either attacking a target, using a special
power, or canceling a turn. If the health points of a character reaches 0,
it is defeated. The stats of the characters are updated after every turn.
'''


def list_charac(character_list): #this function shows a list of all the characters and their stats
    print("Available Characters:")
    print()
    character_list.display_list()
    print()

def add(character_list):
    name=input("Name: ")
    
    while True: #checking for health points
        try:
            hp=int(input("Health Points (1-200): "))
            if 1 <= hp <= 200:
                break
            else:
                print("Health Points need to be between 1 and 200. Please try again")
        except ValueError:
            print("Please enter an integer...")   

    while True: #checking for attack
        try:
            atk=int(input("Attack (1-200): "))
            if 1 <= atk <= 200:
                break
            else:
                print("Attack need to be between 1 and 200. Please try again")
        except ValueError:
            print("Please enter an integer...")

    while True: #checking for defense
        try:
            defe=int(input("Defense (1-200): "))
            if 1 <= defe <= 200:
                break
            else:
                print("Defense need to be between 1 and 200. Please try again")
        except ValueError:
            print("Please enter an integer...")

       
    char_type=input("Select character type (Hero/Monster): ").lower()

    while char_type not in ["hero", "monster"]: #checking if the character type is valid
            print("Please select a valid character type")
            char_type=input("Select character type (Hero/Monster): ").lower()
        
        
    if char_type=="hero": #a hero can be a warrior or healer, but a monster can only be a boss
        role=input("Role (Warrior/Healer): ").lower()
        
        while role not in ["warrior", "healer"]:
            print("Please select a valid role")
            role=input("Role (Warrior/Healer): ").lower()
            
    else:
        role="boss"
    

    
    if 1<=hp<=200 and 1<=atk<=200 and 1<=defe<=200: #we are updating the character list
        if char_type=="Hero":
            character=Hero(name,hp,atk,defe,role)
        else:
            character=Monster(name,hp,atk,defe,role)
        character_list.addCharacter(character)
        TK_game_DataBase.write_characters(character_list)
        print("Character successfully added")
        print()
    else:
        print("Invalid input! Character not added.")
        print()

def dele(character_list): #this code deletes charaters from the list
    while True:
        ch=input("Enter name of the character to remove: ").lower()
        character=character_list.getCharacter(ch)
        if character is not None:
            character_list.removeCharacter(ch)
            TK_game_DataBase.write_characters(character_list)
            print("Character removed successfully")
            print()
            break
        else:
            print(f"No character named {ch}. Please try again.")
            continue
        
    

def play(character_list): #this function allows us to play certain commands
    while True:
        name=input("Enter name of the character to select: ")
        character=character_list.getCharacter(name)
        if character is None:
            print(f"No character named {name}. Please try again.")
            continue
        else:
            print(f"{name} selected")
            break

    print("ACTIONS:") #these are the options for playing
    print("Attack     - Attack another character")
    print("Special    - Use special move on another character")
    print("Cancel     - Cancel turn")
    action=input("Select action: ")
    
    while action not in ["Attack", "Special", "Cancel"]:
        print("Please enter a valid action..")
        print()
        action=input("Select action: ")
    
    if action == "Attack": #attack reduces a target's health points
        target_name = input("Enter name of the target: ")
        target_character = character_list.getCharacter(target_name)
        if target_character is None:
            print(f"No character named {target_name}. Please try again.")
            target_name = input("Enter name of the target: ")
        else:
            character.attack(target_character)

    elif action == "Special": #this is specific to a role and is outlined in the Objects file
        target_name = input("Enter name of the target: ")
        target_character = character_list.getCharacter(target_name)
        if target_character is None:
            print(f"No character named {target_name}. Please try again.")
            target_name = input("Enter name of the target: ")
        else:
            character.special_move(target_character)
                
                
def main():
    print('Welcome to My Game!')# intro
    print()
    print("COMMAND MENU")
    print("List     - List all characters")
    print("Add      - Add a character")
    print("Delete   - Delete a character")
    print("Play     - Select a character and Play")
    print("Exit     - Exit program")
    print()
    print('Please add at least two characters to continue...')

    character_list=CharacterList()

    print("Character 1:") #mandatory addition of two characters before commands
    add(character_list)
    print("Character 2:")
    add(character_list)

    while True: 
        command=input("Command: ").lower()
        if command=="list":
            list_charac(character_list)
        elif command=="add":
            add(character_list)
            list_charac(character_list)
        elif command=="delete":
            dele(character_list)
            list_charac(character_list)
        elif command=="play":
            play(character_list)
            list_charac(character_list)
        elif command=="exit":
            TK_game_DataBase.write_characters(character_list)
            print("Saving characters...")
            print("Thank you for playing! Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            print()
if __name__=="__main__":
    main()
        
