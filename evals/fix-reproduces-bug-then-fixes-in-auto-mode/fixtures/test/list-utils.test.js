const assert = require("assert");
const { max } = require("../src/list-utils");

assert.strictEqual(max([1, 5, 3]), 5, "max of [1, 5, 3] should be 5");
assert.strictEqual(
  max([10]),
  10,
  "max of a single-element list should be that element"
);

console.log("list-utils.test.js: all tests passed");
