# interfaces/pantallaConfiguracion/InterfazConfiguracion.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath

from interfaces.pantallaConfiguracion.botonRegreso import BotonRegreso
# from interfaces.pantallaConfiguracion.cuadroPredecir import CuadroPredecir
# from interfaces.pantallaConfiguracion.cuadroComportamiento import CuadroComportamiento  
# from interfaces.pantallaConfiguracion.cuadroParametros import CuadroParametros

class VentanaConfiguracion(QMainWindow):
    # Señal para comunicar el cierre de la ventana
    ventanaCerrada = pyqtSignal()
    
    def __init__(self, ventana_padre=None):
        super().__init__()
        self.ventana_padre = ventana_padre
        self.arrastrando = False
        self.posicion_click = None
        self.configurarVentana()
        self.crearInterfaz()
        self.aplicarEfectoSombra()
        
    def configurarVentana(self):
        """Configurar propiedades básicas de la ventana de configuración"""
        # Quitar la barra de título y hacer la ventana sin marco
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        
        # Tamaño fijo según especificaciones de Figma
        self.setFixedSize(1123, 450)
        
        # Posicionar relativo a la ventana padre
        self.posicionarRelativoAPadre()
        
        # Fondo transparente para permitir que se vea la sombra
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Hacer la ventana modal (bloquea la ventana principal)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
    def posicionarRelativoAPadre(self):
        """Posicionar la ventana relativa a la ventana padre"""
        if self.ventana_padre:
            # Obtener la posición de la ventana padre
            pos_padre = self.ventana_padre.pos()
            
            # Calcular la posición relativa (79, 50) dentro de la ventana padre
            # Ajustamos un poco para compensar la sombra
            nueva_x = pos_padre.x() + 79 - 5  # -5 para compensar la sombra
            nueva_y = pos_padre.y() + 50 - 5  # -5 para compensar la sombra
            
            # Posicionar la ventana
            self.move(nueva_x, nueva_y)
        else:
            # Fallback a posición absoluta si no hay ventana padre
            self.move(74, 45)  # Ajustado para compensar sombra
        
    def crearInterfaz(self):
        """Crear la interfaz de configuración (contenedor principal)"""
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        # El widget central tendrá el fondo y bordes personalizados
        widget_central.setStyleSheet("background-color: transparent;")
        
        # Cargar todos los componentes de la interfaz de configuración
        self.cargarComponentes()
        
    def cargarComponentes(self):
        """Cargar todos los componentes de la ventana de configuración"""
        self.cargarBotonRegreso()
        self.cargarCuadroPredecir()
        self.cargarCuadroComportamiento()
        self.cargarCuadroParametros()
        
    def cargarBotonRegreso(self):
        """Cargar el botón de regreso"""
        self.boton_regreso = BotonRegreso()
        self.boton_regreso.setParent(self)
        self.boton_regreso.move(1022, 358)
        
    def cargarCuadroPredecir(self):
        """Cargar el cuadro de predicción"""
        # self.cuadro_predecir = CuadroPredecir()
        # self.cuadro_predecir.setParent(self)
        # self.cuadro_predecir.move(x, y)  # Posición a definir
        pass
        
    def cargarCuadroComportamiento(self):
        """Cargar el cuadro de comportamiento"""
        # self.cuadro_comportamiento = CuadroComportamiento()
        # self.cuadro_comportamiento.setParent(self)
        # self.cuadro_comportamiento.move(x, y)  # Posición a definir
        pass
        
    def cargarCuadroParametros(self):
        """Cargar el cuadro de parámetros"""
        # self.cuadro_parametros = CuadroParametros()
        # self.cuadro_parametros.setParent(self)
        # self.cuadro_parametros.move(x, y)  # Posición a definir
        pass
        
    def aplicarEfectoSombra(self):
        """Aplicar efecto de sombra proyectada a la ventana"""
        efecto_sombra = QGraphicsDropShadowEffect()
        efecto_sombra.setBlurRadius(10)  # Radio de desenfoque de la sombra
        efecto_sombra.setXOffset(3)      # Desplazamiento horizontal
        efecto_sombra.setYOffset(3)      # Desplazamiento vertical
        efecto_sombra.setColor(QColor(0, 0, 0, 100))  # Color negro con transparencia
        
        # Aplicar el efecto al widget central
        self.centralWidget().setGraphicsEffect(efecto_sombra)
        
    def paintEvent(self, event):
        """Dibujar la ventana con esquinas redondeadas y borde negro"""
        pintor = QPainter(self)
        pintor.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Definir el área de dibujo (dejando espacio para la sombra)
        margen_sombra = 10
        ancho_real = self.width() - margen_sombra
        alto_real = self.height() - margen_sombra
        
        # Crear el path con esquinas redondeadas
        ruta = QPainterPath()
        radio_esquina = 10
        ruta.addRoundedRect(5, 5, ancho_real - 10, alto_real - 10, radio_esquina, radio_esquina)
        
        # Dibujar el fondo blanco
        pintor.fillPath(ruta, QBrush(QColor(255, 255, 255)))
        
        # Dibujar el borde negro de 3px
        pintor.strokePath(ruta, QPen(QColor(0, 0, 0), 3, Qt.PenStyle.SolidLine))
        
    def cerrar(self):
        """Cerrar la ventana de configuración"""
        self.ventanaCerrada.emit()
        self.close()
        
    def closeEvent(self, event):
        """Evento al cerrar la ventana"""
        self.ventanaCerrada.emit()
        super().closeEvent(event)
        
    def mousePressEvent(self, event):
        """Iniciar el arrastre de ambas ventanas"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.arrastrando = True
            self.posicion_click = event.globalPosition().toPoint()
        
    def mouseMoveEvent(self, event):
        """Mover ambas ventanas al arrastrar"""
        if self.arrastrando and event.buttons() == Qt.MouseButton.LeftButton:
            # Calcular la diferencia de movimiento
            nueva_posicion = event.globalPosition().toPoint()
            diferencia = nueva_posicion - self.posicion_click
            
            # Mover la ventana de configuración
            nueva_pos_config = self.pos() + diferencia
            self.move(nueva_pos_config)
            
            # Mover también la ventana padre
            if self.ventana_padre:
                nueva_pos_padre = self.ventana_padre.pos() + diferencia
                self.ventana_padre.move(nueva_pos_padre)
            
            # Actualizar la posición de referencia
            self.posicion_click = nueva_posicion
            
    def mouseReleaseEvent(self, event):
        """Finalizar el arrastre"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.arrastrando = False
            self.posicion_click = None