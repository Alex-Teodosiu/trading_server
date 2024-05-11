from flask_restx import Namespace, Resource
from flask import request  
from src.services.asset_service import AssetService


assets = Namespace('assets')
api = Namespace('api') 

class BaseResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._asset_service = AssetService()

@assets.route('/getassets')
class AccountList(BaseResource):
    def get(self):
        return self._asset_service.get_assets(), 200