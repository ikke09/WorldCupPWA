import urllib
import json

groupsArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
teams = []
flags = []
stages = []

def update_game_info():
    teams.clear()
    flags.clear()
    stages.clear()


    with urllib.request.urlopen("https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json") as url:
        data = json.loads(url.read().decode())

        for team in data['teams']:
            teams.append(team)

        stages.append(data['groups'])
        stages.append(data['knockout']['round_16'])
        stages.append(data['knockout']['round_8'])
        stages.append(data['knockout']['round_4'])
        stages.append(data['knockout']['round_2_loser'])
        stages.append(data['knockout']['round_2'])

        counter = 0
        for stage in stages:
            if counter == 0:
                stage['name'] = 'groups'
                for groupName in groupsArray:
                    map_team_id_to_name(stage[groupName]['matches'])
            else:
                map_team_id_to_name(stage['matches'])
            counter = counter + 1

def map_team_id_to_name(matches):
    for match in matches:
        if (type(match['home_team']) is int) and (type(match['away_team']) is int):
            if not(match['home_team'] > len(teams)) or not(match['away_team'] > len(teams)):
                match['home_flag'] = teams[match['home_team'] - 1]['flag']
                match['away_flag'] = teams[match['away_team'] - 1]['flag']
                match['home_team'] = teams[match['home_team'] - 1]['name']
                match['away_team'] = teams[match['away_team'] - 1]['name']