from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    category: str
    details: str