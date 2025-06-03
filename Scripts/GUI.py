from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QHBoxLayout, QLineEdit, QTabWidget
from PyQt5.QtGui import *
import sys
import json
import Layout
import os


metagame="gen9vgc2025regi"
json_path="../Database/sd_"+metagame+".json"
manual_json_path="../Database/sd_manual_"+metagame+".json"
database_directory = "../Database/"+metagame+"/"


# Creating tab widgets
class MenuTabWidget(QWidget):
    def __init__(self, parent):

        super(QWidget, self).__init__(parent)
        filelist = os.listdir(database_directory)
        replay_data = []
        count=1
        for file in filelist:
            with open(database_directory+file, 'r') as data_file:
                filedata = json.load(data_file)
                replay_data = replay_data + filedata
                #if count == 1:
                #    replay_data.update(filedata)
                #    count += 1
                #else:
                #    replay_data.update(filedata)
                #data_file.close()
        self.data = replay_data
        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        #self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(300, 200)
  
        # Add tabs
        self.tabs.addTab(self.tab1, "Check Statistics")
        self.tabs.addTab(self.tab2, "Statistic Matrix")
        self.tabs.addTab(self.tab3, "Statistic Improvement")
        #self.tabs.addTab(self.tab4, "Manual Addition")
        self.tabs.addTab(self.tab5, "Leads")
        self.tabs.addTab(self.tab6, "Backs")
  
  
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
        #self.tab4.layout = QVBoxLayout(self)
        #self.tab4.setLayout(Layout.createManualAdditionLayout(self.data))

        # Create Leads Tab
        self.tab5.layout = QVBoxLayout(self)
        self.tab5.setLayout(Layout.createLeadsLayout(self.data))

        # Create Backs Tab
        self.tab6.layout = QVBoxLayout(self)
        self.tab6.setLayout(Layout.createBacksLayout(self.data))
  
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
     # setting window icon
    app.setWindowIcon(QIcon("../Sources/Pokeball.png"))
    app.setApplicationName("Pokemon Matchup Analyzer")
    app.setStyleSheet(stylesheet)
    window = MainWindow()

    window.show()
    
    app.exec()