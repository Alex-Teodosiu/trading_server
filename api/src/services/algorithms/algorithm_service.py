
class AlgorithmService:
    def __init__(self):
        self._base_url = "https://broker-api.sandbox.alpaca.markets"
        credentials = base64.b64encode(b'CKF9YAMKM078ANKRNDHJ:exM97y6X8LDNh29ndSgDNyn3cdv1NLaZCpjCKcSB').decode('utf-8')
        self._headers = {'Authorization': f'Basic {credentials}'}


    def get_algorithm_by_id(self):
        return none
    
    def get_all_algorithms(self):
        return none
    
    def create_algorithm(self):
        return none