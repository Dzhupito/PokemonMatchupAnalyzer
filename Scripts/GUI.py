from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QHBoxLayout, QLineEdit, QTabWidget
import sys
import json
import Layout


metagame="gen8vgc2021series8"
json_path="../Database/sd_"+metagame+".json"
manual_json_path="../Database/sd_manual_"+metagame+".json"


# Creating tab widgets
class MenuTabWidget(QWidget):
    def __init__(self, parent):

        super(QWidget, self).__init__(parent)
        with open(json_path, 'r') as data_file:
            self.data = json.load(data_file)
            data_file.close()

        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300, 200)
  
        # Add tabs
        self.tabs.addTab(self.tab1, "Check Statistics")
        self.tabs.addTab(self.tab2, "Statistic Matrix")
        self.tabs.addTab(self.tab3, "Statistic Improvement")
        self.tabs.addTab(self.tab4, "Manual Addition")
  
        # Create Check Statistics Tab
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.setLayout(Layout.createCheckStatiscsLayout(self.data))

        # Create Statistic Matrix Tab
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.setLayout(Layout.createStatisticMatrixLayout(self.data))

        # Create Statistic Improvement Tab
        self.tab3.layout = QVBoxLayout(self)
        self.tab3.setLayout(Layout.createStatisticImprovemntLayout(self.data))

        # Create Manual Addition Tab
        self.tab4.layout = QVBoxLayout(self)
        self.tab4.setLayout(Layout.createManualAdditionLayout(self.data))
  
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.centralwidget.setFixedWidth(1850)
        self.centralwidget.setFixedHeight(950)
        
        mainlayout=QVBoxLayout(self.centralwidget)
        menuwidget=MenuTabWidget(self.centralwidget)

        mainlayout.addWidget(menuwidget)
        

stylesheet = """
    MainWindow {
        background-image: url("../Sources/Background.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Pokemon Matchup Analyzer")
    app.setStyleSheet(stylesheet)
    window = MainWindow()

    window.show()
    
    app.exec()