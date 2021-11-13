class isprime:
    def isprime(num):
        divider = 2
        result = int(num) / divider
        if (result == int(result)) and (result != 1):
            return False
        else:
            while (result != int(result)) and (result != 1):   
                result = int(num) / divider
                divider += 1
            if (result == int(result)) and (result == 1):
                return True
            else:
                return False
