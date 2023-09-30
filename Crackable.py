#Crackable? AI Password Analyzer.
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/hello/", response_class=HTMLResponse)

async def app(request: Request):
    return templates.TemplateResponse("Crackable.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("Crackable:app", port=5000, log_level="info")