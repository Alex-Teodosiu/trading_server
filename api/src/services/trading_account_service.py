from src.data_access.trading_account_repository import TradingAccountRepository
from src.models.trading_account_model import TradingAccount

class TradingAccountService():
    def __init__(self):
        self._trading_account_repository = TradingAccountRepository()

    def get_accounts(self):
        account_rows = self._trading_account_repository.get_accounts()
        accounts = []
        for account_row in account_rows:
            account = TradingAccount(account_row[0], account_row[1], account_row[2], account_row[3])
            account = account.to_dict()
            accounts.append(account)
        return accounts

    def get_account_by_id(self, id):
        account_row = self._trading_account_repository.get_account_by_id(id)
        if account_row is not None:
            account = TradingAccount(account_row[0], account_row[1], account_row[2], account_row[3])
            account = account.to_dict()
        else:
            account = None
        return account

    def validate_account(self, account):
        # Logic for validating an account
        is_valid = self._trading_account_repository.validate_account(account)
        return is_valid

    def dummy(self):
        # Logic for the dummy service
        return {'message': 'Dummy service called.'}