# webshop

Online shop back end: the order model and its storage in `orders/`, the
product catalog mapped through SQLAlchemy in `catalog/`, the checkout use
case in `checkout/`, the stock reservation in `inventory/`, the shop
preferences in `settings/`, the Flask routes in `api/`.

## Modules
- `orders` — order aggregate, money, events, persistence row, repository
- `catalog` — products and their variants, the supplier import
- `checkout` — place an order
- `inventory` — reserve stock when an order is placed
- `settings` — shop preferences edited from the admin page
- `api` — HTTP routes

## Decisions
- `decisions/001-buyer-kept-in-public-api.md`
