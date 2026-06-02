# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse  # Added for premium UX redirection
from app.schemas import ETARequest, ETAResponse
from app.services.intelligence import LogisticsIntelligenceService

app = FastAPI(
    title="Delhivery Graph Intelligence Core Network Engine",
    version="1.0.0",
    description="Asynchronous Graph ML and Operations Research Dispatch Service"
)

def get_intelligence_service() -> LogisticsIntelligenceService:
    return LogisticsIntelligenceService()

# NEW: Automatically route raw users straight to the clean documentation workspace
@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/health", status_code=status.HTTP_200_OK, tags=["Infrastructure"])
async def health_check():
    return {"status": "healthy", "engine": "Graph_Intelligence_V1"}

@app.post(
    "/api/v1/predict-eta", 
    response_model=ETAResponse, 
    status_code=status.HTTP_200_OK,
    tags=["Logistics Core"]
)
async def predict_network_eta(
    payload: ETARequest,
    service: LogisticsIntelligenceService = Depends(get_intelligence_service)
):
    try:
        response = await service.infer_network_state(payload)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Network Intelligence Engine Failure: {str(e)}"
        )