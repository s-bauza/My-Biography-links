.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
$env:API_URL = "https://my-biography-links.up.railway.app" 
reflex export --frontend-only
Remove-Item -Recurse -Force public
Expand-Archive -Path frontend.zip -DestinationPath .\public
Remove-Item -Force frontend.zip
deactivate