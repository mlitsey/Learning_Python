class PrintNums:
    numToPrint=0    
    def sayNum(self):
        numwords = ('one','two','three','four','five','six')
        atWord = self.numToPrint - 1  
        print(numwords[atWord])
        
def main():
    myPrintNums = PrintNums()
    myPrintNums.numToPrint = 4
    myPrintNums.sayNum()
        
main()