.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
Remove-Item -Recurse -Force public
reflex init
$env:API_URL = "https://my-biography-links.up.railway.app" 
reflex export --frontend-only
Write-Host "Directorio actual: $(Get-Location)"
Expand-Archive -Path frontend.zip -DestinationPath .\public
Remove-Item -Force frontend.zip
deactivate