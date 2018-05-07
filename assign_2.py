class User:
	def __init__(self, first_name, middle_name, last_name):
		self.first_name = first_name
		self.middle_name = middle_name
		self.last_name = last_name
		self.BankAccounts = []

	def addBankAccount(self, bank_account):
		self.bank_accounts.append(bank_account)

class BankAccount:
	def __init__(self, account_type, balance, status):
		self.account_type = account_type
		self.balance = balance
		self.status = status

	def transfer(self, amount, toAccount):
		toAccount.updateBalance += amount

user = User("John", "Doe")

checking_account = BankAccount(user, "Checking", 100)
print(checking_account)
print(checking_account.user.first_name)
print(checking_account.user.last_name)

savings_account = BankAccount(user, "Saving", 0)

checking_account.transfer(20, savings_account)