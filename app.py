from flask import Flask

app = Flask(__name__)

# -------------------------------
# ⚠️ FAKE CREDENTIALS - DO NOT USE
# These are test secrets for regex scanning/testing only.
# -------------------------------

AWS_ACCESS_KEY_ID = "AKIAFAKE1234567890FAKE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/fake-secret-key"

GCP_API_KEY = "AIzaSyD-FakeKeyForTestingOnly123456"
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=fakeaccount;AccountKey=fakeKey123==;EndpointSuffix=core.windows.net"

SENDGRID_API_KEY = "SG.fakeApiKeyForTestOnly.abc123"
TWILIO_AUTH_TOKEN = "abc123fakeTwilioToken987xyz"

STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
SLACK_BOT_TOKEN = "xoxb-123456789012-abcdefghijABCDEFGHIJ"

GITHUB_TOKEN = "ghp_8fT1Yv9pXJkD4e0QwLr5Kbzx9uVNmU1aZ3xP"
DOCKER_HUB_PASSWORD = "fakeDockerHubPass123!"
DATABASE_PASSWORD = "FakeDbPassword!@#123"

PRIVATE_SSH_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA7fakekeytest1234567890testKEYblock==
-----END RSA PRIVATE KEY-----
'''

ALFRED_SSH_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
MIIBOQIBAAJAXWRPQyGlEY+SXz8Uslhe+MLjTgWd8lf/nA0hgCm9JFKC1tq1S73c
Q9naClNXsMqY7pwPt1bSY8jYRqHHbdoUvwIDAQABAkAfJkz1pCwtfkig8iZSEf2j
VUWBiYgUA9vizdJlsAZBLceLrdk8RZF2YOYCWHrpUtZVea37dzZJe99Dr53K0UZx
AiEAtyHQBGoCVHfzPM//a+4tv2ba3tx9at+3uzGR86YNMzcCIQCCjWHcLW/+sQTW
OXeXRrtxqHPp28ir8AVYuNX0nT1+uQIgJm158PMtufvRlpkux78a6mby1oD98Ecx
jp5AOhhF/NECICyHsQN69CJ5mt6/R01wMOt5u9/eubn76rbyhPgk0h7xAiEAjn6m
EmLwkIYD9VnZfp9+2UoWSh0qZiTIHyNwFpJH78o=
-----END RSA PRIVATE KEY-----
'''
SLACK_BOT_TOKEN = "xoxb-8228459186116-9224178209446-cnRAK5ms7Sz1Vmjbrybb4p0K"
GOOGLE_API_KEY = "AIzaSyA-FakeKey1234567890abcdefghijklmno"

@app.route("/")
def home():
    return "Fake secret testing Flask app is running."

if __name__ == "__main__":
    app.run(debug=True)

