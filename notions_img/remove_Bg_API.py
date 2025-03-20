from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from rembg import remove
from PIL import Image
import io
import os

# pip install fastapi uvicorn python-multipart


app = FastAPI(
    title="Suppression Arrière plan Image API",
    description="(FR) API pour effacer l'arriere plan d'une image. (EN) API to remove the background from images.",
    version="1.0.0",
    contact={
        "name": "S Daou",
        "email": "daoland21@gmail.com",
    },
)

@app.post("/remove-background/", summary="Remove Background from Image", description="Upload an image to remove its background.")
async def remove_background(file: UploadFile = File(...)):
    """
    Remove the background from the uploaded image.

    Parameters:
    - file: UploadFile = The image file to process.

    Returns:
    - FileResponse: The image with the background removed.

    Raises:
    - HTTPException: If there is an error processing the image.
    """
    try:
        # Lecture de l'image uiploadée
        contents = await file.read()
        input_img = Image.open(io.BytesIO(contents))

        # Suppression de l'arrière plan de l'image
        output_img = remove(input_img)

        # Sauvegarde de l'image sans arrière plan dans un fichier temporaire
        output_path = "output_image.png"
        output_img.save(output_path)

        # Renvoie de l'image sans arrière plan
        return FileResponse(output_path, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Suppression du fichier temporaire après la réponse
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
