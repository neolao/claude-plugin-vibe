function formatRow(label, amountCents) {
  return `${label}: ${(amountCents / 100).toFixed(2)}`;
}

module.exports = { formatRow };
