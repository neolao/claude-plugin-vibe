function average(numbers) {
  if (numbers.length === 0) {
    throw new Error("average: cannot compute the average of an empty list");
  }
  const total = numbers.reduce((sum, n) => sum + n, 0);
  return total / numbers.length;
}

module.exports = { average };
