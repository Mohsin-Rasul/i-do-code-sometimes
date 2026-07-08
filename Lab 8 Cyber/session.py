import time

def createToken(userName, validSeconds):
    expirationTime = int(time.time()) + validSeconds
    tokenData = {
        "user": userName,
        "exp": expirationTime
    }
    return tokenData

def checkToken(tokenData):
    currentTime = int(time.time())
    if currentTime > tokenData["exp"]:
        return False, "tokenExpired"
    else:
        return True, tokenData["user"]


if __name__ == "__main__":
    print("--- Step 1: Create Token ---")
    userName = "studentOne"
    tokenData = createToken(userName, 3)
    print("Token Created:", tokenData)

    print("\n--- Step 2: Check Immediately ---")
    isValid, result = checkToken(tokenData)
    if isValid:
        print("Token valid for user:", result)
    else:
        print("Token check failed:", result)

    print("\n--- Step 3: Wait 4 Seconds ---")
    time.sleep(4)

    print("\n--- Step 4: Check Again ---")
    isValid, result = checkToken(tokenData)
    if isValid:
        print("Token valid for user:", result)
    else:
        print("Token check failed:", result)
