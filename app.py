import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)


twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
openai_api_key = os.environ['OPENAI_API_KEY']

openai.api_key = openai_api_key

@app.route('/bot', methods=['POST'])
def bot():
    
    incoming_msg = request.values.get('Body', '').strip()

    
    gpt_response = generate_gpt_response(incoming_msg)

    
    response = MessagingResponse()
    response.message(gpt_response)

    return str(response)

def generate_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run()
