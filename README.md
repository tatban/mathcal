# Mathcal: An LLM based approach to do math calculation over string input

### Installation:
The app runs in docker containers, so make sure you have `docker` and `docker-compose` installed. Then type the following commands in command line:<br>
- `git clone https://github.com/tatban/mathcal.git` 
- `cd mathcal`
- `docker-compose up --build` and wait for build to finish (first time takes a few minutes to run)
- `docker ps` to verify that two services namely `ollama` and `mathcal_app` are running
### Usage:
This web api helps to perform mathematical calculation when the inputs are in string question format. For example: `what is 5 minus 3?` instead of `5-3`.
- open a browser and type: `http://localhost:38080`. If everything was set up correctly, it will show `mathcal server is running`.
- Then try `http://localhost:38080/mathcal/{your_question}` where `your_question` for example could be `what is 2 times 5?`
- If everything is set up correctly, a dict (json) response is sent with two keys: `question` and `result`
- For more API reference see the Swagger docs at `http://localhost:38080/docs`
