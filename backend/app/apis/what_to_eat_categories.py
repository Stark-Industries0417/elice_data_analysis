from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse
from models import Restaurants, Categories, Reviews, TotalRating, Menus
from app import db
import random

eat_categories = Blueprint("eat-categories", __name__)
api = Api(eat_categories)

# request를 받기 위해서는 parser에 argument 추가 필요
parser = reqparse.RequestParser()
parser.add_argument("subcategory", type=str, location="json")


class WhatToEatCategories(Resource):
    def get(self):
        categories = Categories.query.all()
        category_ids = [cat.id for cat in categories]
        random_ids = random.sample(category_ids, 10)  # 무작위로 10개 뽑기
        #
        result = []
        for random_id in random_ids:
            restaurant = Restaurants.query.filter_by(category_id=random_id).first()
            category = Categories.query.filter_by(id=random_id).first()
            tmp = {
                "category_id": category.id,
                "category": category.subcategory,
                "img_url": restaurant.img_url,
            }
            result.append(tmp)

        return jsonify(status=200, data=result)

    # def post(self):
    #     args = parser.parse_args()
    #     subcategories = args["subcategory"]

    #     categories = Categories.query.all()
    #     category_ids = [cat.id for cat in categories]
    #     random_ids = random.sample(category_ids, 10)  # 무작위로 10개 뽑기


api.add_resource(WhatToEatCategories, "/what-to-eat")
