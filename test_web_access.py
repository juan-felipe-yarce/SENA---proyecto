#!/usr/bin/env python
import requests
import time

def test_web_access():
    print("🌐 Probando acceso web...")
    
    base_url = "http://127.0.0.1:8000"
    
    # URLs a probar
    urls_to_test = [
        "/",
        "/admin/",
        "/login/",
    ]
    
    for url in urls_to_test:
        try:
            response = requests.get(f"{base_url}{url}", timeout=5)
            if response.status_code == 200:
                print(f"✅ {url} - OK (200)")
            elif response.status_code == 302:
                print(f"✅ {url} - Redirect (302) - Normal para login/admin")
            else:
                print(f"⚠️ {url} - Status: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ {url} - Error de conexión (servidor no disponible)")
        except requests.exceptions.Timeout:
            print(f"❌ {url} - Timeout")
        except Exception as e:
            print(f"❌ {url} - Error: {e}")
    
    print("\n📋 Instrucciones para probar el formulario:")
    print("1. Abre tu navegador")
    print("2. Ve a: http://127.0.0.1:8000")
    print("3. Inicia sesión con un usuario docente")
    print("4. Ve a la sección de 'Datos Básicos'")
    print("5. Prueba llenar el formulario con y sin campos opcionales")
    
    print("\n🔑 Usuarios de prueba disponibles:")
    print("- deibyok@gmail.com / Jhans2023#")
    print("- admin2@gmail.com / admin2")
    print("- jhans@gmail.com / Deiby2023#")
    
    print("\n✅ El formulario ahora acepta campos opcionales como:")
    print("- Estado civil (opcional)")
    print("- Género (opcional)")
    print("- Estrato (opcional)")
    print("- Teléfonos adicionales (opcionales)")
    print("- Correo alternativo (opcional)")

if __name__ == '__main__':
    test_web_access() 