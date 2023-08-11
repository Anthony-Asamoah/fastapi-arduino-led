import uvicorn
from config import logging

if __name__ == "__main__":
    logging.info('Init Server')
    uvicorn.run(
        "app:app",
        # host="0.0.0.0",
        port=8080,
        reload=False
    )
