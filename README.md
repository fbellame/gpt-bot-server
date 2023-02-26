# gpt-bot-server

A chatbot microservice that use OPENAI GPT 3.0 API for conversation.

JSON call:

```json
{
    "question":"a question for GPT...",
    "option":[ "" | "thera_prompt", | "thera_prompt_with_context" ],
    "max_token":300,
    "temperature":0.6,
    "CHAT_TOKEN":""
}
```
The option is the prompt model to use 
 - no prompt
 - thera_prompt is the promt_response.txt (or _fr if config.ini language is fr)
 - thera_prompt_with_context is the promt_response_note.txt (or _fr if config.ini language is fr). This prompt add the last messages to the prompt as context.


Start with Python:
```sh
export OPENAI_API_KEY=[Your OpenAI API key]
export CHAT_TOKEN=[base64_generated_token]
export MY_ORGANISATION=[Your OpenAI organisation]
```

```python
cd app
pip3 install -r requirements.txt

python3 server.py
```
