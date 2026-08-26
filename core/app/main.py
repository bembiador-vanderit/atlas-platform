from fastapi import FastAPI

app = FastAPI(
    title="Atlas Core API",
    version="0.1.0",
    description="Core platform API for the Atlas ecosystem.",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "atlas-core"}


@app.get("/api/v1/health", tags=["system"])
def api_health() -> dict[str, str]:
    return {"status": "ok", "service": "atlas-core", "api": "v1"}
