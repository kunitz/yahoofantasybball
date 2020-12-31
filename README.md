# yahoofantasybball

Project dependencies:
- https://github.com/uberfastman/yfpy
   This is a yahoo fantasy sports API wrapper.
   
- Setup specific for your yahoo account:
    see https://github.com/uberfastman/yfpy/blob/develop/README.md
    see the YahooLeagueData class in NBAFantasyAPI.py to find the specific updates for your league
    Game keys in the initialize_yahoo() function may also need to be updated for future seasons.
    
- Using the program:
    Run "main.py" from the console or terminal. 
    From the terminal you can pass in the team name as an argument to only list a single team in the results.
    The results are tab delimited, so can be copied to a spreadsheet for printing/sharing.
    
Example result:

Team Not here
2020-12-31 11:09:53.710217
-------------------------
Player Name                   	Season Ave	Games     	Proj Pts   	Injury Report
CJ McCollum                   	53.33     	3         	159.98    	
Jrue Holiday                  	39.04     	4         	156.16    	
Russell Westbrook             	50.80     	3         	152.40    	
Kyrie Irving                  	39.20     	4         	156.80    	
LeBron James                  	49.20     	4         	196.80    	injured, Ankle, Game Time Decision
Anthony Davis                 	32.62     	4         	130.48    	
LaMarcus Aldridge             	18.65     	4         	74.60     	injured, Knee, Expected to be out until at least Jan 1
Myles Turner                  	40.30     	3         	120.90    	
Rudy Gobert                   	49.27     	4         	197.07    	
Andre Drummond                	63.80     	4         	255.20    	
Chris Paul                    	36.00     	3         	108.00    	
Joel Embiid                   	45.50     	4         	182.00    	injured, Back, Game Time Decision
Kyle Lowry                    	47.10     	4         	188.40    	
Damian Lillard                	44.27     	3         	132.82    	
-------------------------
