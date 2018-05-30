import sys
import json
sys.path.append('../..')

import match_updater
from flask import Blueprint, render_template, session, abort, request

requestedMatches = []
match_route = Blueprint('match_route', __name__)
@match_route.route("/worldcup2018/matches")
def match():
    requestedMatches.clear()
    date = request.args.get('date')
    team = request.args.get('team')

    for stage in match_updater.stages:
        if stage['name'] == 'groups':
            for groupName in match_updater.groupsArray:
                getRequestedMatches(date, team, stage[groupName]['matches'])
        else:
            getRequestedMatches(date, team, stage['matches'])

    return json.dumps(requestedMatches)


def getRequestedMatches(date, team, matches):
    for match in matches:
        if (match['date'] is date) or (match['home_team'] == str(team)) or (match['away_team'] == str(team)):
            requestedMatches.append(match)
