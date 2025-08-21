from fastapi import APIRouter,Depends, UploadFile, File, Form
from app.api.decorators.decorators import create
from app.api.dependencies.dependencies import get_analysis_use_case
from typing import Any,Optional

analysis_router = APIRouter(prefix="/analysis", tags=["Files"])

@create(
    router=analysis_router,
    api_func=lambda use_case, file, text: use_case.execute(
        file=file,
        text=text
    ),
    rule="",
    response_model=Any,
    description="Faz o upload de um arquivo ou envia um texto bruto",
    status_code=201
)
async def upload_file_endpoint(
    file: Optional[UploadFile] = File(None),
    text: Optional[str] = Form(None),
    use_case = Depends(get_analysis_use_case)
):
    pass