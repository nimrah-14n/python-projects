class Logger:
    def __init__(self):
        print("object created")#constructor

    def __del__(self):
        print("object destroyed")#destructor

if __name__=="__main__":
    log=Logger()
    del log