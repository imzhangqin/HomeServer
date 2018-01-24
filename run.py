import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
ab = AppBuilder(app, db.session)

@ab.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=ab.base_template, appbuilder=ab), 404

import views

db.create_all()
views.register_views(ab)
app.run(host='0.0.0.0', port=8080, debug=True)

