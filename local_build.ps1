.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
Remove-Item -Recurse -Force public
reflex init
reflex export --frontend-only
Expand-Archive -Path frontend.zip -DestinationPath .\public
Remove-Item -Force frontend.zip
deactivate