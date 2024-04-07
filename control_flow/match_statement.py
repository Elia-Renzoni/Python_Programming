# Control flow instructions
# @author Elia Renzoni
# @brief Match control flow instruction

def getStatement():
    return int(input("Inserisci un http status: "))

def httpSatus():
    status = getStatement()
    match status:
        case 400:
            return "Bad Request"
        case 500:
            return "Internal Server Error"
        case _:
            return "OSS"
    

print(httpSatus())
