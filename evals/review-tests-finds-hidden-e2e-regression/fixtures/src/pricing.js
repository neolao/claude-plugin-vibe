// Prices in cents, owned by the catalog team.
const CATALOG = { "sku-apple": 150, "sku-pear": 200, "sku-melon": 900 };

export function priceOf(sku) {
  if (!(sku in CATALOG)) throw new Error(`unknown sku ${sku}`);
  return CATALOG[sku];
}

// Bulk discount set by marketing: 10 percent off from 10.00 upwards.
export function discountFor(subtotal) {
  return subtotal >= 1000 ? 10 : 0;
}
