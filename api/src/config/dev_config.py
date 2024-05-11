class DevConfig:
    def __init__(self):
        self.ENV = "development"
        self.DEBUG = True
        self.PORT = 3000
        self.HOST = '0.0.0.0'
        self.SECRET_KEY = 'your-secret-key'
        self.JWT_SECRET_KEY = 'your-jwt-secret-key'
        self.ALPACA_API_KEY = 'PKFYPB97OWCB1M3CVPBN'
        self.ALPACA_API_SECRET = '9MkEQw9h0d7Pf79OvT14k8ludqOZt05JYaMF4DAd'