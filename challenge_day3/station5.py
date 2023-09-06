import pandas as pd
import numpy as np

dic = {1 : ['Mika', 'Maria', 'Isis', 'Rosa', 'Maja', 'Damaris'], 2 : ['Emily ', 'Celia', 'Carine', 'Sabrina', 'Maria', 'Gur'], 3 : ['Elisa', 'Sari', 'Kavin', 'Dima', 'Jesper', 'Martyna'], 4 : ['Kelt', 'Sebastian', 'Quanpu', 'Ruben', 'Sofia', 'Gabriella'], 5 : ['Kian', 'Sahir', 'Tom', 'Gonzalo', 'Ameer', 'Teun'], 6 : ['Angelica', 'Matas', 'Caleb', 'Angeline', 'Raven', 'Paulina'], 7 : ['Martyna', 'Maja ', 'Mate', 'Vincent', 'Eryk', 'Emma'], 8 : ['Hielke', 'Liss', 'Beatris', 'Caio', 'Sally', 'Sanne'], 9 : ['Atlas', 'Elli', 'Felix', 'Diana', 'Yash'], 10 : ['Akanksha', 'Charlie', 'Andrey', 'Max', 'Hugo', 'Al-Fatihi'], 11 : ['Misha', 'Ioanna', 'Ella', 'Cristian', 'Vanessa'], 12 : ['Luca', 'Rachna', 'Jelle', 'Karolina', 'Yuyue', 'Alexia']}

def solution_station_5(name):
    for i in range(1, 13):
        if name in dic[i]:
            result = i
    return result
