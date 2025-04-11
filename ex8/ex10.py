import json


def sort_by_points(player):     # Sorting helper function
    return player["points"]

# Part 1
def main():

    # Asking for filename; trying to open the chosen file
    file = input("Enter filename: ")
    try:                                # Attempts to open the file
        with open(file) as players_data:
            contents = players_data.read()
    except Exception as e:
        print(f"Error: {e}")
        return      # failsafe

    all_players = json.loads(contents)  # Converts JSON string to Python list of dicts
    print(f"File {file} loaded successfully! \n")

    try:
        while True:
               
            print("Available commands: \n")
            choice = input(
                "Quit - press 0 \n " \
                "Search for player - press 1 \n" \
                "Teams - press 2 \n" \
                "Countries - press 3 \n" \
                "Players in the team - press 4 \n" \
                "Players from the country - press 5 \n" \
                "Most points - press 6 \n" \
                "Most goals - press 7 \n" \
            )

            if choice.isdigit():
                choice = int(choice)

                if choice == 0:     # Quit
                    break

                if choice == 1:     # Search for player
                    searched_player = input("Player name: ")
                    found = False 

                    for player in all_players:
                        if player["name"].lower() == searched_player.lower():
                            print(f"{player['name']}   {player['team']}  {player['goals']} + {player['assists']}")
                            found = True
                            break

                    if not found:
                        print("Player not found! \n")

                if choice == 2:     # Print team codes alphabetically
                    teams = set()
                    for player in all_players:
                        teams.add(player["team"])
                    for team in sorted(teams):
                        print(team)

                if choice == 3:     # Print country codes alphabetically
                    countries = set()
                    for player in all_players:
                        countries.add(player["nationality"])
                    for country in sorted(countries):
                        print(country)

                # Part 2:
                if choice == 4:     # Print players in the team, descending points
                    
                    team_name = input("Team code (3 letters): ").upper()
                    team_players = [player for player in all_players if player["team"] == team_name]

                    for player in team_players:     # Calculating points
                        player["points"] = player["goals"] + player["assists"]

                    team_players.sort(key=sort_by_points, reverse=True)   # Sorts players by highest score

                    if team_players:
                        for player in team_players:
                            print(f"{player['name']}   {player['team']}   {player['goals']} + {player['assists']} = {player['points']}")
                    else:
                        print(f"No players found in a given team - {team_name}")
            
                if choice == 5:     # Print players in the country, descending points
                    country_name = input("Country code (3 letters): ").upper()
                    country_players = [player for player in all_players if player["nationality"] == country_name]

                    for player in country_players:     # Calculating points
                        player["points"] = player["goals"] + player["assists"]

                    country_players.sort(key=sort_by_points, reverse=True)  # Sorts players by highest score

                    if country_players:
                        for player in country_players:
                            print(f"{player['name']}   {player['team']}   {player['goals']} + {player['assists']} = {player['points']}")
                    else:
                        print(f"No players found in a given country - {country_name}")
                    
                #if choice == 6:

                #if choice == 7:


            else:
                print("Enter a number from 0 to 7!")
    
    except Exception as e:
        print(f"Unknown error! {e}")

main()

