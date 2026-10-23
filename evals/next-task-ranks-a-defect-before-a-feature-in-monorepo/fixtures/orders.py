def order_total(lines):
    return sum(quantity * unit_price for quantity, unit_price in lines)
