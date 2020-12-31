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
    
Example result:<br>

<table cellspacing="0" border="0">
	<colgroup width="231"></colgroup>
	<colgroup span="3" width="68"></colgroup>
	<colgroup width="414"></colgroup>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Team Not here</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom sdval="44196.3293636343" sdnum="1033;0;[$-F800]DDDD\, MMMM DD\, YYYY"><font color="#000000">Thursday, December 31, 2020</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">-------------------------</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Player Name                   </font></td>
		<td align="left" valign=bottom><font color="#000000">Season Ave</font></td>
		<td align="left" valign=bottom><font color="#000000">Games     </font></td>
		<td align="left" valign=bottom><font color="#000000">Proj Pts   </font></td>
		<td align="left" valign=bottom><font color="#000000">Injury Report</font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">CJ McCollum                   </font></td>
		<td align="left" valign=bottom sdval="53.33" sdnum="1033;"><font color="#000000">53.33</font></td>
		<td align="left" valign=bottom sdval="3" sdnum="1033;"><font color="#000000">3</font></td>
		<td align="left" valign=bottom sdval="159.98" sdnum="1033;"><font color="#000000">159.98</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Jrue Holiday                  </font></td>
		<td align="left" valign=bottom sdval="39.04" sdnum="1033;"><font color="#000000">39.04</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="156.16" sdnum="1033;"><font color="#000000">156.16</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Russell Westbrook             </font></td>
		<td align="left" valign=bottom sdval="50.8" sdnum="1033;"><font color="#000000">50.8</font></td>
		<td align="left" valign=bottom sdval="3" sdnum="1033;"><font color="#000000">3</font></td>
		<td align="left" valign=bottom sdval="152.4" sdnum="1033;"><font color="#000000">152.4</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Kyrie Irving                  </font></td>
		<td align="left" valign=bottom sdval="39.2" sdnum="1033;"><font color="#000000">39.2</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="156.8" sdnum="1033;"><font color="#000000">156.8</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">LeBron James                  </font></td>
		<td align="left" valign=bottom sdval="49.2" sdnum="1033;"><font color="#000000">49.2</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="196.8" sdnum="1033;"><font color="#000000">196.8</font></td>
		<td align="left" valign=bottom><font color="#000000">injured, Ankle, Game Time Decision</font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Anthony Davis                 </font></td>
		<td align="left" valign=bottom sdval="32.62" sdnum="1033;"><font color="#000000">32.62</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="130.48" sdnum="1033;"><font color="#000000">130.48</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">LaMarcus Aldridge             </font></td>
		<td align="left" valign=bottom sdval="18.65" sdnum="1033;"><font color="#000000">18.65</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="74.6" sdnum="1033;"><font color="#000000">74.6</font></td>
		<td align="left" valign=bottom><font color="#000000">injured, Knee, Expected to be out until at least Jan 1</font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Myles Turner                  </font></td>
		<td align="left" valign=bottom sdval="40.3" sdnum="1033;"><font color="#000000">40.3</font></td>
		<td align="left" valign=bottom sdval="3" sdnum="1033;"><font color="#000000">3</font></td>
		<td align="left" valign=bottom sdval="120.9" sdnum="1033;"><font color="#000000">120.9</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Rudy Gobert                   </font></td>
		<td align="left" valign=bottom sdval="49.27" sdnum="1033;"><font color="#000000">49.27</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="197.07" sdnum="1033;"><font color="#000000">197.07</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Andre Drummond                </font></td>
		<td align="left" valign=bottom sdval="63.8" sdnum="1033;"><font color="#000000">63.8</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="255.2" sdnum="1033;"><font color="#000000">255.2</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Chris Paul                    </font></td>
		<td align="left" valign=bottom sdval="36" sdnum="1033;"><font color="#000000">36</font></td>
		<td align="left" valign=bottom sdval="3" sdnum="1033;"><font color="#000000">3</font></td>
		<td align="left" valign=bottom sdval="108" sdnum="1033;"><font color="#000000">108</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Joel Embiid                   </font></td>
		<td align="left" valign=bottom sdval="45.5" sdnum="1033;"><font color="#000000">45.5</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="182" sdnum="1033;"><font color="#000000">182</font></td>
		<td align="left" valign=bottom><font color="#000000">injured, Back, Game Time Decision</font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Kyle Lowry                    </font></td>
		<td align="left" valign=bottom sdval="47.1" sdnum="1033;"><font color="#000000">47.1</font></td>
		<td align="left" valign=bottom sdval="4" sdnum="1033;"><font color="#000000">4</font></td>
		<td align="left" valign=bottom sdval="188.4" sdnum="1033;"><font color="#000000">188.4</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	<tr>
		<td height="20" align="left" valign=bottom><font color="#000000">Damian Lillard                </font></td>
		<td align="left" valign=bottom sdval="44.27" sdnum="1033;"><font color="#000000">44.27</font></td>
		<td align="left" valign=bottom sdval="3" sdnum="1033;"><font color="#000000">3</font></td>
		<td align="left" valign=bottom sdval="132.82" sdnum="1033;"><font color="#000000">132.82</font></td>
		<td align="left" valign=bottom><font color="#000000"><br></font></td>
	</tr>
	</table>
