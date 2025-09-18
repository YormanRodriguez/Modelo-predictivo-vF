# main.py
import sys
from PyQt6.QtWidgets import QApplication
from interfaces.interfaz import VentanaPrincipalSAIDI

def main():
    """Función principal para ejecutar la aplicación SAIDI Analysis"""
    app = QApplication(sys.argv)
    
    try:
        # Configuraciones adicionales de la aplicación si son necesarias
        app.setApplicationName("SAIDI Analysis")
        app.setApplicationVersion("2.0")
        
    except Exception as e:
        print(f"Error inicializando la aplicación: {e}")
    
    # Crear y mostrar la ventana principal
    ventana = VentanaPrincipalSAIDI()
    ventana.show()
    
    # Ejecutar la aplicación
    sys.exit(app.exec())

if __name__ == "__main__":
    main()