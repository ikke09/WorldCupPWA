import time
import match_updater

from flask import Flask

from overview import overview_route
from table import table_route
from match import match_route

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from pytz import utc

main_app = Flask(__name__)
main_app.register_blueprint(overview_route)
main_app.register_blueprint(table_route)
main_app.register_blueprint(match_route)


def update_match_info():
    match_updater.update_game_info()


scheduler = BackgroundScheduler(timezone=utc)
scheduler.start()

update_match_info()
scheduler.add_job(
    func=update_match_info,
    trigger=IntervalTrigger(hours=1, timezone=utc),
    id='update_match_info',
    name='Updates the information about the matches every hour',
    replace_existing=True)

main_app.run(
    host='0.0.0.0')
# use in production only:
#    ssl_context=('/etc/letsencrypt/live/anabell.info/fullchain.pem',
#                 '/etc/letsencrypt/live/anabell.info/privkey.pem')