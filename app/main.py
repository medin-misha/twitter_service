from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pathlib import Path
from handlers import user_router, media_router, tweet_router, get_image
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user_router)
app.include_router(media_router)
app.include_router(tweet_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники 
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т. д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

@app.get("/me", response_class=HTMLResponse)
async def main():
    return FileResponse("./static/index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
