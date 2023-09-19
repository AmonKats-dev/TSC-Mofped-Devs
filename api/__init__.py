from flask import Flask
#import the API instance of flask_restx
from flask_restx import Api
#Import database instance
from .utils import db
from .tickets.views import ticket_namespace
from .votes.views import vote_namespace
from .categories.views import category_namespace
from .commonIssues.views import common_namespace
#Import our models
from .models.tickets import Ticket

#Import config dictionary
from .config.config import Config_dict

from flask_migrate import Migrate

#Define method to create the app istance
def create_app(config=Config_dict['dev']):
    app=Flask(__name__)

    #add configuration to the app instance
    app.config.from_object(config)

    #Hook the db instance unto our app This should be done after adding the configurations to avoid errors
    db.init_app(app)
    migrate = Migrate(app,db)
    #add api to the flask instance
    api = Api(app)

    #add the name spaces to the api instance
    api.add_namespace(ticket_namespace,path="/ticket-tracker")
    api.add_namespace(vote_namespace,path="/votes")
    api.add_namespace(category_namespace,path="/categories")
    api.add_namespace(common_namespace,path="/common-issues")
    
    
    #make shell context
    @app.shell_context_processor
    def make_shell_context():
        return{
            'db':db,
            'Ticket':Ticket
        }

    return app