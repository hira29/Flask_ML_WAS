from flask import request
from flask_restx import Resource

from src.model.mlmodel import MLModel
from src.dao.mldao import MLDao


Model = MLModel()
Dao = MLDao()


api = Model.ns
_ml = Model.ml

@api.route('/')
class MLRequest(Resource):
    @api.doc('ML Processing')
    @api.response(201, 'ML Return')
    @api.expect(_ml, validate=True)
    @api.marshal_with(_ml)
    def post(self):
        data = request.json
        return Dao.predict(data)

