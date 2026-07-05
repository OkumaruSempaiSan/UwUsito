@echo off
chcp 65001 >nul
echo ========================================
echo GitHub Auto Updater - Windows
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado o no está en el PATH
    echo 🔗 Descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python detectado
echo.

REM Ejecutar el script Python
python github_auto_updater.py

if errorlevel 1 (
    echo.
    echo ❌ Error al ejecutar el script
) else (
    echo.
    echo ✅ Script ejecutado correctamente
)

echo.
pause