import json
import numpy
import sys

#opponent_vector = [["Kyogre", "Tornadus"],["Groudon", "Venusaur", "Charizard"],["Calyrex-Ice", "Mimikyu"], ["Calyrex-Shadow"], ["Zacian"], ["Regigigas", "Weezing"],["Palkia"],["Dialga"],["Spectrier","Solgaleo"],["Zacian", "Blastoise"]]
opponent_vector=[["Zacian","Kyogre"],["Kyogre","Calyrex-Ice"],["Zacian","Calyrex-Shadow"],["Kyogre","Calyrex-Shadow"],["Zacian","Groudon"],["Groudon","Yveltal"],["Groudon","Calyrex-Shadow"],["Zacian","Yveltal"],["Solgaleo","Kyogre"],["Palkia","Zacian"],["Dialga","Zacian"],["Dialga","Kyogre"],["Kyurem-White","Zacian"],["Kyurem-White","Kyogre"],["Rayquaza","Zacian"],["Calyrex-Shadow", "Solgaleo"]]

team_array = ["Zacian","Kyogre"]
metagame="gen8vgc2022"
json_path="../Database/sd_"+metagame+".json"
mate_dictionary = {}

teams_with = []


def add_mate_statistics(match, team, did_win, size, opponent_index) :
    elements = []
    if team == 0 :
        elements = match["players"][0]["player1_lead"] + match["players"][0]["player1_back"]
    else :
        elements = match["players"][1]["player2_lead"] + match["players"][1]["player2_back"] 
        
    for element in elements:
        if element not in team_array:
            if element not in mate_dictionary:
                mate_dictionary[element]=numpy.zeros((size,2))
            mate_dictionary[element][opponent_index][0]+=1
            if did_win == 1:
                mate_dictionary[element][opponent_index][1]+=1
                
def construct_statistics(data,size):
    win_vector = numpy.zeros(size)
    occurrence_vector = numpy.zeros(size)

    if (len(team_array)==0):
        print("please, insert a target")
        exit()

    for match in data:
        if set(team_array).issubset(set(match["players"][0]["player1_team"])):
            teams_with.append(match["players"][0]["player1_team"])
            for i in range(0,size):
                if set(opponent_vector[i]).issubset(set(match["players"][1]["player2_team"])):
                    occurrence_vector[i]+=1
                    if (match["players"][0]["player1_name"] == match["winner"]):
                        add_mate_statistics(match, 0, 1, size, i)
                        win_vector[i]+=1
                    else :
                        add_mate_statistics(match, 0, 0, size, i) 

        if set(team_array).issubset(set(match["players"][1]["player2_team"])):
            teams_with.append(match["players"][1]["player2_team"])
            for i in range(0,size):
                if set(opponent_vector[i]).issubset(set(match["players"][0]["player1_team"])):
                    occurrence_vector[i]+=1
                    if (match["players"][1]["player2_name"] == match["winner"]):
                        add_mate_statistics(match, 1, 1, size, i)
                        win_vector[i]+=1
                    else :
                        add_mate_statistics(match, 1, 0, size, i)
        
    for i in range(0,size):
        print (opponent_vector[i]," : ", int(occurrence_vector[i])," (",float(win_vector[i]/occurrence_vector[i]),")")

if __name__=="__main__":
    with open(json_path, 'r') as data_file:
        data = json.load(data_file)
        data_file.close()
    construct_statistics(data, len(opponent_vector))

    print (mate_dictionary)
    # for team in teams_with:
    #     print (team)
    #print_results()

