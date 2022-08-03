from setup.config import HOST, PORT,LOG_LEVEL
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, log_level=LOG_LEVEL)