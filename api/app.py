from flask import Flask

from functions.overview import overview_route
from functions.table import table_route
from functions.match import match_route

main_app = Flask(__name__)
main_app.register_blueprint(overview_route)
main_app.register_blueprint(table_route)
main_app.register_blueprint(match_route)

if __name__ == '__main__':
    main_app.run(debug=True)