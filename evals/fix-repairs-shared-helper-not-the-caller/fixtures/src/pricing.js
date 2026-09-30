const { roundCents } = require("./money");

function lineTotal(item) {
  return roundCents(item.price * item.qty);
}

function orderTotal(items) {
  return roundCents(items.reduce((sum, item) => sum + lineTotal(item), 0));
}

function applyDiscount(total, percent) {
  return roundCents(total * (1 - percent / 100));
}

module.exports = { lineTotal, orderTotal, applyDiscount };
