const fs = require("fs");
const path = require("path");

const STORE_PATH = process.env.WIDGETCLI_HOME
  ? path.join(process.env.WIDGETCLI_HOME, "widgets.json")
  : path.join(__dirname, "..", "..", "widgets.json");

function readWidgets() {
  if (!fs.existsSync(STORE_PATH)) return [];
  return JSON.parse(fs.readFileSync(STORE_PATH, "utf8"));
}

function writeWidgets(widgets) {
  fs.writeFileSync(STORE_PATH, JSON.stringify(widgets, null, 2));
}

module.exports = { readWidgets, writeWidgets };
