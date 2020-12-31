from unittest import TestCase
from yahoofantasybball.NBAFantasyAPI import NBAFantasy

class TestNBAFantasy(TestCase):
    def setUp(self) -> None:
        self.nbafantasy = NBAFantasy() #todo - cache the data after first run.
        pass

    def test_get_player_from_name(self):
        first = "Lebron"
        last = "James"
        player = self.nbafantasy.get_player_from_name(first, last)
        assert player.name == "Lebron James"

    def test_get_teams(self):
        teams = self.nbafantasy.get_teams()
        for t in teams:
            print(t)
        assert len(teams) == 4

    def test_get_team_from_name(self):
        team_name = ""
        teams = self.nbafantasy.get_teams()
        for t in teams:
            team_name = t
        team2 = self.nbafantasy.get_teams()[team_name]
        print(team_name)
        assert team_name == team2.name

    def test_get_players_from_team(self):
        teams = self.nbafantasy.get_teams()
        t = ""
        for t in teams:
            break
        players = teams[t].roster
        assert len(players) > 0

    def test_get_player_stats(self):
        teams = self.nbafantasy.get_teams()
        t = ""
        for t in teams:
            break
        player = teams[t].roster[0]
        points = player.fantasy_points_by_week()
        point = points[0]
        injured = player.injured()
        games = player.projected_games_this_week()


