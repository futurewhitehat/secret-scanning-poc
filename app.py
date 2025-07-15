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

GITHUB_TOKEN = "ghp_FAKE1234567890FakeToken098765"
DOCKER_HUB_PASSWORD = "fakeDockerHubPass123!"
DATABASE_PASSWORD = "FakeDbPassword!@#123"

PRIVATE_SSH_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA7fakekeytest1234567890testKEYblock==
-----END RSA PRIVATE KEY-----
'''

@app.route("/")
def home():
    return "Fake secret testing Flask app is running."

if __name__ == "__main__":
    app.run(debug=True)

