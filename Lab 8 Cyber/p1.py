import jwt
import time

secretKey="kuchbhi"
def createToken(userName,validSec):
    currentTime=int(time.time())
    expireTime=currentTime+validSec
    tokenPayload={
        "sub":userName,
        "iat":currentTime,
        "exp":expireTime
    }
    encodeT=jwt.encode(tokenPayload,secretKey,algorithm="HS256")
    return encodeT

def checkToken(encodeT):
    try:
        decodeT=jwt.decode(encodeT,secretKey,algorithms="HS256")
        userName=decodeT["sub"]
        return True,userName
    except jwt.ExpiredSignatureError:
        return False,"tokkenExpired"
    except Exception:
        return False,"invalidTokken"
    
userName="studentOne"
validSec=3
token=createToken(userName,validSec)
print("Token Created:")
print(token)
isValid,result=checkToken(token)
if isValid:
    print("Token is valid for user:",result)
else:
    print("Token check failed:",result)
time.sleep(4)
isValid,result=checkToken(token)
if isValid:
    print("Token is valid for user:",result)
else:
    print("Token check failed:",result)
    
