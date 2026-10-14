import logging

log = logging.getLogger("billing")


def effective_price(item):
    if item.get("sale_price") is not None and item["sale_price"] < item["price"]:
        return item["sale_price"]
    return item["price"]


def compute_invoice_line(item, quantity, tax_rate):
    unit_price = effective_price(item)
    log.debug("unit price for %s: %s", item["sku"], unit_price)
    net = unit_price * quantity
    log.debug("net for %s: %s", item["sku"], net)
    tax = round(net * tax_rate, 2)
    log.debug("tax for %s: %s", item["sku"], tax)
    gross = net + tax
    log.debug("gross for %s: %s", item["sku"], gross)
    return {"sku": item["sku"], "net": net, "tax": tax, "gross": gross}


def invoice_total(items, tax_rate):
    lines = [compute_invoice_line(item, qty, tax_rate) for item, qty in items]
    return sum(line["gross"] for line in lines)
