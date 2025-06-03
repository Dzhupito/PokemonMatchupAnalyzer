from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QTableWidget, QDialog, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import numpy
import os
import json

page=1
lastsubdata=[]
currentdata=[]

def loadPreviousPage(data, tablewidget):
    # printing pressed
    global page
    if page > 1 :
        page=page-1
        #tablewidget.setCellWidget(0,0,QLabel("Hello"))
        fillStatisticMatrix(data, tablewidget)

def loadNextPage(data, tablewidget):
    # printing pressed
    global page
    if page <= ((len(data)-1)/50) :
        page=page+1
        #tablewidget.setCellWidget(0,0,QLabel("Hello"))
        fillStatisticMatrix(data, tablewidget)

def createSubdata(data, tablewidget,poke1,poke2,poke3,poke4,poke5,poke6,poke7,poke8,poke9,poke10,poke11,poke12,minrating,zerostate,nteamslabel,nwinslabel):
    # printing pressed
    rating_minimo = 0
    if minrating!="":
        rating_minimo = int (minrating)
    # print (rating_minimo)
    global lastsubdata
    global currentdata
    subteam1=[poke1,poke2,poke3,poke4,poke5,poke6]
    subteam1 = list(filter(None, subteam1))
    subteam2=[poke7,poke8,poke9,poke10,poke11,poke12]
    subteam2 = list(filter(None, subteam2))
    subdata=[]
    totalwins=0
    for match in data:
        rating_1 = match["players"][0]["player1_rating"]
        rating_2 = match["players"][1]["player2_rating"]
        if ((rating_1 == 0 and zerostate == 2) or (rating_2== 0 and zerostate == 2))  or rating_1 >= rating_minimo or rating_2 >= rating_minimo: 
            if set(subteam1).issubset(set(match["players"][0]["player1_team"])):
                if set(subteam2).issubset(set(match["players"][1]["player2_team"])):
                    if (match["players"][0]["player1_name"] == match["winner"]):
                        totalwins=totalwins+1        
                    subdata.append(match)

            elif set(subteam1).issubset(set(match["players"][1]["player2_team"])):
                if set(subteam2).issubset(set(match["players"][0]["player1_team"])):
                    if (match["players"][1]["player2_name"] == match["winner"]):
                        totalwins=totalwins+1 
                    subdata.append(match)
                    
    lastsubdata=subdata
    currentdata=subdata
    nteamslabel.setText("Number of results:"+ str(len(subdata)))
    if len(subdata)>0:
        nwinslabel.setText("Number of wins :" + str(totalwins)+" ("+ str(round(float(totalwins/len(subdata)),2))+")")
    else:
        nwinslabel.setText("Number of wins :" + str(totalwins))
    global page
    page=1
    #tablewidget.setCellWidget(0,0,QLabel("Hello"))
    fillStatisticMatrix(lastsubdata, tablewidget)

def fillStatisticMatrix(data, tablewidget):
    index=(page-1)*50
    tabindex=0
    
    while index < page*50 and index < len(data):
        tablewidget.setCellWidget(tabindex,0,QLabel(str(data[index]["players"][0]["player1_rating"])))
        player1name=QLabel(str(data[index]["players"][0]["player1_name"]))
        tablewidget.setCellWidget(tabindex,1,player1name)
        poke1=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][0]["player1_team"][0]))
        pic = pic.scaled(50, 50)
        poke1.setPixmap(pic)
        if str(data[index]["players"][0]["player1_team"][0]) == data[index]["players"][0]["player1_terastallized"]:
            poke1.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,2,poke1)

        poke2=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][0]["player1_team"][1]))
        pic = pic.scaled(50, 50)
        poke2.setPixmap(pic)
        if str(data[index]["players"][0]["player1_team"][1]) == data[index]["players"][0]["player1_terastallized"]:
            poke2.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,3,poke2)

        poke3=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][0]["player1_team"][2]))
        pic = pic.scaled(50, 50)
        poke3.setPixmap(pic)
        if str(data[index]["players"][0]["player1_team"][2]) == data[index]["players"][0]["player1_terastallized"]:
            poke3.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,4,poke3)

        poke4=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][0]["player1_team"][3]))
        pic = pic.scaled(50, 50)
        poke4.setPixmap(pic)
        if str(data[index]["players"][0]["player1_team"][3]) == data[index]["players"][0]["player1_terastallized"]:
            poke4.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,5,poke4)

        poke5=QLabel()
        if len(data[index]["players"][0]["player1_team"]) > 4:
            pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][0]["player1_team"][4]))
            pic = pic.scaled(50, 50)
            poke5.setPixmap(pic)
            if str(data[index]["players"][0]["player1_team"][4]) == data[index]["players"][0]["player1_terastallized"]:
                poke5.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,6,poke5)

        poke6=QLabel()
        if len(data[index]["players"][0]["player1_team"]) > 5:
            pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][0]["player1_team"][5]))
            pic = pic.scaled(50, 50)
            poke6.setPixmap(pic)
            if str(data[index]["players"][0]["player1_team"][5]) == data[index]["players"][0]["player1_terastallized"]:
                poke6.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,7,poke6)

        tablewidget.setCellWidget(tabindex,8,QLabel(str(data[index]["players"][1]["player2_rating"])))

        player2name=QLabel(str(data[index]["players"][1]["player2_name"]))
        tablewidget.setCellWidget(tabindex,9,player2name)

        poke7=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][1]["player2_team"][0]))
        pic = pic.scaled(50, 50)
        poke7.setPixmap(pic)
        if str(data[index]["players"][1]["player2_team"][0]) == data[index]["players"][1]["player2_terastallized"]:
            poke7.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,10,poke7)

        poke8=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][1]["player2_team"][1]))
        pic = pic.scaled(50, 50)
        poke8.setPixmap(pic)
        if str(data[index]["players"][1]["player2_team"][1]) == data[index]["players"][1]["player2_terastallized"]:
            poke8.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,11,poke8)

        poke9=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][1]["player2_team"][2]))
        pic = pic.scaled(50, 50)
        poke9.setPixmap(pic)
        if str(data[index]["players"][1]["player2_team"][2]) == data[index]["players"][1]["player2_terastallized"]:
            poke9.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,12,poke9)

        poke10=QLabel()
        pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][1]["player2_team"][3]))
        pic = pic.scaled(50, 50)
        poke10.setPixmap(pic)
        if str(data[index]["players"][1]["player2_team"][3]) == data[index]["players"][1]["player2_terastallized"]:
            poke10.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,13,poke10)

        poke11=QLabel()
        if len(data[index]["players"][1]["player2_team"]) > 4:
            pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][1]["player2_team"][4]))
            pic = pic.scaled(50, 50)
            poke11.setPixmap(pic)
            if str(data[index]["players"][1]["player2_team"][4]) == data[index]["players"][1]["player2_terastallized"]:
                poke11.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,14,poke11)
        
        poke12=QLabel()
        if len(data[index]["players"][1]["player2_team"]) > 5:
            pic = QPixmap("../Sources/Sprites/"+str(data[index]["players"][1]["player2_team"][5]))
            pic = pic.scaled(50, 50)
            poke12.setPixmap(pic)
            if str(data[index]["players"][1]["player2_team"][5]) == data[index]["players"][1]["player2_terastallized"]:
                poke12.setStyleSheet("background-color: yellow")
        tablewidget.setCellWidget(tabindex,15,poke12)
        
        replayurl = QLabel()
        replayurl.setText(str(data[index]["replay_url"]))
        replayurl.setTextInteractionFlags(Qt.TextSelectableByMouse)
        replayurl.setOpenExternalLinks(True)
        
        tablewidget.setCellWidget(tabindex,16,replayurl)

        if data[index]["players"][0]["player1_name"] == data[index]["winner"]:
            player1name.setStyleSheet("background-color: lightgreen")
        else:
            player2name.setStyleSheet("background-color: lightgreen")

        index=index+1
        tabindex=tabindex+1

    while tabindex<50 and index == len(data):
        tablewidget.setCellWidget(tabindex,0,QLabel(""))
        tablewidget.setCellWidget(tabindex,1,QLabel(""))
        tablewidget.setCellWidget(tabindex,2,QLabel(""))
        tablewidget.setCellWidget(tabindex,3,QLabel(""))
        tablewidget.setCellWidget(tabindex,4,QLabel(""))
        tablewidget.setCellWidget(tabindex,5,QLabel(""))
        tablewidget.setCellWidget(tabindex,6,QLabel(""))
        tablewidget.setCellWidget(tabindex,7,QLabel(""))
        tablewidget.setCellWidget(tabindex,8,QLabel(""))
        tablewidget.setCellWidget(tabindex,9,QLabel(""))
        tablewidget.setCellWidget(tabindex,10,QLabel(""))
        tablewidget.setCellWidget(tabindex,11,QLabel(""))
        tablewidget.setCellWidget(tabindex,12,QLabel(""))
        tablewidget.setCellWidget(tabindex,13,QLabel(""))
        tablewidget.setCellWidget(tabindex,14,QLabel(""))
        tablewidget.setCellWidget(tabindex,15,QLabel(""))
        tablewidget.setCellWidget(tabindex,16,QLabel(""))
        tablewidget.setCellWidget(tabindex,17,QLabel(""))

        tabindex=tabindex+1

def setPokemonImage (pokemonname, pokemonlabel):
    pic = QPixmap("../Sources/Sprites/"+str(pokemonname)+".png")
    pokemonlabel.setPixmap(pic) 

def createCheckStatiscsLayout(data):
    global currentdata
    currentdata=data
    teamslayout=QVBoxLayout()
    team1layout=QHBoxLayout()
    team2layout=QHBoxLayout()
    utilitylayout=QHBoxLayout()
    pokemon11label=QLabel()
    pokemon11label.setMaximumWidth(40)
    pokemon11text = QLineEdit()
    pokemon11text.textChanged.connect(lambda: setPokemonImage(pokemon11text.text(), pokemon11label))
    pokemon12label=QLabel()
    pokemon12label.setMaximumWidth(40)
    pokemon12text = QLineEdit()
    pokemon12text.textChanged.connect(lambda: setPokemonImage(pokemon12text.text(), pokemon12label))
    pokemon13label=QLabel()
    pokemon13label.setMaximumWidth(40)
    pokemon13text = QLineEdit()
    pokemon13text.textChanged.connect(lambda: setPokemonImage(pokemon13text.text(), pokemon13label))
    pokemon14label=QLabel()
    pokemon14label.setMaximumWidth(40)
    pokemon14text = QLineEdit()
    pokemon14text.textChanged.connect(lambda: setPokemonImage(pokemon14text.text(), pokemon14label))
    pokemon15label=QLabel()
    pokemon15label.setMaximumWidth(40)
    pokemon15text = QLineEdit()
    pokemon15text.textChanged.connect(lambda: setPokemonImage(pokemon15text.text(), pokemon15label))
    pokemon16label=QLabel()
    pokemon16label.setMaximumWidth(40)
    pokemon16text = QLineEdit()
    pokemon16text.textChanged.connect(lambda: setPokemonImage(pokemon16text.text(), pokemon16label))
    team1layout.addWidget(QLabel("Team 1"))
    team1layout.addWidget(pokemon11label)
    team1layout.addWidget(pokemon11text)
    team1layout.addWidget(pokemon12label)
    team1layout.addWidget(pokemon12text)
    team1layout.addWidget(pokemon13label)
    team1layout.addWidget(pokemon13text)
    team1layout.addWidget(pokemon14label)
    team1layout.addWidget(pokemon14text)
    team1layout.addWidget(pokemon15label)
    team1layout.addWidget(pokemon15text)
    team1layout.addWidget(pokemon16label)
    team1layout.addWidget(pokemon16text)
    pokemon21label=QLabel()
    pokemon21label.setMaximumWidth(40)
    pokemon21text = QLineEdit()
    pokemon21text.textChanged.connect(lambda: setPokemonImage(pokemon21text.text(), pokemon21label))
    pokemon22label=QLabel()
    pokemon22label.setMaximumWidth(40)
    pokemon22text = QLineEdit()
    pokemon22text.textChanged.connect(lambda: setPokemonImage(pokemon22text.text(), pokemon22label))
    pokemon23label=QLabel()
    pokemon23label.setMaximumWidth(40)
    pokemon23text = QLineEdit()
    pokemon23text.textChanged.connect(lambda: setPokemonImage(pokemon23text.text(), pokemon23label))
    pokemon24label=QLabel()
    pokemon24label.setMaximumWidth(40)
    pokemon24text = QLineEdit()
    pokemon24text.textChanged.connect(lambda: setPokemonImage(pokemon24text.text(), pokemon24label))
    pokemon25label=QLabel()
    pokemon25label.setMaximumWidth(40)
    pokemon25text = QLineEdit()
    pokemon25text.textChanged.connect(lambda: setPokemonImage(pokemon25text.text(), pokemon25label))
    pokemon26label=QLabel()
    pokemon26label.setMaximumWidth(40)
    pokemon26text = QLineEdit()
    pokemon26text.textChanged.connect(lambda: setPokemonImage(pokemon26text.text(), pokemon26label))
    team2layout.addWidget(QLabel("Team 2"))
    team2layout.addWidget(pokemon21label)
    team2layout.addWidget(pokemon21text)
    team2layout.addWidget(pokemon22label)
    team2layout.addWidget(pokemon22text)
    team2layout.addWidget(pokemon23label)
    team2layout.addWidget(pokemon23text)
    team2layout.addWidget(pokemon24label)
    team2layout.addWidget(pokemon24text)
    team2layout.addWidget(pokemon25label)
    team2layout.addWidget(pokemon25text)
    team2layout.addWidget(pokemon26label)
    team2layout.addWidget(pokemon26text)

    minratinglabel=QLabel()
    minratinglabel.setText("Minimum player rating :")
    minratinglabel.setMaximumHeight(30)
    minratingtext = QLineEdit()
    minratingtext.setMaximumHeight(30)
    checkteambutton=QPushButton('Check teams')
    checkteambutton.setMaximumHeight(30)
    includezerocheck=QCheckBox("Include 0s")
    includezerocheck.setMaximumHeight(30)
    nteamslabel=QLabel()
    nteamslabel.setText("Number of results :" + str(len(data)))
    nteamslabel.setMaximumHeight(30)
    nwinslabel=QLabel()
    nwinslabel.setText("Number of wins :" + str(0))
    nwinslabel.setMaximumHeight(30)
    checkteambutton.clicked.connect(lambda: createSubdata(data, tablewidget,pokemon11text.text(),pokemon12text.text(),pokemon13text.text(),pokemon14text.text(),pokemon15text.text(),pokemon16text.text(),pokemon21text.text(),pokemon22text.text(),pokemon23text.text(),pokemon24text.text(),pokemon25text.text(),pokemon26text.text(), minratingtext.text(), includezerocheck.checkState(), nteamslabel, nwinslabel)) 
    
    utilitylayout.addWidget(minratinglabel)
    utilitylayout.addWidget(minratingtext)
    utilitylayout.addWidget(includezerocheck)  
    utilitylayout.addWidget(checkteambutton)
    utilitylayout.addWidget(nteamslabel)
    utilitylayout.addWidget(nwinslabel)  
    
    teamslayout.addLayout(team1layout,1)
    teamslayout.addLayout(team2layout,1)
    teamslayout.addLayout(utilitylayout,1)
    
    
    #tablewidget=QTableWidget()
    tablewidget=QTableWidget()
    tablewidget.setRowCount(50)
    tablewidget.setColumnCount(17)
    columnnames=["P1 Rat", "P1 name", "Pok1", "Pok2", "Pok3", "Pok4", "Pok5", "Pok6", "P2 Rat", "P2 Name", "Pok1", "Pok2", "Pok3", "Pok4", "Pok5", "Pok6", "url"]
    tablewidget.setHorizontalHeaderLabels(columnnames)
    tablewidget.setColumnWidth(0,60)
    tablewidget.setColumnWidth(1,250)
    tablewidget.setColumnWidth(2,40)
    tablewidget.setColumnWidth(3,40)
    tablewidget.setColumnWidth(4,40)
    tablewidget.setColumnWidth(5,40)
    tablewidget.setColumnWidth(6,40)
    tablewidget.setColumnWidth(7,40)
    tablewidget.setColumnWidth(8,60)
    tablewidget.setColumnWidth(9,250)
    tablewidget.setColumnWidth(10,40)
    tablewidget.setColumnWidth(11,40)
    tablewidget.setColumnWidth(12,40)
    tablewidget.setColumnWidth(13,40)
    tablewidget.setColumnWidth(14,40)
    tablewidget.setColumnWidth(15,40)
    tablewidget.setColumnWidth(16,500)
    fillStatisticMatrix(data,tablewidget)
    teamslayout.addWidget(tablewidget)

    buttonlayout=QHBoxLayout()
    previousbutton=QPushButton('Previous page')
    previousbutton.setMaximumHeight(30)   
    previousbutton.setMaximumWidth(120)
    previousbutton.clicked.connect(lambda: loadPreviousPage(currentdata, tablewidget)) 
    buttonlayout.addWidget(previousbutton)
    nextbutton=QPushButton('Next page')
    nextbutton.setMaximumHeight(30)   
    nextbutton.setMaximumWidth(120) 
    nextbutton.clicked.connect(lambda: loadNextPage(currentdata, tablewidget)) 

    buttonlayout.addWidget(nextbutton) 
    teamslayout.addLayout(buttonlayout)
    
    
    return teamslayout

def setPokemonTeams (pokemonname, pokemonlabel, index, teamvector):
    pic = QPixmap("../Sources/Sprites/"+str(pokemonname)+".png")
    pokemonlabel.setPixmap(pic)
    teamvector[index]=pokemonname

