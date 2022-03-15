from flask import Flask, make_response, request
import json

app = Flask(__name__)
from flask_cors import cross_origin


@app.route('/', methods=['GET'])
@cross_origin()
def welcome():
    return "App is running"


@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    print("-->", intent_name)
    if intent_name == "welcome":
        return build_response("Welcome to EVA Chatbot, How may I assist you?")
    elif intent_name == "exit":
        return build_response("Thank you for contacting EVA Chatbot, Have a nice day!!")


def build_response(response_text):
    json_response = json.dumps({
        "fulfillmentText": response_text
    })
    res = make_response(json_response)
    res.headers['Content-Type'] = 'application/json'
    return res


if __name__ == "__main__":
    app.run(debug=True)
