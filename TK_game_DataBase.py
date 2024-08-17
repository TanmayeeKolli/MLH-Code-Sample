import TK_game_Objects

def write_characters(CharacterList):
    with open("characters.txt", "w") as file:
        for character in CharacterList:
            file.write(f"{character.name},{character.hp}, {character.atk}, {character.defense}, {character.role}")

def get_characters():
    list=CharacterList()
    with open("characters.txt", "r") as file:
        lines=file.readlines()
        for line in lines:
            if line[4]=="boss":
                character=Monster(name, int(hp), int(atk), int(defense), role)
            elif line[4]=="healer" or line[4]=="warrior":
                charater=Hero(name, int(hp), int(atk), int(defense), role)
            list.addCharacter(character)
    return list
