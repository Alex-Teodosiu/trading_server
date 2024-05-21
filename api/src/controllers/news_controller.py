# from flask import request, jsonify
# from flask_restx import Namespace, Resource
# from services.news_service import NewsService

# news = Namespace('news')
# api = Namespace('api') 
# news_service = NewsService()

# @news.route('/news-historical')
# class get_historical_news(Resource):
#     def get(self):
#         user_id = request.args.get('user_id')
#         symbols = request.args.get('symbols')
#         start_date = request.args.get('start_date')
#         end_date = request.args.get('end_date')

#         if not symbols or not start_date or not end_date:
#             return jsonify({"error": "symbols, start_date, and end_date are required parameters"}), 400

#         news_data, status_code = news_service.fetch_historical_news(user_id, symbols, start_date, end_date)
#         return jsonify(news_data), status_code

from flask import request, jsonify
from flask_restx import Namespace, Resource
from services.news_service import NewsService

news = Namespace('news')
api = Namespace('api')
news_service = NewsService()

@news.route('/news-historical')
class GetHistoricalNews(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        symbols = request.args.get('symbols')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        if not symbols or not start_date or not end_date:
            return jsonify({"error": "symbols, start_date, and end_date are required parameters"}), 400

        news_data, status_code = news_service.fetch_historical_news(user_id, symbols, start_date, end_date)
        return jsonify(news_data), status_code
