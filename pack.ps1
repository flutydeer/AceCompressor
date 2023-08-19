# Activate virtual environment
& ./venv/Scripts/Activate.ps1

# Run PyInstaller
pyinstaller --onedir --noconsole --version-file file_version_info.txt acecompressor.py --noconfirm --onefile