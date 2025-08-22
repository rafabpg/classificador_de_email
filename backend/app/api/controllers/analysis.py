from fastapi import APIRouter,Depends, UploadFile, File, Form
from app.api.decorators.decorators import create
from app.api.dependencies.dependencies import get_analysis_use_case
from app.api.schemas.responses import AnalysisResponse
from typing import Optional

analysis_router = APIRouter(prefix="/analysis", tags=["Files"])

@create(
    router=analysis_router,
    api_func=lambda use_case, file, text: use_case.execute(
        file=file,
        text=text
    ),
    rule="",
    response_model=AnalysisResponse,
    description="Faz o upload de um arquivo ou envia um texto bruto",
    status_code=200
)
async def upload_file_endpoint(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None),
    use_case = Depends(get_analysis_use_case)
):
    pass