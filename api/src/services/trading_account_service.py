import base64
import json
from src.config.dev_config import DevConfig
from src.data_access.trading_account_repository import TradingAccountRepository
from src.models.trading_account_model import TradingAccount
import requests
from alpaca.trading.client import TradingClient
from alpaca.common.exceptions import APIError

class TradingAccountService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()
        config = DevConfig()
        self._api_key = config.ALPACA_API_KEY
        self._secret_key = config.ALPACA_API_SECRET
        self._trading_client = TradingClient(self._api_key, self._secret_key, paper=True)
    

    def get_account_by_credentials(self, api_key, secret):
        try:
            temp_trading_client = TradingClient(api_key, secret, paper=True)
            account_data = temp_trading_client.get_account()
            account = TradingAccount(
                id=account_data.id,
                account_number=account_data.account_number,
                status=account_data.status,
                crypto_status=account_data.crypto_status,
                currency=account_data.currency,
                buying_power=account_data.buying_power,
                regt_buying_power=account_data.regt_buying_power,
                daytrading_buying_power=account_data.daytrading_buying_power,
                non_marginable_buying_power=account_data.non_marginable_buying_power,
                cash=account_data.cash,
                accrued_fees=account_data.accrued_fees,
                pending_transfer_out=account_data.pending_transfer_out,
                pending_transfer_in=account_data.pending_transfer_in,
                portfolio_value=account_data.portfolio_value,
                pattern_day_trader=account_data.pattern_day_trader,
                trading_blocked=account_data.trading_blocked,
                transfers_blocked=account_data.transfers_blocked,
                account_blocked=account_data.account_blocked,
                created_at=account_data.created_at,
                trade_suspended_by_user=account_data.trade_suspended_by_user,
                multiplier=account_data.multiplier,
                shorting_enabled=account_data.shorting_enabled,
                equity=account_data.equity,
                last_equity=account_data.last_equity,
                long_market_value=account_data.long_market_value,
                short_market_value=account_data.short_market_value,
                initial_margin=account_data.initial_margin,
                maintenance_margin=account_data.maintenance_margin,
                last_maintenance_margin=account_data.last_maintenance_margin,
                sma=account_data.sma,
                daytrade_count=account_data.daytrade_count,
                options_buying_power=account_data.options_buying_power,
                options_approved_level=account_data.options_approved_level,
                options_trading_level=account_data.options_trading_level,
            )
            self._trading_account_repository.save_account(account)
            return account.to_dict()
        except APIError as e:
            return str(e)




    # def create_ACH_relationship(self, account_id, ach_info):
    #     url = f"{self._base_url}/v1/accounts/{account_id}/ach_relationships"
    #     response = requests.post(url, headers=self._headers, data=json.dumps(ach_info))

    #     if response.status_code != 201:
    #         raise Exception(f"Request to create ACH relationship failed with status {response.status_code}. Response: {response.text}")

    #     return response.json()


    # def make_ACH_transfer(self, account_id, transfer_info):
    #     url = f"{self._base_url}/v1/accounts/{account_id}/transfers"
    #     response = requests.post(url, headers=self._headers, data=json.dumps(transfer_info))

    #     if response.status_code != 201:
    #         raise Exception(f"Request to make ACH transfer failed with status {response.status_code}. Response: {response.text}")

    #     return response.json()    

    # def get_accounts(self):
    #     account_rows = self._trading_account_repository.get_accounts()
    #     accounts = []
    #     for account_row in account_rows:
    #         account = TradingAccount(account_row[0], account_row[1], account_row[2], account_row[3])
    #         account = account.to_dict()
    #         accounts.append(account)
    #     return accounts

    # def get_account_by_id(self, id):
    #     account_row = self._trading_account_repository.get_account_by_id(id)
    #     if account_row is not None:
    #         account = TradingAccount(account_row[0], account_row[1], account_row[2], account_row[3])
    #         account = account.to_dict()
    #     else:
    #         account = None
    #     return account

    # def validate_account(self, account):
    #     # Logic for validating an account
    #     is_valid = self._trading_account_repository.validate_account(account)
    #     return is_valid

    # def dummy(self):
    #     # Logic for the dummy service
    #     return {'message': 'Dummy service called.'}