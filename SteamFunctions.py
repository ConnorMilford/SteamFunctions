from bs4 import BeautifulSoup
import requests
import json
import logging

def findIntersection(list1, list2):
    newList = [value for value in list1 if value in list2]
    return newList

# -- Function to get steam API key --

def getKey():
    key = 'D:\PYTHON\steamProject\key.txt'
    with open(key, 'r') as file:
        key = file.read()
        return key  # steam key used to access api jsons


# -- Function to return name --

def getName(steamId):
    nameList = []
    namePage = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={getKey()}&steamids={steamId}'
    name = BeautifulSoup(requests.get(namePage).text, 'html.parser')  # send request to page using beautiful soup
    nameData = json.loads(name.text)['response']['players']  # access multilayer json
    for element in nameData:
        nameList.append(element['personaname'])  # append username to list

    nameString = ''.join(nameList)  # convert list to string
    return nameString


# -- Functions to compare games --

def getUserGames(steamId):
    games = []
    steamPage = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={getKey()}&steamid={steamId}&include_appinfo=True&format=json'
    user = BeautifulSoup(requests.get(steamPage).text, 'html.parser')  # send request to page using beautiful soup
    data = json.loads(user.text)['response']['games']
    for i in data:
        games.append(i['name'])

    return games

def getUserAvatar(steamId):
    image = ''
    steamPage = f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={getKey()}&steamid={steamId}&include_appinfo=True&format=json'
    user = BeautifulSoup(requests.get(steamPage).text, 'html.parser')  # send request to page using beautiful soup
    data = json.loads(user.text)['response']['games']
    for i in data:
        image.join(i['avatarfull:'])

    return image


# -- Function to get the games of user 1 and 2, then create a list with the games they have in common --

def compareGames(user1ID, user2ID):
    user1 = getUserGames(user1ID)
    user2 = getUserGames(user2ID)  # get games list
    user1name = getName(user1ID)
    user2name = getName(user2ID)
    sameGames = list(set(user1).intersection(set(user2)))
    return f' {user1name} and {user2name} friend have these games in common: \n{", ".join(sameGames)}'


# -- Function to return list intersections of the two user's friend lists --

def returnFriends(steamId):
    friendsID = []
    friendsNames = []
    friendSite = f'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={getKey()}&steamid={steamId}&relationship=friend'  # access json site
    user = BeautifulSoup(requests.get(friendSite).text, 'html.parser')  # send request to page using beautiful soup
    friendData = json.loads(user.text)['friendslist']['friends']
    for element in friendData:
        friendsID.append(element['steamid'])  # append steamid to list

    for friendId in friendsID:
        friendsNames.append(getName(friendId))

    return friendsNames


def compareFriends(steamId1, steamId2):
    friends = []
    user1 = returnFriends(steamId1)
    user2 = returnFriends(steamId2)
    user1name = getName(steamId2)
    user2name = getName(steamId2)
    friends = findIntersection(user1, user2)
    return f' {user1name} and {user2name} are both friends with:\n {", ".join(friends)}'

print(getUserAvatar(76561199019474484))