from flask_restx import Namespace,Resource,fields
from flask import request
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from ..models.tickets import Ticket
from ..models.votes import Vote
from ..models.commonissues import CommonIssue

ticket_history__namespace = Namespace('ticket-history',description='Ticket history namespace')

ticket_model = ticket_history__namespace.model(
    'CreateTicket',{
        'id':fields.Integer(),
        'title':fields.String(required=True,description="Title of ticket"),
        'description':fields.String(required=True,description="A description of the ticket")
    }
)
class GetTicketHistory(Resource):
    @ticket_history__namespace.marshal_with(ticket_model)
    #@jwt_required()
    def get(self):
        """ 
            Get all tickets
        """

        tickets = Ticket.query.all()
        return tickets, HTTPStatus.OK