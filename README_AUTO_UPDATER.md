# GitHub Auto Updater

Script Python para actualizar automáticamente archivos en tu repositorio de GitHub.

## 📁 Archivos creados:

1. **`github_auto_updater.py`** - Script principal de Python
2. **`update_config.json`** - Configuración de actualizaciones automáticas
3. **`update_github.bat`** - Script batch para Windows
4. **`README_AUTO_UPDATER.md`** - Este archivo

## 🚀 Uso rápido:

### En Windows:
1. Haz doble clic en **`update_github.bat`**
2. Selecciona una opción del menú
3. Los cambios se subirán automáticamente a GitHub

### En línea de comandos:
```bash
python github_auto_updater.py
```

## 📋 Opciones disponibles:

1. **Actualizar ShowStatus a false** - Deshabilita la barra de progreso
2. **Actualizar ShowStatus a true** - Habilita la barra de progreso  
3. **Actualizar SafeMode a false** - Deshabilita el modo seguro (sin kick)
4. **Actualizar SafeMode a true** - Habilita el modo seguro
5. **Actualizar número de versión** - Cambia la versión en LOADSTRING.txt
6. **Actualización automática completa** - Usa la configuración de update_config.json
7. **Crear archivo de configuración** - Genera update_config.json
8. **Ver estado Git** - Muestra cambios pendientes
9. **Salir**

## ⚙️ Configuración automática:

Edita `update_config.json` para configurar actualizaciones automáticas:

```json
{
  "update_showstatus": true,      // Actualizar ShowStatus
  "showstatus_value": false,      // Valor de ShowStatus (true/false)
  "update_safemode": true,        // Actualizar SafeMode
  "safemode_value": false,        // Valor de SafeMode (true/false)
  "update_version": false,        // Actualizar número de versión
  "new_version": "1.5",          // Nueva versión
  "auto_commit": true,           // Hacer commit automáticamente
  "commit_message": "Auto update from script"
}
```

## 🔧 Requisitos:

- **Python 3.6+** instalado
- **Git** instalado y en PATH
- **Repositorio Git** inicializado en la carpeta
- **Conexión a GitHub** configurada

## 🎯 Ejemplos de uso:

### Actualizar ShowStatus a false en todos los archivos:
```bash
python github_auto_updater.py
# Selecciona opción 1
```

### Configuración personalizada:
1. Edita `update_config.json`
2. Ejecuta:
```bash
python github_auto_updater.py
# Selecciona opción 6
```

### Solo ver estado:
```bash
python github_auto_updater.py
# Selecciona opción 8
```

## 📊 Archivos que se pueden actualizar:

- `saveinstance.lua`
- `saveinstance.luau`  
- `LOADSTRING.txt`
- `HELLO_KITTY_LOADSTRING.txt`

## ⚠️ Notas:

- El script buscará y reemplazará texto en todos los archivos
- Los cambios se commitean y se suben automáticamente a GitHub
- Verifica los cambios antes de hacer commit
- Asegúrate de tener permisos para escribir en el repositorio