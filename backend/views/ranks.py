from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api, reqparse
from models import Restaurants, Menus, Reviews
from sqlalchemy.sql import func
from app import db
from get_food_category import categories_csv_to_list

ranks = Blueprint("ranks", __name__)
api = Api(ranks)

# request를 받기 위해서는 parser에 argument 추가 필요
parser = reqparse.RequestParser()
parser.add_argument("category", type=str)


class Ranks(Resource):
    # 음식 카테고리 제공
    def get(self):
        data = dict()

        food_category_list = categories_csv_to_list()
        data["categories_of_food"] = food_category_list

        return data, 200

    # 선택한 카테고리에 대한 결과 전송
    def post(self):
        args = parser.parse_args()
        category = args["category"].strip()
        # print(category)

        # 해당 카테고리를 가진 restaurant_id 찾기
        menus = Menus.query.filter_by(category=category).all()
        restaurant_ids = list(set([menu.restaurant_id for menu in menus]))

        # restaurant_id 이용 전체 평점 기준 ordering
        total_rating_ordred = []
        for id in restaurant_ids:
            res = Restaurants.query.filter_by(id=id).first()
            # 평점, 이름, id 추가
            total_rating_ordred.append((res.total_rating, res.name, id))
        print(total_rating_ordred)

        # total_rating 기준으로 내림차순 정렬
        total_rating_ordred = sorted(total_rating_ordred, key=lambda x: -x[0])

        top_ranked_res = []
        for total_rating, res_name, res_id in total_rating_ordered:
            tmp = dict()
            menus = Menu.query.filter_by(restaurant_id=res_id).all()
            tmp = {
                "name": res_name,
                "total_rating": total_rating,
                "menus": [menu.name for menu in menus],
            }
            top_ranks_res.append(tmp)

        data = {"result": top_ranked_res}

        print(data)
        # return data, 200
        return


api.add_resource(Ranks, "/ranks")
