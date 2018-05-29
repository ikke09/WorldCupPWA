import time
import match_updater

from flask import Flask

from functions.overview import overview_route
from functions.table import table_route
from functions.match import match_route

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

main_app = Flask(__name__)
main_app.register_blueprint(overview_route)
main_app.register_blueprint(table_route)
main_app.register_blueprint(match_route)

def update_match_info():
    match_updater.update_game_info()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.start()
    
    update_match_info()
    scheduler.add_job(
        func=update_match_info,
        trigger=IntervalTrigger(hours=1),
        id='update_match_info',
        name='Updates the information about the matches every hour',
        replace_existing=True)
    
    main_app.run(debug=True)