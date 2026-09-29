const assert = require("assert");
const { average, middleValue } = require("../src/stats");

assert.strictEqual(average([2, 4, 6]), 4, "average of [2, 4, 6] should be 4");
assert.throws(
  () => average([]),
  /empty list/,
  "average of [] should throw a clear error"
);

assert.strictEqual(middleValue([5, 1, 3]), 3, "middle value of [5, 1, 3] should be 3");
assert.strictEqual(middleValue([4, 1, 3, 2]), 2.5, "middle value of an even list is the mean of the two centre values");
assert.throws(
  () => middleValue([]),
  /empty list/,
  "middleValue of [] should throw a clear error"
);

console.log("stats.test.js: all tests passed");
