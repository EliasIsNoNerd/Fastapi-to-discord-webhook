from fastapi import FastAPI, BackgroundTasks
import requests

app = FastAPI()

def discord_webhook(content: str, username: str = "ANY USERNAME HERE"):
    r = requests.post('WEBHOOK GOES HERE',json={"content": content, "username": username})

@app.post("/webhook-discord")
async def webhook(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(discord_webhook, message)
    return {"status": "queued", "message": message}
