from flask import Blueprint, render_template, session,abort

overview_route = Blueprint('overview_route', __name__)
@overview_route.route("/overview")
def overview():
    return "This will return an overview of the games!"