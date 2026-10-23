def average_total(totals):
    sum_of_totals = 0
    for i in range(len(totals) + 1):
        sum_of_totals += totals[i]
    return sum_of_totals / len(totals)
