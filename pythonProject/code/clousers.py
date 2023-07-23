def outterfun(text):
    def innerfun():
        print(text)
    return innerfun
if __name__=='__main__':
    for i in range(1,10):
       myfunction=outterfun("hey lalit")
       myfunction()