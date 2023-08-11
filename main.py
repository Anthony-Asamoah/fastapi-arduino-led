import uvicorn
from config import logging

if __name__ == "__main__":
    logging.info('Init Server')
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8080,
        reload=False
    )
