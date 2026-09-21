const { readWidgets } = require("../storage/store");

function listWidgets() {
  const widgets = readWidgets();
  widgets.forEach((w) => console.log(w.name));
}

module.exports = { listWidgets };
