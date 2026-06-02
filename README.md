# 🚚 Delhivery Graph Intelligence Core & Prescriptive Dispatch Engine

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-green)
![ML](https://img.shields.io/badge/ML-Node2Vec%20%2B%20RandomForest-orange)
![Optimization](https://img.shields.io/badge/Optimization-MILP-red)
![License](https://img.shields.io/badge/Status-Academic%20Project-success)

> Graph Analytics + Machine Learning + Operations Research for intelligent ETA prediction and fleet dispatch optimization.

---

# 📌 Problem Statement

Traditional ETA systems estimate travel time using road distance and traffic conditions. They ignore internal logistics bottlenecks such as:

- Cross-dock congestion
- Sorting center overload
- Yard truck queues
- Hub processing delays
- Delay propagation across the network

This project models the logistics ecosystem as a graph and uses graph intelligence to improve ETA prediction and dispatch decisions.

---

# 🏗 System Architecture

```mermaid
flowchart LR

A[Shipment Data] --> B[Spatio-Temporal Graph Layer]
B --> C[Node2Vec Embeddings]
C --> D[Random Forest ETA Engine]
D --> E[MILP Optimization Engine]
E --> F[Dispatch Recommendation]

B --> G[Network Risk Analysis]
G --> E
```

---

# 🔄 End-to-End Workflow

```mermaid
flowchart TD

A[Input Shipment Request]
--> B[Graph Construction]

B --> C[Centrality Computation]

C --> D[Node2Vec Feature Generation]

D --> E[ETA Prediction]

E --> F[Risk Assessment]

F --> G[MILP Optimization]

G --> H[Carting or FTL Recommendation]

H --> I[Final API Response]
```

---

# 📸 API Demonstration

## Input Request

![Input Request](images/api_input.png)

```json
{
  "source_facility_id": "IND282001AAA",
  "destination_facility_id": "IND110037AAM",
  "baseline_osrm_time_mins": 180.0,
  "departure_timestamp": "2026-06-02T15:45:00Z",
  "batch_volume_parcels": 650
}
```

---

## Output Response

![Output Response](images/api_output.png)

```json
{
  "graph_corrected_eta_mins": 180,
  "confidence_interval_95": [171, 189],
  "prescriptive_action": "ALLOCATE CARTING (Cost Minimal)",
  "path_vulnerability_score": 0,
  "primary_bottleneck_risk": null
}
```

---

# 📊 Results

| Metric | Value |
|----------|---------|
| ETA Improvement | 14.1% MAE Reduction |
| Graph Representation | Node2Vec |
| ML Model | Random Forest |
| Optimization | MILP |
| Decision Output | Carting vs FTL |

### Performance Visualization

```text
Baseline ETA Error      ████████████████████ 100%
Graph-Aware ETA Error   █████████████████ 85.9%
```

---

# 🛠 Tech Stack

- FastAPI
- Pydantic v2
- NetworkX
- Node2Vec
- Scikit-Learn
- PuLP
- Streamlit
- Docker
- Python 3.12

---

# 📂 Repository Structure

```text
delhivery_graph_api/
│
├── images/
│   ├── api_input.png
│   └── api_output.png
│
├── app/
├── notebooks/
├── frontend.py
├── requirements.txt
├── Dockerfile
└── README.md
```



---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/delhivery-graph-intelligence.git
cd delhivery-graph-intelligence
```

## 2. Create a Python Environment

Using Conda:

```bash
conda create -n delhivery_graph python=3.12 -y
conda activate delhivery_graph
```

Or using venv:

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Backend API

Launch the FastAPI server:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Once the server starts, open:

```text
http://127.0.0.1:8000/docs
```

This launches the interactive Swagger UI where you can test the ETA prediction API.

---

# ▶ Running the Dashboard

Open a new terminal and activate the environment:

```bash
conda activate delhivery_graph
```

Launch Streamlit:

```bash
streamlit run frontend.py
```

The dashboard will automatically open in your browser.

---

# 🧪 Example API Request

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/predict-eta" \
-H "Content-Type: application/json" \
-d '{
    "source_facility_id":"IND282001AAA",
    "destination_facility_id":"IND110037AAM",
    "baseline_osrm_time_mins":180,
    "departure_timestamp":"2026-06-02T15:45:00Z",
    "batch_volume_parcels":650
}'
```

---

# 🐳 Docker Deployment

Build Image:

```bash
docker build -t delhivery-graph-api .
```

Run Container:

```bash
docker run -p 8000:8000 delhivery-graph-api
```

Access:

```text
http://localhost:8000/docs
```


---

# 🚀 Future Enhancements

- Reinforcement Learning Dispatch Policies
- Digital Twin Simulation
- Multi-Objective Optimization

---

## 👨‍💻 Domains

- Graph Theory
- Machine Learning
- Operations Research
- Backend Development
- Supply Chain Analytics
