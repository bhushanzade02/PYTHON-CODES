def CountDigLetSpc(n):
        countwhsp = 0
        countdig = 0
        countlet = 0
        digits = "1234567890"
        letter = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        for i in n :
            if i in " ":
                countwhsp +=1
            elif i in digits:
                countdig +=1
            elif i in  letter:
                countlet +=1
        
        print( countwhsp )
        print(countdig )
        print(countlet )

t = "Hello 123 World"

CountDigLetSpc(t)

