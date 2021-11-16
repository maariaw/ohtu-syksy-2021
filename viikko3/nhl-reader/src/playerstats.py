class PlayerStats:
    def __init__(self, player_reader):
        self.reader = player_reader
    
    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        national_players = filter(
            lambda player : player.nationality == nationality,
            all_players
        )
        return sorted(national_players,
            key=lambda player: player.points, reverse=True)
