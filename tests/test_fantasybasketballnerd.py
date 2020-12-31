from unittest import TestCase
from yahoofantasybball.fantasybasketballnerd import FantastyBasketballNerd


class TestFantastBasketballNerd(TestCase):
    def test_read_url(self):
        bball = FantastyBasketballNerd()
        bball.readPlayers()


class TestFantastBasketballNerd(TestCase):
    def test_read_team_schedule(self):
        bball = FantastyBasketballNerd()
        bball.readTeamSchedule(bball.players["LeBron James"].team)
        print(bball.players["LeBron James"].team)
        print("done")


class TestFantastBasketballNerd(TestCase):
    def test_week_start(self):
        bball = FantastyBasketballNerd()
        weekstart, weekend = bball.weekStartEnd(1)
        print(str(weekstart) + "  " + str(weekend))


class TestFantastBasketballNerd(TestCase):
    def test_number_player_games_week(self):
        bball = FantastyBasketballNerd()
        for i in range(10):
            numgames = bball.numberPlayerGamesWeek("LeBron James", i)
            print(numgames)
