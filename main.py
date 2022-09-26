from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import routes
from AuthUtil import is_authorized

app = FastAPI(title="Sensing Pipline APIs", version='0.1.42', dependencies=[Depends(is_authorized)])

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)