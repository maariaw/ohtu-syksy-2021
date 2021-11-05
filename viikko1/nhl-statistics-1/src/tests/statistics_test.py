import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_existing_player(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_if_no_player(self):
        player = self.statistics.search("zzzz")
        self.assertIsNone(player)

    def test_team_finds_all_members(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_team_finds_empty_list_if_false_team_name(self):
        self.assertEqual(len(self.statistics.team("HOT")), 0)

    def test_top_scorers_finds_best_player(self):
        best = self.statistics.top_scorers(3)[0]
        self.assertEqual(best.name, "Gretzky")

    def test_top_scorers_finds_worst_player(self):
        best = self.statistics.top_scorers(5)[4]
        self.assertEqual(best.name, "Semenko")

    def test_top_scorers_finds_right_amount_of_players(self):
        top_three = self.statistics.top_scorers(3)
        self.assertEqual(len(top_three), 3)

    def test_top_scorers_works_if_more_than_total_players_requested(self):
        top_three = self.statistics.top_scorers(10)
        self.assertEqual(len(top_three), 5)