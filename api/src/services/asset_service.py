import requests
import base64
from src.models.asset_model import Asset

class AssetService:
    def __init__(self):
        self._base_url = "https://broker-api.sandbox.alpaca.markets"
        credentials = base64.b64encode(b'CKF9YAMKM078ANKRNDHJ:exM97y6X8LDNh29ndSgDNyn3cdv1NLaZCpjCKcSB').decode('utf-8')
        self._headers = {'Authorization': f'Basic {credentials}'}

    def get_assets(self):
        response = requests.get(f"{self._base_url}/v1/assets", headers=self._headers)
        data = response.json()
        print(list(data[0].keys()))
        valid_keys = ['id', 'class', 'exchange', 'symbol', 'name', 'status', 'tradable', 'marginable', 'maintenance_margin_requirement', 'shortable', 'easy_to_borrow', 'fractionable']
        #class from the response is a protected key word, so renaming it to asset_class
        assets = [Asset(**{k if k != 'class' else 'asset_class': v for k, v in asset.items() if k in valid_keys}).to_dict() for asset in data]
        return assets[:5]