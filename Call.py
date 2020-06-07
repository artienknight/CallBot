from twilio.rest import TwilioRestClient
import time

FROM = "+1"
CALLED = "+1"
ACCOUNT_SID = ""
AUTH_TOKEN = ""

class Call:
    def __init__(self):
        self.FROM = FROM
        self.CALLED = CALLED
        self.ACCOUNT_SID = ACCOUNT_SID
        self.AUTH_TOKEN = AUTH_TOKEN
        self.callCounter = 0
        self.limit = 50

    def makeCall(self):
        client = TwilioRestClient(self.ACCOUNT_SID, self.AUTH_TOKEN)

        while self.callCounter < self.LIMIT:
            call = client.call.create(to=self.CALLED, from_=self.FROM, url="")
            self.CallCounter = self.callCounter + 1
            print("Call #" + str(self.callCounter) + "Calling Number: " + str(self.CALLED))
            time.sleep(200)

def main():
    robo = Call()
    robo.makeCall()

if __name__ == "__main__":
    main()
