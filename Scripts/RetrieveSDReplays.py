from bs4 import BeautifulSoup
from datetime import datetime
import io
import os
import json
import requests
from time import sleep

showdown_url="https://replay.pokemonshowdown.com"
metagame="gen8vgc2021series11"
threshold_path="../Database/date.json"
threshold_date=0
replay_format="/search?user=&format="+metagame+"&page={}"
json_path="../Database/sd_"+metagame+".json"
replay_links_list = []
entries_array = []

class Player:
    def __init__(self):
        self.name = ""
        self.rating = 0
        self.team = []
        self.lead = []
        self.back = []
        self.dynamaxed = ""

class Match:
    def __init__(self):
        self.metagame = ""
        self.date = 0
        self.p1 = Player()
        self.p2 = Player()
        self.winner = ""
        self.replay_link = ""

def get_showdown_page(page):
    sleep(10)
    response = None

    while response is None:
        try:
            response = requests.get(showdown_url + replay_format.format(page))
        except Exception as e:
            sleep(150)
            response = None

    return response

def get_date(address):
    print (address)
    date = 0 
    if metagame in address : 
        sleep(0.5)
        replay = None

        while replay is None:
            try:
                replay = requests.get(address)
            except Exception:
                sleep(150)
                replay = None

        soup = BeautifulSoup(replay.text, 'html.parser')
        #date = 0 
        try:
            date = soup.findAll("small", {"class": "uploaddate"})[0]['data-timestamp']
        except:
            print("Date exception thrown")
            date = "0"
            return int(date)
    return int(date)

#         date = get_date(host + l.a['href'])


def get_replay(address):
    sleep(2)
    replay_log = None

    while replay_log is None:
        try:
            replay_log = requests.get(address)
        except Exception:
            sleep(150)
            replay_log = None

    return replay_log

def write_json ():
    already_present_entries = []
    global entries_array
    if len(entries_array)>=1 :
        if os.path.isfile(json_path) and os.access(json_path, os.R_OK):
            print ("file already exists")
            with open(json_path, 'r') as data_file:
                already_present_entries = json.load(data_file)
                data_file.close()
            os.remove(json_path)
        open(json_path, "x")
        with open(json_path, 'w') as outfile:
            if len(already_present_entries) > 0 :
                entries_array+=already_present_entries
            json.dump(entries_array, outfile)
            outfile.close()
        date_file = open(threshold_path, "r")
        date_object = json.load(date_file)
        date_file.close()
        date_object[metagame] = entries_array[0]["date"]
        date_file = open(threshold_path, "w")
        json.dump(date_object, date_file)
        date_file.close()
    

    # json.dump(date_object, date_file)
    # date_file.close()
    

def manage_json(match):
    new_entry = {
        "date": match.date,
        "metagame": match.metagame,
        "players": [
            {
                "player1_name": match.p1.name, 
                "player1_rating": match.p1.rating,
                "player1_team": match.p1.team, 
                "palyer1_lead": match.p1.lead,
                "player1_back": match.p1.back,
                "player1_dynamax": match.p1.dynamaxed,
            },
            {
                "player2_name": match.p2.name, 
                "player2_rating": match.p2.rating,
                "player2_team": match.p2.team, 
                "palyer2_lead": match.p2.lead,
                "player2_back": match.p2.back,
                "player2_dynamax": match.p2.dynamaxed,
            },
        ],
        "winner": match.winner,
        "replay_url": match.replay_link,
    }
    entries_array.append(new_entry)