def createStatisticMatrix(data, tablewidget, team1, team2, team3, team4, team5, team6, team7, team8):
    selectedTeams=[]
    team1 = list(filter(None, team1)) 
    if len(team1)>0:
        selectedTeams.append(team1)
    team2 = list(filter(None, team2)) 
    if len(team2)>0:
        selectedTeams.append(team2)
    team3 = list(filter(None, team3)) 
    if len(team3)>0:
        selectedTeams.append(team3)
    team4 = list(filter(None, team4)) 
    if len(team4)>0:
        selectedTeams.append(team4)
    team5 = list(filter(None, team5))
    if len(team5)>0:
        selectedTeams.append(team5) 
    team6 = list(filter(None, team6)) 
    if len(team6)>0:
        selectedTeams.append(team6)
    team7 = list(filter(None, team7)) 
    if len(team7)>0:
        selectedTeams.append(team7)
    team8 = list(filter(None, team8)) 
    if len(team8)>0:
        selectedTeams.append(team8)

    matrixsize = len(selectedTeams)

    if (matrixsize>1):
        win_matrix = numpy.zeros((matrixsize, matrixsize))
        ratio_matrix = numpy.zeros((matrixsize, matrixsize))
        for match in data:
            for i in range(0, matrixsize):
                if set(selectedTeams[i]).issubset(set(match["players"][0]["player1_team"])):
                    for j in range(i+1,matrixsize):
                        if set(selectedTeams[j]).issubset(set(match["players"][1]["player2_team"])):
                            if (match["players"][0]["player1_name"] == match["winner"]):
                                win_matrix[i][j]+=1
                            else :
                                win_matrix[j][i]+=1
                elif set(selectedTeams[i]).issubset(set(match["players"][1]["player2_team"])):
                    for j in range(i+1,matrixsize):
                        if set(selectedTeams[j]).issubset(set(match["players"][0]["player1_team"])):
                            if (match["players"][1]["player2_name"] == match["winner"]):
                                win_matrix[i][j]+=1
                            else :
                                win_matrix[j][i]+=1  

        for i in range (0, matrixsize):
            for j in range (0, matrixsize):
                if i!=j:
                    if float(win_matrix[i][j])==0 :
                        ratio_matrix[i][j]=0
                    else :
                        ratio_matrix[i][j]=float(win_matrix[i][j]/(win_matrix[i][j]+win_matrix[j][i]))
                else:
                    ratio_matrix[i][j]=0
        #print("%.2f" % ratio_matrix[i][j]," ", end="")
        
        
    for i in range (0,8):
        for j in range (0,6):
            clearpokemon= QLabel()
            tablewidget.setCellWidget(i+6,5-j,clearpokemon)
            tablewidget.setCellWidget(5-j,i+6,clearpokemon)

    
    nteam=0
    for team in selectedTeams:
        for i in range (0, len(team)):
            hpokemon = QLabel()
            vpokemon = QLabel()
            pic = QPixmap("../Sources/Sprites/"+str(team[i]))
            hpokemon.setPixmap(pic)
            vpokemon.setPixmap(pic)
            tablewidget.setCellWidget(nteam+6,5-i,hpokemon)
            tablewidget.setCellWidget(5-i,nteam+6,vpokemon)
        nteam=nteam+1
    
    for i in range (0,matrixsize):
        nullcell=QLabel()
        nullcell.setStyleSheet("background-color: black")
        tablewidget.setCellWidget(i+6,i+6,nullcell)

    for i in range (0, matrixsize):
        for j in range (0, matrixsize):
            if i != j:
                result=QLabel(str(round(win_matrix[i][j],0))+"("+str(round(ratio_matrix[i][j],2))+")")
                if ratio_matrix[i][j]>=0.67:
                    result.setStyleSheet("background-color: green")
                elif ratio_matrix[i][j]<0.67 and ratio_matrix[i][j]>0.5:
                    result.setStyleSheet("background-color: lightgreen")
                elif ratio_matrix[i][j]==0.5:
                    result.setStyleSheet("background-color: yellow")
                elif ratio_matrix[i][j]<0.5 and ratio_matrix[i][j]>=0.33:
                    result.setStyleSheet("background-color: orange")
                elif ratio_matrix[i][j]<0.5 and ratio_matrix[i][j]<0.33:
                    result.setStyleSheet("background-color: red")
                if win_matrix[i][j]+win_matrix[j][i]==0:
                    result.setStyleSheet("background-color: grey")
                tablewidget.setCellWidget(i+6,j+6,result)

