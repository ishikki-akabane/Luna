from LUNA.app import app
import uvicorn


if __name__ == "__main__":
    uvicorn.run("LUNA.app:app", port=5000, reload=True)
