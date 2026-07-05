#!/usr/bin/env python3
"""
GitHub Auto Updater - Actualiza automáticamente archivos en el repositorio GitHub
"""

import os
import sys
import subprocess
import time
from pathlib import Path
import json

class GitHubAutoUpdater:
    def __init__(self, repo_path=None):
        """Inicializa el actualizador automático de GitHub"""
        self.repo_path = repo_path or os.getcwd()
        self.changes_made = False
        self.commit_messages = []
        
    def check_git_status(self):
        """Verifica el estado del repositorio Git"""
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            return result.stdout.strip()
        except Exception as e:
            print(f"❌ Error al verificar estado Git: {e}")
            return ""
    
    def get_current_branch(self):
        """Obtiene la rama actual"""
        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            return result.stdout.strip()
        except:
            return "main"
    
    def update_file(self, file_path, old_text, new_text):
        """Actualiza un archivo reemplazando texto"""
        try:
            full_path = os.path.join(self.repo_path, file_path)
            
            if not os.path.exists(full_path):
                print(f"❌ Archivo no encontrado: {file_path}")
                return False
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_text not in content:
                print(f"⚠️ Texto no encontrado en {file_path}")
                return False
            
            new_content = content.replace(old_text, new_text)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Actualizado: {file_path}")
            self.changes_made = True
            self.commit_messages.append(f"Update {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error al actualizar {file_path}: {e}")
            return False
    
    def update_showstatus_all_files(self, new_value="false"):
        """Actualiza ShowStatus en todos los archivos Lua/Luau"""
        print(f"\n🔄 Actualizando ShowStatus a {new_value} en todos los archivos...")
        
        files_to_update = [
            "saveinstance.lua",
            "saveinstance.luau",
            "LOADSTRING.txt",
            "HELLO_KITTY_LOADSTRING.txt"
        ]
        
        updated_count = 0
        for file_name in files_to_update:
            file_path = os.path.join(self.repo_path, file_name)
            
            if os.path.exists(file_path):
                # Buscar y reemplazar ShowStatus = true/false
                old_value = "true" if new_value == "false" else "false"
                
                patterns = [
                    f"ShowStatus = {old_value}",
                    f"ShowStatus = {old_value.capitalize()}",
                    f"ShowStatus={old_value}",
                    f"ShowStatus={old_value.capitalize()}"
                ]
                
                for pattern in patterns:
                    if self.update_file(file_name, pattern, f"ShowStatus = {new_value}"):
                        updated_count += 1
                        break
        
        print(f"✅ Actualizados {updated_count} archivos")
        return updated_count > 0
    
    def update_safe_mode_all_files(self, new_value="false"):
        """Actualiza SafeMode en todos los archivos Lua/Luau"""
        print(f"\n🔄 Actualizando SafeMode a {new_value} en todos los archivos...")
        
        files_to_update = [
            "saveinstance.lua",
            "saveinstance.luau",
            "LOADSTRING.txt",
            "HELLO_KITTY_LOADSTRING.txt"
        ]
        
        updated_count = 0
        for file_name in files_to_update:
            file_path = os.path.join(self.repo_path, file_name)
            
            if os.path.exists(file_path):
                # Buscar y reemplazar SafeMode = true/false
                old_value = "true" if new_value == "false" else "false"
                
                patterns = [
                    f"SafeMode = {old_value}",
                    f"SafeMode = {old_value.capitalize()}",
                    f"SafeMode={old_value}",
                    f"SafeMode={old_value.capitalize()}"
                ]
                
                for pattern in patterns:
                    if self.update_file(file_name, pattern, f"SafeMode = {new_value}"):
                        updated_count += 1
                        break
        
        print(f"✅ Actualizados {updated_count} archivos")
        return updated_count > 0
    
    def update_version_number(self, new_version):
        """Actualiza el número de versión en LOADSTRING.txt"""
        print(f"\n🔄 Actualizando versión a {new_version}...")
        
        patterns = [
            "LOADSTRINGS UNIVERSAL SYN SAVE INSTANCE v",
            "-- LOADSTRINGS UNIVERSAL SYN SAVE INSTANCE v"
        ]
        
        for pattern in patterns:
            # Buscar línea con versión
            with open(os.path.join(self.repo_path, "LOADSTRING.txt"), 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                if pattern in line:
                    # Extraer número de versión actual
                    import re
                    current_version_match = re.search(r'v(\d+\.\d+)', line)
                    if current_version_match:
                        current_version = current_version_match.group(1)
                        new_line = line.replace(f"v{current_version}", f"v{new_version}")
                        
                        with open(os.path.join(self.repo_path, "LOADSTRING.txt"), 'w', encoding='utf-8') as f:
                            f.writelines(lines[:i] + [new_line] + lines[i+1:])
                        
                        print(f"✅ Versión actualizada de v{current_version} a v{new_version}")
                        self.changes_made = True
                        self.commit_messages.append(f"Update version to v{new_version}")
                        return True
        
        print("⚠️ No se encontró número de versión")
        return False
    
    def git_add_all(self):
        """Agrega todos los cambios al staging area de Git"""
        try:
            result = subprocess.run(
                ["git", "add", "."],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if result.returncode == 0:
                print("✅ Cambios agregados a Git")
                return True
            else:
                print(f"❌ Error al agregar cambios: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error en git add: {e}")
            return False
    
    def git_commit(self, message=None):
        """Realiza commit de los cambios"""
        if not message:
            if self.commit_messages:
                message = " | ".join(self.commit_messages)
            else:
                message = "Auto update"
        
        try:
            result = subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if result.returncode == 0:
                print(f"✅ Commit realizado: {message}")
                return True
            else:
                print(f"⚠️ Commit fallido o sin cambios: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error en git commit: {e}")
            return False
    
    def git_push(self, branch=None):
        """Sube los cambios al repositorio remoto"""
        if not branch:
            branch = self.get_current_branch()
        
        try:
            print(f"🔼 Subiendo cambios a rama '{branch}'...")
            result = subprocess.run(
                ["git", "push", "origin", branch],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if result.returncode == 0:
                print("✅ Cambios subidos a GitHub")
                return True
            else:
                print(f"❌ Error al subir cambios: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error en git push: {e}")
            return False
    
    def auto_update_all(self, commit_message="Auto update"):
        """Actualiza todo automáticamente y sube a GitHub"""
        print("🚀 Iniciando actualización automática...")
        
        # 1. Verificar estado
        status = self.check_git_status()
        if status:
            print(f"📊 Cambios pendientes:\n{status}")
        else:
            print("📊 No hay cambios pendientes")
        
        # 2. Actualizar archivos según configuración
        config_file = os.path.join(self.repo_path, "update_config.json")
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                if config.get("update_showstatus", False):
                    new_value = "true" if config.get("showstatus_value", False) else "false"
                    self.update_showstatus_all_files(new_value)
                
                if config.get("update_safemode", False):
                    new_value = "true" if config.get("safemode_value", False) else "false"
                    self.update_safe_mode_all_files(new_value)
                
                if config.get("update_version", False):
                    new_version = config.get("new_version", "1.0")
                    self.update_version_number(new_version)
                    
            except Exception as e:
                print(f"⚠️ Error al leer configuración: {e}")
        
        # 3. Si hubo cambios, hacer commit y push
        if self.changes_made:
            self.git_add_all()
            self.git_commit(commit_message)
            self.git_push()
            print("🎉 Actualización completada y subida a GitHub")
        else:
            print("ℹ️ No se realizaron cambios")
        
        return self.changes_made

def create_config_file():
    """Crea un archivo de configuración de ejemplo"""
    config = {
        "update_showstatus": True,
        "showstatus_value": False,  # false para deshabilitar, true para habilitar
        "update_safemode": True,
        "safemode_value": False,   # false para deshabilitar, true para habilitar
        "update_version": True,
        "new_version": "1.5",
        "auto_commit": True,
        "commit_message": "Auto update from script"
    }
    
    with open("update_config.json", 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    
    print("📁 Archivo de configuración creado: update_config.json")
    print("📝 Edita este archivo para configurar las actualizaciones automáticas")

def main():
    """Función principal"""
    print("=" * 60)
    print("GitHub Auto Updater v1.0")
    print("=" * 60)
    
    # Obtener ruta actual
    current_dir = os.getcwd()
    print(f"📂 Directorio actual: {current_dir}")
    
    # Crear instancia del actualizador
    updater = GitHubAutoUpdater(current_dir)
    
    # Verificar si estamos en un repositorio Git
    git_dir = os.path.join(current_dir, ".git")
    if not os.path.exists(git_dir):
        print("❌ No se encontró repositorio Git en esta carpeta")
        return
    
    # Mostrar menú
    print("\n📋 Menú de opciones:")
    print("1. Actualizar ShowStatus a false")
    print("2. Actualizar ShowStatus a true")
    print("3. Actualizar SafeMode a false")
    print("4. Actualizar SafeMode a true")
    print("5. Actualizar número de versión")
    print("6. Actualización automática completa")
    print("7. Crear archivo de configuración")
    print("8. Ver estado Git")
    print("9. Salir")
    
    try:
        option = input("\n🎯 Selecciona una opción (1-9): ").strip()
        
        if option == "1":
            updater.update_showstatus_all_files("false")
            if updater.changes_made:
                updater.git_add_all()
                message = input("💬 Mensaje de commit (deja vacío para auto): ") or "Update ShowStatus to false"
                updater.git_commit(message)
                updater.git_push()
        
        elif option == "2":
            updater.update_showstatus_all_files("true")
            if updater.changes_made:
                updater.git_add_all()
                message = input("💬 Mensaje de commit (deja vacío para auto): ") or "Update ShowStatus to true"
                updater.git_commit(message)
                updater.git_push()
        
        elif option == "3":
            updater.update_safe_mode_all_files("false")
            if updater.changes_made:
                updater.git_add_all()
                message = input("💬 Mensaje de commit (deja vacío para auto): ") or "Update SafeMode to false"
                updater.git_commit(message)
                updater.git_push()
        
        elif option == "4":
            updater.update_safe_mode_all_files("true")
            if updater.changes_made:
                updater.git_add_all()
                message = input("💬 Mensaje de commit (deja vacío para auto): ") or "Update SafeMode to true"
                updater.git_commit(message)
                updater.git_push()
        
        elif option == "5":
            new_version = input("🎯 Nueva versión (ej: 1.5): ").strip()
            if new_version:
                updater.update_version_number(new_version)
                if updater.changes_made:
                    updater.git_add_all()
                    message = input("💬 Mensaje de commit (deja vacío para auto): ") or f"Update version to v{new_version}"
                    updater.git_commit(message)
                    updater.git_push()
        
        elif option == "6":
            create_config_file()
            print("\n🔄 Ejecutando actualización automática...")
            updater.auto_update_all()
        
        elif option == "7":
            create_config_file()
        
        elif option == "8":
            status = updater.check_git_status()
            branch = updater.get_current_branch()
            print(f"\n📊 Rama actual: {branch}")
            if status:
                print(f"📊 Cambios pendientes:\n{status}")
            else:
                print("📊 No hay cambios pendientes")
        
        elif option == "9":
            print("👋 ¡Hasta luego!")
        
        else:
            print("❌ Opción inválida")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Operación cancelada por el usuario")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()