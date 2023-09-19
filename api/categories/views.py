from flask_restx import Namespace,Resource,fields
from flask import request
from http import HTTPStatus
from flask_jwt_extended import  jwt_required
from ..models.votes import Vote
from ..models.categories import Category

category_namespace = Namespace('category',description='categories namespace')


category_model = category_namespace.model(
    'Registercategory',{
        'category_id':fields.Integer(),
        'category_name':fields.String(required=True,description="Category name")
    }
)


# Class that creates and displays categorys
@category_namespace.route("/category")
class CreateViewcategory(Resource):
    @category_namespace.marshal_with(category_model)
    #@jwt_required()
    def get(self):
        """ 
            Get all categories
        """

        categories = Category.query.all()
        return categories, HTTPStatus.OK


    @category_namespace.expect(category_model)
    @category_namespace.marshal_with(category_model)
    def post(self):
        """
            create a new category 
        """
        data = request.get_json()
        new_category = Category(
            category_name = data.get('category_name')
        )

        new_category.save()
        return new_category, HTTPStatus.CREATED