def get_teams_from_replay(replay_log, date, replay_url):
    print ("-------------------- new match")
    print (date)
    match = Match()
    match.date=int(date)
    match.replay_link = replay_url
    match.metagame=metagame

    nicknames_pokemons = [[],[]]

    for n in [x for x in replay_log.text.split('\n')] :
        if n.startswith("|player|p1|") and (match.p1.name=="" or match.p2.name==""):
            match.p1.name=n.split('|')[3]
            if n.split('|')[-1]!='':
                match.p1.rating=int(n.split('|')[-1])
        if n.startswith("|player|p2|") and (match.p1.name=="" or match.p2.name==""):
            match.p2.name=n.split('|')[3]
            if n.split('|')[-1]!='':
                match.p2.rating=int(n.split('|')[-1])
        if n.startswith('|-start|') and "Dynamax" in n:
            dynamaxed_pokemon = n.split('|')[2].split(': ')[1]
            i=0
            if n.startswith('|-start|p1') :
                while i < (len(match.p1.back) + 2) :
                    if nicknames_pokemons[0][i] == dynamaxed_pokemon :
                        if i < 2 :
                            match.p1.dynamaxed =  match.p1.lead[i]
                            i = 3
                        else :
                            match.p1.dynamaxed = match.p1.back[i-2]
                            i = 3
                    i+=1
            else : 
                while i < (len(match.p2.back) + 2) :
                    if nicknames_pokemons[1][i] == dynamaxed_pokemon:
                        if i < 2 :
                            match.p2.dynamaxed =  match.p2.lead[i]
                            i = 3
                        else :
                            match.p2.dynamaxed = match.p2.back[i-2]
                            i = 3
                    i+=1
        if n.startswith("|switch|p1") and len(match.p1.back)<2:
            pokemon = n.split('|')[3].split(', ')[0]
            pokemon = pokemon.replace("-East", "").replace("-West", "").replace("-*", "").replace("’", "'") 
            if "Urshifu" in pokemon :
                i = 0
                while i<len(match.p1.team) :
                    if "Urshifu" in match.p1.team[i] :
                        match.p1.team[i] = pokemon
                    i+=1
            if len(match.p1.lead)<2 :
                match.p1.lead.append(pokemon)
                nicknames_pokemons[0].append(n.split('|')[2].split(': ')[1])
            elif pokemon not in match.p1.lead and pokemon not in match.p1.back :
                match.p1.back.append(pokemon)
                nicknames_pokemons[0].append(n.split('|')[2].split(': ')[1])
        if n.startswith("|switch|p2") and len(match.p2.back)<2:
            pokemon = n.split('|')[3].split(', ')[0]
            pokemon = pokemon.replace("-East", "").replace("-West", "").replace("-*", "").replace("’", "'") 
            if "Urshifu" in pokemon :
                i = 0
                while i<len(match.p2.team) :
                    if "Urshifu" in match.p2.team[i] :
                        match.p2.team[i] = pokemon
                    i+=1
            if len(match.p2.lead)<2 :
                match.p2.lead.append(pokemon)
                nicknames_pokemons[1].append(n.split('|')[2].split(': ')[1])
            elif pokemon not in match.p2.lead and pokemon not in match.p2.back :
                match.p2.back.append(pokemon)
                nicknames_pokemons[1].append(n.split('|')[2].split(': ')[1])

            
        if n.startswith("|poke") :
            pokemon = n.split('|')[3].split(', ')[0]
            pokemon = pokemon.replace("-East", "").replace("-West", "").replace("’", "'")
            if "Urshifu" not in pokemon :
                pokemon = pokemon.replace("-*", "")

            if pokemon.startswith("Alcremie"):
                pokemon = "Alcremie"

            if n.startswith("|poke|p1"):
                match.p1.team.append(pokemon)
            elif n.startswith("|poke|p2"):
                match.p2.team.append(pokemon)
        if n.startswith("|win|") :
            match.winner = n.split('|')[2]
    manage_json(match)


def get_replay_links(replay_list):
    
    for replay_params in replay_list :
        #print (replay_params)
        replay_url = showdown_url + replay_params.a['href']
        if replay_url not in replay_links_list :
            print (replay_url)
            replay_links_list.append(replay_url)
            replay_log = get_replay(replay_url + '.log')
            date = get_date(showdown_url + replay_params.a['href'])
            if int(date) <= int(threshold_date) :
                print ("new entries " + str(len(entries_array)))
                print (entries_array[-1])
                write_json()
                exit()
            # if date < threshold --> break the loop
            get_teams_from_replay (replay_log, date, replay_url)
            #print (teams)
            #replay_links_list.append(replay_params.a['href'])
            #print (datetime.fromtimestamp(get_date(showdown_url + replay_params.a['href'])).strftime("%A, %B %d, %Y %H:%M:%S"))
    return replay_links_list

def get_replay_list(page):
    print("Retrieving page {}".format(page))
    response = get_showdown_page(page)
    if response == None:
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    len_replay = (len(soup.findAll("li")) - 6) * (-1)
    replay_links = soup.findAll("li")[len_replay:]
    return replay_links

def retrieve_threshold():
    date_file = open(threshold_path, "r")
    date_object = json.load(date_file)
    date_file.close()
    global threshold_date
    threshold_date = int(date_object[metagame])


def run():
    #unique_teams = set()
    #teams = []
    #threshold_date = (datetime.datetime(2020, 6, 24) - datetime.datetime(1970,1,1)).total_seconds()
    retrieve_threshold()
    replay_list = []
    replay_data = []

    page = 15
    print("Retrieving Main Format Teams: " + replay_format)
    while page != -1:
        #teams, unique_teams = get_teams(replay_format, page)
        replay_data = get_replay_list(page)
        if len(replay_data) > 7 :
            replay_list += get_replay_links(replay_data)
            page += 1
        else :
            page = -1 
    
    print(len(replay_links_list))
    # teams.extend([list(t) for t in unique_teams])
    # print("Writing {} sample teams".format(len(teams)))
    # write_teams(write_loc, teams)

def check() :
    with open(json_path, 'r') as data_file:
        data = json.load(data_file)
        data_file.close()
    print (len(data))

if __name__=="__main__":
    run()
    write_json()
    #check()
    #insert main.





# to do:
# beautify the code
# add threshold and a control in json.
# define class for trainers-pokemon