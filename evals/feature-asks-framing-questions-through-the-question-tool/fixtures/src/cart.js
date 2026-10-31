// Called from the checkout page to show the amount the customer pays.
function orderTotal(items) {
  if (!Array.isArray(items)) {
    throw new Error("orderTotal expects an array of items");
  }
  return items.reduce((sum, item) => {
    if (!Number.isInteger(item.priceCents) || !Number.isInteger(item.quantity)) {
      throw new Error("each item needs an integer priceCents and quantity");
    }
    return sum + item.priceCents * item.quantity;
  }, 0);
}

module.exports = { orderTotal };
