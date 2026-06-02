from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import List, Optional

class ETARequest(BaseModel):
    source_facility_id: str = Field(..., examples=["IND562132AAA"])
    destination_facility_id: str = Field(..., examples=["IND560099AAB"])
    baseline_osrm_time_mins: float = Field(..., gt=0, description="Baseline OSRM duration must be positive")
    departure_timestamp: datetime = Field(default_factory=datetime.utcnow)
    batch_volume_parcels: int = Field(..., ge=1, description="Volume must be at least 1 parcel")

    @field_validator('source_facility_id', 'destination_facility_id')
    @classmethod
    def validate_facility_format(cls, v: str) -> str:
        if not v.startswith("IND") or len(v) < 6:
            raise ValueError("Facility ID must follow standard regional naming conventions (e.g., INDXXXXXX)")
        return v.upper()

class BottleneckDetail(BaseModel):
    facility_id: str
    reason: str

class ETAResponse(BaseModel):
    graph_corrected_eta_mins: float
    confidence_interval_95: List[float]
    prescriptive_action: str
    path_vulnerability_score: float
    primary_bottleneck_risk: Optional[BottleneckDetail] = None