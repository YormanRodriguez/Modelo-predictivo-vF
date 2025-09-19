# interfaces/pantallaPrincipal/parteMediaSuperior.py
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QLinearGradient, QPainter, QBrush, QColor, QPixmap

class BotonRegional(QPushButton):
    def __init__(self, texto):
        super().__init__(texto)
        self.configurarBoton()
        
    def configurarBoton(self):
        self.setFixedSize(75, 30)
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid #0D9648;
                border-radius: 4px;
                color: #0D9648;
                font-family: 'Segoe UI';
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f0f8f3;
            }
            QPushButton:pressed {
                background-color: #e0f0e6;
            }
        """)

class CuadroRegional(QFrame):
    def __init__(self, nombreRegional):
        super().__init__()
        self.nombreRegional = nombreRegional
        self.configurarCuadro()
        self.crearComponentes()
        
    def configurarCuadro(self):
        self.setFixedSize(170, 110)
        self.setStyleSheet("""
            QFrame {
                background-color: #B6B6B6;
                border: 2px solid #B6B6B6;
                border-radius: 5px;
            }
        """)
        
    def crearComponentes(self):
        self.crearEtiquetaRegional()
        self.crearBotonSeleccion()
        
    def crearEtiquetaRegional(self):
        self.etiquetaRegional = QLabel(self.nombreRegional, self)
        self.etiquetaRegional.setGeometry(37, 15, 96, 24)
        
        fuenteRegional = QFont("Segoe UI", 14)
        fuenteRegional.setBold(True)
        
        self.etiquetaRegional.setFont(fuenteRegional)
        self.etiquetaRegional.setStyleSheet("color: white; background-color: transparent; border: none;")
        self.etiquetaRegional.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def crearBotonSeleccion(self):
        self.botonSeleccion = BotonRegional("Seleccionar")
        self.botonSeleccion.setParent(self)
        self.botonSeleccion.move(47, 56)

class ContenedorRegionales(QWidget):
    def __init__(self):
        super().__init__()
        self.regionalesNombres = ["Cúcuta", "Ocaña", "Pamplona", "Tibú", "Aguachica"]
        self.configurarContenedor()
        self.crearCuadrosRegionales()
        
    def configurarContenedor(self):
        self.setFixedSize(950, 110)
        
    def crearCuadrosRegionales(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(18)
        
        for nombreRegional in self.regionalesNombres:
            cuadroRegional = CuadroRegional(nombreRegional)
            layout.addWidget(cuadroRegional)
            
        self.setLayout(layout)

class ContenedorSuperior(QFrame):
    def __init__(self):
        super().__init__()
        self.configurarContenedor()
        
    def configurarContenedor(self):
        self.setFixedSize(1224, 77)
        
    def paintEvent(self, event):
        pintor = QPainter(self)
        pintor.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        gradiente = QLinearGradient(0, 0, self.width(), 0)
        gradiente.setColorAt(0, QColor("#0D9648"))
        gradiente.setColorAt(1, QColor("#9FCF67"))
        
        pincel = QBrush(gradiente)
        
        from PyQt6.QtGui import QPainterPath
        ruta = QPainterPath()
        ruta.addRoundedRect(0, 0, self.width(), self.height(), 8, 8)
        
        rectanguloInferior = QPainterPath()
        rectanguloInferior.addRect(0, self.height()-10, self.width(), 10)
        ruta = ruta.united(rectanguloInferior)
        
        pintor.fillPath(ruta, pincel)

class WidgetParteMediaSuperior(QFrame):
    def __init__(self):
        super().__init__()
        self.configurarWidget()
        self.crearComponentes()
        
    def configurarWidget(self):
        self.setFixedSize(1280, 225)
        
    def crearComponentes(self):
        self.crearCuadroPrincipal()
        self.crearContenedorSuperior()
        self.crearIconoParteSuperior()
        self.crearTextoSuperior()
        self.crearTextoMedio()
        self.crearContenedorRegionales()
        
    def crearCuadroPrincipal(self):
        self.cuadroPrincipal = QFrame(self)
        self.cuadroPrincipal.setGeometry(25, 0, 1230, 225)
        self.cuadroPrincipal.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 3px solid #0D9648;
                border-radius: 10px;
            }
        """)
        
    def crearContenedorSuperior(self):
        self.contenedorSuperior = ContenedorSuperior()
        self.contenedorSuperior.setParent(self)
        self.contenedorSuperior.move(28, 2)
        
    def crearIconoParteSuperior(self):
        self.etiquetaIcono = QLabel(self)
        self.etiquetaIcono.setGeometry(57, 18, 40, 40)
        
        rutaIcono = "Frontend/recursos/iconos/iconoParteSuperior.png"
        pixmap = QPixmap(rutaIcono)
        
        if not pixmap.isNull():
            pixmapEscalado = pixmap.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.etiquetaIcono.setPixmap(pixmapEscalado)
        else:
            self.etiquetaIcono.setText("ICO")
            self.etiquetaIcono.setStyleSheet("color: white; background-color: transparent; border: none;")
            self.etiquetaIcono.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
    def crearTextoSuperior(self):
        self.etiquetaTextoSuperior = QLabel("Selección de Regional del Sistema", self)
        self.etiquetaTextoSuperior.setGeometry(108, 22, 417, 33)
        
        fuenteTextoSuperior = QFont("Segoe UI", 19)
        fuenteTextoSuperior.setBold(True)
        
        self.etiquetaTextoSuperior.setFont(fuenteTextoSuperior)
        self.etiquetaTextoSuperior.setStyleSheet("color: white; background-color: transparent; border: none;")
        self.etiquetaTextoSuperior.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
    def crearTextoMedio(self):
        self.etiquetaTextoMedio = QLabel("Selección de regional:", self)
        self.etiquetaTextoMedio.setGeometry(40, 133, 215, 28)
        
        fuenteTextoMedio = QFont("Segoe UI", 16)
        fuenteTextoMedio.setBold(True)
        
        self.etiquetaTextoMedio.setFont(fuenteTextoMedio)
        self.etiquetaTextoMedio.setStyleSheet("color: #0D9648; background-color: transparent; border: none;")
        self.etiquetaTextoMedio.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
    def crearContenedorRegionales(self):
        self.contenedorRegionales = ContenedorRegionales()
        self.contenedorRegionales.setParent(self)
        self.contenedorRegionales.move(275, 105)