import os
import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoint import router as api_endpoint_router
from app.api.views import app as api_endpoint_router
from config.settings import (
    SERVER_HOST,
    ALLOWED_HEADERS,
    ALLOWED_METHODS,
    ALLOWED_ORIGINS,
    IS_ALLOWED_CREDENTIALS
)

sys.path.append(os.path.join(os.path.dirname(__file__)))


def initialize_backend_application() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=IS_ALLOWED_CREDENTIALS,
        allow_methods=ALLOWED_METHODS,
        allow_headers=ALLOWED_HEADERS,
    )

    app.include_router(router=api_endpoint_router)
    return app


backend_app: FastAPI = initialize_backend_application()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:backend_app",
        host=SERVER_HOST,
        port=8080,
        reload=False,
        workers=4,
        log_level="info",
    )
