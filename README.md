Tennis Insights


Tennis Insights is an application that allows tennis players, coaches, parents to input their player’s match results to see realtime live scores and stats. Unlike many other match tracking apps out there, Tennis Insights will provide you valuable recommendations that you can use in match to improve your chances of winning. Utilized Monte Carlo methods to design and develop accurate simulations of tennis matches. Additionally, I integrated the application with Google+ API to provide login authentication and allow players to access trends of key stats using matplotlib and numpy. Designed clean and simple user interface while maintaining the complexity of the application. 

Languages: Python

Feel Free to Watch Video of Tennis Insights in Action:
https://www.youtube.com/watch?v=HVF5851zRSo&feature=youtu.be

-----
Python 3

Necessary Libraries

- Google Plus API 
--> https://developers.google.com/api-client-library/python/apis/plus/v1
--> $ pip install --upgrade google-api-python-client

- Matplotlib
--> https://matplotlib.org/users/installing.html
--> python -m pip install -U matplotlib

-----

Run the application by running __init__.py 

-----
Key Information to Run the Application

1. Login 
	- In order to login to Tennis Insights application using Google+ account. 

2. Match History
	- Match History is only accessible after >=2 matches have been played in your account

3. Home Screen
	- Access HELP screen, MATCH HISTORY, START MATCH screen, LOG OUT

4. Start Match
	- Choose between a 3 SET or 5 SET Match, and who is serving first in match (You or Opponent)

5. In Match
	- Select result of the serve (FIRST SERVE IN, SECOND SERVE IN, or DOUBLE FAULT)
	- Select result of the return (IN or OUT)
	- Select result of point (WON or LOST)
	- Access summary stats of match (50% is inserted as placeholder if no current stat)
	- Finish Match at anytime by clicking END GAME

6. Summary Stats
	- See summary stats for YOU and your OPPONENT in the current match
	- Click IMPROVE to run Monte Carlo Simulations to determine stats needed to win match and % chance of winning the match
		- Improve is only allowed after 3 or more games have been played and on changeover (odd games in current set)

7. Improve
	- View current stats
	- View stats needed to win match (AIM)

8. Match Over
	- View MATCH SUMMARY -- Match Stats
	- LOG OUT of your account
	- Go back HOME 
	- Tennis Insights automatically saves your match history when you LOG OUT or go back HOME

	
**** To test User/Account Settings & Match History ****
	--> Log Out of TennisInsights
	--> Move token.json to TennisInsights Directory (sampleToken --> token.json)
	--> Run Application and Log In
	--> App should not prompt for authentication and Match History is visible

-----
Application will create a token for Google+ API when logged in and remove token after logging out. Graphs for the current user (if any) are stored in graphs Folder. All users are stored in the users folder.
-----