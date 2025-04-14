from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import time
import random

app = FastAPI()

# Serve static files (for CSS/JS if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process")
async def process_task(background_tasks: BackgroundTasks):
    # Simulate a long-running process
    time.sleep(random.randint(1, 5))  # Simulate processing time
    if random.choice([True, False]):  # Randomly succeed or fail
        return {"status": "success", "message": "Process completed successfully!"}
    else:
        return {"status": "error", "message": "An error occurred during the process."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

