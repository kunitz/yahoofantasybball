## Logan Kunitz
## API for analyzing NBA Fantasy
import math
from datetime import datetime, timedelta

from yfpy import YahooFantasySportsQuery

class NBAPlayer:
    def __init__(self):
        #public data
        self.name = ""
        self.positions = list()
        self.selected_position = ""
        self.ownerteam = ""
        self.seasonpoints = 0
        #private data
        self.__games_by_week = list()
        self.__fantasypoints_by_week = list()


    def new(self, name, positions=list(), ownerteam="", games_by_week=list(), fantasypoints_by_week=list()):
        self.name = name
        self.positions = positions
        self.ownerteam = ownerteam
        self.__games_by_week = games_by_week
        self.__fantasypoints_by_week = fantasypoints_by_week


class NBATeam:
    players = list() #fill with players
    name = ""
    id = ""

class YahooLeagueData:
    statsdisable = False
    players = list() #fill with datatype NBAPlayer
    teams = list() #fill with datatype NBATeam

    def __init__(self, week="next"):
        #todo - update this with your own fantasy league values
        self.week = week
        consumer_key = "dj0yJmk9RU5nY0M3aGNuWVVQJmQ9WVdrOWMwODRlbk4xUVZNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ3",
        consumer_secret = "b84c5592dbecc76e2979c068c5950d8b39561b33",
        self.yahoo_data = self.initialize_yahoo('45255', consumer_key, consumer_secret, 'nba', '2020')
        #self.yahooplayers = self.yahoo_data.get_league_players()
        self.yahooteams = self.yahoo_data.get_league_teams()
        self.teams = self.parseyahooteams(self.yahooteams)
        #self.players = self.parseyahooplayers(self.yahooplayers)


    def parseyahooteams(self, yahooteams):
        teams = []
        for t in yahooteams:
            team = NBATeam()
            team.name = t["team"].name.decode("ascii")  # name formatted a b"<team name>"
            team.id = t["team"].team_id
            #teammatchup = self.getmatchup(t["team"].team_id)
            #for m in teammatchup:
            #    for t2 in m["matchup"].teams:
            #        pass
            team.players = self.getteamroster(t["team"].team_id, self.week)
            teams.append(team)
        return teams

    def getkeys(self):
        return self.yahoo_data.get_all_yahoo_fantasy_game_keys()

    def getplayerstats(self, player_key):
        #stats = self.yahoo_data.get_player_stats_by_week(player_key, 1)
        #stats = self.yahoo_data.get_player_stats_by_date(player_key)
        stats = self.yahoo_data.get_player_stats_for_season(player_key)
        return stats


    def getteamroster(self,team_id,week="next"):
        week_param = week
        if week == "next":
            yahooroster = self.yahoo_data.get_team_roster_by_week(team_id, "1")
            initialweek = yahooroster.extracted_data["date"]
            date = datetime.strptime(initialweek, '%Y-%m-%d')  # format: 2020-12-22 19:00:00
            oneweek = timedelta(days=7)
            week_param = math.ceil((datetime.today() - date) / oneweek) + 2  #apparently the first week starts at 2.
        yahooroster = self.yahoo_data.get_team_roster_by_week(team_id, week_param)
        #yahooroster = self.yahoo_data.get_team_roster_player_info_by_week(team_id, 0)
        players = list()

        for p in yahooroster.players:
            player = NBAPlayer()
            player_name = p["player"].name.full
            if not self.statsdisable:
                playerstats = self.getplayerstats(p["player"].player_key)
                player.seasonpoints = playerstats.player_points_value
            player.selected_position = p['player'].selected_position_value
            positions = list()
            for i in p['player'].eligible_positions:
                positions.append(i['position'])
            player.new(player_name, positions)
            players.append(player)
        return players

    def getmatchup(self, team_id):
        return self.yahoo_data.get_team_matchups(team_id)

    def initialize_yahoo(self, league_id, consumer_key, consumer_secret, game_code = 'nba', season = '2020'):
        # Example vars using public Yahoo league (still requires auth through a personal Yahoo account - see README.md)
        # game_key = "399"  # NFL 2020 game key

        game_keys = {
            'nba2020':'402',
            'nba2019':'395',
            'nba2018':'381'
        }

        game_key = game_keys[game_code+season]
        # game_key = "402"  # NBA 2020 game key
        # game_key = "395" # NBA 2019
        # game_key = "385" # NBA 2018
        # game_key = "331"
        # game_key = "390"
        # game_key = "303"  # NHL
        # game_key = "348"  # divisions

        # game_code = "nba"
        # game_code = "nfl"
        # game_code = "nhl"  # NHL

        # season = "2014"
        # season = "2019"
        # season = "2020"
        # season = "2012"  # NHL
        # season = "2015"  # divisions

        # league_id = "45255"   # 2020 to 2021 quarantine NBA league
        # league_id = "89912" # 2019 to 2020 NBA league
        # league_id = "896385"  # quarantine football league
        # league_id = "655434"
        # league_id = "729259"
        # league_id = "79230"
        # league_id = "69624"  # NHL
        # league_id = "907359"  # divisions

        return YahooFantasySportsQuery(
            "",  # Auth directory where "private.json" is located (default to ".")
            league_id,  # League ID
            game_id=game_key,
            game_code=game_code,
            offline=False, # this will use cached data if set to true - at least in theory
            all_output_as_json=False,
            # consumer_key=os.environ["YFPY_CONSUMER_KEY"],
            # consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            browser_callback=True
        )

    def parseyahooplayers(self, yahooplayers):
        players = list()
        for p in yahooplayers:
            positions = list()
            player = NBAPlayer()
            player_name = p["player"].name.full
            yahoo_positions = p["player"].eligible_positions
            for pos in yahoo_positions:
                positions.append(pos["position"])
            ownerteam = p["player"].ownership.owner_team_name
            player.new(player_name, positions, ownerteam)
            players.append(player)
        return players




class NBAFantasy:
    statsdisable = False

    def __init__(self, week="next"):
        YahooLeagueData.statsdisable = self.statsdisable
        self.yahoodata = YahooLeagueData(week)
        pass

    def get_player_from_name(self, first, last) -> NBAPlayer:
        player = NBAPlayer()
        player.name = first + " " + last
        return player

    def get_teams(self):
        teams_dict = dict()
        teams = self.yahoodata.teams
        for t in teams:
            teams_dict[t.name] = t
        return teams_dict

    def get_players(self):
        players = self.yahoodata.players
        return players

    def print_game_keys(self):
        for key in self.yahoodata.getkeys():
            print(key)
