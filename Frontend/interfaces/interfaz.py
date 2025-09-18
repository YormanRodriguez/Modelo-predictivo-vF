# interfaces/interfaz.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from interfaces.pantallaPrincipal.parteSuperior import WidgetParteSuperior
# from interfaces.pantallaPrincipal.parteMediaSuperior import WidgetParteMediaSuperior
# from interfaces.pantallaPrincipal.parteMediaInferior import WidgetParteMediaInferior  
# from interfaces.pantallaPrincipal.parteInferior import WidgetParteInferior

class VentanaPrincipalSAIDI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.configurarVentana()
        self.cargarInterfaz()
        
    def configurarVentana(self):
        """Configurar propiedades básicas de la ventana"""
        self.setWindowTitle("SAIDI Analysis")
        self.setFixedSize(1280, 720)
        self.centrarVentana()
        self.setStyleSheet("QMainWindow { background-color: white; }")
        
    def centrarVentana(self):
        """Centrar la ventana en la pantalla"""
        screen = QApplication.primaryScreen()
        geometria = screen.availableGeometry()
        
        x = (geometria.width() - self.width()) // 2
        y = (geometria.height() - self.height()) // 2
        
        x = max(0, x)
        y = max(0, y)
        
        self.move(x, y)
        
    def cargarInterfaz(self):
        """Cargar todas las partes de la interfaz"""
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        # Layout principal con espaciado uniforme entre partes
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(32)  # 32 píxeles entre cada parte
        layout_principal.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Cargar cada parte de la interfaz
        self.cargarParteSuperior(layout_principal)
        # self.cargarParteMediaSuperior(layout_principal)
        # self.cargarParteMediaInferior(layout_principal)  
        # self.cargarParteInferior(layout_principal)
        
        widget_central.setLayout(layout_principal)
        
    def cargarParteSuperior(self, layout):
        """Cargar la parte superior (header)"""
        self.parte_superior = WidgetParteSuperior()
        layout.addWidget(self.parte_superior)
        
    def cargarParteMediaSuperior(self, layout):
        """Cargar la parte media superior (gestión de datos)"""
        # self.parte_media_superior = WidgetParteMediaSuperior()
        # layout.addWidget(self.parte_media_superior)
        pass
        
    def cargarParteMediaInferior(self, layout):
        """Cargar la parte media inferior (simulador)"""
        # self.parte_media_inferior = WidgetParteMediaInferior()
        # layout.addWidget(self.parte_media_inferior)
        pass
        
    def cargarParteInferior(self, layout):
        """Cargar la parte inferior (footer)"""
        # self.parte_inferior = WidgetParteInferior()
        # layout.addWidget(self.parte_inferior)
        pass