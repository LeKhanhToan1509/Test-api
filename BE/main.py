from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from secrets import token_hex
from typing import List
import uvicorn

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    responses = []
    for file in files:
        file_ext = file.filename.split(".").pop()
        file_name = token_hex(10)
        file_path = f"Files/{file_name}.{file_ext}"
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        responses.append({"file_name": file_name, "message": "Uploaded successfully"})

    return {"success": True, "files": responses}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)