def createStatisticMatrixLayout(data):
    statisticLayout = QVBoxLayout()
    team1layout=QHBoxLayout()
    team2layout=QHBoxLayout()
    team3layout=QHBoxLayout()
    team4layout=QHBoxLayout()
    team5layout=QHBoxLayout()
    team6layout=QHBoxLayout()
    team7layout=QHBoxLayout()
    team8layout=QHBoxLayout()
    utilitylayout=QHBoxLayout()

    team1=[None]*6
    team2=[None]*6
    team3=[None]*6
    team4=[None]*6
    team5=[None]*6
    team6=[None]*6
    team7=[None]*6
    team8=[None]*6

    pokemon11label=QLabel()
    pokemon11label.setMaximumWidth(40)
    pokemon11text = QLineEdit()
    pokemon11text.textChanged.connect(lambda: setPokemonTeams(pokemon11text.text(), pokemon11label,0,team1))
    pokemon12label=QLabel()
    pokemon12label.setMaximumWidth(40)
    pokemon12text = QLineEdit()
    pokemon12text.textChanged.connect(lambda: setPokemonTeams(pokemon12text.text(), pokemon12label,1,team1))
    pokemon13label=QLabel()
    pokemon13label.setMaximumWidth(40)
    pokemon13text = QLineEdit()
    pokemon13text.textChanged.connect(lambda: setPokemonTeams(pokemon13text.text(), pokemon13label,2,team1))
    pokemon14label=QLabel()
    pokemon14label.setMaximumWidth(40)
    pokemon14text = QLineEdit()
    pokemon14text.textChanged.connect(lambda: setPokemonTeams(pokemon14text.text(), pokemon14label,3,team1))
    pokemon15label=QLabel()
    pokemon15label.setMaximumWidth(40)
    pokemon15text = QLineEdit()
    pokemon15text.textChanged.connect(lambda: setPokemonTeams(pokemon15text.text(), pokemon15label,4,team1))
    pokemon16label=QLabel()
    pokemon16label.setMaximumWidth(40)
    pokemon16text = QLineEdit()
    pokemon16text.textChanged.connect(lambda: setPokemonTeams(pokemon16text.text(), pokemon16label,5,team1))
    team1layout.addWidget(QLabel("Team 1"))
    team1layout.addWidget(pokemon11label)
    team1layout.addWidget(pokemon11text)
    team1layout.addWidget(pokemon12label)
    team1layout.addWidget(pokemon12text)
    team1layout.addWidget(pokemon13label)
    team1layout.addWidget(pokemon13text)
    team1layout.addWidget(pokemon14label)
    team1layout.addWidget(pokemon14text)
    team1layout.addWidget(pokemon15label)
    team1layout.addWidget(pokemon15text)
    team1layout.addWidget(pokemon16label)
    team1layout.addWidget(pokemon16text)

    pokemon21label=QLabel()
    pokemon21label.setMaximumWidth(40)
    pokemon21text = QLineEdit()
    pokemon21text.textChanged.connect(lambda: setPokemonTeams(pokemon21text.text(), pokemon21label,0,team2))
    pokemon22label=QLabel()
    pokemon22label.setMaximumWidth(40)
    pokemon22text = QLineEdit()
    pokemon22text.textChanged.connect(lambda: setPokemonTeams(pokemon22text.text(), pokemon22label,1,team2))
    pokemon23label=QLabel()
    pokemon23label.setMaximumWidth(40)
    pokemon23text = QLineEdit()
    pokemon23text.textChanged.connect(lambda: setPokemonTeams(pokemon23text.text(), pokemon23label,2,team2))
    pokemon24label=QLabel()
    pokemon24label.setMaximumWidth(40)
    pokemon24text = QLineEdit()
    pokemon24text.textChanged.connect(lambda: setPokemonTeams(pokemon24text.text(), pokemon24label,3,team2))
    pokemon25label=QLabel()
    pokemon25label.setMaximumWidth(40)
    pokemon25text = QLineEdit()
    pokemon25text.textChanged.connect(lambda: setPokemonTeams(pokemon25text.text(), pokemon25label,4,team2))
    pokemon26label=QLabel()
    pokemon26label.setMaximumWidth(40)
    pokemon26text = QLineEdit()
    pokemon26text.textChanged.connect(lambda: setPokemonTeams(pokemon26text.text(), pokemon26label,5,team2))
    team2layout.addWidget(QLabel("Team 2"))
    team2layout.addWidget(pokemon21label)
    team2layout.addWidget(pokemon21text)
    team2layout.addWidget(pokemon22label)
    team2layout.addWidget(pokemon22text)
    team2layout.addWidget(pokemon23label)
    team2layout.addWidget(pokemon23text)
    team2layout.addWidget(pokemon24label)
    team2layout.addWidget(pokemon24text)
    team2layout.addWidget(pokemon25label)
    team2layout.addWidget(pokemon25text)
    team2layout.addWidget(pokemon26label)
    team2layout.addWidget(pokemon26text)

    pokemon31label=QLabel()
    pokemon31label.setMaximumWidth(40)
    pokemon31text = QLineEdit()
    pokemon31text.textChanged.connect(lambda: setPokemonTeams(pokemon31text.text(), pokemon31label,0,team3))
    pokemon32label=QLabel()
    pokemon32label.setMaximumWidth(40)
    pokemon32text = QLineEdit()
    pokemon32text.textChanged.connect(lambda: setPokemonTeams(pokemon32text.text(), pokemon32label,1,team3))
    pokemon33label=QLabel()
    pokemon33label.setMaximumWidth(40)
    pokemon33text = QLineEdit()
    pokemon33text.textChanged.connect(lambda: setPokemonTeams(pokemon33text.text(), pokemon33label,2,team3))
    pokemon34label=QLabel()
    pokemon34label.setMaximumWidth(40)
    pokemon34text = QLineEdit()
    pokemon34text.textChanged.connect(lambda: setPokemonTeams(pokemon34text.text(), pokemon34label,3,team3))
    pokemon35label=QLabel()
    pokemon35label.setMaximumWidth(40)
    pokemon35text = QLineEdit()
    pokemon35text.textChanged.connect(lambda: setPokemonTeams(pokemon35text.text(), pokemon35label,4,team3))
    pokemon36label=QLabel()
    pokemon36label.setMaximumWidth(40)
    pokemon36text = QLineEdit()
    pokemon36text.textChanged.connect(lambda: setPokemonTeams(pokemon36text.text(), pokemon36label,5,team3))
    team3layout.addWidget(QLabel("Team 3"))
    team3layout.addWidget(pokemon31label)
    team3layout.addWidget(pokemon31text)
    team3layout.addWidget(pokemon32label)
    team3layout.addWidget(pokemon32text)
    team3layout.addWidget(pokemon33label)
    team3layout.addWidget(pokemon33text)
    team3layout.addWidget(pokemon34label)
    team3layout.addWidget(pokemon34text)
    team3layout.addWidget(pokemon35label)
    team3layout.addWidget(pokemon35text)
    team3layout.addWidget(pokemon36label)
    team3layout.addWidget(pokemon36text)

    pokemon41label=QLabel()
    pokemon41label.setMaximumWidth(40)
    pokemon41text = QLineEdit()
    pokemon41text.textChanged.connect(lambda: setPokemonTeams(pokemon41text.text(), pokemon41label,0,team4))
    pokemon42label=QLabel()
    pokemon42label.setMaximumWidth(40)
    pokemon42text = QLineEdit()
    pokemon42text.textChanged.connect(lambda: setPokemonTeams(pokemon42text.text(), pokemon42label,1,team4))
    pokemon43label=QLabel()
    pokemon43label.setMaximumWidth(40)
    pokemon43text = QLineEdit()
    pokemon43text.textChanged.connect(lambda: setPokemonTeams(pokemon43text.text(), pokemon43label,2,team4))
    pokemon44label=QLabel()
    pokemon44label.setMaximumWidth(40)
    pokemon44text = QLineEdit()
    pokemon44text.textChanged.connect(lambda: setPokemonTeams(pokemon44text.text(), pokemon44label,3,team4))
    pokemon45label=QLabel()
    pokemon45label.setMaximumWidth(40)
    pokemon45text = QLineEdit()
    pokemon45text.textChanged.connect(lambda: setPokemonTeams(pokemon45text.text(), pokemon45label,4,team4))
    pokemon46label=QLabel()
    pokemon46label.setMaximumWidth(40)
    pokemon46text = QLineEdit()
    pokemon46text.textChanged.connect(lambda: setPokemonTeams(pokemon46text.text(), pokemon46label,5,team4))
    team4layout.addWidget(QLabel("Team 4"))
    team4layout.addWidget(pokemon41label)
    team4layout.addWidget(pokemon41text)
    team4layout.addWidget(pokemon42label)
    team4layout.addWidget(pokemon42text)
    team4layout.addWidget(pokemon43label)
    team4layout.addWidget(pokemon43text)
    team4layout.addWidget(pokemon44label)
    team4layout.addWidget(pokemon44text)
    team4layout.addWidget(pokemon45label)
    team4layout.addWidget(pokemon45text)
    team4layout.addWidget(pokemon46label)
    team4layout.addWidget(pokemon46text)

    pokemon51label=QLabel()
    pokemon51label.setMaximumWidth(40)
    pokemon51text = QLineEdit()
    pokemon51text.textChanged.connect(lambda: setPokemonTeams(pokemon51text.text(), pokemon51label,0,team5))
    pokemon52label=QLabel()
    pokemon52label.setMaximumWidth(40)
    pokemon52text = QLineEdit()
    pokemon52text.textChanged.connect(lambda: setPokemonTeams(pokemon52text.text(), pokemon52label,1,team5))
    pokemon53label=QLabel()
    pokemon53label.setMaximumWidth(40)
    pokemon53text = QLineEdit()
    pokemon53text.textChanged.connect(lambda: setPokemonTeams(pokemon53text.text(), pokemon53label,2,team5))
    pokemon54label=QLabel()
    pokemon54label.setMaximumWidth(40)
    pokemon54text = QLineEdit()
    pokemon54text.textChanged.connect(lambda: setPokemonTeams(pokemon54text.text(), pokemon54label,3,team5))
    pokemon55label=QLabel()
    pokemon55label.setMaximumWidth(40)
    pokemon55text = QLineEdit()
    pokemon55text.textChanged.connect(lambda: setPokemonTeams(pokemon55text.text(), pokemon55label,4,team5))
    pokemon56label=QLabel()
    pokemon56label.setMaximumWidth(40)
    pokemon56text = QLineEdit()
    pokemon56text.textChanged.connect(lambda: setPokemonTeams(pokemon56text.text(), pokemon56label,5,team5))
    team5layout.addWidget(QLabel("Team 5"))
    team5layout.addWidget(pokemon51label)
    team5layout.addWidget(pokemon51text)
    team5layout.addWidget(pokemon52label)
    team5layout.addWidget(pokemon52text)
    team5layout.addWidget(pokemon53label)
    team5layout.addWidget(pokemon53text)
    team5layout.addWidget(pokemon54label)
    team5layout.addWidget(pokemon54text)
    team5layout.addWidget(pokemon55label)
    team5layout.addWidget(pokemon55text)
    team5layout.addWidget(pokemon56label)
    team5layout.addWidget(pokemon56text)

    pokemon61label=QLabel()
    pokemon61label.setMaximumWidth(40)
    pokemon61text = QLineEdit()
    pokemon61text.textChanged.connect(lambda: setPokemonTeams(pokemon61text.text(), pokemon61label,0,team6))
    pokemon62label=QLabel()
    pokemon62label.setMaximumWidth(40)
    pokemon62text = QLineEdit()
    pokemon62text.textChanged.connect(lambda: setPokemonTeams(pokemon62text.text(), pokemon62label,1,team6))
    pokemon63label=QLabel()
    pokemon63label.setMaximumWidth(40)
    pokemon63text = QLineEdit()
    pokemon63text.textChanged.connect(lambda: setPokemonTeams(pokemon63text.text(), pokemon63label,2,team6))
    pokemon64label=QLabel()
    pokemon64label.setMaximumWidth(40)
    pokemon64text = QLineEdit()
    pokemon64text.textChanged.connect(lambda: setPokemonTeams(pokemon64text.text(), pokemon64label,3,team6))
    pokemon65label=QLabel()
    pokemon65label.setMaximumWidth(40)
    pokemon65text = QLineEdit()
    pokemon65text.textChanged.connect(lambda: setPokemonTeams(pokemon65text.text(), pokemon65label,4,team6))
    pokemon66label=QLabel()
    pokemon66label.setMaximumWidth(40)
    pokemon66text = QLineEdit()
    pokemon66text.textChanged.connect(lambda: setPokemonTeams(pokemon66text.text(), pokemon66label,5,team6))
    team6layout.addWidget(QLabel("Team 6"))
    team6layout.addWidget(pokemon61label)
    team6layout.addWidget(pokemon61text)
    team6layout.addWidget(pokemon62label)
    team6layout.addWidget(pokemon62text)
    team6layout.addWidget(pokemon63label)
    team6layout.addWidget(pokemon63text)
    team6layout.addWidget(pokemon64label)
    team6layout.addWidget(pokemon64text)
    team6layout.addWidget(pokemon65label)
    team6layout.addWidget(pokemon65text)
    team6layout.addWidget(pokemon66label)
    team6layout.addWidget(pokemon66text)

    pokemon71label=QLabel()
    pokemon71label.setMaximumWidth(40)
    pokemon71text = QLineEdit()
    pokemon71text.textChanged.connect(lambda: setPokemonTeams(pokemon71text.text(), pokemon71label,0,team7))
    pokemon72label=QLabel()
    pokemon72label.setMaximumWidth(40)
    pokemon72text = QLineEdit()
    pokemon72text.textChanged.connect(lambda: setPokemonTeams(pokemon72text.text(), pokemon72label,1,team7))
    pokemon73label=QLabel()
    pokemon73label.setMaximumWidth(40)
    pokemon73text = QLineEdit()
    pokemon73text.textChanged.connect(lambda: setPokemonTeams(pokemon73text.text(), pokemon73label,2,team7))
    pokemon74label=QLabel()
    pokemon74label.setMaximumWidth(40)
    pokemon74text = QLineEdit()
    pokemon74text.textChanged.connect(lambda: setPokemonTeams(pokemon74text.text(), pokemon74label,3,team7))
    pokemon75label=QLabel()
    pokemon75label.setMaximumWidth(40)
    pokemon75text = QLineEdit()
    pokemon75text.textChanged.connect(lambda: setPokemonTeams(pokemon75text.text(), pokemon75label,4,team7))
    pokemon76label=QLabel()
    pokemon76label.setMaximumWidth(40)
    pokemon76text = QLineEdit()
    pokemon76text.textChanged.connect(lambda: setPokemonTeams(pokemon76text.text(), pokemon76label,5,team7))
    team7layout.addWidget(QLabel("Team 7"))
    team7layout.addWidget(pokemon71label)
    team7layout.addWidget(pokemon71text)
    team7layout.addWidget(pokemon72label)
    team7layout.addWidget(pokemon72text)
    team7layout.addWidget(pokemon73label)
    team7layout.addWidget(pokemon73text)
    team7layout.addWidget(pokemon74label)
    team7layout.addWidget(pokemon74text)
    team7layout.addWidget(pokemon75label)
    team7layout.addWidget(pokemon75text)
    team7layout.addWidget(pokemon76label)
    team7layout.addWidget(pokemon76text)

    pokemon81label=QLabel()
    pokemon81label.setMaximumWidth(40)
    pokemon81text = QLineEdit()
    pokemon81text.textChanged.connect(lambda: setPokemonTeams(pokemon81text.text(), pokemon81label,0,team8))
    pokemon82label=QLabel()
    pokemon82label.setMaximumWidth(40)
    pokemon82text = QLineEdit()
    pokemon82text.textChanged.connect(lambda: setPokemonTeams(pokemon82text.text(), pokemon82label,1,team8))
    pokemon83label=QLabel()
    pokemon83label.setMaximumWidth(40)
    pokemon83text = QLineEdit()
    pokemon83text.textChanged.connect(lambda: setPokemonTeams(pokemon83text.text(), pokemon83label,2,team8))
    pokemon84label=QLabel()
    pokemon84label.setMaximumWidth(40)
    pokemon84text = QLineEdit()
    pokemon84text.textChanged.connect(lambda: setPokemonTeams(pokemon84text.text(), pokemon84label,3,team8))
    pokemon85label=QLabel()
    pokemon85label.setMaximumWidth(40)
    pokemon85text = QLineEdit()
    pokemon85text.textChanged.connect(lambda: setPokemonTeams(pokemon85text.text(), pokemon85label,4,team8))
    pokemon86label=QLabel()
    pokemon86label.setMaximumWidth(40)
    pokemon86text = QLineEdit()
    pokemon86text.textChanged.connect(lambda: setPokemonTeams(pokemon86text.text(), pokemon86label,5,team8))
    team8layout.addWidget(QLabel("Team 8"))
    team8layout.addWidget(pokemon81label)
    team8layout.addWidget(pokemon81text)
    team8layout.addWidget(pokemon82label)
    team8layout.addWidget(pokemon82text)
    team8layout.addWidget(pokemon83label)
    team8layout.addWidget(pokemon83text)
    team8layout.addWidget(pokemon84label)
    team8layout.addWidget(pokemon84text)
    team8layout.addWidget(pokemon85label)
    team8layout.addWidget(pokemon85text)
    team8layout.addWidget(pokemon86label)
    team8layout.addWidget(pokemon86text)

    checkteambutton=QPushButton('Check teams')
    checkteambutton.setMaximumHeight(30)
    checkteambutton.setMaximumWidth(80)
    checkteambutton.clicked.connect(lambda: createStatisticMatrix(data, tablewidget, team1, team2, team3, team4, team5, team6, team7, team8)) 
    utilitylayout.addWidget(checkteambutton)

    tablewidget=QTableWidget()
    tablewidget.setRowCount(14)
    tablewidget.setColumnCount(14)
    columnnames=["", "", "", "", "", "", "T1", "T2","T3","T4","T5","T6","T7","T8"]
    rownames=["", "", "", "", "", "", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    tablewidget.setHorizontalHeaderLabels(columnnames)
    tablewidget.setVerticalHeaderLabels(rownames)
    tablewidget.setColumnWidth(0,40)
    tablewidget.setColumnWidth(1,40)
    tablewidget.setColumnWidth(2,40)
    tablewidget.setColumnWidth(3,40)
    tablewidget.setColumnWidth(4,40)
    tablewidget.setColumnWidth(5,40)
    tablewidget.setColumnWidth(6,80)
    tablewidget.setColumnWidth(7,80)
    tablewidget.setColumnWidth(8,80)
    tablewidget.setColumnWidth(9,80)
    tablewidget.setColumnWidth(10,80)
    tablewidget.setColumnWidth(11,80)
    tablewidget.setColumnWidth(12,80)
    tablewidget.setColumnWidth(13,80)
    for i in range (0, 6):
        for j in range (0, 6):
            nullcell=QLabel()
            nullcell.setStyleSheet("background-color: black")
            tablewidget.setCellWidget(i,j,nullcell)

    teamsLayout = QVBoxLayout()
    teamsWidget = QWidget()
    teamsWidget.setMaximumHeight(300)
    teamsLayout.addLayout(team1layout)
    teamsLayout.addLayout(team2layout)
    teamsLayout.addLayout(team3layout)
    teamsLayout.addLayout(team4layout)
    teamsLayout.addLayout(team5layout)
    teamsLayout.addLayout(team6layout)
    teamsLayout.addLayout(team7layout)
    teamsLayout.addLayout(team8layout)
    teamsLayout.addLayout(utilitylayout)
    teamsWidget.setLayout(teamsLayout)
    statisticLayout.addWidget(teamsWidget)
    statisticLayout.addWidget(tablewidget)

    return statisticLayout

improvement_page=1
current_dictionary = {}
enemy_vector = []
enemy_teams = []

def loadPreviousPageImpr(improvementtablewidget):
    # printing pressed
    global improvement_page
    global current_dictionary
    if improvement_page > 1 :
        improvement_page=improvement_page-1
        #tablewidget.setCellWidget(0,0,QLabel("Hello"))
        fillImprovementTable(current_dictionary, improvementtablewidget)

def loadNextPageImpr(improvementtablewidget):
    # printing pressed
    global improvement_page
    global current_dictionary
    if improvement_page <= ((len(current_dictionary)-1)/50) :
        improvement_page=improvement_page+1
        fillImprovementTable(current_dictionary, improvementtablewidget)

def fillImprovementTable (mate_dictionary, improvementtablewidget):
    global enemy_teams
    global improvement_page
    index=0
    
    for i in range (0,14):
        for j in range (0,50):
            clearpokemon= QLabel()
            improvementtablewidget.setCellWidget(j,i,clearpokemon)

    for element in mate_dictionary:
        if index >= (improvement_page-1)*50 and index < len(mate_dictionary) and index < improvement_page*50 :
            impindex=index-(improvement_page-1)*50
            hpokemon = QLabel()
            pic = QPixmap("../Sources/Sprites/"+str(element))
            hpokemon.setPixmap(pic)
            improvementtablewidget.setCellWidget(impindex,0,hpokemon)
            improvementtablewidget.setCellWidget(impindex,1,QLabel(str(element)))
            for i in range (0, len(enemy_teams)):
                result=QLabel(str(round(mate_dictionary[element][i][0],0))+"("+str(round(mate_dictionary[element][i][2],2))+")")
                if mate_dictionary[element][i][0]==0:
                    result.setStyleSheet("background-color: grey")
                elif mate_dictionary[element][i][2] >= enemy_vector[i] + 0.05:
                    result.setStyleSheet("background-color: green")
                elif mate_dictionary[element][i][2] < enemy_vector[i] + 0.05 and mate_dictionary[element][i][2] > enemy_vector[i] - 0.05 :
                    result.setStyleSheet("background-color: yellow")
                elif mate_dictionary[element][i][2] <= enemy_vector[i] - 0.05:
                    result.setStyleSheet("background-color: red")
                improvementtablewidget.setCellWidget(impindex,i+2,result)
        index+=1

def add_mate_statistics(match, team, teamtarget, did_win, mate_dictionary, opponent_index) :
    elements = []
    if team == 0 :
        elements = match["players"][0]["player1_lead"] + match["players"][0]["player1_back"]
    else :
        elements = match["players"][1]["player2_lead"] + match["players"][1]["player2_back"] 
        
    for element in elements:
        if element not in teamtarget:
            if element not in mate_dictionary:
                mate_dictionary[element]=numpy.zeros((8,3))
            mate_dictionary[element][opponent_index][0]+=1
            if did_win == 1:
                mate_dictionary[element][opponent_index][1]+=1
            mate_wins=mate_dictionary[element][opponent_index][1]
            mate_occurrency=mate_dictionary[element][opponent_index][0]
            mate_dictionary[element][opponent_index][2]=float(mate_wins/mate_occurrency)

def createStatisticImprovementMatrix(data, tablewidget, improvementtablewidget, teamtarget, team1, team2, team3, team4, team5, team6, team7, team8):
    global improvement_page
    improvement_page=1
    selectedTeams=[]
    mate_dictionary={}

    teamtarget = list(filter(None, teamtarget)) 

    team1 = list(filter(None, team1)) 
    if len(team1)>0:
        selectedTeams.append(team1)
    team2 = list(filter(None, team2)) 
    if len(team2)>0:
        selectedTeams.append(team2)
    team3 = list(filter(None, team3)) 
    if len(team3)>0:
        selectedTeams.append(team3)
    team4 = list(filter(None, team4)) 
    if len(team4)>0:
        selectedTeams.append(team4)
    team5 = list(filter(None, team5))
    if len(team5)>0:
        selectedTeams.append(team5) 
    team6 = list(filter(None, team6)) 
    if len(team6)>0:
        selectedTeams.append(team6)
    team7 = list(filter(None, team7)) 
    if len(team7)>0:
        selectedTeams.append(team7)
    team8 = list(filter(None, team8)) 
    if len(team8)>0:
        selectedTeams.append(team8)

    matrixsize = len(selectedTeams)

    if (matrixsize>0):

        win_vector = numpy.zeros(matrixsize)
        ratio_vector = numpy.zeros(matrixsize)
        occurrence_vector = numpy.zeros(matrixsize)

        for match in data:
            if set(teamtarget).issubset(set(match["players"][0]["player1_team"])):
                for i in range(0,matrixsize):
                    if set(selectedTeams[i]).issubset(set(match["players"][1]["player2_team"])):
                        occurrence_vector[i]+=1
                        if (match["players"][0]["player1_name"] == match["winner"]):
                            add_mate_statistics(match, 0, teamtarget, 1, mate_dictionary, i)
                            win_vector[i]+=1            
                        else :
                            add_mate_statistics(match, 0, teamtarget, 0, mate_dictionary, i) 
            if set(teamtarget).issubset(set(match["players"][1]["player2_team"])):
                for i in range(0,matrixsize):
                    if set(selectedTeams[i]).issubset(set(match["players"][0]["player1_team"])):
                        occurrence_vector[i]+=1
                        if (match["players"][1]["player2_name"] == match["winner"]):
                            add_mate_statistics(match, 1, teamtarget, 1, mate_dictionary, i)
                            win_vector[i]+=1
                        else :
                            add_mate_statistics(match, 1, teamtarget, 0, mate_dictionary, i)  

        for i in range (0, matrixsize):
            if float(occurrence_vector[i])==0 :
                ratio_vector[i]=0
            else :
                ratio_vector[i]=float(win_vector[i]/(occurrence_vector[i]))

        for i in range (0,14):
            clearpokemon= QLabel()
            tablewidget.setCellWidget(0,i,clearpokemon)
   
        for i in range (0, len(teamtarget)):
            hpokemon = QLabel()
            pic = QPixmap("../Sources/Sprites/"+str(teamtarget[i]))
            hpokemon.setPixmap(pic)
            tablewidget.setCellWidget(0,5-i,hpokemon)

        for i in range (0, matrixsize):
            result=QLabel(str(round(occurrence_vector[i],0))+"("+str(round(ratio_vector[i],2))+")")
            if ratio_vector[i]>=0.67:
                result.setStyleSheet("background-color: green")
            elif ratio_vector[i]<0.67 and ratio_vector[i]>0.5:
                result.setStyleSheet("background-color: lightgreen")
            elif ratio_vector[i]==0.5:
                result.setStyleSheet("background-color: yellow")
            elif ratio_vector[i]<0.5 and ratio_vector[i]>=0.33:
                result.setStyleSheet("background-color: orange")
            elif ratio_vector[i]<0.5 and ratio_vector[i]<0.33:
                result.setStyleSheet("background-color: red")
            if occurrence_vector[i]==0:
                result.setStyleSheet("background-color: grey")
            tablewidget.setCellWidget(0,i+6,result)

    global current_dictionary
    global enemy_vector
    global enemy_teams
    current_dictionary=mate_dictionary
    enemy_vector=ratio_vector
    enemy_teams=selectedTeams
    fillImprovementTable (mate_dictionary, improvementtablewidget)  
    
def createStatisticImprovemntLayout(data):
    improvementLayout = QVBoxLayout()
    targetteamlayout=QHBoxLayout()
    team1layout=QHBoxLayout()
    team2layout=QHBoxLayout()
    team3layout=QHBoxLayout()
    team4layout=QHBoxLayout()
    team5layout=QHBoxLayout()
    team6layout=QHBoxLayout()
    team7layout=QHBoxLayout()
    team8layout=QHBoxLayout()
    utilitylayout=QHBoxLayout()

    targetteam=[None]*6
    team1=[None]*6
    team2=[None]*6
    team3=[None]*6
    team4=[None]*6
    team5=[None]*6
    team6=[None]*6
    team7=[None]*6
    team8=[None]*6

    pokemon1label=QLabel()
    pokemon1label.setMaximumWidth(40)
    pokemon1text = QLineEdit()
    pokemon1text.textChanged.connect(lambda: setPokemonTeams(pokemon1text.text(), pokemon1label,0,targetteam))
    pokemon2label=QLabel()
    pokemon2label.setMaximumWidth(40)
    pokemon2text = QLineEdit()
    pokemon2text.textChanged.connect(lambda: setPokemonTeams(pokemon2text.text(), pokemon2label,1,targetteam))
    pokemon3label=QLabel()
    pokemon3label.setMaximumWidth(40)
    pokemon3text = QLineEdit()
    pokemon3text.textChanged.connect(lambda: setPokemonTeams(pokemon3text.text(), pokemon3label,2,targetteam))
    pokemon4label=QLabel()
    pokemon4label.setMaximumWidth(40)
    pokemon4text = QLineEdit()
    pokemon4text.textChanged.connect(lambda: setPokemonTeams(pokemon4text.text(), pokemon4label,3,targetteam))
    pokemon5label=QLabel()
    pokemon5label.setMaximumWidth(40)
    pokemon5text = QLineEdit()
    pokemon5text.textChanged.connect(lambda: setPokemonTeams(pokemon5text.text(), pokemon5label,4,targetteam))
    pokemon6label=QLabel()
    pokemon6label.setMaximumWidth(40)
    pokemon6text = QLineEdit()
    pokemon6text.textChanged.connect(lambda: setPokemonTeams(pokemon6text.text(), pokemon6label,5,targetteam))
    targetteamlayout.addWidget(QLabel("Target"))
    targetteamlayout.addWidget(pokemon1label)
    targetteamlayout.addWidget(pokemon1text)
    targetteamlayout.addWidget(pokemon2label)
    targetteamlayout.addWidget(pokemon2text)
    targetteamlayout.addWidget(pokemon3label)
    targetteamlayout.addWidget(pokemon3text)
    targetteamlayout.addWidget(pokemon4label)
    targetteamlayout.addWidget(pokemon4text)
    targetteamlayout.addWidget(pokemon5label)
    targetteamlayout.addWidget(pokemon5text)
    targetteamlayout.addWidget(pokemon6label)
    targetteamlayout.addWidget(pokemon6text)

    pokemon11label=QLabel()
    pokemon11label.setMaximumWidth(40)
    pokemon11text = QLineEdit()
    pokemon11text.textChanged.connect(lambda: setPokemonTeams(pokemon11text.text(), pokemon11label,0,team1))
    pokemon12label=QLabel()
    pokemon12label.setMaximumWidth(40)
    pokemon12text = QLineEdit()
    pokemon12text.textChanged.connect(lambda: setPokemonTeams(pokemon12text.text(), pokemon12label,1,team1))
    pokemon13label=QLabel()
    pokemon13label.setMaximumWidth(40)
    pokemon13text = QLineEdit()
    pokemon13text.textChanged.connect(lambda: setPokemonTeams(pokemon13text.text(), pokemon13label,2,team1))
    pokemon14label=QLabel()
    pokemon14label.setMaximumWidth(40)
    pokemon14text = QLineEdit()
    pokemon14text.textChanged.connect(lambda: setPokemonTeams(pokemon14text.text(), pokemon14label,3,team1))
    pokemon15label=QLabel()
    pokemon15label.setMaximumWidth(40)
    pokemon15text = QLineEdit()
    pokemon15text.textChanged.connect(lambda: setPokemonTeams(pokemon15text.text(), pokemon15label,4,team1))
    pokemon16label=QLabel()
    pokemon16label.setMaximumWidth(40)
    pokemon16text = QLineEdit()
    pokemon16text.textChanged.connect(lambda: setPokemonTeams(pokemon16text.text(), pokemon16label,5,team1))
    team1layout.addWidget(QLabel("Team 1"))
    team1layout.addWidget(pokemon11label)
    team1layout.addWidget(pokemon11text)
    team1layout.addWidget(pokemon12label)
    team1layout.addWidget(pokemon12text)
    team1layout.addWidget(pokemon13label)
    team1layout.addWidget(pokemon13text)
    team1layout.addWidget(pokemon14label)
    team1layout.addWidget(pokemon14text)
    team1layout.addWidget(pokemon15label)
    team1layout.addWidget(pokemon15text)
    team1layout.addWidget(pokemon16label)
    team1layout.addWidget(pokemon16text)

    pokemon21label=QLabel()
    pokemon21label.setMaximumWidth(40)
    pokemon21text = QLineEdit()
    pokemon21text.textChanged.connect(lambda: setPokemonTeams(pokemon21text.text(), pokemon21label,0,team2))
    pokemon22label=QLabel()
    pokemon22label.setMaximumWidth(40)
    pokemon22text = QLineEdit()
    pokemon22text.textChanged.connect(lambda: setPokemonTeams(pokemon22text.text(), pokemon22label,1,team2))
    pokemon23label=QLabel()
    pokemon23label.setMaximumWidth(40)
    pokemon23text = QLineEdit()
    pokemon23text.textChanged.connect(lambda: setPokemonTeams(pokemon23text.text(), pokemon23label,2,team2))
    pokemon24label=QLabel()
    pokemon24label.setMaximumWidth(40)
    pokemon24text = QLineEdit()
    pokemon24text.textChanged.connect(lambda: setPokemonTeams(pokemon24text.text(), pokemon24label,3,team2))
    pokemon25label=QLabel()
    pokemon25label.setMaximumWidth(40)
    pokemon25text = QLineEdit()
    pokemon25text.textChanged.connect(lambda: setPokemonTeams(pokemon25text.text(), pokemon25label,4,team2))
    pokemon26label=QLabel()
    pokemon26label.setMaximumWidth(40)
    pokemon26text = QLineEdit()
    pokemon26text.textChanged.connect(lambda: setPokemonTeams(pokemon26text.text(), pokemon26label,5,team2))
    team2layout.addWidget(QLabel("Team 2"))
    team2layout.addWidget(pokemon21label)
    team2layout.addWidget(pokemon21text)
    team2layout.addWidget(pokemon22label)
    team2layout.addWidget(pokemon22text)
    team2layout.addWidget(pokemon23label)
    team2layout.addWidget(pokemon23text)
    team2layout.addWidget(pokemon24label)
    team2layout.addWidget(pokemon24text)
    team2layout.addWidget(pokemon25label)
    team2layout.addWidget(pokemon25text)
    team2layout.addWidget(pokemon26label)
    team2layout.addWidget(pokemon26text)

    pokemon31label=QLabel()
    pokemon31label.setMaximumWidth(40)
    pokemon31text = QLineEdit()
    pokemon31text.textChanged.connect(lambda: setPokemonTeams(pokemon31text.text(), pokemon31label,0,team3))
    pokemon32label=QLabel()
    pokemon32label.setMaximumWidth(40)
    pokemon32text = QLineEdit()
    pokemon32text.textChanged.connect(lambda: setPokemonTeams(pokemon32text.text(), pokemon32label,1,team3))
    pokemon33label=QLabel()
    pokemon33label.setMaximumWidth(40)
    pokemon33text = QLineEdit()
    pokemon33text.textChanged.connect(lambda: setPokemonTeams(pokemon33text.text(), pokemon33label,2,team3))
    pokemon34label=QLabel()
    pokemon34label.setMaximumWidth(40)
    pokemon34text = QLineEdit()
    pokemon34text.textChanged.connect(lambda: setPokemonTeams(pokemon34text.text(), pokemon34label,3,team3))
    pokemon35label=QLabel()
    pokemon35label.setMaximumWidth(40)
    pokemon35text = QLineEdit()
    pokemon35text.textChanged.connect(lambda: setPokemonTeams(pokemon35text.text(), pokemon35label,4,team3))
    pokemon36label=QLabel()
    pokemon36label.setMaximumWidth(40)
    pokemon36text = QLineEdit()
    pokemon36text.textChanged.connect(lambda: setPokemonTeams(pokemon36text.text(), pokemon36label,5,team3))
    team3layout.addWidget(QLabel("Team 3"))
    team3layout.addWidget(pokemon31label)
    team3layout.addWidget(pokemon31text)
    team3layout.addWidget(pokemon32label)
    team3layout.addWidget(pokemon32text)
    team3layout.addWidget(pokemon33label)
    team3layout.addWidget(pokemon33text)
    team3layout.addWidget(pokemon34label)
    team3layout.addWidget(pokemon34text)
    team3layout.addWidget(pokemon35label)
    team3layout.addWidget(pokemon35text)
    team3layout.addWidget(pokemon36label)
    team3layout.addWidget(pokemon36text)

    pokemon41label=QLabel()
    pokemon41label.setMaximumWidth(40)
    pokemon41text = QLineEdit()
    pokemon41text.textChanged.connect(lambda: setPokemonTeams(pokemon41text.text(), pokemon41label,0,team4))
    pokemon42label=QLabel()
    pokemon42label.setMaximumWidth(40)
    pokemon42text = QLineEdit()
    pokemon42text.textChanged.connect(lambda: setPokemonTeams(pokemon42text.text(), pokemon42label,1,team4))
    pokemon43label=QLabel()
    pokemon43label.setMaximumWidth(40)
    pokemon43text = QLineEdit()
    pokemon43text.textChanged.connect(lambda: setPokemonTeams(pokemon43text.text(), pokemon43label,2,team4))
    pokemon44label=QLabel()
    pokemon44label.setMaximumWidth(40)
    pokemon44text = QLineEdit()
    pokemon44text.textChanged.connect(lambda: setPokemonTeams(pokemon44text.text(), pokemon44label,3,team4))
    pokemon45label=QLabel()
    pokemon45label.setMaximumWidth(40)
    pokemon45text = QLineEdit()
    pokemon45text.textChanged.connect(lambda: setPokemonTeams(pokemon45text.text(), pokemon45label,4,team4))
    pokemon46label=QLabel()
    pokemon46label.setMaximumWidth(40)
    pokemon46text = QLineEdit()
    pokemon46text.textChanged.connect(lambda: setPokemonTeams(pokemon46text.text(), pokemon46label,5,team4))
    team4layout.addWidget(QLabel("Team 4"))
    team4layout.addWidget(pokemon41label)
    team4layout.addWidget(pokemon41text)
    team4layout.addWidget(pokemon42label)
    team4layout.addWidget(pokemon42text)
    team4layout.addWidget(pokemon43label)
    team4layout.addWidget(pokemon43text)
    team4layout.addWidget(pokemon44label)
    team4layout.addWidget(pokemon44text)
    team4layout.addWidget(pokemon45label)
    team4layout.addWidget(pokemon45text)
    team4layout.addWidget(pokemon46label)
    team4layout.addWidget(pokemon46text)

    pokemon51label=QLabel()
    pokemon51label.setMaximumWidth(40)
    pokemon51text = QLineEdit()
    pokemon51text.textChanged.connect(lambda: setPokemonTeams(pokemon51text.text(), pokemon51label,0,team5))
    pokemon52label=QLabel()
    pokemon52label.setMaximumWidth(40)
    pokemon52text = QLineEdit()
    pokemon52text.textChanged.connect(lambda: setPokemonTeams(pokemon52text.text(), pokemon52label,1,team5))
    pokemon53label=QLabel()
    pokemon53label.setMaximumWidth(40)
    pokemon53text = QLineEdit()
    pokemon53text.textChanged.connect(lambda: setPokemonTeams(pokemon53text.text(), pokemon53label,2,team5))
    pokemon54label=QLabel()
    pokemon54label.setMaximumWidth(40)
    pokemon54text = QLineEdit()
    pokemon54text.textChanged.connect(lambda: setPokemonTeams(pokemon54text.text(), pokemon54label,3,team5))
    pokemon55label=QLabel()
    pokemon55label.setMaximumWidth(40)
    pokemon55text = QLineEdit()
    pokemon55text.textChanged.connect(lambda: setPokemonTeams(pokemon55text.text(), pokemon55label,4,team5))
    pokemon56label=QLabel()
    pokemon56label.setMaximumWidth(40)
    pokemon56text = QLineEdit()
    pokemon56text.textChanged.connect(lambda: setPokemonTeams(pokemon56text.text(), pokemon56label,5,team5))
    team5layout.addWidget(QLabel("Team 5"))
    team5layout.addWidget(pokemon51label)
    team5layout.addWidget(pokemon51text)
    team5layout.addWidget(pokemon52label)
    team5layout.addWidget(pokemon52text)
    team5layout.addWidget(pokemon53label)
    team5layout.addWidget(pokemon53text)
    team5layout.addWidget(pokemon54label)
    team5layout.addWidget(pokemon54text)
    team5layout.addWidget(pokemon55label)
    team5layout.addWidget(pokemon55text)
    team5layout.addWidget(pokemon56label)
    team5layout.addWidget(pokemon56text)

    pokemon61label=QLabel()
    pokemon61label.setMaximumWidth(40)
    pokemon61text = QLineEdit()
    pokemon61text.textChanged.connect(lambda: setPokemonTeams(pokemon61text.text(), pokemon61label,0,team6))
    pokemon62label=QLabel()
    pokemon62label.setMaximumWidth(40)
    pokemon62text = QLineEdit()
    pokemon62text.textChanged.connect(lambda: setPokemonTeams(pokemon62text.text(), pokemon62label,1,team6))
    pokemon63label=QLabel()
    pokemon63label.setMaximumWidth(40)
    pokemon63text = QLineEdit()
    pokemon63text.textChanged.connect(lambda: setPokemonTeams(pokemon63text.text(), pokemon63label,2,team6))
    pokemon64label=QLabel()
    pokemon64label.setMaximumWidth(40)
    pokemon64text = QLineEdit()
    pokemon64text.textChanged.connect(lambda: setPokemonTeams(pokemon64text.text(), pokemon64label,3,team6))
    pokemon65label=QLabel()
    pokemon65label.setMaximumWidth(40)
    pokemon65text = QLineEdit()
    pokemon65text.textChanged.connect(lambda: setPokemonTeams(pokemon65text.text(), pokemon65label,4,team6))
    pokemon66label=QLabel()
    pokemon66label.setMaximumWidth(40)
    pokemon66text = QLineEdit()
    pokemon66text.textChanged.connect(lambda: setPokemonTeams(pokemon66text.text(), pokemon66label,5,team6))
    team6layout.addWidget(QLabel("Team 6"))
    team6layout.addWidget(pokemon61label)
    team6layout.addWidget(pokemon61text)
    team6layout.addWidget(pokemon62label)
    team6layout.addWidget(pokemon62text)
    team6layout.addWidget(pokemon63label)
    team6layout.addWidget(pokemon63text)
    team6layout.addWidget(pokemon64label)
    team6layout.addWidget(pokemon64text)
    team6layout.addWidget(pokemon65label)
    team6layout.addWidget(pokemon65text)
    team6layout.addWidget(pokemon66label)
    team6layout.addWidget(pokemon66text)

    pokemon71label=QLabel()
    pokemon71label.setMaximumWidth(40)
    pokemon71text = QLineEdit()
    pokemon71text.textChanged.connect(lambda: setPokemonTeams(pokemon71text.text(), pokemon71label,0,team7))
    pokemon72label=QLabel()
    pokemon72label.setMaximumWidth(40)
    pokemon72text = QLineEdit()
    pokemon72text.textChanged.connect(lambda: setPokemonTeams(pokemon72text.text(), pokemon72label,1,team7))
    pokemon73label=QLabel()
    pokemon73label.setMaximumWidth(40)
    pokemon73text = QLineEdit()
    pokemon73text.textChanged.connect(lambda: setPokemonTeams(pokemon73text.text(), pokemon73label,2,team7))
    pokemon74label=QLabel()
    pokemon74label.setMaximumWidth(40)
    pokemon74text = QLineEdit()
    pokemon74text.textChanged.connect(lambda: setPokemonTeams(pokemon74text.text(), pokemon74label,3,team7))
    pokemon75label=QLabel()
    pokemon75label.setMaximumWidth(40)
    pokemon75text = QLineEdit()
    pokemon75text.textChanged.connect(lambda: setPokemonTeams(pokemon75text.text(), pokemon75label,4,team7))
    pokemon76label=QLabel()
    pokemon76label.setMaximumWidth(40)
    pokemon76text = QLineEdit()
    pokemon76text.textChanged.connect(lambda: setPokemonTeams(pokemon76text.text(), pokemon76label,5,team7))
    team7layout.addWidget(QLabel("Team 7"))
    team7layout.addWidget(pokemon71label)
    team7layout.addWidget(pokemon71text)
    team7layout.addWidget(pokemon72label)
    team7layout.addWidget(pokemon72text)
    team7layout.addWidget(pokemon73label)
    team7layout.addWidget(pokemon73text)
    team7layout.addWidget(pokemon74label)
    team7layout.addWidget(pokemon74text)
    team7layout.addWidget(pokemon75label)
    team7layout.addWidget(pokemon75text)
    team7layout.addWidget(pokemon76label)
    team7layout.addWidget(pokemon76text)

    pokemon81label=QLabel()
    pokemon81label.setMaximumWidth(40)
    pokemon81text = QLineEdit()
    pokemon81text.textChanged.connect(lambda: setPokemonTeams(pokemon81text.text(), pokemon81label,0,team8))
    pokemon82label=QLabel()
    pokemon82label.setMaximumWidth(40)
    pokemon82text = QLineEdit()
    pokemon82text.textChanged.connect(lambda: setPokemonTeams(pokemon82text.text(), pokemon82label,1,team8))
    pokemon83label=QLabel()
    pokemon83label.setMaximumWidth(40)
    pokemon83text = QLineEdit()
    pokemon83text.textChanged.connect(lambda: setPokemonTeams(pokemon83text.text(), pokemon83label,2,team8))
    pokemon84label=QLabel()
    pokemon84label.setMaximumWidth(40)
    pokemon84text = QLineEdit()
    pokemon84text.textChanged.connect(lambda: setPokemonTeams(pokemon84text.text(), pokemon84label,3,team8))
    pokemon85label=QLabel()
    pokemon85label.setMaximumWidth(40)
    pokemon85text = QLineEdit()
    pokemon85text.textChanged.connect(lambda: setPokemonTeams(pokemon85text.text(), pokemon85label,4,team8))
    pokemon86label=QLabel()
    pokemon86label.setMaximumWidth(40)
    pokemon86text = QLineEdit()
    pokemon86text.textChanged.connect(lambda: setPokemonTeams(pokemon86text.text(), pokemon86label,5,team8))
    team8layout.addWidget(QLabel("Team 8"))
    team8layout.addWidget(pokemon81label)
    team8layout.addWidget(pokemon81text)
    team8layout.addWidget(pokemon82label)
    team8layout.addWidget(pokemon82text)
    team8layout.addWidget(pokemon83label)
    team8layout.addWidget(pokemon83text)
    team8layout.addWidget(pokemon84label)
    team8layout.addWidget(pokemon84text)
    team8layout.addWidget(pokemon85label)
    team8layout.addWidget(pokemon85text)
    team8layout.addWidget(pokemon86label)
    team8layout.addWidget(pokemon86text)

    checkteambutton=QPushButton('Check teams')
    checkteambutton.setMaximumHeight(30)
    checkteambutton.setMaximumWidth(80)
    checkteambutton.clicked.connect(lambda: createStatisticImprovementMatrix(data, tablewidget, improvementtablewidget, targetteam, team1, team2, team3, team4, team5, team6, team7, team8)) 
    utilitylayout.addWidget(checkteambutton)

    tablewidget=QTableWidget()
    tablewidget.setRowCount(1)
    tablewidget.setColumnCount(14)
    columnnames=["", "", "", "", "", "", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    rownames=["Team"]
    tablewidget.setHorizontalHeaderLabels(columnnames)
    tablewidget.setVerticalHeaderLabels(rownames)
    tablewidget.setColumnWidth(0,40)
    tablewidget.setColumnWidth(1,40)
    tablewidget.setColumnWidth(2,40)
    tablewidget.setColumnWidth(3,40)
    tablewidget.setColumnWidth(4,40)
    tablewidget.setColumnWidth(5,40)
    tablewidget.setColumnWidth(6,80)
    tablewidget.setColumnWidth(7,80)
    tablewidget.setColumnWidth(8,80)
    tablewidget.setColumnWidth(9,80)
    tablewidget.setColumnWidth(10,80)
    tablewidget.setColumnWidth(11,80)
    tablewidget.setColumnWidth(12,80)
    tablewidget.setColumnWidth(13,80)
    tablewidget.setMaximumHeight(70)

    improvementtablewidget=QTableWidget()
    improvementtablewidget.setRowCount(50)
    improvementtablewidget.setColumnCount(10)
    improvementcolumnnames=["","Pokemon", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    improvementtablewidget.setHorizontalHeaderLabels(improvementcolumnnames)
    improvementtablewidget.setColumnWidth(0,40)
    improvementtablewidget.setColumnWidth(1,150)
    improvementtablewidget.setColumnWidth(2,80)
    improvementtablewidget.setColumnWidth(3,80)
    improvementtablewidget.setColumnWidth(4,80)
    improvementtablewidget.setColumnWidth(5,80)
    improvementtablewidget.setColumnWidth(6,80)
    improvementtablewidget.setColumnWidth(7,80)
    improvementtablewidget.setColumnWidth(8,80)
    improvementtablewidget.setColumnWidth(9,80)

    teamsLayout=QVBoxLayout()
    teamsWidget=QWidget()
    teamsWidget.setMaximumHeight(320)
    teamsLayout.addLayout(targetteamlayout)
    teamsLayout.addLayout(team1layout)
    teamsLayout.addLayout(team2layout)
    teamsLayout.addLayout(team3layout)
    teamsLayout.addLayout(team4layout)
    teamsLayout.addLayout(team5layout)
    teamsLayout.addLayout(team6layout)
    teamsLayout.addLayout(team7layout)
    teamsLayout.addLayout(team8layout)
    teamsLayout.addLayout(utilitylayout)
    teamsWidget.setLayout(teamsLayout)

    global current_dictionary
    buttonlayout=QHBoxLayout()
    previousbutton=QPushButton('Previous page')
    previousbutton.setMaximumHeight(30)   
    previousbutton.setMaximumWidth(120)
    previousbutton.clicked.connect(lambda: loadPreviousPageImpr(improvementtablewidget)) 
    buttonlayout.addWidget(previousbutton)
    nextbutton=QPushButton('Next page')
    nextbutton.setMaximumHeight(30)   
    nextbutton.setMaximumWidth(120) 
    nextbutton.clicked.connect(lambda: loadNextPageImpr(improvementtablewidget)) 
    buttonlayout.addWidget(nextbutton)

    improvementLayout.addWidget(teamsWidget)
    improvementLayout.addWidget(tablewidget)
    improvementLayout.addWidget(improvementtablewidget)
    improvementLayout.addLayout(buttonlayout)

    return improvementLayout  

metagame="gen9vgc2023series1"
manual_json_path="../Database/sd_manual_"+metagame+".json"

def write_json (new_entry):
    already_entered = []
    new = []
    new.append(new_entry)
    if os.path.isfile(manual_json_path) and os.access(manual_json_path, os.R_OK):
        with open(manual_json_path, 'r') as data_file:
            already_entered = json.load(data_file)
            data_file.close()
    else:
        open(manual_json_path, "x")
    new+=already_entered
    with open(manual_json_path, 'w') as outfile:
        json.dump(new, outfile)
        outfile.close()

def writeToManualJson(trainer1, team1, lead1, back1, trainer2, team2, lead2, back2, dynamaxed, winner, url):
    global metagame
    new_entry = {
        "date": " ",
        "metagame": metagame,
        "players": [
            {
                "player1_name": trainer1, 
                "player1_rating": 0,
                "player1_team": team1, 
                "player1_lead": lead1,
                "player1_back": back1,
                "player1_terastallized": dynamaxed[0],
            },
            {
                "player2_name": trainer2, 
                "player2_rating": 0,
                "player2_team": team2, 
                "player2_lead": lead2,
                "player2_back": back2,
                "player2_terastallized": dynamaxed[1],
            },
        ],
        "winner": winner,
        "replay_url": url,
    }

    write_json(new_entry)

    dlg = QDialog()
    dlg.setWindowTitle("Match added to database")
    dlg.exec()
    
def createManualAdditionLayout(data):
    manualLayout = QVBoxLayout()
    teamsLayout=QHBoxLayout()
    team1layout = QVBoxLayout()
    team2layout = QVBoxLayout()
    generalLayout=QHBoxLayout()

    team1=[None]*6
    lead1=[None]*2
    back1=[None]*2
    team2=[None]*6
    lead2=[None]*2
    back2=[None]*2
    dynamaxed=[None]*2

    trainer1alt=QLabel("Trainer 1:")
    trainer1text=QLineEdit()   
    trainer1layout = QHBoxLayout()
    trainer1layout.addWidget(trainer1alt)
    trainer1layout.addWidget(trainer1text)
    pokemon11alt=QLabel("Pokemon 1:")
    pokemon11label=QLabel()
    pokemon11label.setMaximumWidth(40)
    pokemon11text = QLineEdit()
    pokemon11text.textChanged.connect(lambda: setPokemonTeams(pokemon11text.text(), pokemon11label,0,team1))
    team11layout = QHBoxLayout()
    team11layout.addWidget(pokemon11alt)
    team11layout.addWidget(pokemon11label)
    team11layout.addWidget(pokemon11text)
    pokemon12alt=QLabel("Pokemon 2:")
    pokemon12label=QLabel()
    pokemon12label.setMaximumWidth(40)
    pokemon12text = QLineEdit()
    pokemon12text.textChanged.connect(lambda: setPokemonTeams(pokemon12text.text(), pokemon12label,1,team1))
    team12layout = QHBoxLayout()
    team12layout.addWidget(pokemon12alt)
    team12layout.addWidget(pokemon12label)
    team12layout.addWidget(pokemon12text)
    pokemon13alt=QLabel("Pokemon 3:")
    pokemon13label=QLabel()
    pokemon13label.setMaximumWidth(40)
    pokemon13text = QLineEdit()
    pokemon13text.textChanged.connect(lambda: setPokemonTeams(pokemon13text.text(), pokemon13label,2,team1))
    team13layout = QHBoxLayout()
    team13layout.addWidget(pokemon13alt)
    team13layout.addWidget(pokemon13label)
    team13layout.addWidget(pokemon13text)
    pokemon14alt=QLabel("Pokemon 4:")
    pokemon14label=QLabel()
    pokemon14label.setMaximumWidth(40)
    pokemon14text = QLineEdit()
    pokemon14text.textChanged.connect(lambda: setPokemonTeams(pokemon14text.text(), pokemon14label,3,team1))
    team14layout = QHBoxLayout()
    team14layout.addWidget(pokemon14alt)
    team14layout.addWidget(pokemon14label)
    team14layout.addWidget(pokemon14text)
    pokemon15alt=QLabel("Pokemon 5:")
    pokemon15label=QLabel()
    pokemon15label.setMaximumWidth(40)
    pokemon15text = QLineEdit()
    pokemon15text.textChanged.connect(lambda: setPokemonTeams(pokemon15text.text(), pokemon15label,4,team1))
    team15layout = QHBoxLayout()
    team15layout.addWidget(pokemon15alt)
    team15layout.addWidget(pokemon15label)
    team15layout.addWidget(pokemon15text)
    pokemon16alt=QLabel("Pokemon 6:")
    pokemon16label=QLabel()
    pokemon16label.setMaximumWidth(40)
    pokemon16text = QLineEdit()
    pokemon16text.textChanged.connect(lambda: setPokemonTeams(pokemon16text.text(), pokemon16label,5,team1))
    team16layout = QHBoxLayout()
    team16layout.addWidget(pokemon16alt)
    team16layout.addWidget(pokemon16label)
    team16layout.addWidget(pokemon16text)

    lead11alt=QLabel("Lead Pokemon 1:")
    lead11label=QLabel()
    lead11label.setMaximumWidth(40)
    lead11text = QLineEdit()
    lead11text.textChanged.connect(lambda: setPokemonTeams(lead11text.text(), lead11label,0,lead1))
    lead11layout = QHBoxLayout()
    lead11layout.addWidget(lead11alt)
    lead11layout.addWidget(lead11label)
    lead11layout.addWidget(lead11text)
    lead12alt=QLabel("Lead Pokemon 2:")
    lead12label=QLabel()
    lead12label.setMaximumWidth(40)
    lead12text = QLineEdit()
    lead12text.textChanged.connect(lambda: setPokemonTeams(lead12text.text(), lead12label,1,lead1))
    lead12layout = QHBoxLayout()
    lead12layout.addWidget(lead12alt)
    lead12layout.addWidget(lead12label)
    lead12layout.addWidget(lead12text)
    back11alt=QLabel("Back Pokemon 1:")
    back11label=QLabel()
    back11label.setMaximumWidth(40)
    back11text = QLineEdit()
    back11text.textChanged.connect(lambda: setPokemonTeams(back11text.text(), back11label,0,back1))
    back11layout = QHBoxLayout()
    back11layout.addWidget(back11alt)
    back11layout.addWidget(back11label)
    back11layout.addWidget(back11text)
    back12alt=QLabel("Back Pokemon 2:")
    back12label=QLabel()
    back12label.setMaximumWidth(40)
    back12text = QLineEdit()
    back12text.textChanged.connect(lambda: setPokemonTeams(back12text.text(), back12label,1,back1))
    back12layout = QHBoxLayout()
    back12layout.addWidget(back12alt)
    back12layout.addWidget(back12label)
    back12layout.addWidget(back12text)
    dynamaxed1alt=QLabel("Dynamaxed Pokemon:")
    dynamaxed1label=QLabel()
    dynamaxed1label.setMaximumWidth(40)
    dynamaxed1text = QLineEdit()
    dynamaxed1text.textChanged.connect(lambda: setPokemonTeams(dynamaxed1text.text(), dynamaxed1label,0,dynamaxed))
    dynamaxed1layout = QHBoxLayout()
    dynamaxed1layout.addWidget(dynamaxed1alt)
    dynamaxed1layout.addWidget(dynamaxed1label)
    dynamaxed1layout.addWidget(dynamaxed1text)

    team1layout.addLayout(trainer1layout)
    team1layout.addLayout(team11layout)
    team1layout.addLayout(team12layout)
    team1layout.addLayout(team13layout)
    team1layout.addLayout(team14layout)
    team1layout.addLayout(team15layout)
    team1layout.addLayout(team16layout)
    team1layout.addLayout(lead11layout)
    team1layout.addLayout(lead12layout)
    team1layout.addLayout(back11layout)
    team1layout.addLayout(back12layout)
    team1layout.addLayout(dynamaxed1layout)

    trainer2alt=QLabel("Trainer 2:")
    trainer2text=QLineEdit()   
    trainer2layout = QHBoxLayout()
    trainer2layout.addWidget(trainer2alt)
    trainer2layout.addWidget(trainer2text)
    pokemon21alt=QLabel("Pokemon 1:")
    pokemon21label=QLabel()
    pokemon21label.setMaximumWidth(40)
    pokemon21text = QLineEdit()
    pokemon21text.textChanged.connect(lambda: setPokemonTeams(pokemon21text.text(), pokemon21label,0,team2))
    team21layout = QHBoxLayout()
    team21layout.addWidget(pokemon21alt)
    team21layout.addWidget(pokemon21label)
    team21layout.addWidget(pokemon21text)
    pokemon22alt=QLabel("Pokemon 2:")
    pokemon22label=QLabel()
    pokemon22label.setMaximumWidth(40)
    pokemon22text = QLineEdit()
    pokemon22text.textChanged.connect(lambda: setPokemonTeams(pokemon22text.text(), pokemon22label,1,team2))
    team22layout = QHBoxLayout()
    team22layout.addWidget(pokemon22alt)
    team22layout.addWidget(pokemon22label)
    team22layout.addWidget(pokemon22text)
    pokemon23alt=QLabel("Pokemon 3:")
    pokemon23label=QLabel()
    pokemon23label.setMaximumWidth(40)
    pokemon23text = QLineEdit()
    pokemon23text.textChanged.connect(lambda: setPokemonTeams(pokemon23text.text(), pokemon23label,2,team2))
    team23layout = QHBoxLayout()
    team23layout.addWidget(pokemon23alt)
    team23layout.addWidget(pokemon23label)
    team23layout.addWidget(pokemon23text)
    pokemon24alt=QLabel("Pokemon 4:")
    pokemon24label=QLabel()
    pokemon24label.setMaximumWidth(40)
    pokemon24text = QLineEdit()
    pokemon24text.textChanged.connect(lambda: setPokemonTeams(pokemon24text.text(), pokemon24label,3,team2))
    team24layout = QHBoxLayout()
    team24layout.addWidget(pokemon24alt)
    team24layout.addWidget(pokemon24label)
    team24layout.addWidget(pokemon24text)
    pokemon25alt=QLabel("Pokemon 5:")
    pokemon25label=QLabel()
    pokemon25label.setMaximumWidth(40)
    pokemon25text = QLineEdit()
    pokemon25text.textChanged.connect(lambda: setPokemonTeams(pokemon25text.text(), pokemon25label,4,team2))
    team25layout = QHBoxLayout()
    team25layout.addWidget(pokemon25alt)
    team25layout.addWidget(pokemon25label)
    team25layout.addWidget(pokemon25text)
    pokemon26alt=QLabel("Pokemon 6:")
    pokemon26label=QLabel()
    pokemon26label.setMaximumWidth(40)
    pokemon26text = QLineEdit()
    pokemon26text.textChanged.connect(lambda: setPokemonTeams(pokemon26text.text(), pokemon26label,5,team2))
    team26layout = QHBoxLayout()
    team26layout.addWidget(pokemon26alt)
    team26layout.addWidget(pokemon26label)
    team26layout.addWidget(pokemon26text)

    lead21alt=QLabel("Lead Pokemon 1:")
    lead21label=QLabel()
    lead21label.setMaximumWidth(40)
    lead21text = QLineEdit()
    lead21text.textChanged.connect(lambda: setPokemonTeams(lead21text.text(), lead21label,0,lead2))
    lead21layout = QHBoxLayout()
    lead21layout.addWidget(lead21alt)
    lead21layout.addWidget(lead21label)
    lead21layout.addWidget(lead21text)
    lead22alt=QLabel("Lead Pokemon 2:")
    lead22label=QLabel()
    lead22label.setMaximumWidth(40)
    lead22text = QLineEdit()
    lead22text.textChanged.connect(lambda: setPokemonTeams(lead22text.text(), lead22label,1,lead2))
    lead22layout = QHBoxLayout()
    lead22layout.addWidget(lead22alt)
    lead22layout.addWidget(lead22label)
    lead22layout.addWidget(lead22text)
    back21alt=QLabel("Back Pokemon 1:")
    back21label=QLabel()
    back21label.setMaximumWidth(40)
    back21text = QLineEdit()
    back21text.textChanged.connect(lambda: setPokemonTeams(back21text.text(), back21label,0,back2))
    back21layout = QHBoxLayout()
    back21layout.addWidget(back21alt)
    back21layout.addWidget(back21label)
    back21layout.addWidget(back21text)
    back22alt=QLabel("Back Pokemon 2:")
    back22label=QLabel()
    back22label.setMaximumWidth(40)
    back22text = QLineEdit()
    back22text.textChanged.connect(lambda: setPokemonTeams(back22text.text(), back22label,1,back2))
    back22layout = QHBoxLayout()
    back22layout.addWidget(back22alt)
    back22layout.addWidget(back22label)
    back22layout.addWidget(back22text)
    dynamaxed2alt=QLabel("Dynamaxed Pokemon:")
    dynamaxed2label=QLabel()
    dynamaxed2label.setMaximumWidth(40)
    dynamaxed2text = QLineEdit()
    dynamaxed2text.textChanged.connect(lambda: setPokemonTeams(dynamaxed2text.text(), dynamaxed2label,1,dynamaxed))
    dynamaxed2layout = QHBoxLayout()
    dynamaxed2layout.addWidget(dynamaxed2alt)
    dynamaxed2layout.addWidget(dynamaxed2label)
    dynamaxed2layout.addWidget(dynamaxed2text)

    team2layout.addLayout(trainer2layout)
    team2layout.addLayout(team21layout)
    team2layout.addLayout(team22layout)
    team2layout.addLayout(team23layout)
    team2layout.addLayout(team24layout)
    team2layout.addLayout(team25layout)
    team2layout.addLayout(team26layout)
    team2layout.addLayout(lead21layout)
    team2layout.addLayout(lead22layout)
    team2layout.addLayout(back21layout)
    team2layout.addLayout(back22layout)
    team2layout.addLayout(dynamaxed2layout)

    winneralt=QLabel("Winner:")
    winnertext=QLineEdit()   
    generalLayout.addWidget(winneralt)
    generalLayout.addWidget(winnertext)
    urlalt=QLabel("Url to match:")
    urltext=QLineEdit()   
    generalLayout.addWidget(urlalt)
    generalLayout.addWidget(urltext)  
    saveButton = QPushButton("Save match")
    saveButton.clicked.connect(lambda: writeToManualJson(trainer1text.text(), team1, lead1, back1, trainer2text.text(), team2, lead2, back2, dynamaxed, winnertext.text(), urltext.text()))
    generalLayout.addWidget(saveButton)  

    teamsLayout.addLayout(team1layout)
    teamsLayout.addLayout(team2layout)
    manualLayout.addLayout(teamsLayout)
    manualLayout.addLayout(generalLayout)


    return manualLayout

lead_page = 1 
lead_list = []

def fillLeadTable (lead_dictionary, improvementtablewidget) : 
    global enemy_teams
    global lead_page
    global lead_list
    index=0
    result = []

    for i in range (0,14):
        for j in range (0,50):
            clearpokemon= QLabel()
            improvementtablewidget.setCellWidget(j,i,clearpokemon)

    for element in lead_list:
        if index >= (lead_page-1)*50 and index < len(lead_dictionary) and index < lead_page*50 :
            impindex=index-(lead_page-1)*50
            hpokemon1 = QLabel()
            hpokemon2 = QLabel()
            el_lead=element.split("_")
            pic1 = QPixmap("../Sources/Sprites/"+str(el_lead[0]))
            hpokemon1.setPixmap(pic1)
            pic2 = QPixmap("../Sources/Sprites/"+str(el_lead[1]))
            hpokemon2.setPixmap(pic2)
            improvementtablewidget.setCellWidget(impindex,0,hpokemon1)
            improvementtablewidget.setCellWidget(impindex,1,hpokemon2)
            el_lead
            improvementtablewidget.setCellWidget(impindex,2,QLabel(str(element)))
            for i in range (0, len(enemy_teams)):
                result=QLabel(str(round(lead_dictionary[element][i][0],0))+"("+str(round(lead_dictionary[element][i][2],2))+")")
                if lead_dictionary[element][i][0]==0:
                    result.setStyleSheet("background-color: grey")
                elif lead_dictionary[element][i][2] >= enemy_vector[i] + 0.05:
                    result.setStyleSheet("background-color: green")
                elif lead_dictionary[element][i][2] < enemy_vector[i] + 0.05 and lead_dictionary[element][i][2] > enemy_vector[i] - 0.05 :
                    result.setStyleSheet("background-color: yellow")
                elif lead_dictionary[element][i][2] <= enemy_vector[i] - 0.05:
                    result.setStyleSheet("background-color: red")
                improvementtablewidget.setCellWidget(impindex,i+3,result)
        index+=1



def add_lead_statistics(match, team, teamtarget, did_win, lead_dictionary, opponent_index) :
    lead = []
    global lead_list
    key = ""
    if team == 0 :
        lead = match["players"][0]["player1_lead"]
    else :
        lead = match["players"][1]["player2_lead"]

    if len(lead)>0:
        if lead[0]<lead[1]:
            key = lead[0]+"_"+lead[1]
        else:
            key = lead[1]+"_"+lead[0]

        if key not in lead_dictionary:
            lead_dictionary[key]=numpy.zeros((8,3))
            lead_list.append(key)
        lead_dictionary[key][opponent_index][0]+=1
        if did_win == 1:
            lead_dictionary[key][opponent_index][1]+=1
            lead_wins=lead_dictionary[key][opponent_index][1]
            lead_occurrency=lead_dictionary[key][opponent_index][0]
            lead_dictionary[key][opponent_index][2]=float(lead_wins/lead_occurrency)


def createLeadsMatrix(data, tablewidget, improvementtablewidget, teamtarget, team1, team2, team3, team4, team5, team6, team7, team8):
    global lead_page
    lead_page=1
    selectedTeams=[]
    lead_dictionary={}
    teamtarget = list(filter(None, teamtarget)) 

    team1 = list(filter(None, team1)) 
    if len(team1)>0:
        selectedTeams.append(team1)
    team2 = list(filter(None, team2)) 
    if len(team2)>0:
        selectedTeams.append(team2)
    team3 = list(filter(None, team3)) 
    if len(team3)>0:
        selectedTeams.append(team3)
    team4 = list(filter(None, team4)) 
    if len(team4)>0:
        selectedTeams.append(team4)
    team5 = list(filter(None, team5))
    if len(team5)>0:
        selectedTeams.append(team5) 
    team6 = list(filter(None, team6)) 
    if len(team6)>0:
        selectedTeams.append(team6)
    team7 = list(filter(None, team7)) 
    if len(team7)>0:
        selectedTeams.append(team7)
    team8 = list(filter(None, team8)) 
    if len(team8)>0:
        selectedTeams.append(team8)

    matrixsize = len(selectedTeams)

    if (matrixsize>0):

        win_vector = numpy.zeros(matrixsize)
        ratio_vector = numpy.zeros(matrixsize)
        occurrence_vector = numpy.zeros(matrixsize)

        for match in data:
            if set(teamtarget).issubset(set(match["players"][0]["player1_team"])):
                for i in range(0,matrixsize):
                    if set(selectedTeams[i]).issubset(set(match["players"][1]["player2_team"])):
                        occurrence_vector[i]+=1
                        if (match["players"][0]["player1_name"] == match["winner"]):
                            add_lead_statistics(match, 0, teamtarget, 1, lead_dictionary, i)
                            win_vector[i]+=1            
                        else :
                            add_lead_statistics(match, 0, teamtarget, 0, lead_dictionary, i) 
            if set(teamtarget).issubset(set(match["players"][1]["player2_team"])):
                for i in range(0,matrixsize):
                    if set(selectedTeams[i]).issubset(set(match["players"][0]["player1_team"])):
                        occurrence_vector[i]+=1
                        if (match["players"][1]["player2_name"] == match["winner"]):
                            add_lead_statistics(match, 1, teamtarget, 1, lead_dictionary, i)
                            win_vector[i]+=1
                        else :
                            add_lead_statistics(match, 1, teamtarget, 0, lead_dictionary, i)  

        for i in range (0, matrixsize):
            if float(occurrence_vector[i])==0 :
                ratio_vector[i]=0
            else :
                ratio_vector[i]=float(win_vector[i]/(occurrence_vector[i]))

        for i in range (0,14):
            clearpokemon= QLabel()
            tablewidget.setCellWidget(0,i,clearpokemon)
   
        for i in range (0, len(teamtarget)):
            hpokemon = QLabel()
            pic = QPixmap("../Sources/Sprites/"+str(teamtarget[i]))
            hpokemon.setPixmap(pic)
            tablewidget.setCellWidget(0,5-i,hpokemon)

        for i in range (0, matrixsize):
            result=QLabel(str(round(occurrence_vector[i],0))+"("+str(round(ratio_vector[i],2))+")")
            if ratio_vector[i]>=0.67:
                result.setStyleSheet("background-color: green")
            elif ratio_vector[i]<0.67 and ratio_vector[i]>0.5:
                result.setStyleSheet("background-color: lightgreen")
            elif ratio_vector[i]==0.5:
                result.setStyleSheet("background-color: yellow")
            elif ratio_vector[i]<0.5 and ratio_vector[i]>=0.33:
                result.setStyleSheet("background-color: orange")
            elif ratio_vector[i]<0.5 and ratio_vector[i]<0.33:
                result.setStyleSheet("background-color: red")
            if occurrence_vector[i]==0:
                result.setStyleSheet("background-color: grey")
            tablewidget.setCellWidget(0,i+6,result)

    global current_dictionary
    global enemy_vector
    global enemy_teams
    current_dictionary=lead_dictionary
    enemy_vector=ratio_vector
    enemy_teams=selectedTeams
    print ("lead dictrionary: ", len (lead_dictionary))
    fillLeadTable (lead_dictionary, improvementtablewidget)  


def createLeadsLayout(data):
    LeadsLayout = QVBoxLayout()
    targetteamlayout=QHBoxLayout()
    team1layout=QHBoxLayout()
    team2layout=QHBoxLayout()
    team3layout=QHBoxLayout()
    team4layout=QHBoxLayout()
    team5layout=QHBoxLayout()
    team6layout=QHBoxLayout()
    team7layout=QHBoxLayout()
    team8layout=QHBoxLayout()
    utilitylayout=QHBoxLayout()

    targetteam=[None]*6
    team1=[None]*6
    team2=[None]*6
    team3=[None]*6
    team4=[None]*6
    team5=[None]*6
    team6=[None]*6
    team7=[None]*6
    team8=[None]*6

    pokemon1label=QLabel()
    pokemon1label.setMaximumWidth(40)
    pokemon1text = QLineEdit()
    pokemon1text.textChanged.connect(lambda: setPokemonTeams(pokemon1text.text(), pokemon1label,0,targetteam))
    pokemon2label=QLabel()
    pokemon2label.setMaximumWidth(40)
    pokemon2text = QLineEdit()
    pokemon2text.textChanged.connect(lambda: setPokemonTeams(pokemon2text.text(), pokemon2label,1,targetteam))
    pokemon3label=QLabel()
    pokemon3label.setMaximumWidth(40)
    pokemon3text = QLineEdit()
    pokemon3text.textChanged.connect(lambda: setPokemonTeams(pokemon3text.text(), pokemon3label,2,targetteam))
    pokemon4label=QLabel()
    pokemon4label.setMaximumWidth(40)
    pokemon4text = QLineEdit()
    pokemon4text.textChanged.connect(lambda: setPokemonTeams(pokemon4text.text(), pokemon4label,3,targetteam))
    pokemon5label=QLabel()
    pokemon5label.setMaximumWidth(40)
    pokemon5text = QLineEdit()
    pokemon5text.textChanged.connect(lambda: setPokemonTeams(pokemon5text.text(), pokemon5label,4,targetteam))
    pokemon6label=QLabel()
    pokemon6label.setMaximumWidth(40)
    pokemon6text = QLineEdit()
    pokemon6text.textChanged.connect(lambda: setPokemonTeams(pokemon6text.text(), pokemon6label,5,targetteam))
    targetteamlayout.addWidget(QLabel("Target"))
    targetteamlayout.addWidget(pokemon1label)
    targetteamlayout.addWidget(pokemon1text)
    targetteamlayout.addWidget(pokemon2label)
    targetteamlayout.addWidget(pokemon2text)
    targetteamlayout.addWidget(pokemon3label)
    targetteamlayout.addWidget(pokemon3text)
    targetteamlayout.addWidget(pokemon4label)
    targetteamlayout.addWidget(pokemon4text)
    targetteamlayout.addWidget(pokemon5label)
    targetteamlayout.addWidget(pokemon5text)
    targetteamlayout.addWidget(pokemon6label)
    targetteamlayout.addWidget(pokemon6text)

    pokemon11label=QLabel()
    pokemon11label.setMaximumWidth(40)
    pokemon11text = QLineEdit()
    pokemon11text.textChanged.connect(lambda: setPokemonTeams(pokemon11text.text(), pokemon11label,0,team1))
    pokemon12label=QLabel()
    pokemon12label.setMaximumWidth(40)
    pokemon12text = QLineEdit()
    pokemon12text.textChanged.connect(lambda: setPokemonTeams(pokemon12text.text(), pokemon12label,1,team1))
    pokemon13label=QLabel()
    pokemon13label.setMaximumWidth(40)
    pokemon13text = QLineEdit()
    pokemon13text.textChanged.connect(lambda: setPokemonTeams(pokemon13text.text(), pokemon13label,2,team1))
    pokemon14label=QLabel()
    pokemon14label.setMaximumWidth(40)
    pokemon14text = QLineEdit()
    pokemon14text.textChanged.connect(lambda: setPokemonTeams(pokemon14text.text(), pokemon14label,3,team1))
    pokemon15label=QLabel()
    pokemon15label.setMaximumWidth(40)
    pokemon15text = QLineEdit()
    pokemon15text.textChanged.connect(lambda: setPokemonTeams(pokemon15text.text(), pokemon15label,4,team1))
    pokemon16label=QLabel()
    pokemon16label.setMaximumWidth(40)
    pokemon16text = QLineEdit()
    pokemon16text.textChanged.connect(lambda: setPokemonTeams(pokemon16text.text(), pokemon16label,5,team1))
    team1layout.addWidget(QLabel("Team 1"))
    team1layout.addWidget(pokemon11label)
    team1layout.addWidget(pokemon11text)
    team1layout.addWidget(pokemon12label)
    team1layout.addWidget(pokemon12text)
    team1layout.addWidget(pokemon13label)
    team1layout.addWidget(pokemon13text)
    team1layout.addWidget(pokemon14label)
    team1layout.addWidget(pokemon14text)
    team1layout.addWidget(pokemon15label)
    team1layout.addWidget(pokemon15text)
    team1layout.addWidget(pokemon16label)
    team1layout.addWidget(pokemon16text)

    pokemon21label=QLabel()
    pokemon21label.setMaximumWidth(40)
    pokemon21text = QLineEdit()
    pokemon21text.textChanged.connect(lambda: setPokemonTeams(pokemon21text.text(), pokemon21label,0,team2))
    pokemon22label=QLabel()
    pokemon22label.setMaximumWidth(40)
    pokemon22text = QLineEdit()
    pokemon22text.textChanged.connect(lambda: setPokemonTeams(pokemon22text.text(), pokemon22label,1,team2))
    pokemon23label=QLabel()
    pokemon23label.setMaximumWidth(40)
    pokemon23text = QLineEdit()
    pokemon23text.textChanged.connect(lambda: setPokemonTeams(pokemon23text.text(), pokemon23label,2,team2))
    pokemon24label=QLabel()
    pokemon24label.setMaximumWidth(40)
    pokemon24text = QLineEdit()
    pokemon24text.textChanged.connect(lambda: setPokemonTeams(pokemon24text.text(), pokemon24label,3,team2))
    pokemon25label=QLabel()
    pokemon25label.setMaximumWidth(40)
    pokemon25text = QLineEdit()
    pokemon25text.textChanged.connect(lambda: setPokemonTeams(pokemon25text.text(), pokemon25label,4,team2))
    pokemon26label=QLabel()
    pokemon26label.setMaximumWidth(40)
    pokemon26text = QLineEdit()
    pokemon26text.textChanged.connect(lambda: setPokemonTeams(pokemon26text.text(), pokemon26label,5,team2))
    team2layout.addWidget(QLabel("Team 2"))
    team2layout.addWidget(pokemon21label)
    team2layout.addWidget(pokemon21text)
    team2layout.addWidget(pokemon22label)
    team2layout.addWidget(pokemon22text)
    team2layout.addWidget(pokemon23label)
    team2layout.addWidget(pokemon23text)
    team2layout.addWidget(pokemon24label)
    team2layout.addWidget(pokemon24text)
    team2layout.addWidget(pokemon25label)
    team2layout.addWidget(pokemon25text)
    team2layout.addWidget(pokemon26label)
    team2layout.addWidget(pokemon26text)

    pokemon31label=QLabel()
    pokemon31label.setMaximumWidth(40)
    pokemon31text = QLineEdit()
    pokemon31text.textChanged.connect(lambda: setPokemonTeams(pokemon31text.text(), pokemon31label,0,team3))
    pokemon32label=QLabel()
    pokemon32label.setMaximumWidth(40)
    pokemon32text = QLineEdit()
    pokemon32text.textChanged.connect(lambda: setPokemonTeams(pokemon32text.text(), pokemon32label,1,team3))
    pokemon33label=QLabel()
    pokemon33label.setMaximumWidth(40)
    pokemon33text = QLineEdit()
    pokemon33text.textChanged.connect(lambda: setPokemonTeams(pokemon33text.text(), pokemon33label,2,team3))
    pokemon34label=QLabel()
    pokemon34label.setMaximumWidth(40)
    pokemon34text = QLineEdit()
    pokemon34text.textChanged.connect(lambda: setPokemonTeams(pokemon34text.text(), pokemon34label,3,team3))
    pokemon35label=QLabel()
    pokemon35label.setMaximumWidth(40)
    pokemon35text = QLineEdit()
    pokemon35text.textChanged.connect(lambda: setPokemonTeams(pokemon35text.text(), pokemon35label,4,team3))
    pokemon36label=QLabel()
    pokemon36label.setMaximumWidth(40)
    pokemon36text = QLineEdit()
    pokemon36text.textChanged.connect(lambda: setPokemonTeams(pokemon36text.text(), pokemon36label,5,team3))
    team3layout.addWidget(QLabel("Team 3"))
    team3layout.addWidget(pokemon31label)
    team3layout.addWidget(pokemon31text)
    team3layout.addWidget(pokemon32label)
    team3layout.addWidget(pokemon32text)
    team3layout.addWidget(pokemon33label)
    team3layout.addWidget(pokemon33text)
    team3layout.addWidget(pokemon34label)
    team3layout.addWidget(pokemon34text)
    team3layout.addWidget(pokemon35label)
    team3layout.addWidget(pokemon35text)
    team3layout.addWidget(pokemon36label)
    team3layout.addWidget(pokemon36text)

    pokemon41label=QLabel()
    pokemon41label.setMaximumWidth(40)
    pokemon41text = QLineEdit()
    pokemon41text.textChanged.connect(lambda: setPokemonTeams(pokemon41text.text(), pokemon41label,0,team4))
    pokemon42label=QLabel()
    pokemon42label.setMaximumWidth(40)
    pokemon42text = QLineEdit()
    pokemon42text.textChanged.connect(lambda: setPokemonTeams(pokemon42text.text(), pokemon42label,1,team4))
    pokemon43label=QLabel()
    pokemon43label.setMaximumWidth(40)
    pokemon43text = QLineEdit()
    pokemon43text.textChanged.connect(lambda: setPokemonTeams(pokemon43text.text(), pokemon43label,2,team4))
    pokemon44label=QLabel()
    pokemon44label.setMaximumWidth(40)
    pokemon44text = QLineEdit()
    pokemon44text.textChanged.connect(lambda: setPokemonTeams(pokemon44text.text(), pokemon44label,3,team4))
    pokemon45label=QLabel()
    pokemon45label.setMaximumWidth(40)
    pokemon45text = QLineEdit()
    pokemon45text.textChanged.connect(lambda: setPokemonTeams(pokemon45text.text(), pokemon45label,4,team4))
    pokemon46label=QLabel()
    pokemon46label.setMaximumWidth(40)
    pokemon46text = QLineEdit()
    pokemon46text.textChanged.connect(lambda: setPokemonTeams(pokemon46text.text(), pokemon46label,5,team4))
    team4layout.addWidget(QLabel("Team 4"))
    team4layout.addWidget(pokemon41label)
    team4layout.addWidget(pokemon41text)
    team4layout.addWidget(pokemon42label)
    team4layout.addWidget(pokemon42text)
    team4layout.addWidget(pokemon43label)
    team4layout.addWidget(pokemon43text)
    team4layout.addWidget(pokemon44label)
    team4layout.addWidget(pokemon44text)
    team4layout.addWidget(pokemon45label)
    team4layout.addWidget(pokemon45text)
    team4layout.addWidget(pokemon46label)
    team4layout.addWidget(pokemon46text)

    pokemon51label=QLabel()
    pokemon51label.setMaximumWidth(40)
    pokemon51text = QLineEdit()
    pokemon51text.textChanged.connect(lambda: setPokemonTeams(pokemon51text.text(), pokemon51label,0,team5))
    pokemon52label=QLabel()
    pokemon52label.setMaximumWidth(40)
    pokemon52text = QLineEdit()
    pokemon52text.textChanged.connect(lambda: setPokemonTeams(pokemon52text.text(), pokemon52label,1,team5))
    pokemon53label=QLabel()
    pokemon53label.setMaximumWidth(40)
    pokemon53text = QLineEdit()
    pokemon53text.textChanged.connect(lambda: setPokemonTeams(pokemon53text.text(), pokemon53label,2,team5))
    pokemon54label=QLabel()
    pokemon54label.setMaximumWidth(40)
    pokemon54text = QLineEdit()
    pokemon54text.textChanged.connect(lambda: setPokemonTeams(pokemon54text.text(), pokemon54label,3,team5))
    pokemon55label=QLabel()
    pokemon55label.setMaximumWidth(40)
    pokemon55text = QLineEdit()
    pokemon55text.textChanged.connect(lambda: setPokemonTeams(pokemon55text.text(), pokemon55label,4,team5))
    pokemon56label=QLabel()
    pokemon56label.setMaximumWidth(40)
    pokemon56text = QLineEdit()
    pokemon56text.textChanged.connect(lambda: setPokemonTeams(pokemon56text.text(), pokemon56label,5,team5))
    team5layout.addWidget(QLabel("Team 5"))
    team5layout.addWidget(pokemon51label)
    team5layout.addWidget(pokemon51text)
    team5layout.addWidget(pokemon52label)
    team5layout.addWidget(pokemon52text)
    team5layout.addWidget(pokemon53label)
    team5layout.addWidget(pokemon53text)
    team5layout.addWidget(pokemon54label)
    team5layout.addWidget(pokemon54text)
    team5layout.addWidget(pokemon55label)
    team5layout.addWidget(pokemon55text)
    team5layout.addWidget(pokemon56label)
    team5layout.addWidget(pokemon56text)

    pokemon61label=QLabel()
    pokemon61label.setMaximumWidth(40)
    pokemon61text = QLineEdit()
    pokemon61text.textChanged.connect(lambda: setPokemonTeams(pokemon61text.text(), pokemon61label,0,team6))
    pokemon62label=QLabel()
    pokemon62label.setMaximumWidth(40)
    pokemon62text = QLineEdit()
    pokemon62text.textChanged.connect(lambda: setPokemonTeams(pokemon62text.text(), pokemon62label,1,team6))
    pokemon63label=QLabel()
    pokemon63label.setMaximumWidth(40)
    pokemon63text = QLineEdit()
    pokemon63text.textChanged.connect(lambda: setPokemonTeams(pokemon63text.text(), pokemon63label,2,team6))
    pokemon64label=QLabel()
    pokemon64label.setMaximumWidth(40)
    pokemon64text = QLineEdit()
    pokemon64text.textChanged.connect(lambda: setPokemonTeams(pokemon64text.text(), pokemon64label,3,team6))
    pokemon65label=QLabel()
    pokemon65label.setMaximumWidth(40)
    pokemon65text = QLineEdit()
    pokemon65text.textChanged.connect(lambda: setPokemonTeams(pokemon65text.text(), pokemon65label,4,team6))
    pokemon66label=QLabel()
    pokemon66label.setMaximumWidth(40)
    pokemon66text = QLineEdit()
    pokemon66text.textChanged.connect(lambda: setPokemonTeams(pokemon66text.text(), pokemon66label,5,team6))
    team6layout.addWidget(QLabel("Team 6"))
    team6layout.addWidget(pokemon61label)
    team6layout.addWidget(pokemon61text)
    team6layout.addWidget(pokemon62label)
    team6layout.addWidget(pokemon62text)
    team6layout.addWidget(pokemon63label)
    team6layout.addWidget(pokemon63text)
    team6layout.addWidget(pokemon64label)
    team6layout.addWidget(pokemon64text)
    team6layout.addWidget(pokemon65label)
    team6layout.addWidget(pokemon65text)
    team6layout.addWidget(pokemon66label)
    team6layout.addWidget(pokemon66text)

    pokemon71label=QLabel()
    pokemon71label.setMaximumWidth(40)
    pokemon71text = QLineEdit()
    pokemon71text.textChanged.connect(lambda: setPokemonTeams(pokemon71text.text(), pokemon71label,0,team7))
    pokemon72label=QLabel()
    pokemon72label.setMaximumWidth(40)
    pokemon72text = QLineEdit()
    pokemon72text.textChanged.connect(lambda: setPokemonTeams(pokemon72text.text(), pokemon72label,1,team7))
    pokemon73label=QLabel()
    pokemon73label.setMaximumWidth(40)
    pokemon73text = QLineEdit()
    pokemon73text.textChanged.connect(lambda: setPokemonTeams(pokemon73text.text(), pokemon73label,2,team7))
    pokemon74label=QLabel()
    pokemon74label.setMaximumWidth(40)
    pokemon74text = QLineEdit()
    pokemon74text.textChanged.connect(lambda: setPokemonTeams(pokemon74text.text(), pokemon74label,3,team7))
    pokemon75label=QLabel()
    pokemon75label.setMaximumWidth(40)
    pokemon75text = QLineEdit()
    pokemon75text.textChanged.connect(lambda: setPokemonTeams(pokemon75text.text(), pokemon75label,4,team7))
    pokemon76label=QLabel()
    pokemon76label.setMaximumWidth(40)
    pokemon76text = QLineEdit()
    pokemon76text.textChanged.connect(lambda: setPokemonTeams(pokemon76text.text(), pokemon76label,5,team7))
    team7layout.addWidget(QLabel("Team 7"))
    team7layout.addWidget(pokemon71label)
    team7layout.addWidget(pokemon71text)
    team7layout.addWidget(pokemon72label)
    team7layout.addWidget(pokemon72text)
    team7layout.addWidget(pokemon73label)
    team7layout.addWidget(pokemon73text)
    team7layout.addWidget(pokemon74label)
    team7layout.addWidget(pokemon74text)
    team7layout.addWidget(pokemon75label)
    team7layout.addWidget(pokemon75text)
    team7layout.addWidget(pokemon76label)
    team7layout.addWidget(pokemon76text)

    pokemon81label=QLabel()
    pokemon81label.setMaximumWidth(40)
    pokemon81text = QLineEdit()
    pokemon81text.textChanged.connect(lambda: setPokemonTeams(pokemon81text.text(), pokemon81label,0,team8))
    pokemon82label=QLabel()
    pokemon82label.setMaximumWidth(40)
    pokemon82text = QLineEdit()
    pokemon82text.textChanged.connect(lambda: setPokemonTeams(pokemon82text.text(), pokemon82label,1,team8))
    pokemon83label=QLabel()
    pokemon83label.setMaximumWidth(40)
    pokemon83text = QLineEdit()
    pokemon83text.textChanged.connect(lambda: setPokemonTeams(pokemon83text.text(), pokemon83label,2,team8))
    pokemon84label=QLabel()
    pokemon84label.setMaximumWidth(40)
    pokemon84text = QLineEdit()
    pokemon84text.textChanged.connect(lambda: setPokemonTeams(pokemon84text.text(), pokemon84label,3,team8))
    pokemon85label=QLabel()
    pokemon85label.setMaximumWidth(40)
    pokemon85text = QLineEdit()
    pokemon85text.textChanged.connect(lambda: setPokemonTeams(pokemon85text.text(), pokemon85label,4,team8))
    pokemon86label=QLabel()
    pokemon86label.setMaximumWidth(40)
    pokemon86text = QLineEdit()
    pokemon86text.textChanged.connect(lambda: setPokemonTeams(pokemon86text.text(), pokemon86label,5,team8))
    team8layout.addWidget(QLabel("Team 8"))
    team8layout.addWidget(pokemon81label)
    team8layout.addWidget(pokemon81text)
    team8layout.addWidget(pokemon82label)
    team8layout.addWidget(pokemon82text)
    team8layout.addWidget(pokemon83label)
    team8layout.addWidget(pokemon83text)
    team8layout.addWidget(pokemon84label)
    team8layout.addWidget(pokemon84text)
    team8layout.addWidget(pokemon85label)
    team8layout.addWidget(pokemon85text)
    team8layout.addWidget(pokemon86label)
    team8layout.addWidget(pokemon86text)

    checkteambutton=QPushButton('Check teams')
    checkteambutton.setMaximumHeight(30)
    checkteambutton.setMaximumWidth(80)
    checkteambutton.clicked.connect(lambda: createLeadsMatrix(data, tablewidget, improvementtablewidget, targetteam, team1, team2, team3, team4, team5, team6, team7, team8)) 
    utilitylayout.addWidget(checkteambutton)

    tablewidget=QTableWidget()
    tablewidget.setRowCount(1)
    tablewidget.setColumnCount(14)
    columnnames=["", "", "", "", "", "", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    rownames=["Team"]
    tablewidget.setHorizontalHeaderLabels(columnnames)
    tablewidget.setVerticalHeaderLabels(rownames)
    tablewidget.setColumnWidth(0,40)
    tablewidget.setColumnWidth(1,40)
    tablewidget.setColumnWidth(2,40)
    tablewidget.setColumnWidth(3,40)
    tablewidget.setColumnWidth(4,40)
    tablewidget.setColumnWidth(5,40)
    tablewidget.setColumnWidth(6,80)
    tablewidget.setColumnWidth(7,80)
    tablewidget.setColumnWidth(8,80)
    tablewidget.setColumnWidth(9,80)
    tablewidget.setColumnWidth(10,80)
    tablewidget.setColumnWidth(11,80)
    tablewidget.setColumnWidth(12,80)
    tablewidget.setColumnWidth(13,80)
    tablewidget.setMaximumHeight(70)

    improvementtablewidget=QTableWidget()
    improvementtablewidget.setRowCount(50)
    improvementtablewidget.setColumnCount(11)
    improvementcolumnnames=["P1","P2","Lead", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    improvementtablewidget.setHorizontalHeaderLabels(improvementcolumnnames)
    improvementtablewidget.setColumnWidth(0,40)
    improvementtablewidget.setColumnWidth(1,40)
    improvementtablewidget.setColumnWidth(2,150)
    improvementtablewidget.setColumnWidth(3,80)
    improvementtablewidget.setColumnWidth(4,80)
    improvementtablewidget.setColumnWidth(5,80)
    improvementtablewidget.setColumnWidth(6,80)
    improvementtablewidget.setColumnWidth(7,80)
    improvementtablewidget.setColumnWidth(8,80)
    improvementtablewidget.setColumnWidth(9,80)
    improvementtablewidget.setColumnWidth(10,80)

    teamsLayout=QVBoxLayout()
    teamsWidget=QWidget()
    teamsWidget.setMaximumHeight(320)
    teamsLayout.addLayout(targetteamlayout)
    teamsLayout.addLayout(team1layout)
    teamsLayout.addLayout(team2layout)
    teamsLayout.addLayout(team3layout)
    teamsLayout.addLayout(team4layout)
    teamsLayout.addLayout(team5layout)
    teamsLayout.addLayout(team6layout)
    teamsLayout.addLayout(team7layout)
    teamsLayout.addLayout(team8layout)
    teamsLayout.addLayout(utilitylayout)
    teamsWidget.setLayout(teamsLayout)

    global current_dictionary
    buttonlayout=QHBoxLayout()
    previousbutton=QPushButton('Previous page')
    previousbutton.setMaximumHeight(30)   
    previousbutton.setMaximumWidth(120)
    previousbutton.clicked.connect(lambda: loadPreviousPageImpr(improvementtablewidget)) 
    buttonlayout.addWidget(previousbutton)
    nextbutton=QPushButton('Next page')
    nextbutton.setMaximumHeight(30)   
    nextbutton.setMaximumWidth(120) 
    nextbutton.clicked.connect(lambda: loadNextPageImpr(improvementtablewidget)) 
    buttonlayout.addWidget(nextbutton)

    LeadsLayout.addWidget(teamsWidget)
    LeadsLayout.addWidget(tablewidget)
    LeadsLayout.addWidget(improvementtablewidget)
    LeadsLayout.addLayout(buttonlayout)

    return LeadsLayout

Back_page = 1 
Back_list = []

def fillBackTable (Back_dictionary, improvementtablewidget) : 
    global enemy_teams
    global Back_page
    global Back_list
    index=0

    for i in range (0,14):
        for j in range (0,50):
            clearpokemon= QLabel()
            improvementtablewidget.setCellWidget(j,i,clearpokemon)

    for element in Back_list:
        if index >= (Back_page-1)*50 and index < len(Back_dictionary) and index < Back_page*50 :
            impindex=index-(Back_page-1)*50
            hpokemon1 = QLabel()
            hpokemon2 = QLabel()
            el_Back=element.split("_")
            pic1 = QPixmap("../Sources/Sprites/"+str(el_Back[0]))
            hpokemon1.setPixmap(pic1)
            pic2 = QPixmap("../Sources/Sprites/"+str(el_Back[1]))
            hpokemon2.setPixmap(pic2)
            improvementtablewidget.setCellWidget(impindex,0,hpokemon1)
            improvementtablewidget.setCellWidget(impindex,1,hpokemon2)
            el_Back
            improvementtablewidget.setCellWidget(impindex,2,QLabel(str(element)))
            for i in range (0, len(enemy_teams)):
                result=QLabel(str(round(Back_dictionary[element][i][0],0))+"("+str(round(Back_dictionary[element][i][2],2))+")")
                if Back_dictionary[element][i][0]==0:
                    result.setStyleSheet("background-color: grey")
                elif Back_dictionary[element][i][2] >= enemy_vector[i] + 0.05:
                    result.setStyleSheet("background-color: green")
                elif Back_dictionary[element][i][2] < enemy_vector[i] + 0.05 and Back_dictionary[element][i][2] > enemy_vector[i] - 0.05 :
                    result.setStyleSheet("background-color: yellow")
                elif Back_dictionary[element][i][2] <= enemy_vector[i] - 0.05:
                    result.setStyleSheet("background-color: red")
                improvementtablewidget.setCellWidget(impindex,i+3,result)
        index+=1



def add_Back_statistics(match, team, teamtarget, did_win, Back_dictionary, opponent_index) :
    Back = []
    global Back_list
    key = ""
    if team == 0 :
        Back = match["players"][0]["player1_back"]
    else :
        Back = match["players"][1]["player2_back"]

    if len(Back)==2:
        if Back[0]<Back[1]:
            key = Back[0]+"_"+Back[1]
        else:
            key = Back[1]+"_"+Back[0]

        if key not in Back_dictionary:
            Back_dictionary[key]=numpy.zeros((8,3))
            Back_list.append(key)
        Back_dictionary[key][opponent_index][0]+=1
        if did_win == 1:
            Back_dictionary[key][opponent_index][1]+=1
            Back_wins=Back_dictionary[key][opponent_index][1]
            Back_occurrency=Back_dictionary[key][opponent_index][0]
            Back_dictionary[key][opponent_index][2]=float(Back_wins/Back_occurrency)


def createBacksMatrix(data, tablewidget, improvementtablewidget, teamtarget, team1, team2, team3, team4, team5, team6, team7, team8):
    global Back_page
    Back_page=1
    selectedTeams=[]
    Back_dictionary={}

    teamtarget = list(filter(None, teamtarget)) 

    team1 = list(filter(None, team1)) 
    if len(team1)>0:
        selectedTeams.append(team1)
    team2 = list(filter(None, team2)) 
    if len(team2)>0:
        selectedTeams.append(team2)
    team3 = list(filter(None, team3)) 
    if len(team3)>0:
        selectedTeams.append(team3)
    team4 = list(filter(None, team4)) 
    if len(team4)>0:
        selectedTeams.append(team4)
    team5 = list(filter(None, team5))
    if len(team5)>0:
        selectedTeams.append(team5) 
    team6 = list(filter(None, team6)) 
    if len(team6)>0:
        selectedTeams.append(team6)
    team7 = list(filter(None, team7)) 
    if len(team7)>0:
        selectedTeams.append(team7)
    team8 = list(filter(None, team8)) 
    if len(team8)>0:
        selectedTeams.append(team8)

    matrixsize = len(selectedTeams)

    if (matrixsize>0):

        win_vector = numpy.zeros(matrixsize)
        ratio_vector = numpy.zeros(matrixsize)
        occurrence_vector = numpy.zeros(matrixsize)

        for match in data:
            if set(teamtarget).issubset(set(match["players"][0]["player1_team"])):
                for i in range(0,matrixsize):
                    if set(selectedTeams[i]).issubset(set(match["players"][1]["player2_team"])):
                        occurrence_vector[i]+=1
                        if (match["players"][0]["player1_name"] == match["winner"]):
                            add_Back_statistics(match, 0, teamtarget, 1, Back_dictionary, i)
                            win_vector[i]+=1            
                        else :
                            add_Back_statistics(match, 0, teamtarget, 0, Back_dictionary, i) 
            if set(teamtarget).issubset(set(match["players"][1]["player2_team"])):
                for i in range(0,matrixsize):
                    if set(selectedTeams[i]).issubset(set(match["players"][0]["player1_team"])):
                        occurrence_vector[i]+=1
                        if (match["players"][1]["player2_name"] == match["winner"]):
                            add_Back_statistics(match, 1, teamtarget, 1, Back_dictionary, i)
                            win_vector[i]+=1
                        else :
                            add_Back_statistics(match, 1, teamtarget, 0, Back_dictionary, i)  

        for i in range (0, matrixsize):
            if float(occurrence_vector[i])==0 :
                ratio_vector[i]=0
            else :
                ratio_vector[i]=float(win_vector[i]/(occurrence_vector[i]))

        for i in range (0,14):
            clearpokemon= QLabel()
            tablewidget.setCellWidget(0,i,clearpokemon)
   
        for i in range (0, len(teamtarget)):
            hpokemon = QLabel()
            pic = QPixmap("../Sources/Sprites/"+str(teamtarget[i]))
            hpokemon.setPixmap(pic)
            tablewidget.setCellWidget(0,5-i,hpokemon)

        for i in range (0, matrixsize):
            result=QLabel(str(round(occurrence_vector[i],0))+"("+str(round(ratio_vector[i],2))+")")
            if ratio_vector[i]>=0.67:
                result.setStyleSheet("background-color: green")
            elif ratio_vector[i]<0.67 and ratio_vector[i]>0.5:
                result.setStyleSheet("background-color: lightgreen")
            elif ratio_vector[i]==0.5:
                result.setStyleSheet("background-color: yellow")
            elif ratio_vector[i]<0.5 and ratio_vector[i]>=0.33:
                result.setStyleSheet("background-color: orange")
            elif ratio_vector[i]<0.5 and ratio_vector[i]<0.33:
                result.setStyleSheet("background-color: red")
            if occurrence_vector[i]==0:
                result.setStyleSheet("background-color: grey")
            tablewidget.setCellWidget(0,i+6,result)

    global current_dictionary
    global enemy_vector
    global enemy_teams
    current_dictionary=Back_dictionary
    enemy_vector=ratio_vector
    enemy_teams=selectedTeams
    fillBackTable (Back_dictionary, improvementtablewidget)  


def createBacksLayout(data):
    BacksLayout = QVBoxLayout()
    targetteamlayout=QHBoxLayout()
    team1layout=QHBoxLayout()
    team2layout=QHBoxLayout()
    team3layout=QHBoxLayout()
    team4layout=QHBoxLayout()
    team5layout=QHBoxLayout()
    team6layout=QHBoxLayout()
    team7layout=QHBoxLayout()
    team8layout=QHBoxLayout()
    utilitylayout=QHBoxLayout()

    targetteam=[None]*6
    team1=[None]*6
    team2=[None]*6
    team3=[None]*6
    team4=[None]*6
    team5=[None]*6
    team6=[None]*6
    team7=[None]*6
    team8=[None]*6

    pokemon1label=QLabel()
    pokemon1label.setMaximumWidth(40)
    pokemon1text = QLineEdit()
    pokemon1text.textChanged.connect(lambda: setPokemonTeams(pokemon1text.text(), pokemon1label,0,targetteam))
    pokemon2label=QLabel()
    pokemon2label.setMaximumWidth(40)
    pokemon2text = QLineEdit()
    pokemon2text.textChanged.connect(lambda: setPokemonTeams(pokemon2text.text(), pokemon2label,1,targetteam))
    pokemon3label=QLabel()
    pokemon3label.setMaximumWidth(40)
    pokemon3text = QLineEdit()
    pokemon3text.textChanged.connect(lambda: setPokemonTeams(pokemon3text.text(), pokemon3label,2,targetteam))
    pokemon4label=QLabel()
    pokemon4label.setMaximumWidth(40)
    pokemon4text = QLineEdit()
    pokemon4text.textChanged.connect(lambda: setPokemonTeams(pokemon4text.text(), pokemon4label,3,targetteam))
    pokemon5label=QLabel()
    pokemon5label.setMaximumWidth(40)
    pokemon5text = QLineEdit()
    pokemon5text.textChanged.connect(lambda: setPokemonTeams(pokemon5text.text(), pokemon5label,4,targetteam))
    pokemon6label=QLabel()
    pokemon6label.setMaximumWidth(40)
    pokemon6text = QLineEdit()
    pokemon6text.textChanged.connect(lambda: setPokemonTeams(pokemon6text.text(), pokemon6label,5,targetteam))
    targetteamlayout.addWidget(QLabel("Target"))
    targetteamlayout.addWidget(pokemon1label)
    targetteamlayout.addWidget(pokemon1text)
    targetteamlayout.addWidget(pokemon2label)
    targetteamlayout.addWidget(pokemon2text)
    targetteamlayout.addWidget(pokemon3label)
    targetteamlayout.addWidget(pokemon3text)
    targetteamlayout.addWidget(pokemon4label)
    targetteamlayout.addWidget(pokemon4text)
    targetteamlayout.addWidget(pokemon5label)
    targetteamlayout.addWidget(pokemon5text)
    targetteamlayout.addWidget(pokemon6label)
    targetteamlayout.addWidget(pokemon6text)

    pokemon11label=QLabel()
    pokemon11label.setMaximumWidth(40)
    pokemon11text = QLineEdit()
    pokemon11text.textChanged.connect(lambda: setPokemonTeams(pokemon11text.text(), pokemon11label,0,team1))
    pokemon12label=QLabel()
    pokemon12label.setMaximumWidth(40)
    pokemon12text = QLineEdit()
    pokemon12text.textChanged.connect(lambda: setPokemonTeams(pokemon12text.text(), pokemon12label,1,team1))
    pokemon13label=QLabel()
    pokemon13label.setMaximumWidth(40)
    pokemon13text = QLineEdit()
    pokemon13text.textChanged.connect(lambda: setPokemonTeams(pokemon13text.text(), pokemon13label,2,team1))
    pokemon14label=QLabel()
    pokemon14label.setMaximumWidth(40)
    pokemon14text = QLineEdit()
    pokemon14text.textChanged.connect(lambda: setPokemonTeams(pokemon14text.text(), pokemon14label,3,team1))
    pokemon15label=QLabel()
    pokemon15label.setMaximumWidth(40)
    pokemon15text = QLineEdit()
    pokemon15text.textChanged.connect(lambda: setPokemonTeams(pokemon15text.text(), pokemon15label,4,team1))
    pokemon16label=QLabel()
    pokemon16label.setMaximumWidth(40)
    pokemon16text = QLineEdit()
    pokemon16text.textChanged.connect(lambda: setPokemonTeams(pokemon16text.text(), pokemon16label,5,team1))
    team1layout.addWidget(QLabel("Team 1"))
    team1layout.addWidget(pokemon11label)
    team1layout.addWidget(pokemon11text)
    team1layout.addWidget(pokemon12label)
    team1layout.addWidget(pokemon12text)
    team1layout.addWidget(pokemon13label)
    team1layout.addWidget(pokemon13text)
    team1layout.addWidget(pokemon14label)
    team1layout.addWidget(pokemon14text)
    team1layout.addWidget(pokemon15label)
    team1layout.addWidget(pokemon15text)
    team1layout.addWidget(pokemon16label)
    team1layout.addWidget(pokemon16text)

    pokemon21label=QLabel()
    pokemon21label.setMaximumWidth(40)
    pokemon21text = QLineEdit()
    pokemon21text.textChanged.connect(lambda: setPokemonTeams(pokemon21text.text(), pokemon21label,0,team2))
    pokemon22label=QLabel()
    pokemon22label.setMaximumWidth(40)
    pokemon22text = QLineEdit()
    pokemon22text.textChanged.connect(lambda: setPokemonTeams(pokemon22text.text(), pokemon22label,1,team2))
    pokemon23label=QLabel()
    pokemon23label.setMaximumWidth(40)
    pokemon23text = QLineEdit()
    pokemon23text.textChanged.connect(lambda: setPokemonTeams(pokemon23text.text(), pokemon23label,2,team2))
    pokemon24label=QLabel()
    pokemon24label.setMaximumWidth(40)
    pokemon24text = QLineEdit()
    pokemon24text.textChanged.connect(lambda: setPokemonTeams(pokemon24text.text(), pokemon24label,3,team2))
    pokemon25label=QLabel()
    pokemon25label.setMaximumWidth(40)
    pokemon25text = QLineEdit()
    pokemon25text.textChanged.connect(lambda: setPokemonTeams(pokemon25text.text(), pokemon25label,4,team2))
    pokemon26label=QLabel()
    pokemon26label.setMaximumWidth(40)
    pokemon26text = QLineEdit()
    pokemon26text.textChanged.connect(lambda: setPokemonTeams(pokemon26text.text(), pokemon26label,5,team2))
    team2layout.addWidget(QLabel("Team 2"))
    team2layout.addWidget(pokemon21label)
    team2layout.addWidget(pokemon21text)
    team2layout.addWidget(pokemon22label)
    team2layout.addWidget(pokemon22text)
    team2layout.addWidget(pokemon23label)
    team2layout.addWidget(pokemon23text)
    team2layout.addWidget(pokemon24label)
    team2layout.addWidget(pokemon24text)
    team2layout.addWidget(pokemon25label)
    team2layout.addWidget(pokemon25text)
    team2layout.addWidget(pokemon26label)
    team2layout.addWidget(pokemon26text)

    pokemon31label=QLabel()
    pokemon31label.setMaximumWidth(40)
    pokemon31text = QLineEdit()
    pokemon31text.textChanged.connect(lambda: setPokemonTeams(pokemon31text.text(), pokemon31label,0,team3))
    pokemon32label=QLabel()
    pokemon32label.setMaximumWidth(40)
    pokemon32text = QLineEdit()
    pokemon32text.textChanged.connect(lambda: setPokemonTeams(pokemon32text.text(), pokemon32label,1,team3))
    pokemon33label=QLabel()
    pokemon33label.setMaximumWidth(40)
    pokemon33text = QLineEdit()
    pokemon33text.textChanged.connect(lambda: setPokemonTeams(pokemon33text.text(), pokemon33label,2,team3))
    pokemon34label=QLabel()
    pokemon34label.setMaximumWidth(40)
    pokemon34text = QLineEdit()
    pokemon34text.textChanged.connect(lambda: setPokemonTeams(pokemon34text.text(), pokemon34label,3,team3))
    pokemon35label=QLabel()
    pokemon35label.setMaximumWidth(40)
    pokemon35text = QLineEdit()
    pokemon35text.textChanged.connect(lambda: setPokemonTeams(pokemon35text.text(), pokemon35label,4,team3))
    pokemon36label=QLabel()
    pokemon36label.setMaximumWidth(40)
    pokemon36text = QLineEdit()
    pokemon36text.textChanged.connect(lambda: setPokemonTeams(pokemon36text.text(), pokemon36label,5,team3))
    team3layout.addWidget(QLabel("Team 3"))
    team3layout.addWidget(pokemon31label)
    team3layout.addWidget(pokemon31text)
    team3layout.addWidget(pokemon32label)
    team3layout.addWidget(pokemon32text)
    team3layout.addWidget(pokemon33label)
    team3layout.addWidget(pokemon33text)
    team3layout.addWidget(pokemon34label)
    team3layout.addWidget(pokemon34text)
    team3layout.addWidget(pokemon35label)
    team3layout.addWidget(pokemon35text)
    team3layout.addWidget(pokemon36label)
    team3layout.addWidget(pokemon36text)

    pokemon41label=QLabel()
    pokemon41label.setMaximumWidth(40)
    pokemon41text = QLineEdit()
    pokemon41text.textChanged.connect(lambda: setPokemonTeams(pokemon41text.text(), pokemon41label,0,team4))
    pokemon42label=QLabel()
    pokemon42label.setMaximumWidth(40)
    pokemon42text = QLineEdit()
    pokemon42text.textChanged.connect(lambda: setPokemonTeams(pokemon42text.text(), pokemon42label,1,team4))
    pokemon43label=QLabel()
    pokemon43label.setMaximumWidth(40)
    pokemon43text = QLineEdit()
    pokemon43text.textChanged.connect(lambda: setPokemonTeams(pokemon43text.text(), pokemon43label,2,team4))
    pokemon44label=QLabel()
    pokemon44label.setMaximumWidth(40)
    pokemon44text = QLineEdit()
    pokemon44text.textChanged.connect(lambda: setPokemonTeams(pokemon44text.text(), pokemon44label,3,team4))
    pokemon45label=QLabel()
    pokemon45label.setMaximumWidth(40)
    pokemon45text = QLineEdit()
    pokemon45text.textChanged.connect(lambda: setPokemonTeams(pokemon45text.text(), pokemon45label,4,team4))
    pokemon46label=QLabel()
    pokemon46label.setMaximumWidth(40)
    pokemon46text = QLineEdit()
    pokemon46text.textChanged.connect(lambda: setPokemonTeams(pokemon46text.text(), pokemon46label,5,team4))
    team4layout.addWidget(QLabel("Team 4"))
    team4layout.addWidget(pokemon41label)
    team4layout.addWidget(pokemon41text)
    team4layout.addWidget(pokemon42label)
    team4layout.addWidget(pokemon42text)
    team4layout.addWidget(pokemon43label)
    team4layout.addWidget(pokemon43text)
    team4layout.addWidget(pokemon44label)
    team4layout.addWidget(pokemon44text)
    team4layout.addWidget(pokemon45label)
    team4layout.addWidget(pokemon45text)
    team4layout.addWidget(pokemon46label)
    team4layout.addWidget(pokemon46text)

    pokemon51label=QLabel()
    pokemon51label.setMaximumWidth(40)
    pokemon51text = QLineEdit()
    pokemon51text.textChanged.connect(lambda: setPokemonTeams(pokemon51text.text(), pokemon51label,0,team5))
    pokemon52label=QLabel()
    pokemon52label.setMaximumWidth(40)
    pokemon52text = QLineEdit()
    pokemon52text.textChanged.connect(lambda: setPokemonTeams(pokemon52text.text(), pokemon52label,1,team5))
    pokemon53label=QLabel()
    pokemon53label.setMaximumWidth(40)
    pokemon53text = QLineEdit()
    pokemon53text.textChanged.connect(lambda: setPokemonTeams(pokemon53text.text(), pokemon53label,2,team5))
    pokemon54label=QLabel()
    pokemon54label.setMaximumWidth(40)
    pokemon54text = QLineEdit()
    pokemon54text.textChanged.connect(lambda: setPokemonTeams(pokemon54text.text(), pokemon54label,3,team5))
    pokemon55label=QLabel()
    pokemon55label.setMaximumWidth(40)
    pokemon55text = QLineEdit()
    pokemon55text.textChanged.connect(lambda: setPokemonTeams(pokemon55text.text(), pokemon55label,4,team5))
    pokemon56label=QLabel()
    pokemon56label.setMaximumWidth(40)
    pokemon56text = QLineEdit()
    pokemon56text.textChanged.connect(lambda: setPokemonTeams(pokemon56text.text(), pokemon56label,5,team5))
    team5layout.addWidget(QLabel("Team 5"))
    team5layout.addWidget(pokemon51label)
    team5layout.addWidget(pokemon51text)
    team5layout.addWidget(pokemon52label)
    team5layout.addWidget(pokemon52text)
    team5layout.addWidget(pokemon53label)
    team5layout.addWidget(pokemon53text)
    team5layout.addWidget(pokemon54label)
    team5layout.addWidget(pokemon54text)
    team5layout.addWidget(pokemon55label)
    team5layout.addWidget(pokemon55text)
    team5layout.addWidget(pokemon56label)
    team5layout.addWidget(pokemon56text)

    pokemon61label=QLabel()
    pokemon61label.setMaximumWidth(40)
    pokemon61text = QLineEdit()
    pokemon61text.textChanged.connect(lambda: setPokemonTeams(pokemon61text.text(), pokemon61label,0,team6))
    pokemon62label=QLabel()
    pokemon62label.setMaximumWidth(40)
    pokemon62text = QLineEdit()
    pokemon62text.textChanged.connect(lambda: setPokemonTeams(pokemon62text.text(), pokemon62label,1,team6))
    pokemon63label=QLabel()
    pokemon63label.setMaximumWidth(40)
    pokemon63text = QLineEdit()
    pokemon63text.textChanged.connect(lambda: setPokemonTeams(pokemon63text.text(), pokemon63label,2,team6))
    pokemon64label=QLabel()
    pokemon64label.setMaximumWidth(40)
    pokemon64text = QLineEdit()
    pokemon64text.textChanged.connect(lambda: setPokemonTeams(pokemon64text.text(), pokemon64label,3,team6))
    pokemon65label=QLabel()
    pokemon65label.setMaximumWidth(40)
    pokemon65text = QLineEdit()
    pokemon65text.textChanged.connect(lambda: setPokemonTeams(pokemon65text.text(), pokemon65label,4,team6))
    pokemon66label=QLabel()
    pokemon66label.setMaximumWidth(40)
    pokemon66text = QLineEdit()
    pokemon66text.textChanged.connect(lambda: setPokemonTeams(pokemon66text.text(), pokemon66label,5,team6))
    team6layout.addWidget(QLabel("Team 6"))
    team6layout.addWidget(pokemon61label)
    team6layout.addWidget(pokemon61text)
    team6layout.addWidget(pokemon62label)
    team6layout.addWidget(pokemon62text)
    team6layout.addWidget(pokemon63label)
    team6layout.addWidget(pokemon63text)
    team6layout.addWidget(pokemon64label)
    team6layout.addWidget(pokemon64text)
    team6layout.addWidget(pokemon65label)
    team6layout.addWidget(pokemon65text)
    team6layout.addWidget(pokemon66label)
    team6layout.addWidget(pokemon66text)

    pokemon71label=QLabel()
    pokemon71label.setMaximumWidth(40)
    pokemon71text = QLineEdit()
    pokemon71text.textChanged.connect(lambda: setPokemonTeams(pokemon71text.text(), pokemon71label,0,team7))
    pokemon72label=QLabel()
    pokemon72label.setMaximumWidth(40)
    pokemon72text = QLineEdit()
    pokemon72text.textChanged.connect(lambda: setPokemonTeams(pokemon72text.text(), pokemon72label,1,team7))
    pokemon73label=QLabel()
    pokemon73label.setMaximumWidth(40)
    pokemon73text = QLineEdit()
    pokemon73text.textChanged.connect(lambda: setPokemonTeams(pokemon73text.text(), pokemon73label,2,team7))
    pokemon74label=QLabel()
    pokemon74label.setMaximumWidth(40)
    pokemon74text = QLineEdit()
    pokemon74text.textChanged.connect(lambda: setPokemonTeams(pokemon74text.text(), pokemon74label,3,team7))
    pokemon75label=QLabel()
    pokemon75label.setMaximumWidth(40)
    pokemon75text = QLineEdit()
    pokemon75text.textChanged.connect(lambda: setPokemonTeams(pokemon75text.text(), pokemon75label,4,team7))
    pokemon76label=QLabel()
    pokemon76label.setMaximumWidth(40)
    pokemon76text = QLineEdit()
    pokemon76text.textChanged.connect(lambda: setPokemonTeams(pokemon76text.text(), pokemon76label,5,team7))
    team7layout.addWidget(QLabel("Team 7"))
    team7layout.addWidget(pokemon71label)
    team7layout.addWidget(pokemon71text)
    team7layout.addWidget(pokemon72label)
    team7layout.addWidget(pokemon72text)
    team7layout.addWidget(pokemon73label)
    team7layout.addWidget(pokemon73text)
    team7layout.addWidget(pokemon74label)
    team7layout.addWidget(pokemon74text)
    team7layout.addWidget(pokemon75label)
    team7layout.addWidget(pokemon75text)
    team7layout.addWidget(pokemon76label)
    team7layout.addWidget(pokemon76text)

    pokemon81label=QLabel()
    pokemon81label.setMaximumWidth(40)
    pokemon81text = QLineEdit()
    pokemon81text.textChanged.connect(lambda: setPokemonTeams(pokemon81text.text(), pokemon81label,0,team8))
    pokemon82label=QLabel()
    pokemon82label.setMaximumWidth(40)
    pokemon82text = QLineEdit()
    pokemon82text.textChanged.connect(lambda: setPokemonTeams(pokemon82text.text(), pokemon82label,1,team8))
    pokemon83label=QLabel()
    pokemon83label.setMaximumWidth(40)
    pokemon83text = QLineEdit()
    pokemon83text.textChanged.connect(lambda: setPokemonTeams(pokemon83text.text(), pokemon83label,2,team8))
    pokemon84label=QLabel()
    pokemon84label.setMaximumWidth(40)
    pokemon84text = QLineEdit()
    pokemon84text.textChanged.connect(lambda: setPokemonTeams(pokemon84text.text(), pokemon84label,3,team8))
    pokemon85label=QLabel()
    pokemon85label.setMaximumWidth(40)
    pokemon85text = QLineEdit()
    pokemon85text.textChanged.connect(lambda: setPokemonTeams(pokemon85text.text(), pokemon85label,4,team8))
    pokemon86label=QLabel()
    pokemon86label.setMaximumWidth(40)
    pokemon86text = QLineEdit()
    pokemon86text.textChanged.connect(lambda: setPokemonTeams(pokemon86text.text(), pokemon86label,5,team8))
    team8layout.addWidget(QLabel("Team 8"))
    team8layout.addWidget(pokemon81label)
    team8layout.addWidget(pokemon81text)
    team8layout.addWidget(pokemon82label)
    team8layout.addWidget(pokemon82text)
    team8layout.addWidget(pokemon83label)
    team8layout.addWidget(pokemon83text)
    team8layout.addWidget(pokemon84label)
    team8layout.addWidget(pokemon84text)
    team8layout.addWidget(pokemon85label)
    team8layout.addWidget(pokemon85text)
    team8layout.addWidget(pokemon86label)
    team8layout.addWidget(pokemon86text)

    checkteambutton=QPushButton('Check teams')
    checkteambutton.setMaximumHeight(30)
    checkteambutton.setMaximumWidth(80)
    checkteambutton.clicked.connect(lambda: createBacksMatrix(data, tablewidget, improvementtablewidget, targetteam, team1, team2, team3, team4, team5, team6, team7, team8)) 
    utilitylayout.addWidget(checkteambutton)

    tablewidget=QTableWidget()
    tablewidget.setRowCount(1)
    tablewidget.setColumnCount(14)
    columnnames=["", "", "", "", "", "", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    rownames=["Team"]
    tablewidget.setHorizontalHeaderLabels(columnnames)
    tablewidget.setVerticalHeaderLabels(rownames)
    tablewidget.setColumnWidth(0,40)
    tablewidget.setColumnWidth(1,40)
    tablewidget.setColumnWidth(2,40)
    tablewidget.setColumnWidth(3,40)
    tablewidget.setColumnWidth(4,40)
    tablewidget.setColumnWidth(5,40)
    tablewidget.setColumnWidth(6,80)
    tablewidget.setColumnWidth(7,80)
    tablewidget.setColumnWidth(8,80)
    tablewidget.setColumnWidth(9,80)
    tablewidget.setColumnWidth(10,80)
    tablewidget.setColumnWidth(11,80)
    tablewidget.setColumnWidth(12,80)
    tablewidget.setColumnWidth(13,80)
    tablewidget.setMaximumHeight(70)

    improvementtablewidget=QTableWidget()
    improvementtablewidget.setRowCount(50)
    improvementtablewidget.setColumnCount(11)
    improvementcolumnnames=["P1","P2","Back", "Team 1", "Team 2","Team 3","Team 4","Team 5","Team 6","Team 7","Team 8"]
    improvementtablewidget.setHorizontalHeaderLabels(improvementcolumnnames)
    improvementtablewidget.setColumnWidth(0,40)
    improvementtablewidget.setColumnWidth(1,40)
    improvementtablewidget.setColumnWidth(2,150)
    improvementtablewidget.setColumnWidth(3,80)
    improvementtablewidget.setColumnWidth(4,80)
    improvementtablewidget.setColumnWidth(5,80)
    improvementtablewidget.setColumnWidth(6,80)
    improvementtablewidget.setColumnWidth(7,80)
    improvementtablewidget.setColumnWidth(8,80)
    improvementtablewidget.setColumnWidth(9,80)
    improvementtablewidget.setColumnWidth(10,80)

    teamsLayout=QVBoxLayout()
    teamsWidget=QWidget()
    teamsWidget.setMaximumHeight(320)
    teamsLayout.addLayout(targetteamlayout)
    teamsLayout.addLayout(team1layout)
    teamsLayout.addLayout(team2layout)
    teamsLayout.addLayout(team3layout)
    teamsLayout.addLayout(team4layout)
    teamsLayout.addLayout(team5layout)
    teamsLayout.addLayout(team6layout)
    teamsLayout.addLayout(team7layout)
    teamsLayout.addLayout(team8layout)
    teamsLayout.addLayout(utilitylayout)
    teamsWidget.setLayout(teamsLayout)

    global current_dictionary
    buttonlayout=QHBoxLayout()
    previousbutton=QPushButton('Previous page')
    previousbutton.setMaximumHeight(30)   
    previousbutton.setMaximumWidth(120)
    previousbutton.clicked.connect(lambda: loadPreviousPageImpr(improvementtablewidget)) 
    buttonlayout.addWidget(previousbutton)
    nextbutton=QPushButton('Next page')
    nextbutton.setMaximumHeight(30)   
    nextbutton.setMaximumWidth(120) 
    nextbutton.clicked.connect(lambda: loadNextPageImpr(improvementtablewidget)) 
    buttonlayout.addWidget(nextbutton)

    BacksLayout.addWidget(teamsWidget)
    BacksLayout.addWidget(tablewidget)
    BacksLayout.addWidget(improvementtablewidget)
    BacksLayout.addLayout(buttonlayout)

    return BacksLayout