from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .providers import list_providers

app = FastAPI(title="RoPilot Local Bridge", version="0.1.0")

# Local development UI only. Keep the bridge bound to 127.0.0.1.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

@app.get("/health")
def health():
    return {"ok": True, "service": "ropilot-bridge", "stage": "scaffold"}

@app.get("/providers")
def providers():
    return {"providers": list_providers()}
