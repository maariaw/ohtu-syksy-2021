import requests
from player import Player
from datetime import date, datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

#    print("JSON-muotoinen vastaus:")
#    print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == "FIN":
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            players.append(player)

    ranked = sorted(players, key=lambda player: player.points, reverse=True)

    print("Players from Finland", datetime.now().strftime("%d.%m.%Y %H:%M"))

    for player in ranked:
        print(player)

if __name__ == "__main__":
    main()