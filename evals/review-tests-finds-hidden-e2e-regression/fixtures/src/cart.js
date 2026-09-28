import * as catalogPricing from "./pricing.js";

// Called by the checkout page; returns the amount to charge, in cents.
export function cartTotal(items, pricing = catalogPricing) {
  if (items.length === 0) throw new Error("empty cart");
  const subtotal = items.reduce((sum, { sku, qty }) => sum + pricing.priceOf(sku) * qty, 0);
  return Math.round(subtotal * (1 - pricing.discountFor(subtotal)));
}
