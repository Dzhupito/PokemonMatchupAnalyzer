import json
import numpy
import sys

#team_vector = [["Kyogre"],["Groudon"],["Calyrex-Ice"], ["Calyrex-Shadow"], ["Zacian"], ["Zygarde"],["Palkia"],["Dialga"],["Necrozma"]]
team_vector=[["Zacian","Kyogre"],["Kyogre","Calyrex-Ice"],["Zacian","Calyrex-Shadow"],["Kyogre","Calyrex-Shadow"],["Zacian","Groudon"],["Groudon","Yveltal"],["Groudon","Calyrex-Shadow"],["Zacian","Yveltal"],["Solgaleo","Kyogre"],["Palkia","Zacian"],["Dialga","Zacian"],["Dialga","Kyogre"],["Kyurem-White","Zacian"],["Kyurem-White","Kyogre"],["Rayquaza","Zacian"],["Calyrex-Shadow", "Solgaleo"]]

metagame="gen8vgc2022"
metagame_original="gen8vgc2021series8"
json_path="../Database/sd_"+metagame+".json"
#json_path_original="../Database/sd_"+metagame_original+".json"

def construct_winmatrix(data, size):
    win_matrix = numpy.zeros((size, size))
    ratio_matrix = numpy.zeros((size, size))

    if (len(team_vector)==0):
        print("please, insert a target")
        exit()
    
    for match in data:
        for i in range(0, size):
            if set(team_vector[i]).issubset(set(match["players"][0]["player1_team"])):
                for j in range(i+1,size):
                    if set(team_vector[j]).issubset(set(match["players"][1]["player2_team"])):
                        if (match["players"][0]["player1_name"] == match["winner"]):
                            win_matrix[i][j]+=1
                        else :
                            win_matrix[j][i]+=1
            elif set(team_vector[i]).issubset(set(match["players"][1]["player2_team"])):
                for j in range(i+1,size):
                    if set(team_vector[j]).issubset(set(match["players"][0]["player1_team"])):
                        if (match["players"][1]["player2_name"] == match["winner"]):
                            win_matrix[i][j]+=1
                        else :
                            win_matrix[j][i]+=1
    print (team_vector)
    print (win_matrix)
    for i in range (0, size):
        for j in range (0, size):
            if i!=j:
                if float(win_matrix[i][j])==0 :
                    ratio_matrix[i][j]=0
                else :
                    ratio_matrix[i][j]=float(win_matrix[i][j]/(win_matrix[i][j]+win_matrix[j][i]))
            else:
                ratio_matrix[i][j]=0
            print("%.2f" % ratio_matrix[i][j]," ", end="")
        print(" ")
    

if __name__=="__main__":
    with open(json_path, 'r') as data_file:
        data = json.load(data_file)
        data_file.close()
    #with open(json_path_original, 'r') as data_file:
    #    data += json.load(data_file)
    #    data_file.close()
    construct_winmatrix(data, len(team_vector))
    #print_results()

