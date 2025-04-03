import time
from flask import Blueprint, render_template, request, jsonify, Response
import os
from openai import OpenAI

main = Blueprint('main', __name__)
delay_time = 0.03 #  faster
system_role ="You are a helpful friend and therapist that offers asafe and supportive environment for the user to discuss their feelings and thoughts. " \
"Use therapeutic techniques to address the user's mental health issues such as anxiety, depression, and stress." \
"Help the user understand their emotions, develop coping strategies, and work through their personal challenges."

@main.route('/')
def chat():
    return render_template('chat.html')

@main.route('/send_message', methods=['POST'])
def chat_with_gpt():
    user_message = request.json.get('message', '')  # Use JSON payload instead of form data
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o"

    def stream_gpt_response():
        try:
            client = OpenAI(
                base_url=endpoint,
                api_key=token,
            )
                        
            gpt_response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": user_message},
                ],
                model=model_name,
                stream=True,
            )
            
            # Accumulate the response content
            full_response = ""
            for update in gpt_response:
                if update.choices and update.choices[0].delta:
                    content = update.choices[0].delta.content
                    if content:
                        yield content  # stream the content

        except Exception as e:
            yield "Sorry, I couldn't process your request."

    return Response(stream_gpt_response(), content_type='text/plain')