from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

class UI:
    def __init__(self, stats = None, season = None, nationality = None):
        self.stats = stats
        self.season = season
        self.nationality = None

    def choose_season(self):
        self.season = Prompt.ask("Select season", choices=["2018-19","2019-20","2020-21", "2021-22", "2022-23", "2023-24", "2024-25", ""])
        return self.season
    
    def choose_nationality(self):
        self.nationality = Prompt.ask("Select nationality", choices=["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS" ,"CAN", "LAT", "BLR" "SLO", "USA", "FIN", "GBR", ""])
        return self.nationality
    
    def top_player_by_nationality(self, players):
        table = Table(title=f"Top scorers of {self.nationality} season {self.season}")
        table.add_column("name", justify="left", style="cyan", no_wrap=True)
        table.add_column("team", justify="left", style="magenta", no_wrap=True)
        table.add_column("goals", justify="right", style="green")
        table.add_column("assits", justify="right", style="green")
        table.add_column("points", justify="right", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals+player.assists))
        
        console = Console()
        console.print(table)