import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


class FantastyBasketballNerd:
    __scheduleurl = "https://www.fantasybasketballnerd.com/service/schedule/"
    __playersurl = "https://www.fantasybasketballnerd.com/service/players/"
    __teamsurl = "https://www.fantasybasketballnerd.com/service/teams/"
    __injuriesurl = "https://www.fantasybasketballnerd.com/service/injuries/"
    __depthcharturl = "https://www.fantasybasketballnerd.com/service/depth/{TEAM_CODE}"


    class AppURLopener(urllib.request.FancyURLopener):
        version = "Mozilla/5.0"

    teams = dict()
    players = dict()

    class Injury:
        def __init__(self):
            self.injured = False
            self.injurytext = ""

    class Player:
        def __init__(self):
            self.name = ""
            self.team = ""
            self.id = ""
            self.injury = FantastyBasketballNerd.Injury()


    class Team:
        def __init__(self):
            self.code = ""
            self.name = ""
            self.schedule = list()

    def __readURL(self, url):
        opener = self.AppURLopener()
        webpage = opener.open(url)
        myfile = webpage.read()
        return myfile

    def __init__(self):
        self.__initPlayers()
        self.__initTeams()
        self.__initSchedule()


    def __initPlayers(self):
        playerxml = ET.fromstring(self.__readURL(self.__playersurl))
        injuryxml = ET.fromstring(self.__readURL(self.__injuriesurl))
        injuries = dict()
        for t in injuryxml.findall('Team'):
            for i in t.findall('Player'):
                injury = self.Injury()
                injury.injured = True
                injury.injurytext = i.find('injury').text + ", " + i.find('notes').text
                injuries[i.find('name').text] = injury

        for p in playerxml.findall('Player'):
            player = self.Player()
            player.name = p.find('name').text
            player.id = p.find('playerId').text
            player.team = p.find('team').text #team code
            if player.name in injuries:
                player.injury = injuries[player.name]
            else:
                player.injury.injured = False
                player.injury.injurytext = ""
            if player.name == "C.J. McCollum":
                player.name = "CJ McCollum"
            self.players[player.name] = player

    def __initTeams(self):
        xml = ET.fromstring(self.__readURL(self.__teamsurl))
        for t in xml.findall('Team'):
            team = self.Team()
            team.code = t.find('code').text
            team.name = t.find('name').text
            self.teams[team.code] = team

    def __initSchedule(self):
        xml = ET.fromstring(self.__readURL(self.__scheduleurl))
        for g in xml.findall('Game'):
            date = datetime.strptime(g.find('gameDate').text, '%Y-%m-%d %H:%M:%S') #format: 2020-12-22 19:00:00
            away = g.find('away').text #away team code
            home = g.find('home').text  # home team code
            self.teams[away].schedule.append(date)
            team1 = self.teams[away]
            self.teams[home].schedule.append(date)
            team2 = self.teams[home]

    def readTeamSchedule(self, teamCode):
        team = self.teams[teamCode]
        assert isinstance(team, self.Team)
        return team.schedule

    def weekStartEnd(self, week):
        offset = timedelta(days = 7 - datetime.today().weekday())
        oneweek = timedelta(days=7)
        weekstart =  datetime.today() + offset + (week * oneweek)
        weekstart = weekstart.replace(hour = 0)
        weekend = weekstart + oneweek
        return weekstart, weekend

    def numberPlayerGamesWeek(self, name, week=0):
        schedule = self.readTeamSchedule(self.players[name].team)
        weekstart, weekend = self.weekStartEnd(week)
        numgames = 0
        for d in schedule:
            if ((d > weekstart) and (d < weekend)):
                numgames += 1
        return numgames

    def numberPlayerGamesPlayed(self, name):
        schedule = self.readTeamSchedule(self.players[name].team)
        numgames = 0
        for d in schedule:
            if (d < datetime.today()):
                numgames += 1
        return numgames

    def getPlayerInjured(self, name):
        injurytext = ""
        if self.players[name].injury.injured:
            injurytext = "injured, " + self.players[name].injury.injurytext
        return injurytext

