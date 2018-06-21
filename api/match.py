import sys
import json

import match_updater
from flask import Blueprint, render_template, session, abort, request

from dateutil import parser

from datetime import date
from datetime import timedelta

requestedMatches = []
match_route = Blueprint('match_route', __name__)
@match_route.route("/worldcup2018/matches")
def match():
    requestedMatches.clear()
    date = request.args.get('date')
    team = request.args.get('team')

    requestedStage = request.args.get('stage')
    requestedGroup = request.args.get('group')
    print(requestedStage)

    # all, upcoming (does not equal todays date), or today(does equal todays date)
    filterName = request.args.get('filter')
    print(filterName)
    returnArr = []

    if date or team:
        for stage in match_updater.stages:
            if stage['name'] == 'groups':
                for groupName in match_updater.groupsArray:
                    getRequestedMatches(date, team, stage[groupName]['matches'])
            else:
                getRequestedMatches(date, team, stage['matches'])
        return json.dumps(requestedMatches)
    
    else:
        if filterName is None:
            if requestedStage == 'groups':
                if requestedGroup == 'all':
                    return json.dumps(match_updater.stages[0])
                else:
                    filteredStage = [
                        stage for stage in match_updater.stages if stage['name'] == str(requestedStage)]
                    return json.dumps(filteredStage[0][str(requestedGroup)])
            elif requestedStage != '':
                filteredStage = [
                    stage for stage in match_updater.stages if stage['name'] == str(requestedStage)]
                return json.dumps(filteredStage)
        else:
            returnArr = applyFilter(filterName)
        
        return json.dumps(returnArr)


def getRequestedMatches(date, team, matches):
    for match in matches:
        if (match['date'] is date) or (match['home_team'] == str(team)) or (match['away_team'] == str(team)):
            requestedMatches.append(match)

def applyFilter(filterName):
    returnArr = []

    groupStage = [
        stage for stage in match_updater.stages if stage['name'] == 'groups']
    knockoutStages = [
        stage for stage in match_updater.stages if stage['name'] != 'groups']

    if filterName == 'all':
        for groupName in match_updater.groupsArray:
            returnArr.append(groupStage[0][groupName])

        returnArr.append(knockoutStages)

    elif filterName == 'upcoming':

        for groupName in match_updater.groupsArray:
            for match in groupStage[0][groupName]['matches']:
                if (date.today() < parser.parse(match['date']).date()) and (date.today() + timedelta(days=7) > parser.parse(match['date']).date()):
                    returnArr.append(match)

        for stage in knockoutStages:
            for match in stage['matches']:
                if (date.today() < parser.parse(match['date']).date()) and (date.today() + timedelta(days=7) > parser.parse(match['date']).date()):
                    returnArr.append(match)

    elif filterName == 'today':

        for groupName in match_updater.groupsArray:
            for match in groupStage[0][groupName]['matches']:
                if date.today() == parser.parse(match['date']).date():
                    returnArr.append(match)

        for stage in knockoutStages:
            for match in stage['matches']:
                if date.today() == parser.parse(match['date']).date():
                    returnArr.append(match)
    
    return returnArr