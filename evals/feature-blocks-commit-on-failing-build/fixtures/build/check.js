const fs = require("fs");
const path = require("path");

const rootDir = path.join(__dirname, "..");
const contractPath = path.join(rootDir, "types", "roster.contract.json");
const contract = JSON.parse(fs.readFileSync(contractPath, "utf8"));

const lib = require(path.join(rootDir, "src", "roster.js"));
const exported = Object.keys(lib);

const missing = exported.filter((name) => !(name in contract));

if (missing.length > 0) {
  console.error(
    `BUILD FAILED: src/roster.js exports ${missing
      .map((name) => `"${name}"`)
      .join(", ")} but types/roster.contract.json has no contract entry ` +
      `for ${missing.length === 1 ? "it" : "them"}.\n` +
      `Add an entry to types/roster.contract.json for each one (see the ` +
      `existing "totalScore" entry as a template).`
  );
  process.exit(1);
}

console.log("build/check.js: every exported function has a matching contract entry");
