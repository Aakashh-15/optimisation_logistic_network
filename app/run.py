# run.py
import uvicorn

if __name__ == "__main__":
    print("🚀 Initializing Delhivery Graph Engine...")
    uvicorn.run(
        "app.main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=False,  # Bypasses the Windows 3.13 process freeze
        workers=1
    )