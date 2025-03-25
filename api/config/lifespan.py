from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
	print("-- APP LIFESPAN STARTED --")

	yield

	print("-- APP LIFESPAN ENDED --")
