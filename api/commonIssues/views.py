from flask_restx import Namespace,Resource,fields
from flask import request
from http import HTTPStatus
from flask_jwt_extended import  jwt_required
from ..models.votes import Vote
from ..models.categories import Category
from ..models.commonissues import CommonIssue
common_namespace = Namespace('commonissue',description='categories namespace')


commonissue_model = common_namespace.model(
    'RegisterCommonisssue',{
        'issue_id':fields.Integer(),
        'issue_name':fields.String(required=True,description="Name or title of the common issue")
    }
)


# Class that creates and displays categorys
@common_namespace.route("/commonissue")
class CreateViewCommonisssue(Resource):
    @common_namespace.marshal_with(commonissue_model)
    #@jwt_required()
    def get(self):
        """ 
            Get all common issues
        """

        commonissues = CommonIssue.query.all()
        return commonissues, HTTPStatus.OK


    @common_namespace.expect(commonissue_model)
    @common_namespace.marshal_with(commonissue_model)
    def post(self):
        """
            create a new category 
        """
        data = request.get_json()
        new_issue = CommonIssue(
            issue_name= data.get('issue_name')
        )

        new_issue.save()
        return new_issue, HTTPStatus.CREATED