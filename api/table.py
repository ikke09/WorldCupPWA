from flask import Blueprint, render_template, session,abort

table_route = Blueprint('table_route', __name__)
@table_route.route("/worldcup2018/table")
def table():
    return "This will return a table for the games!"