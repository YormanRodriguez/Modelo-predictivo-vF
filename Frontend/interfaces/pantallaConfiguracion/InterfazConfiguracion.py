# interfaces/pantallaConfiguracion/InterfazConfiguracion.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class VentanaConfiguracion(QMainWindow):
    # Señal para comunicar el cierre de la ventana
    ventanaCerrada = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.configurarVentana()
        self.crearInterfaz()
        
    def configurarVentana(self):
        """Configurar propiedades básicas de la ventana de configuración"""
        self.setWindowTitle("Configuración - SAIDI Analysis")
        self.setFixedSize(800, 600)
        self.centrarVentana()
        self.setStyleSheet("QMainWindow { background-color: white; }")
        
        # Hacer la ventana modal (bloquea la ventana principal)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
    def centrarVentana(self):
        """Centrar la ventana en la pantalla"""
        from PyQt6.QtWidgets import QApplication
        screen = QApplication.primaryScreen()
        geometria = screen.availableGeometry()
        
        x = (geometria.width() - self.width()) // 2
        y = (geometria.height() - self.height()) // 2
        
        x = max(0, x)
        y = max(0, y)
        
        self.move(x, y)
        
    def crearInterfaz(self):
        """Crear la interfaz de configuración"""
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.setContentsMargins(50, 50, 50, 50)
        layout_principal.setSpacing(30)
        
        # Título de la ventana de configuración
        self.crearTitulo(layout_principal)
        
        # Área de contenido (en blanco por ahora)
        self.crearAreaContenido(layout_principal)
        
        # Botones de acción
        self.crearBotones(layout_principal)
        
        widget_central.setLayout(layout_principal)
        
    def crearTitulo(self, layout):
        """Crear título de la ventana de configuración"""
        titulo = QLabel("Configuración del Sistema")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        fuente_titulo = QFont("Segoe UI", 24)
        fuente_titulo.setBold(True)
        fuente_titulo.setWeight(QFont.Weight.Bold)
        
        titulo.setFont(fuente_titulo)
        titulo.setStyleSheet("""
            QLabel {
                color: #0D9648;
                padding: 20px;
                border-bottom: 2px solid #0D9648;
                margin-bottom: 20px;
            }
        """)
        
        layout.addWidget(titulo)
        
    def crearAreaContenido(self, layout):
        """Crear área de contenido principal (en blanco por ahora)"""
        contenido = QLabel("Esta ventana está en construcción.\n\nAquí se mostrarán las opciones de configuración del sistema.")
        contenido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        fuente_contenido = QFont("Segoe UI", 14)
        contenido.setFont(fuente_contenido)
        
        contenido.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #0D9648;
                border-radius: 10px;
                padding: 40px;
                color: #666;
                line-height: 1.6;
            }
        """)
        
        layout.addWidget(contenido)
        
    def crearBotones(self, layout):
        """Crear botones de acción"""
        # Layout horizontal para botones
        from PyQt6.QtWidgets import QHBoxLayout
        layout_botones = QHBoxLayout()
        layout_botones.setSpacing(15)
        
        # Espaciador izquierdo
        layout_botones.addStretch()
        
        # Botón Aceptar
        boton_aceptar = QPushButton("Aceptar")
        boton_aceptar.setFixedSize(120, 40)
        boton_aceptar.clicked.connect(self.aceptar)
        boton_aceptar.setStyleSheet("""
            QPushButton {
                background-color: #0D9648;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #0a7a3a;
            }
            QPushButton:pressed {
                background-color: #085d2c;
            }
        """)
        
        # Botón Cancelar
        boton_cancelar = QPushButton("Cancelar")
        boton_cancelar.setFixedSize(120, 40)
        boton_cancelar.clicked.connect(self.cancelar)
        boton_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
            QPushButton:pressed {
                background-color: #4e555b;
            }
        """)
        
        layout_botones.addWidget(boton_aceptar)
        layout_botones.addWidget(boton_cancelar)
        
        # Espaciador derecho
        layout_botones.addStretch()
        
        layout.addLayout(layout_botones)
        
    def aceptar(self):
        """Acción del botón Aceptar"""
        # Aquí se procesarían las configuraciones
        print("Configuraciones guardadas") # Debug temporal
        self.cerrar()
        
    def cancelar(self):
        """Acción del botón Cancelar"""
        self.cerrar()
        
    def cerrar(self):
        """Cerrar la ventana de configuración"""
        self.ventanaCerrada.emit()
        self.close()
        
    def closeEvent(self, event):
        """Evento al cerrar la ventana"""
        self.ventanaCerrada.emit()
        super().closeEvent(event)