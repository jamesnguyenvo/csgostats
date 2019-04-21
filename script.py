from win10toast import ToastNotifier
import requests

url = 'https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=12A1D1DE83F9932934EDD6DF2BA00463&steamid='
steamid = '' # steam ID
final_url = url + steamid 
data = requests.get(final_url).json()

# valve server stats
stats = {
    'total_kills' : data['playerstats']['stats'][0]['value'], # total kills
    'total_deaths' : data['playerstats']['stats'][1]['value'], # total deaths
    'total_time' : data['playerstats']['stats'][2]['value'] # total time played
}

kd = stats['total_kills']/stats['total_deaths'] # calculate kill death ratio
seconds_min = stats['total_time']/60 # convert seconds to minute
hours = seconds_min/60 # convert minute to hours
kills = str(stats['total_kills']) # kills
deaths = str(stats['total_deaths']) # deaths
timeplayed = str("{:.2f}".format(hours)) # time played
kdratio = str("{:.2f}".format(kd)) # Kill Death Ratio

# windows toast notification
toaster = ToastNotifier()
toaster.show_toast("Steam ID: " + steamid,"\nTotal Kills: " + kills +
                   "\nTotal Deaths: " + deaths + "\nKDR: " + kdratio +
                   "\nTime Played: " + timeplayed + " hours",
                   icon_path=None,duration=10)