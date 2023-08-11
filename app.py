from arduino import Interface
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config import logging, MainSchema, AvailableColors

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse('/docs')


@app.get("/show/{color}")
async def show(color: AvailableColors, timeout: int = 5):
    color = color.value.lower()
    logging.info(f'Show {color}')
    Interface.show(color, timeout)
    return {"message": f"{color} done"}
