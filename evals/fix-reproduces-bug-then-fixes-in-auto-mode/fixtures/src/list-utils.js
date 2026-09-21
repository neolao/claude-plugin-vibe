function max(numbers) {
  let largest = 0;
  for (const n of numbers) {
    if (n > largest) {
      largest = n;
    }
  }
  return largest;
}

module.exports = { max };
