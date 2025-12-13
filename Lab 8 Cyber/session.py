import jwt
import time

class TokenSystem:
    def __init__(self, key):
        # save the secret key
        self.key = key

    def createToken(self, user, seconds):
        # get current time
        now = int(time.time())
        # set when it ends
        end = now + seconds

        # data to put inside
        data = {
            "sub": user,
            "iat": now,
            "exp": end
        }

        # make the token string
        t = jwt.encode(data, self.key, algorithm="HS256")
        return t

    def checkToken(self, t):
        try:
            # try to read it back
            # the library checks time automatically
            data = jwt.decode(t, self.key, algorithms=["HS256"])
            return True, data["sub"]
        
        except jwt.ExpiredSignatureError:
            # time ran out
            return False, "token expired"
        
        except:
            # signature was wrong or other error
            return False, "bad token"

# start the program
if __name__ == "__main__":
    # setup the system
    sys = TokenSystem("mysecretkey")

    print("--- 1. making token ---")
    name = "student1"
    # valid for 3 seconds
    mytoken = sys.createToken(name, 3)
    print("token created:")
    print(mytoken)

    print("\n--- 2. checking now ---")
    ok, res = sys.checkToken(mytoken)
    
    if ok:
        print("success for user: " + res)
    else:
        print("failed: " + res)

    print("\n--- 3. waiting 4 seconds ---")
    time.sleep(4)

    print("\n--- 4. checking again ---")
    ok, res = sys.checkToken(mytoken)
    
    if ok:
        print("success for user: " + res)
    else:
        print("failed: " + res)