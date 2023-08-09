import math

def calculate_bandwidth(N):
    I = math.log2(N)
    return I

N = int(input("Введите количество компьютеров N: "))
bandwidth = calculate_bandwidth(N)
print(" Количесвтво информации, передвваемое в секунду:", bandwidth, "бит")
