# interfaces/pantallaConfiguracion/botonRegreso.py
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

class BotonRegreso(QPushButton):
    def __init__(self):
        super().__init__()
        self.configurarBoton()
        
    def configurarBoton(self):
        """Configurar estilo y icono del botón de regreso"""
        # Tamaño del botón según especificaciones
        self.setFixedSize(int(60.32), int(60.32))
        
        # Configurar icono desde recursos
        ruta_icono = "Frontend/recursos/iconos/iconoRegresar.png"
        icono = QIcon(ruta_icono)
        
        if not icono.isNull():
            self.setIcon(icono)
            # Tamaño del icono: 40.32 x 40.32
            self.setIconSize(self.size() * (40.32 / 60.32))  # Proporción correcta
        else:
            # Fallback si no se encuentra la imagen
            self.setText("←")
        
        # Estilo del botón circular con borde negro
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 38px;
            }
            QPushButton:hover {
                background-color: rgba(240, 240, 240, 1.0);
                border: 2px solid black;
            }
            QPushButton:pressed {
                background-color: rgba(220, 220, 220, 1.0);
                border: 2px solid black;
            }
        """)
        
        # Conectar la funcionalidad de cierre
        self.clicked.connect(self.regresarVentanaPrincipal)
    
    def regresarVentanaPrincipal(self):
        """Cerrar la ventana de configuración y regresar a la principal"""
        # Buscar la ventana padre (VentanaConfiguracion) y cerrarla
        ventana_config = self.window()
        if hasattr(ventana_config, 'cerrar'):
            ventana_config.cerrar()
        else:
            ventana_config.close()