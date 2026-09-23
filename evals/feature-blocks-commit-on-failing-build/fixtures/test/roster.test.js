const assert = require("assert");
const { totalScore } = require("../src/roster");

assert.strictEqual(
  totalScore([{ score: 3 }, { score: 5 }]),
  8,
  "totalScore of two players should sum their scores"
);
assert.strictEqual(totalScore([]), 0, "totalScore of an empty roster should be 0");

console.log("roster.test.js: all tests passed");
