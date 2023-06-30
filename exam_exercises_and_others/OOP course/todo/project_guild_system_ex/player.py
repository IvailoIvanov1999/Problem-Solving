from typing import Dict

class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str:int] = {}  # skills:key  mana_cost:value
        self.guild: str = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:

        output = ''
        for k, v in self.skills.items():
            output += f'==={k} - {v}' + '\n'

        return f'Name: {self.name}\n' + \
               f'Guild: {self.guild}\n' + \
               f'HP: {self.hp}\n' + \
               f'MP: {self.mp}\n' + \
               output

