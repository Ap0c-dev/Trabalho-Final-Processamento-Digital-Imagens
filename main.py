import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QLabel, QToolTip, QGridLayout, QWidget, QMessageBox,QSlider
from PyQt5.QtCore import QSize, Qt
import subprocess

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()        
        self.setup_main_window()
        self.initUI() 

    def setup_main_window(self):
        self.x = 1280
        self.y = 920
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.wid = QWidget(self) 
        self.setCentralWidget(self.wid) 
        self.layout = QGridLayout() 
        self.wid.setLayout(self.layout) 

    def initUI(self): 
        #Criar menu
        self.barraMenu = self.menuBar() 

        #Label Transparencia
        
        self.texto2 = QLabel("Transparencia", self)
        self.texto2.adjustSize()
        self.largura = self.texto2.frameGeometry().width()
        self.altura = self.texto2.frameGeometry().height()
        self.texto2.setAlignment(QtCore.Qt.AlignCenter)   

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.valueChanged[int].connect(self.botaoTransp)

        #Criar o menu
        self.menuArqv = self.barraMenu.addMenu("&Arquivo")
        self.menuTransformacao = self.barraMenu.addMenu("&Transformação")
        self.menuEspelhar = self.barraMenu.addMenu("&Espelhar")
        self.menuEsteg = self.barraMenu.addMenu("&Esteganografia")
        self.menuSobre = self.barraMenu.addMenu("&Sobre") 

        # Criar as ações 
        self.abrir = self.menuArqv.addAction("Abrir") 
        self.abrir.triggered.connect(self.botaoAbrir)
        self.abrir = self.menuArqv.addAction("Salvar Como") 
        self.abrir.triggered.connect(self.botaoSalvar) 
        self.fechar = self.menuArqv.addAction("Fechar") 
        self.fechar.triggered.connect(self.close)

        #Açoes Efeitos
        self.transformar = self.menuTransformacao.addAction("Blur") 
        self.transformar.triggered.connect(self.botaoTransformar) 
        self.menuTransformacao.addSeparator()
        self.transformar3 = self.menuTransformacao.addAction("Contour") 
        self.transformar3.triggered.connect(self.botaoTransformar3) 
        self.menuTransformacao.addSeparator()
        
        self.separaMenu = self.menuTransformacao.addAction("Camada R") 
        self.separaMenu.triggered.connect(self.botaoCamadaR)
        self.menuTransformacao.addSeparator() 
        self.separaMenu1 = self.menuTransformacao.addAction("Camada G") 
        self.separaMenu1.triggered.connect(self.botaoCamadaG)
        self.menuTransformacao.addSeparator() 
        self.separaMenu2 = self.menuTransformacao.addAction("Camada B") 
        self.separaMenu2.triggered.connect(self.botaoCamadaB)
        self.menuTransformacao.addSeparator()  
        
        self.transformar4 = self.menuTransformacao.addAction("Detail") 
        self.transformar4.triggered.connect(self.botaoTransformar4) 
        self.menuTransformacao.addSeparator()

        
        self.detectMenu = self.menuTransformacao.addMenu("Detectar Bordas")
        self.detectMenu.addAction("Detecção Bordas 1")
        self.detectMenu.triggered.connect(self.botaoDeteccao1)
        self.menuTransformacao.addSeparator() 
        self.detectMenu.addAction("Detecção Bordas2")
        self.detectMenu.triggered.connect(self.botaoDeteccao2)
        self.menuTransformacao.addSeparator() 
        self.detectMenu.addAction("Detecção Bordas 3")
        self.detectMenu.triggered.connect(self.botaoDeteccao3)
        self.menuTransformacao.addSeparator()

        self.transformar5 = self.menuTransformacao.addAction("Edge Enhace") 
        self.transformar5.triggered.connect(self.botaoTransformar5) 
        self.menuTransformacao.addSeparator()
        self.transformar6 = self.menuTransformacao.addAction("Edge Enhace More") 
        self.transformar6.triggered.connect(self.botaoTransformar6) 
        self.menuTransformacao.addSeparator()
        self.transformar7 = self.menuTransformacao.addAction("Emboss") 
        self.transformar7.triggered.connect(self.botaoTransformar7) 
        self.menuTransformacao.addSeparator()
        self.transformar1 = self.menuTransformacao.addAction("Find Edges") 
        self.transformar1.triggered.connect(self.botaoTransformar1) 
        self.menuTransformacao.addSeparator()
        self.transformar12 = self.menuTransformacao.addAction("Negativo") 
        self.transformar12.triggered.connect(self.botaoNegativo) 
        self.menuTransformacao.addSeparator()
        self.transformar8 = self.menuTransformacao.addAction("Sharpen") 
        self.transformar8.triggered.connect(self.botaoTransformar8) 
        self.menuTransformacao.addSeparator()
        self.transformar2 = self.menuTransformacao.addAction("Smooth") 
        self.transformar2.triggered.connect(self.botaoTransformar2)
        self.menuTransformacao.addSeparator()
        self.transformar9 = self.menuTransformacao.addAction("Smooth More") 
        self.transformar9.triggered.connect(self.botaoTransformar9) 
        self.menuTransformacao.addSeparator()

        self.transformar11 = self.menuTransformacao.addAction("Tons de Cinza")
        self.transformar11.triggered.connect(self.botaoTonsCinza)
        self.menuTransformacao.addSeparator()


        #Açoes de Rotação
        self.espelhar = self.menuEspelhar.addAction("Horizontal")
        self.espelhar.triggered.connect(self.botaoEspelhar)
        self.menuTransformacao.addSeparator()
        self.espelhar1 = self.menuEspelhar.addAction("Vertical")
        self.espelhar1.triggered.connect(self.botaoEspelhar2)
        self.menuTransformacao.addSeparator()
        
        
        self.espelhar = self.menuEspelhar.addAction('Rotacionar 90')
        self.espelhar.triggered.connect(self.botaoRotacionar90)
        self.menuTransformacao.addSeparator()
        self.espelhar = self.menuEspelhar.addAction('Rotacionar 180')
        self.espelhar.triggered.connect(self.botaoRotacionar180)
        self.menuTransformacao.addSeparator()
        self.espelhar = self.menuEspelhar.addAction('Rotacionar 270')
        self.espelhar.triggered.connect(self.botaoRotacionar270)
        self.menuTransformacao.addSeparator()

        
        #Tentativa de Criar o subMenu 
        self.rotacionarMenu = self.menuEspelhar.addMenu("Rotacionar")
        self.rotacionarMenu .addAction("Rotacionar 90˚")
        self.rotacionarMenu.triggered.connect(self.botaoRotacionar90)
        self.menuTransformacao.addSeparator()
        self.rotacionarMenu.addAction("Rotacionar 180˚")
        self.rotacionarMenu.triggered.connect(self.botaoRotacionar180)
        self.menuTransformacao.addSeparator()
        self.rotacionarMenu.addAction("Rotacionar 270˚")
        self.rotacionarMenu.triggered.connect(self.botaoRotacionar270)
        self.menuTransformacao.addSeparator()

        self.esteg = self.menuEsteg.addAction("Encriptar")
        self.esteg.triggered.connect(self.botaoEncript)

        self.Sobre = self.menuSobre.addAction("Sobre o Desenvolvedor") 
        self.Sobre.triggered.connect(self.botaoSobre) 
        self.sobre = self.menuSobre.addAction("Sobre a Imagem")
        self.sobre.triggered.connect(self.botaoSobre1) 

        #Criando um imagem
        self.imagem1 = QLabel(self) 
        self.endereco1 = 'imagens/leao_colorido.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem1.setPixmap(self.pixmap1)

        #Imagem 2
        self.imagem2 = QLabel(self) 
        self.endereco2 = 'imagens/leao_colorido.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

        #Organizando o Grid
        self.layout.addWidget(self.imagem1, 2, 0)
        self.layout.addWidget(self.imagem2, 2, 1)

        self.layout.addWidget(self.texto2, 5, 4, 3, 2)
        self.layout.addWidget(self.slider, 4, 4, 3, 2)
        

    #OpenFileDialog
    def botaoAbrir(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Abrir arquivo', 
                                                            directory=QtCore.QDir.currentPath(), 
                                                            filter='All files (*.*);; Imagens (*.jpg; *.png)',
                                                            initialFilter='Imagens (*.jpg; *.png)')
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(564, 408, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)

    def botaoSalvar(self):  
        self.arquivo = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title', '/area de trabalho', selectedFilter='*.')
    
    def botaoTransformar(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo.jpg'
        self.script = '.\ef_blur.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar1(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_1.jpg'
        self.script = '.\ef_find_edges.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar2(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_2.jpg'
        self.script = '.\smooth_more.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar3(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_3.jpg'
        self.script = '.\contour.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar4(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_4.jpg'
        self.script = '.\detail.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoTransformar5(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_5.jpg'
        self.script = '.\edge_enhace.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar6(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_6.jpg'
        self.script = '.\edge_enhace_more.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoTransformar7(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_7.jpg'
        self.script = '.\emboss.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar8(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_8.jpg'
        self.script = '.\sharpen.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransformar9(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_9.jpg'
        self.script = '.\smooth.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTonsCinza(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_9.jpg'
        self.script = '.\ef_tons_de_cinza.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoNegativo(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/negativo.jpg'
        self.script = '.\ef_negativo.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoDeteccao1(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/deteccao1.jpg'
        self.script = '.\deteccao_bordas1.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoDeteccao2(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/deteccao2.jpg'
        self.script = '.\deteccao_bordas2.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoDeteccao3(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/deteccao3.jpg'
        self.script = '.\deteccao_bordas3.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoCamadaR(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/camadaR.jpg'
        self.script = '.\camadaR.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoCamadaG(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/camadaG.jpg'
        self.script = '.\camadaG.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoCamadaB(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/camadaB.jpg'
        self.script = '.\camadaB.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)


    #Métodos de Espelhamento

    def botaoEspelhar(self):
        self.imagemOriginal = self.endereco1
        self.imagemEspelhada = 'imagens/espelhada_horz.jpg'
        self.script = '.\espelhar_Horz.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemEspelhada
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemEspelhada
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoEspelhar2(self):
        self.imagemOriginal = self.endereco1
        self.imagemEspelhada = 'imagens/espelhada_vert.jpg'
        self.script = '.\espelhar_Vert.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemEspelhada
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemEspelhada
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoRotacionar90(self):
        self.imagemOriginal = self.endereco1
        self.imagemEspelhada = 'imagens/rotate_90.jpg'
        self.script = '.\ef_rotate_90.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemEspelhada
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemEspelhada
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoRotacionar180(self):
        self.imagemOriginal = self.endereco1
        self.imagemEspelhada = 'imagens/rotate_90.jpg'
        self.script = '.\ef_rotate_180.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemEspelhada
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemEspelhada
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)
    
    def botaoRotacionar270(self):
        self.imagemOriginal = self.endereco1
        self.imagemEspelhada = 'imagens/rotate_270.jpg'
        self.script = '.\ef_rotate_270.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemEspelhada
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemEspelhada
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)

    def botaoTransp(self, value = ""):
        self.entrada = self.endereco1
        self.saida = 'imagens/img_transp.png'
        self.script = '.\ef_transpose.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida + ' \"' + str(value)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def botaoEncript(self):
        self.entrada = 'imagens/img_transp.png'
        self.saida = 'imagens/img_encript.png'
        self.script = '.criptografar.py'
        self.programa = 'python ' + self.script + ' \"' + 'imagens/img_transp.png' + '\" ' + self.img_final
        print(self.programa)
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.img_final
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(564, 408, QtCore.Qt.KeepAspectRatio) 
        self.imagem2.setPixmap(self.pixmap2)



    def botaoSobre(self):
        self.menssagem = QMessageBox()
        self.menssagem.setWindowTitle("Sobre o Desenvolvedor")
        self.menssagem.setText("Tiago de Alcantara e Silva Barros\nApcicativo para transformação de Imagens\n\nFiltors utilizados:\nBlur\nEdge Enhance More.\nSmoth More.\nItuiutaba, 22 de junho de 2021.")
        self.menssagem.exec_()

    def botaoSobre1(self):
        self.menssagem = QMessageBox()
        self.menssagem.setWindowTitle("Sobre a Imagem")
        self.menssagem.setText("Nome: Ponte.jpg\nTipo de Arquivo: JPEG\n\nImagem que será submetida às modificações\nTamanho: 500 x 333\n")
        self.menssagem.exec_()


aplication = QApplication(sys.argv)        
window = MainWindow() 
window.show()
sys.exit(aplication.exec_())