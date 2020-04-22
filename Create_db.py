from flaskblog import create_app
app = create_app()
from flaskblog import db
db.init_app(app)
with app.app_context():
	db.create_all()