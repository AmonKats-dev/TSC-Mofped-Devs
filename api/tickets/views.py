from flask_restx import Namespace,Resource,fields
from flask import request
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from ..models.tickets import Ticket

from ..models.votes import Vote

from ..models.commonissues import CommonIssue
# Initiate Name space for tickets
ticket_namespace = Namespace('ticket',description='Tickets namespace')

ticket_model = ticket_namespace.model(
    'CreateTicket',{
        'id':fields.Integer(),
        'title':fields.String(required=True,description="Title of ticket"),
        'description':fields.String(required=True,description="A description of the ticket")
    }
)

#Get the ticket's timelines
@ticket_namespace.route("/ticket-timelines/<int:ticket_id>") 
class GetTicketTimelines(Resource):
    #@jwt_required()
    def get(self,ticket_id):
        """ Obtain the ticket's timelines """
        pass

# Class that creates and displays tickets
@ticket_namespace.route("/tickets")
class CreateViewTicket(Resource):
    @ticket_namespace.marshal_with(ticket_model)
    #@jwt_required()
    def get(self):
        """ 
            Get all tickets
        """

        tickets = Ticket.query.all()
        return tickets, HTTPStatus.OK


    @ticket_namespace.expect(ticket_model)
    @ticket_namespace.marshal_with(ticket_model)
    def post(self):
        """
            create a new ticket 
        """
        data = request.get_json()
        new_ticket = Ticket(
            title = data.get('title'),
            description = data.get('description')
        )

        new_ticket.save()
        return new_ticket, HTTPStatus.CREATED

#Close ticket
@ticket_namespace.route("/close-ticket/<int:ticket_id>")
class CloseTicket(Resource):
   
    def put(self,ticket_id):
        """ 
            Close ticket
        """
        pass

#Mark Ticket as resolved
@ticket_namespace.route("/reslove-ticket/<int:ticket_id>")
class CloseTicket(Resource):
   
    def put(self,ticket_id):
        """ 
            Mark ticket as resolved
        """
        pass




