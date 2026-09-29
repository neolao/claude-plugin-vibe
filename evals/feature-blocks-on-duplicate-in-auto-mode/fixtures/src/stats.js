function average(numbers) {
  if (numbers.length === 0) {
    throw new Error("average: cannot compute the average of an empty list");
  }
  const total = numbers.reduce((sum, n) => sum + n, 0);
  return total / numbers.length;
}

function middleValue(numbers) {
  if (numbers.length === 0) {
    throw new Error("middleValue: cannot compute the middle value of an empty list");
  }
  const sorted = [...numbers].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 1 ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
}

module.exports = { average, middleValue };
