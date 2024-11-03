from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import json

app = FastAPI()

api_json_name = 'species_images.json'
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/species-images")
def get_species_images():
    try:
        with open(api_json_name) as json_file:
            species_images = json.load(json_file)
        return species_images
    except Exception as e:
        return {"error": str(e)}

@app.get("/species-images/{species_name}")
def get_species_images(species_name: str):
    try:
        with open(api_json_name) as json_file:
            species_images = json.load(json_file)
                
        if species_name in species_images:
            return {species_name: species_images[species_name]}
        else:
            raise HTTPException(status_code=404, detail="Espécie não encontrada.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)