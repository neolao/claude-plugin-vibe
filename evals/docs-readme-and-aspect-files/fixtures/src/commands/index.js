const { listWidgets } = require("./list");
const { addWidget } = require("./add");

function runCommand(args) {
  const [name, ...rest] = args;
  if (name === "list") return listWidgets();
  if (name === "add") return addWidget(rest[0]);
  console.error(`Unknown command: ${name}`);
}

module.exports = { runCommand };
