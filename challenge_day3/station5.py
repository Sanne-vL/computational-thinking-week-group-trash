import pandas as pd
import numpy as np

team_1 = ["Damaris", "Mika", "Isis", "Rosa", "Maja", "Maria"]
team_2 = ["Carine", "Maria", "Célia", "Sabrina", "Emily", "Gur"]
team_3 = ["Dave", "Dmitry", "Elisa", "Jesper", "Martyna", "Sari"]
team_4 = ["Gabriella", "Kelt", "Quanpu", "Ruben", "Sebastian", "Sofia"]
team_5 = ["Ameer", "Gonzalo", "Kian", "Sahir", "Teun", "Tom"]
team_6 = ["Angélica", "Angeline", "Caleb", "Matas", "Paula", "Raven"]
team_7 = ["Emma", "Eryk", "Maja", "Martyna", "Máté", "Vincent"]
team_8 = ["Alyssa", "Beatris", "Caio", "Hielke", "Sally", "Sanne"]
team_9 = ["Atlas", "Diana", "Eliana", "Felix", "Yash"]
team_10 = ["Akanksha", "Al-fatihi", "Andrey", "Charlie", "Hugo", "Max"]
team_11 = ["Alicja", "Cristian", "Ella", "Ioanna", "misha", "Vanessa"]
team_12 = ["Alexia", "Jelle", "Karolina", "Luca", "Yuyue"]

data = {"name" : [i for i in [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8, team_9, team_10, team_11, team_12]],
        "group" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]}
df = pd.DataFrame(data)

df = df.explode("name")

def solution_station_5(name):
    result = df[df["name"] == name].iloc[0, 1]
    return result

print(solution_station_5("Yuyue"))
