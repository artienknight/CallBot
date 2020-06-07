from twilio.rest import TwilioRestClient
import time

FROM = "+14805269314"
CALLED = "+19015790029"
ACCOUNT_SID = "ACb3ee23ba7ddabf9d3580fec88d43768b"
AUTH_TOKEN = "6b86d98e3f7c760b469a811b653aea8a"

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
            call = client.call.create(to=self.CALLED, from_=self.FROM, url="https://handler.twilio.com/twiml/EH55d36396c095b616d393d3ccd698d551")
            self.CallCounter = self.callCounter + 1
            print("Call #" + str(self.callCounter) + "Calling Number: " + str(self.CALLED))
            time.sleep(200)

def main():
    robo = Call()
    robo.makeCall()

if __name__ == "__main__":
    main()
