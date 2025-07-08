class Bank:
    bank_name="abc Bank"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name
if  __name__=="__main__":
    user1=Bank()
    user2=Bank()

    print("before changing bank name:")
    print(f"user1's bank name :{user1.bank_name}")
    print(f"user2's bank name :{user2.bank_name}")

    Bank.change_bank_name("xyz Bank")