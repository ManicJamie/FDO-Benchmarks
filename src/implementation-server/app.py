from flask import Flask, make_response

app = Flask("FDO-Test")

@app.route("/")
def root():
    response = make_response("<h1>FDO Test Server</h1>")
    response.headers["X-Test-Header"] = "i am a test"
    return response
