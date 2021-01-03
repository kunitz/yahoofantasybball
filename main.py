# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import sys
import threading
import time
from datetime import datetime

from NBAFantasyAPI import NBAFantasy, NBAPlayer
from fantasybasketballnerd import FantastyBasketballNerd

def dotsOnTheUI():
    global stopdots
    stopdots = False
    while not stopdots:
        print('.', end='')
        sys.stdout.flush()
        time.sleep(0.3)
    print('\n')

def addwhitespace(s, width):
    s2 = s
    for x in range(width - len(s)):
        s2 += " "
    return s2

def printDate():
    print(datetime.today())


def write_header():
    print(addwhitespace("Player Name", 30) + "\t" + addwhitespace("Season Ave",10) + "\t" +
          addwhitespace("Games", 10) + "\t" + addwhitespace("Proj Pts",10), "\t" + "Injury Report")


def write_player_line(name, games_this_week, seasonpoints, gamesplayed, injuryreport):
    averagepoints = seasonpoints / gamesplayed
    proj_points = averagepoints * games_this_week
    print(addwhitespace(name, 30) + "\t" + addwhitespace("%.2f" % averagepoints, 10) + "\t" + addwhitespace(
        str(games_this_week), 10) + "\t" + addwhitespace("%.2f" % proj_points,
                                                         10) + "\t" + injuryreport)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #debug stuff
    #NBAFantasy.statsdisable = True
    week = "next" #use this to manually configure week from 1.. "current" and "next" are also supported.
    ####
    thread = threading.Thread(target=dotsOnTheUI,args=())
    print("Collecting Team Info...")
    thread.start()
    log = logging.getLogger('yfpy.query') #the logger in this file isn't turning off in non-debug mode.
    log.disabled = True
    League = NBAFantasy(week)
    SchedLeague = FantastyBasketballNerd()
    teams = League.get_teams()
    teamindex = -1
    iteration = 0
    stopdots = True             #send signal to terminate progress thread
    while thread.is_alive():    #wait until thread completes
        pass
    if(len(sys.argv) > 1):
        teamindex = sys.argv[1]
    for t in teams:
        if (teamindex == -1) or (teamindex == t) or (teamindex == str(iteration)) or (teamindex == "teams"):
            teamplayers = teams[t].players
            print("Team " + teams[t].name)
            printDate()
            print("-------------------------")
            write_header()
            if teamindex != "teams":
                for player in teamplayers:
                    assert isinstance(player, NBAPlayer)
                    games_this_week = SchedLeague.numberPlayerGamesWeek(player.name, 0)
                    seasonpoints = player.seasonpoints
                    gamesplayed = SchedLeague.numberPlayerGamesPlayed(player.name)
                    write_player_line(player.name, games_this_week, seasonpoints, gamesplayed,
                                      SchedLeague.getPlayerInjured(player.name))
                print("-------------------------")
                print("")
        iteration+=1


# Yahoo API Details for Logan_Kunitz account
# App ID: sO8zsuAS
# Client ID: dj0yJmk9RU5nY0M3aGNuWVVQJmQ9WVdrOWMwODRlbk4xUVZNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ3
# Client Secret: b84c5592dbecc76e2979c068c5950d8b39561b33


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
