from math import cos, prod
import math
from operator import truediv
import random

Nind = 300
Ncrom = 72
max_iteration = 35
mutation_factor = 3.5
population = [None] * Nind


def newpop():
    for i in range(0, Nind):
        population[i] = [None] * Ncrom
        for j in range(0, Ncrom):
            population[i][j] = random.randint(0, 1)

    return population
            
def rating(pop):
    rated = [None] * Nind
    for i in range(0, len(pop)):
        plot = [None] * 8
        j = 0
        monthpos = 0
        plotpos = 0
        while j < (40 - 5):
            input = ""
            for k in range(j, j+5):
                input+=str(pop[i][k])
            if plotpos < 8:
                plot[plotpos] = input
            plotpos += 1
            j += 5
        month = [None] * 8
        while j >= (40 - 5) and j < (Ncrom - 4):
            input = ""
            for k in range(j, j+4):
                input+=str(pop[i][k])
            if monthpos < 8:
                month[monthpos] = input
            monthpos += 1
            j += 4
        cost = 0.0
        production = 0.0
        harvest_cost = 0.0
        for j in range(0,8):
            fertilizer = ""
            month_method = ""
            if j == 0:
                area = 5.7
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 72 * area
                    cost += 2539.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 72 * area
                    cost += 2543.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 76 * area
                    cost += 2866.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 72 * area
                    cost += 2539.56 * area
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 72 * area
                    cost += 2543.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 76 * area
                    cost += 2866.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 72 * area
                    cost += 2476.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 72 * area
                    cost += 2803.69 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 76 * area
                    cost += 2803.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 68 * area
                    cost += 2323.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 68 * area
                    cost += 2327.46 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 72 * area
                    cost += 2650.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 68 * area
                    cost += 2323.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 68 * area
                    cost += 2327.46 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 72 * area
                    cost += 2650.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 68 * area
                    cost += 2260.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 68 * area
                    cost += 2264.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 72 * area
                    cost += 2587.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 640 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 640 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 640 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 640 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 640 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area

            if j == 1:
                area = 10.0
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 24 * area
                    cost += 2176.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 24 * area
                    cost += 2180.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 26 * area
                    cost += 2503.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 24 * area
                    cost += 2176.56 * area
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 24 * area
                    cost += 2180.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 26 * area
                    cost += 2503.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 24 * area
                    cost += 2125.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 24 * area
                    cost += 2129.33 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 26 * area
                    cost += 2452.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 23 * area
                    cost += 1960.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 23 * area
                    cost += 1964.46 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 24 * area
                    cost += 2287.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 23 * area
                    cost += 1960.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 23 * area
                    cost += 1964.46 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 24 * area
                    cost += 2287.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 23 * area
                    cost += 1909.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 23 * area
                    cost += 1913.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 24 * area
                    cost += 2236.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 216 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 216 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 216 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 216 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 216 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area

            if j == 2:
                area = 2.5
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 41 * area
                    cost += 2297.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 41 * area
                    cost += 2301.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 43 * area
                    cost += 2624.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 41 * area
                    cost += 2297.56 * area
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 41 * area
                    cost += 2301.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 43 * area
                    cost += 2624.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 41 * area
                    cost += 2242.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 41 * area
                    cost += 2246.33 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 43 * area
                    cost += 2569.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 38 * area
                    cost += 1960.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 38 * area
                    cost += 2085.46 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 41 * area
                    cost += 2408.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 38 * area
                    cost += 2081.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 38 * area
                    cost += 2085.46 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 41 * area
                    cost += 2408.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 38 * area
                    cost += 2026.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 38 * area
                    cost += 2030.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 41 * area
                    cost += 2353.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 360 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 360 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 360 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 360 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 360 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area

            if j == 3:
                area = 4.0
                production = 0.0
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    cost += 2175.16 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    cost += 2177.76 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    cost += 2443.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    cost += 2175.16 * area
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    cost += 2177.76 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    cost += 2443.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    cost += 2242.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    cost += 2126.63 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    cost += 2392.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    cost += 1959.16 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    cost += 1961.76 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    cost += 2227.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    cost += 1959.16 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    cost += 1961.76 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    cost += 2227.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    cost += 2026.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    cost += 1910.63 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    cost += 2176.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                elif month[j] == "0010":
                    month_method = "junho_manual"
                elif month[j] == "0011":
                    month_method = "julho_manual"
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area
            
            if j == 4:
                area = 5.0
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 90 * area
                    cost += 2660.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 90 * area
                    cost += 2664.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 95 * area
                    cost += 2987.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 90 * area
                    cost += 2660.56
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 90 * area
                    cost += 2664.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 95 * area
                    cost += 2987.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 90 * area
                    cost += 2593.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 90 * area
                    cost += 2597.33 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 95 * area
                    cost += 2920.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 86 * area
                    cost += 2444.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 86 * area
                    cost += 2448.46 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 90 * area
                    cost += 2771.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 86 * area
                    cost += 2444.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 86 * area
                    cost += 2448.46 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 90 * area
                    cost += 2771.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 86 * area
                    cost += 2377.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 86 * area
                    cost += 2381.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 90 * area
                    cost += 2704.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 800 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 800 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 800 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 800 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 800 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area

            if j == 5:
                area = 5.4
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 27 * area
                    cost += 2176.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 27 * area
                    cost += 2180.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 29 * area
                    cost += 2503.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 27 * area
                    cost += 2176.56
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 27 * area
                    cost += 2180.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 29 * area
                    cost += 2503.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 27 * area
                    cost += 2125.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 27 * area
                    cost += 2129.33 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 29 * area
                    cost += 2452.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 26 * area
                    cost += 1960.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 26 * area
                    cost += 1964.46 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 27 * area
                    cost += 2287.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 26 * area
                    cost += 1960.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 26 * area
                    cost += 1964.46 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 27 * area
                    cost += 2287.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 26 * area
                    cost += 1909.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 26 * area
                    cost += 1913.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 27 * area
                    cost += 2236.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 240 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 240 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 240 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 240 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 240 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area

            if j == 6:
                area = 9.2
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 47 * area
                    cost += 2297.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 47 * area
                    cost += 2301.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 49 * area
                    cost += 2624.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 47 * area
                    cost += 2297.56
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 47 * area
                    cost += 2301.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 49 * area
                    cost += 2624.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 47 * area
                    cost += 2242.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 47 * area
                    cost += 2246.33 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 49 * area
                    cost += 2569.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 44 * area
                    cost += 2081.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 44 * area
                    cost += 2085.46 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 47 * area
                    cost += 2408.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 44 * area
                    cost += 2081.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 44 * area
                    cost += 2085.46 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 47 * area
                    cost += 2408.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 44 * area
                    cost += 2026.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 44 * area
                    cost += 2030.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 47 * area
                    cost += 2353.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 416 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 416 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 416 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 416 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 416 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area

            if j == 7:
                area = 16.9
                if plot[j] == "00001" or plot[j] == "10011":
                    fertilizer = "A7A11L1"
                    production += 30 * area
                    cost += 2176.56 * area
                elif plot[j] == "00010" or plot[j] == "10100":
                    fertilizer = "A7A13L1"
                    production += 30 * area
                    cost += 2180.46 * area
                elif plot[j] == "00011" or plot[j] == "10101":
                    fertilizer = "A7A15L1"
                    production += 31 * area
                    cost += 2503.82 * area
                elif plot[j] == "00100" or plot[j] == "10110":
                    fertilizer = "A8A11L1"
                    production += 30 * area
                    cost += 2176.56
                elif plot[j] == "00101" or plot[j] == "10111":
                    fertilizer = "A8A13L1"
                    production += 30 * area
                    cost += 2180.46 * area
                elif plot[j] == "00110" or plot[j] == "11000":
                    fertilizer = "A8A15L1"
                    production += 31 * area
                    cost += 2503.82 * area
                elif plot[j] == "00111" or plot[j] == "11001":
                    fertilizer = "A9A11L1"
                    production += 30 * area
                    cost += 2125.43 * area
                elif plot[j] == "01000" or plot[j] == "11010":
                    fertilizer = "A9A13L1"
                    production += 30 * area
                    cost += 2129.33 * area
                elif plot[j] == "01001" or plot[j] == "11011":
                    fertilizer = "A9A15L1"
                    production += 31 * area
                    cost += 2452.69 * area
                elif plot[j] == "01010" or plot[j] == "11100":
                    fertilizer = "A7A11L2"
                    production += 28 * area
                    cost += 1960.56 * area
                elif plot[j] == "01011" or plot[j] == "11101":
                    fertilizer = "A7A13L2"
                    production += 28 * area
                    cost += 1960.56 * area
                elif plot[j] == "01100" or plot[j] == "11110":
                    fertilizer = "A7A15L2"
                    production += 30 * area
                    cost += 2287.82 * area
                elif plot[j] == "01101" or plot[j] == "11111":
                    fertilizer = "A8A11L2"
                    production += 28 * area
                    cost += 1960.56 * area
                elif plot[j] == "01110" or plot[j] == "00000":
                    fertilizer = "A8A13L2"
                    production += 28 * area
                    cost += 1964.64 * area
                elif plot[j] == "01111":
                    fertilizer = "A8A15L2"
                    production += 30 * area
                    cost += 2287.82 * area
                elif plot[j] == "10000":
                    fertilizer = "A9A11L2"
                    production += 28 * area
                    cost += 1909.43 * area
                elif plot[j] == "10001":
                    fertilizer = "A9A13L2"
                    production += 28 * area
                    cost += 1913.33 * area
                elif plot[j] == "10010":
                    fertilizer = "A9A15L2"
                    production += 30 * area
                    cost += 2236.69 * area

                if month[j] == "0001":
                    month_method = "maio_manual"
                    harvest_cost += 264 * area
                elif month[j] == "0010":
                    month_method = "junho_manual"
                    harvest_cost += 264 * area
                elif month[j] == "0011":
                    month_method = "julho_manual"
                    harvest_cost += 264 * area
                elif month[j] == "0100":
                    month_method = "agosto_manual"
                    harvest_cost += 264 * area
                elif month[j] == "0101" or month[j] == "0000":
                    month_method = "setembro_manual"
                    harvest_cost += 264 * area
                elif month[j] == "0110" or  month[j] == "1011":
                    month_method = "maio_maquina"
                    harvest_cost += 224 * area
                elif month[j] == "0111" or  month[j] == "1100":
                    month_method = "junho_maquina"
                    harvest_cost += 218 * area
                elif month[j] == "1000" or  month[j] == "1101":
                    month_method = "julho_maquina"
                    harvest_cost += 214 * area
                elif month[j] == "1001" or  month[j] == "1110":
                    month_method = "agosto_maquina"
                    harvest_cost += 209 * area
                elif month[j] == "1010" or  month[j] == "1111":
                    month_method = "setembro_maquina"
                    harvest_cost += 203 * area
        deduction = harvest_cost + cost
        qtd_cereja = math.floor(production * 0.3)
        qtd_boia = math.floor(production * 0.49)
        qtd_verde = math.floor(production * 0.12)
        qtd_varrecao = production - qtd_verde - qtd_cereja - qtd_boia
        income = (qtd_cereja * 300) + (qtd_verde * 180) + (qtd_boia * 200) + (qtd_varrecao * 150)
        profit = income - deduction
        rated[i] = profit
    return rated

