import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_correct_player(self):
        search = self.stats.search("Lemieux")
        
        self.assertEqual(str(search), "Lemieux PIT 45 + 54 = 99")

    def test_search_return_none_if_not_found(self):
        search = self.stats.search("Test")
        
        self.assertEqual(search, None)

    def test_top_1_is_correct(self):
        top1 = self.stats.top(0)

        self.assertEqual(str(top1[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_1_is_correct_assists(self):
        top1 = self.stats.top(0, SortBy.ASSISTS)

        self.assertEqual(str(top1[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_1_is_correct_goals(self):
        top1 = self.stats.top(0, SortBy.GOALS)

        self.assertEqual(str(top1[0]), "Lemieux PIT 45 + 54 = 99")

    def test_team_return_correct_players(self):
            result = self.stats.team("DET")

            self.assertEqual(str(result[0]), "Yzerman DET 42 + 56 = 98")
