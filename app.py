from flask import Flask
from application.database import db
from application.models import User,Role
from application.config import LocalDevelopmentConfig
from flask_security import Security, SQLAlchemyUserDatastore

#All configuration done under this function
def create_app():
    #creating application
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    #connecting app with DB
    db.init_app(app)
    #datastoe has many useful methods in it
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security =Security(app, datastore)

    app.app_context().push()
    return app

app = create_app()


if __name__ == "__main__":
    app.run()