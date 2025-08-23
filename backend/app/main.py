from contextlib import asynccontextmanager
from app.core.nltk_loader import download_nltk_data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import APIRouter
from app.api.controllers.analysis import analysis_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    download_nltk_data()
    yield

app = FastAPI(
    title="Classificator Emails API",
    description="API para classificação automática de emails usando IA",
    lifespan=lifespan,
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
    openapi_url="/api/openapi.json" if settings.DEBUG else None
)

if not settings.DEBUG:
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
    
app.add_middleware(GZipMiddleware, minimum_size=1000)

origins = settings.CORS_ORIGINS.split(",") if "," in settings.CORS_ORIGINS else [settings.CORS_ORIGINS]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api")

api_router.include_router(analysis_router)

app.include_router(api_router)