class bankaccount:
  def_init_(self,access_number,account_holder_name,initial_balance=0.0):
  self._account_number=account_number
  self._account_holder_name=account_holder_name
 self._account_balance=initial_balance

def deposit(self,account):
  if account>0;
   self._account_balance+=account:
  print("deposited Rs.{}.newbalance:Rs{}".format(amount.slef_account_balance))
else:
print("invalid deposit amount.please deposit positive amount.")

def withdraw(self,amount):
  if amount>0and amount <=self._account_balance:
    self._account_balance-=amount
    print("withdraw Rs.{}.newbalance:Rs.{}".format(amount,self._account_balance))
  else:
    print("invalid withdrawal amount or insufficient balance.")

def display_balance(self):
  print("account balance for {} (account #{}:Rs.{}"format(self._account_holder_name,self._account_number,self._account_balance))


account=bankaccount(account_number="12346789",account_holder_name="nithi",initial_balance=5000.0)

account.display_balance()
account.deposit(500.0)