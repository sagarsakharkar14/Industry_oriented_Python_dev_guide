from fastapi import FastAPI

from src.billing_tool.billing import apply_billing

app = FastAPI()


@app.post("/run-billing/")
def run_billing(file_path: str):
    apply_billing(file_path)
    return {"status": "success", "file": file_path}
