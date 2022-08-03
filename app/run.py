from setup.config import HOST, PORT
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, log_level="info")