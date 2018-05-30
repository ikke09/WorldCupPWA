import sys
import json
sys.path.append('../..')

import match_updater

from dateutil import parser

from datetime import date
from datetime import timedelta

from flask import Blueprint, render_template, session, abort, request

overview_route = Blueprint('overview_route', __name__)
@overview_route.route("/worldcup2018/overview")
def overview():
    requestedStage = request.args.get('stage')
    requestedGroup = request.args.get('group')

    # all, upcoming (does not equal todays date), or today(does equal todays date)
    filterName = request.args.get('filter')
    returnArr = []

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