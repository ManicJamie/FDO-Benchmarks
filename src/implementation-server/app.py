from flask import Flask, make_response

import generation

import implementations.signposting

generation.load()
app = Flask("FDO-Test")

@app.route("/")
def root():
    response = make_response("<h1>FDO Test Server</h1>")
    response.headers.add("X-Test-Header", "i am a test")
    return response


app.register_blueprint(implementations.signposting.bp, url_prefix="/signposting")
