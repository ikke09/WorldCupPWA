from flask import Blueprint, render_template, session,abort

match_route = Blueprint('match_route', __name__)
@match_route.route("/match")
def match():
    return "This will return a table for the games!"