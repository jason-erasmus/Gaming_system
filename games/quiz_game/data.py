import requests

# The code is making a GET request to the Open Trivia Database API to retrieve a set of 10 boolean type questions.
parameters = {
    "amount": 10,
    "type" : "boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]