def sort_key(lst):
    return lst[1]

def selection(pop, rated):
    selected_pop = [None for x in range(math.floor(Nind / 2))]
    select_list = [ [ None for y in range( 2 ) ] for x in range( Nind ) ]
    for i in range(0, Nind):
        select_list[i] = [pop[i], rated[i]]

    select_list.sort(key=sort_key, reverse=True)
    for i in range(0, math.floor(Nind / 2)):
        selected_pop[i] = select_list[i][0]
    
    return selected_pop

def crossover(pop):
    kids = [ [ None for y in range( Ncrom ) ] for x in range( math.floor(Nind / 2 )) ]
    for i in range (0, math.floor(Nind / 2)):
        p1 = random.randint(1, Ncrom - 2)
        p2 = random.randint(1, Ncrom - 2)
        while p2 == p1:
            p2 = random.randint(1, Ncrom - 2)
        if p1 > p2:
            p3 = p2
            p2 = p1
            p1 = p3
        parent1 = pop[i]
        parent2 = pop[0]

        if i < ((Nind / 2)-1):
            parent2 = pop[i+1]
        
        for j in range(0, p1):
            kids[i][j] = parent1[j]
        for j in range(p1, p2):
            kids[i][j] = parent2[j]
        for j in range(p2, Ncrom):
            kids[i][j] = parent1[j]
    return kids

def mutate(pop):
    qtd_mutations = math.floor(Nind * mutation_factor / 100)
    for i in range(0, qtd_mutations):
        mutation_index = random.randint(0, Nind-1)
        cromossome_index = random.randint(0, Ncrom-1)
        if pop[mutation_index][cromossome_index] == 0:
            pop[mutation_index][cromossome_index] = 1
        else:
            pop[mutation_index][cromossome_index] = 0
    return pop
         

def concat_pops(pop1, pop2):
    if len(pop1) == Nind:
        return pop1
    if len(pop2) == Nind:
        return pop2
    
    if len(pop1) == Nind / 2 and len(pop2) == Nind / 2:
        return pop1 + pop2


def execute():
    pop = newpop()
    i = 0
    while i < 35:
        rated = rating(pop)
        selected = selection(pop, rated)
        crossbreed = crossover(selected)
        pop = concat_pops(selected, crossbreed)
        pop = mutate(pop)
        i += 1
    
    rated = rating(pop)
    selected = selection(pop, rated)
    selected_individual = [None]
    selected_individual[0] =  selected[0]
    selected_individual_rating = rating(selected_individual)
    print("Profit of the selected: " + str(selected_individual_rating[0]))


execute()