import yaml
import openai
from flask import Flask, jsonify, request

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
app = Flask(__name__)

def load_prompts(filename):
    with open(filename, "r") as file:
        return yaml.safe_load(file)

prompts = load_prompts("prompts.yaml")


def call_chat_gpt_api(prompt):
    messages = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content if response.choices else None


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Simple Prompt API microservice. Use the available URL patterns to access the prompts."})

for prompt in prompts:
    url_pattern = prompt["url_pattern"]
    prompt_text = prompt["prompt_text"]

    def generate_route_func(prompt_text):
        def route_func(**kwargs):
            print(kwargs)
            formatted_prompt = prompt_text.format(**kwargs)
            response = call_chat_gpt_api(formatted_prompt)
            return jsonify({"response": response})
        return route_func
    
    app.add_url_rule(f"{url_pattern}/<string:input>", url_pattern, generate_route_func(prompt_text), methods=["GET"])
    
    
if __name__ == "__main__":
    app.run(debug=True)