#CREATING A BANK ACCOUNT THAT HAS TWO ATTRIBUTES: oWNER AND BALANCE
#AND ALSO TWO METHODS: DEPOSIT AND WITHDRAW

class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self,wd_amt):
        if self.blance >= wd_amt
            self.balance = self.balance - wd_amt
            print("withdrawal accepted")
        else:
            print("sorry not enough balance")
    def __str(self):
        return f"owner: {self.owner} \nBalance: {self.balance}"

a = Account("sam",500)
a.owner
#output: 'Sam'
a.blance
#output: 500
print(a)
#output: Owner: sam
#        balance: 500
a.deposit(100)
#output: added 100 to the BALANCE
print(a)
#output:  Owner: sam
#        balance: 600
a.withdrawal(600)
#output: Withdrawal accepted
print(a)
#output:  Owner: sam
#        balance: 0
a.withdrawal(a)
#output: sorry not enough balance
print(a)
#output:  Owner: sam
#        balance: 0
