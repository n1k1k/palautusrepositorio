from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
from ui import UI

def main():
    view = UI()

    while True:
        s = view.choose_season()
        if s == "":
            break
        url = "https://studies.cs.helsinki.fi/nhlstats/" + s +"/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        view.stats = stats

        while True:
            n = view.choose_nationality()
            if n == "":
                break
            players = stats.top_scorers_by_nationality(n)
            view.top_player_by_nationality(players)

    

if __name__ == "__main__":
    main()
