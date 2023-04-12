# Simple Prompt API Microservice

This is a Python Flask microservice that reads prompt text from a YAML file and exposes it through an API. The microservice utilizes OpenAI's GPT-3.5 Turbo model to generate responses for the given prompts.

## Dependencies

- Python 3.6+
- Flask
- PyYAML
- OpenAI

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/simple-prompt-api.git

2. Change to the project directory:
```
cd simple-prompt-api
```

3. Set up a virtual environment and activate it:

```python
python3 -m venv venv
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```


## Configuration

1. Create a file named `config.py` in the project directory and add your OpenAI API key:

```python
OPENAI_API_KEY = "your_api_key"
```

2. Update the prompts.yaml file with your desired prompts and URL patterns:

```yaml
- url_pattern: "/joke"
  prompt_text: "Tell me a {input} joke."
- url_pattern: "/story"
  prompt_text: "Write a short story about a {input}."

```


## Running the Microservice

1. Run the microservice:
```
python app.py
```

The microservice will be accessible at http://127.0.0.1:5000/. To access the prompts, use the specified URL patterns (e.g., http://127.0.0.1:5000/joke/dad or http://127.0.0.1:5000/story/robot).


## Usage

Send a GET request to the desired URL pattern with the required input. For example, to get a dad joke, send a GET request to:

```
http://127.0.0.1:5000/joke/dad
```

To get a short story about a robot, send a GET request to:

```
http://127.0.0.1:5000/story/robot
```

The response will be in JSON format with the generated content:

