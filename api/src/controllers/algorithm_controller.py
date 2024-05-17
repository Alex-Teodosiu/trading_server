import threading
from src.services.algorithms.three_consecutive_algorithm_service import ThreeConsecutiveAlgorithmService
from src.services.algorithms.algorithm_service import AlgorithmService
from flask import request
from flask_restx import Namespace, Resource
from services.algorithms.bollinger_algorithm_service import BollingerAlgorithmService


algorithm = Namespace('algorithm')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._algorithm_service = AlgorithmService()
        self._three_consecutive_algorithm_service = ThreeConsecutiveAlgorithmService()
        self._bollinger_bands_service = BollingerAlgorithmService()


@algorithm.route('/<int:id>')
class GetAlgorithmById(BaseResource):
    def get(self):
        return self._three_consecutive_algorithm_service.get_algorithm_by_id()
    
@algorithm.route('/')
class GetAllAlgorithms(BaseResource):
    def get(self):
        return self._three_consecutive_algorithm_service.get_all_algorithms()
    
@algorithm.route('/create')
class CreateAlgorithm(BaseResource):
    def post(self):
        return self._three_consecutive_algorithm_service.create_algorithm()
    
@algorithm.route('/run-three-consecutive-algorithm')
class RunAlgorithm(Resource):
    def post(self):
        data = request.json
        user_id = data['user_id']
        symbol = data['symbol']
        qty = data['qty']
        interval = data.get('interval', 60)  # Default interval to 60 seconds if not provided
        
        # Start the algorithm in a separate thread
        threading.Thread(target=self.algorithm_service.run_algorithm, args=(user_id, symbol, qty, interval)).start()
        
        return {"message": "Algorithm started"}
    

@algorithm.route('/run-bollinger-algorithm')
class RunBollingerAlgorithm(Resource):
    def post(self):
        data = request.json
        user_id = data['user_id']
        symbol = data['symbol']
        qty = data['qty']
        interval = data.get('interval', 60)  # Default interval to 60 seconds if not provided
        
        bollinger_algorithm_service = BollingerAlgorithmService()  # Instantiate the BollingerAlgorithmService
        
        # Start the Bollinger Bands algorithm in a separate thread
        threading.Thread(target=bollinger_algorithm_service.run_algorithm, args=(user_id, symbol, qty, interval)).start()
        
        return {"message": "Bollinger Bands Algorithm started"}
