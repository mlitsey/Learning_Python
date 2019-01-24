class Decider():
    atNum = 0
    def SmallNum(self):
        print(f"{self.atNum} small number")
        
    def LargeNum(self):
        print(f"{self.atNum} Large Number")

    def NumCategory(self):
        curNumVal = self.atNum
        if curNumVal<=20:
            self.SmallNum()
        else:
            self.LargeNum()
        
def main():
    print('first decider')
    myDecider = Decider()
    myDecider.atNum = 55
    myDecider.NumCategory()
    
    print('second decider')
    myDecider2 = Decider()
    myDecider2.atNum = 10
    myDecider2.NumCategory()
    
main()