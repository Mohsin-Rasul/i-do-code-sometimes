import jwt
import time

secretKeyValue = "mySecretKey"

def createToken(userNameValue, validSecondsValue):
    currentTimeValue = int(time.time())
    expirationTimeValue = currentTimeValue + validSecondsValue

    tokenPayloadData = {
        "sub": userNameValue,
        "iat": currentTimeValue,
        "exp": expirationTimeValue
    }

    encodedTokenValue = jwt.encode(tokenPayloadData, secretKeyValue, algorithm="HS256")
    return encodedTokenValue


def checkToken(encodedTokenValue):
    try:
        decodedTokenData = jwt.decode(encodedTokenValue, secretKeyValue, algorithms=["HS256"])
        userNameValue = decodedTokenData["sub"]
        return True, userNameValue

    except jwt.ExpiredSignatureError:
        return False, "tokenExpired"

    except Exception:
        return False, "invalidToken"


if __name__ == "__main__":
    print("--- Step 1: Creating Token ---")
    userNameValue = "studentOne"
    validSecondsValue = 3

    createdTokenValue = createToken(userNameValue, validSecondsValue)

    print("Token Created:")
    print(createdTokenValue)

    print("\n--- Step 2: Checking Immediately ---")
    isTokenValid, tokenResultValue = checkToken(createdTokenValue)

    if isTokenValid:
        print("Token is valid for user:", tokenResultValue)
    else:
        print("Token check failed:", tokenResultValue)

    print("\n--- Step 3: Waiting 4 Seconds ---")
    time.sleep(4)

    print("\n--- Step 4: Checking Again ---")
    isTokenValid, tokenResultValue = checkToken(createdTokenValue)

    if isTokenValid:
        print("Token is valid for user:", tokenResultValue)
    else:
        print("Token check failed:", tokenResultValue)
