
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        result = []
        players = self.reader.get_players()

        players.sort(key = lambda player: player.goals+player.assists, reverse=True)
        for player in players:
            if player.nationality == nationality:
                result.append(player)
        
        return result
    