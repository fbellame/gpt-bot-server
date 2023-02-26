from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import nexus

CHAT_TOKEN = os.getenv("CHAT_TOKEN")

app = FastAPI()
conversations = nexus.load_convo()

# Set up CORS middleware
origins = ["*"] # set your allowed origins here
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#
# chat endpoint
#
# 
@app.post("/chat")
async def chat(request_body: dict):
    chat_token = request_body['CHAT_TOKEN']

    # security validation, a valid CHAT_TOKEN must be added
    if valid_token(chat_token):

        # extract parameters from the json query body
        question = request_body['question']
        max_token = request_body['max_token']
        prompt = request_body['option']
        temperature = request_body['temperature']

        # manage conversation
        contexte = nexus.get_last_messages(conversations, 6)
        nexus.save_conversation('UTILISATEUR', question, conversations)
        reponse = nexus.ask_theo(question, prompt, max_token, temperature, contexte)
        nexus.save_conversation('THEO', reponse, conversations)

        return {"response": reponse}
    else:
         return {"error" : "invalid CHAT_TOKEN"}

def valid_token(token):
      return token == CHAT_TOKEN

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
