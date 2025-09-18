# interfaces/pantallaPrincipal/parteSuperior.py
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QLinearGradient, QPainter, QBrush, QColor, QIcon

class BotonConfiguracion(QPushButton):
    def __init__(self):
        super().__init__()
        self.configurarBoton()
        self.conectarEventos()
        
    def configurarBoton(self):
        """Configurar estilo y icono del botón"""
        self.setFixedSize(60, 60)
        
        # Configurar icono desde recursos
        ruta_icono = "Frontend/recursos/iconos/iconoConfiguracion.png"
        icono = QIcon(ruta_icono)
        
        if not icono.isNull():
            self.setIcon(icono)
            self.setIconSize(self.size() * 0.6)
        else:
            # Fallback si no se encuentra la imagen
            self.setText("CFG")
        
        # Estilo simplificado sin propiedades CSS web no soportadas
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.95);
                border: 2px solid white;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 1.0);
                border: 2px solid rgba(255, 255, 255, 0.8);
            }
            QPushButton:pressed {
                background-color: rgba(240, 240, 240, 1.0);
                border: 2px solid rgba(220, 220, 220, 1.0);
            }
        """)
        
    def conectarEventos(self):
        """Conectar eventos del botón"""
        self.clicked.connect(self.mostrarMensajeConfiguracion)
    
    def mostrarMensajeConfiguracion(self):
        """Mostrar mensaje de desarrollo"""
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setWindowTitle("Configuración")
        mensaje.setText("En desarrollo")
        mensaje.setInformativeText("La funcionalidad de configuración está siendo desarrollada.")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        mensaje.setStyleSheet("""
            QMessageBox {
                background-color: white;
                font-family: 'Segoe UI';
            }
            QMessageBox QPushButton {
                background-color: #0D9648;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QMessageBox QPushButton:hover {
                background-color: #0a7a3a;
            }
        """)
        
        mensaje.exec()

class WidgetParteSuperior(QFrame):
    def __init__(self):
        super().__init__()
        self.precisionModelo = 95.0
        self.configurarWidget()
        self.crearComponentes()
        
    def configurarWidget(self):
        """Configurar propiedades del widget"""
        self.setFixedSize(1280, 120)
        
    def crearComponentes(self):
        """Crear todos los componentes de la parte superior"""
        self.crearTituloPrincipal()
        self.crearSubtitulo()
        self.crearMarcoPrecision()
        self.crearEtiquetaPrecision()
        self.crearEtiquetaPorcentaje()
        self.crearBotonConfiguracion()
        
    def crearTituloPrincipal(self):
        """Crear título SAIDI Analysis"""
        self.etiquetaTitulo = QLabel("SAIDI Analysis", self)
        self.etiquetaTitulo.setGeometry(10, 15, 245, 45)
        
        fuenteTitulo = QFont("Segoe UI", 28)
        fuenteTitulo.setBold(True)
        fuenteTitulo.setWeight(QFont.Weight.DemiBold)
        
        self.etiquetaTitulo.setFont(fuenteTitulo)
        self.etiquetaTitulo.setStyleSheet("color: white;")
        self.etiquetaTitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
    def crearSubtitulo(self):
        """Crear subtítulo descriptivo"""
        textoSubtitulo = "Sistema Integral de Análisis Predictivo y Simulación Meteorológica"
        self.etiquetaSubtitulo = QLabel(textoSubtitulo, self)
        self.etiquetaSubtitulo.setGeometry(10, 70, 727, 30)
        
        fuenteSubtitulo = QFont("Segoe UI", 16)
        fuenteSubtitulo.setWeight(QFont.Weight.Normal)
        
        self.etiquetaSubtitulo.setFont(fuenteSubtitulo)
        self.etiquetaSubtitulo.setStyleSheet("color: white;")
        self.etiquetaSubtitulo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
    def crearMarcoPrecision(self):
        """Crear marco contenedor de precisión"""
        self.marcoPrecision = QFrame(self)
        self.marcoPrecision.setGeometry(805, 25, 310, 75)
        self.marcoPrecision.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: 2px solid white;
                border-radius: 10px;
            }
        """)
        
    def crearEtiquetaPrecision(self):
        """Crear etiqueta Precisión del modelo"""
        self.etiquetaPrecision = QLabel("Precisión del modelo", self.marcoPrecision)
        self.etiquetaPrecision.setGeometry(29, 5, 247, 32)
        
        fuentePrecision = QFont("Segoe UI", 19)
        fuentePrecision.setWeight(QFont.Weight.Normal)
        
        self.etiquetaPrecision.setFont(fuentePrecision)
        self.etiquetaPrecision.setStyleSheet("color: white; background-color: transparent; border: none;")
        self.etiquetaPrecision.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
    def crearEtiquetaPorcentaje(self):
        """Crear etiqueta del porcentaje"""
        self.etiquetaPorcentaje = QLabel(f"{self.precisionModelo:.0f}%", self.marcoPrecision)
        self.etiquetaPorcentaje.setGeometry(127, 39, 54, 34)
        
        fuentePorcentaje = QFont("Segoe UI", 21)
        fuentePorcentaje.setWeight(QFont.Weight.DemiBold)
        
        self.etiquetaPorcentaje.setFont(fuentePorcentaje)
        self.etiquetaPorcentaje.setStyleSheet("color: white; background-color: transparent; border: none;")
        self.etiquetaPorcentaje.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        
    def crearBotonConfiguracion(self):
        """Crear botón de configuración con icono"""
        self.botonConfiguracion = BotonConfiguracion()
        self.botonConfiguracion.setParent(self)
        self.botonConfiguracion.move(1195, 30)
    
    def paintEvent(self, event):
        """Dibujar gradiente de fondo"""
        pintor = QPainter(self)
        pintor.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        gradiente = QLinearGradient(0, 0, self.width(), 0)
        gradiente.setColorAt(0, QColor("#0D9648"))
        gradiente.setColorAt(1, QColor("#9FCF67"))
        
        pincel = QBrush(gradiente)
        pintor.fillRect(self.rect(), pincel)
        
    def actualizarPrecision(self, nuevaPrecision):
        """Actualizar precisión del modelo"""
        self.precisionModelo = nuevaPrecision
        self.etiquetaPorcentaje.setText(f"{self.precisionModelo:.0f}%")