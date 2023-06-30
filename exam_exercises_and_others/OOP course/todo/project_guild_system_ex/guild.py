from project_guild_system_ex.player import Player
from typing import List


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []  # list of players

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            player = next(filter(lambda x: x.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = Player.DEFAULT_GUILD
        return f"Player {player.name} has been removed from the guild."

    def guild_info(self) -> str:
        player_info = '\n'.join([p.player_info() for p in self.players])

        return f"Guild: {self.name}\n" + \
               f"{player_info}"


