from flask_restx import Namespace,Resource,fields
from flask import request
from http import HTTPStatus
from flask_jwt_extended import  jwt_required
from ..models.votes import Vote

vote_namespace = Namespace('vote',description='Votes namespace')


vote_model = vote_namespace.model(
    'RegisterVote',{
        'vote_id':fields.Integer(),
        'vote_name':fields.String(required=True,description="Title of ticket"),
        'vote_region':fields.String(required=True,description="A description of the ticket")
    }
)


# Class that creates and displays votes
@vote_namespace.route("/votes")
class CreateViewVote(Resource):
    @vote_namespace.marshal_with(vote_model)
    #@jwt_required()
    def get(self):
        """ 
            Get all votes
        """

        votes = Vote.query.all()
        return votes, HTTPStatus.OK


    @vote_namespace.expect(vote_model)
    @vote_namespace.marshal_with(vote_model)
    def post(self):
        """
            create a new Vote 
        """
        data = request.get_json()
        new_vote = Vote(
            vote_name = data.get('vote_name'),
            vote_region = data.get('vote_region')
        )

        new_vote.save()
        return new_vote, HTTPStatus.CREATED