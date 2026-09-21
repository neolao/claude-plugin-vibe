const assert = require("assert");
const { average } = require("../src/stats");

assert.strictEqual(average([2, 4, 6]), 4, "average of [2, 4, 6] should be 4");
assert.throws(
  () => average([]),
  /empty list/,
  "average of [] should throw a clear error"
);

console.log("stats.test.js: all tests passed");
