#    6. Given stock prices over 7 days: prices = [105, 110, 108, 112, 115, 116, 114].
#       Compute the 3-day rolling average using slicing.
#           Explanation:
#               (105+110+108)/3 ≈ 107.67
#               (110+108+112)/3 = 110.0
#               ... and so on
 
 
prices = [105, 110, 108, 112, 115, 116, 114]

rolling_avg = []

for i in range(len(prices) - 2):
    avg = sum(prices[i:i+3]) / 3
    rolling_avg.append(avg)


for avg in rolling_avg:
    print(round(avg, 2))
