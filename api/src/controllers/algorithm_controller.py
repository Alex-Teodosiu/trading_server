from src.services.algorithm_service import AlgorithmService
from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash
from src.services.market_data_service import MarketDataService
from src.services.trade_service import TradeService
from flask_restx import Namespace, Resource


algorithm = Namespace('algorithm')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._algorithm_service = AlgorithmService()


@algorithm.route('/<int:id>')
class GetAlgorithmById(BaseResource):
    def get(self):
        return self._algorithm_service.get_algorithm_by_id()
    
@algorithm.route('/')
class GetAllAlgorithms(BaseResource):
    def get(self):
        return self._algorithm_service.get_all_algorithms()
    
@algorithm.route('/create')
class CreateAlgorithm(BaseResource):
    def post(self):
        return self._algorithm_service.create_algorithm()