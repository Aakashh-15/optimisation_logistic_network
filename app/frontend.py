# frontend.py
import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Delhivery Ops Panel", layout="wide", page_icon="🚚")

# Custom CSS to make the dashboard look corporate and modern
st.markdown("""
    <style>
    .reportview-container { background: #f5f7f9; }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #3498db;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚚 Delhivery Network Dispatch Control Panel")
st.markdown("### Strategic Fleet Allocation & Predictive ETA Engine")
st.write("---")

# 1. Sidebar Inputs for the Operations Manager
st.sidebar.header("📋 Dispatch Parameters")

source_hub = st.sidebar.selectbox(
    "Source Facility ID", 
    ["IND562132AAA", "IND212402AAA", "IND282001AAA", "IND000000ACB"]
)
dest_hub = st.sidebar.text_input("Destination Facility ID", "IND560099AAB")
osrm_time = st.sidebar.number_input("Standard Road Mapping Time (Mins)", min_value=10, value=450, step=10)
volume = st.sidebar.number_input("Total Consignment Volume (Parcels)", min_value=1, value=1500, step=100)

# Build the payload target matching our FastAPI schema contract
payload = {
    "source_facility_id": source_hub,
    "destination_facility_id": dest_hub,
    "baseline_osrm_time_mins": float(osrm_time),
    "departure_timestamp": datetime.utcnow().isoformat() + "Z",
    "batch_volume_parcels": int(volume)
}

# 2. Trigger Action Button
if st.sidebar.button("🚀 Run Dispatch Optimization", width="stretch"):
    try:
        # Hit our local microservice endpoint
        with st.spinner("Analyzing graph topologies and running cost solver..."):
            response = requests.post("http://127.0.0.1:8000/api/v1/predict-eta", json=payload)
            
        if response.status_code == 200:
            data = response.json()
            
            # --- ROW 1: CORE OPERATIONAL DECISION CARDS ---
            col1, col2, col3 = st.columns(3)
            
            with col1:
                action = data["prescriptive_action"]
                if "FORCE FTL" in action.upper() or "ALLOCATE FTL" in action.upper():
                    st.error(f"🚨 Tactical Action Required\n\n**{action}**")
                else:
                    st.success(f"✅ Route Cleared\n\n**{action}**")
                    
            with col2:
                st.metric(
                    label="Graph-Corrected ETA", 
                    value=f"{data['graph_corrected_eta_mins']} mins",
                    delta=f"{round(data['graph_corrected_eta_mins'] - osrm_time, 1)} mins vs Map Baseline",
                    delta_color="inverse"
                )
                
            with col3:
                vulnerability = data["path_vulnerability_score"]
                st.metric(
                    label="Network Chokepoint Risk Index", 
                    value=f"{round(vulnerability * 100, 2)}%",
                    delta="Critical Node" if vulnerability > 0.05 else "Stable Corridor",
                    delta_color="inverse" if vulnerability > 0.05 else "normal"
                )
            
            st.write("---")
            
            # --- ROW 2: CRITICAL RISK DETAILED READOUTS ---
            col4, col5 = st.columns(2)
            
            with col4:
                st.subheader("📊 Dispatch Confidence Intervals")
                st.info(
                    f"**95% SLA Delivery Window:** Between **{data['confidence_interval_95'][0]}** and **{data['confidence_interval_95'][1]}** minutes.\n\n"
                    "Use these bounds to lock in delivery commitments with enterprise clients."
                )
                
            with col5:
                st.subheader("⚠️ Infrastructure Integrity Alert")
                risk_detail = data["primary_bottleneck_risk"]
                if risk_detail:
                    st.warning(
                        f"**Facility Bottleneck Warning at:** `{risk_detail['facility_id']}`\n\n"
                        f"**Reasoning:** {risk_detail['reason']}"
                    )
                else:
                    st.success("No active node anomalies detected along this logistics corridor pipeline.")
                    
        else:
            st.error(f"Backend API processed request but returned error status code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Transmission Failure: Could not connect to the Graph Intelligence core engine. Make sure your FastAPI terminal is running on port 8000!")
else:
    st.info("👈 Enter consignment telemetry details in the sidebar control frame and execute the optimization model.")