# interfaces/pantallaConfiguracion/InterfazConfiguracion.py
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtCore import Qt, pyqtSignal

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
        
    def configurarVentana(self):
        """Configurar propiedades básicas de la ventana de configuración"""
        # Quitar la barra de título y hacer la ventana sin marco
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        
        # Tamaño fijo según especificaciones de Figma
        self.setFixedSize(1123, 450)
        
        # Posicionar relativo a la ventana padre
        self.posicionarRelativoAPadre()
        
        self.setStyleSheet("QMainWindow { background-color: white; }")
        
        # Hacer la ventana modal (bloquea la ventana principal)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        
    def posicionarRelativoAPadre(self):
        """Posicionar la ventana relativa a la ventana padre"""
        if self.ventana_padre:
            # Obtener la posición de la ventana padre
            pos_padre = self.ventana_padre.pos()
            
            # Calcular la posición relativa (79, 50) dentro de la ventana padre
            nueva_x = pos_padre.x() + 79
            nueva_y = pos_padre.y() + 50
            
            # Posicionar la ventana
            self.move(nueva_x, nueva_y)
        else:
            # Fallback a posición absoluta si no hay ventana padre
            self.move(79, 50)
        
    def crearInterfaz(self):
        """Crear la interfaz de configuración (contenedor principal)"""
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        # Aquí se cargarán los componentes desde otros archivos
        # Similar a como funciona interfaz.py
        
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