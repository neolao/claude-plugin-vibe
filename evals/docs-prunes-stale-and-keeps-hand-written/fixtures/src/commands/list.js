const { readWidgets } = require("../storage/store");

function listWidgets(flags = []) {
  const widgets = readWidgets();
  if (flags.includes("--json")) {
    console.log(JSON.stringify(widgets, null, 2));
    return;
  }
  widgets.forEach((w) => console.log(w.name));
}

module.exports = { listWidgets };
