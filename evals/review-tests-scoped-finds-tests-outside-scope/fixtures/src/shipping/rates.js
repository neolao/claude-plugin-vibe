// Delivery price in cents by weight band; called by the checkout page.
export function rateFor(weightGrams) {
  if (weightGrams <= 0) throw new Error("weight must be positive");
  if (weightGrams <= 1000) return 490;
  if (weightGrams <= 5000) return 890;
  return 1490;
}
