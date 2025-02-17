.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
Remove-Item -Recurse -Force public
reflex init
$env:API_URL = "https://my-biography-links.up.railway.app" 
reflex export --frontend-only

# Usar la ruta correcta para frontend.zip en la raíz del repositorio
Expand-Archive -Path .\frontend.zip -DestinationPath .\public
Remove-Item -Force .\frontend.zip
deactivate
