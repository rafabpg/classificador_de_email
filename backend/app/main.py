from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from app.api.controllers.analysis import analysis_router

app = FastAPI(
    title="Classificator Emails API",
    docs_url="/api/docs",         
    openapi_url="/api/openapi.json",
    redoc_url="/api/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")

api_router.include_router(analysis_router)

app.include_router(api_router)