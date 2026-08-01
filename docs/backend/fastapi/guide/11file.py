from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/file")
async def file_upload(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/files")
async def files_upload(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/upload_file")
async def upload_file(file: Annotated[UploadFile, File(description="上传pdf")]):
    return {"file_name": file.filename}

@app.post("/uploadfiles")
async def upload_files(files: Annotated[list[UploadFile], File(description="上传pdf")]):
    return {"file_names": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)