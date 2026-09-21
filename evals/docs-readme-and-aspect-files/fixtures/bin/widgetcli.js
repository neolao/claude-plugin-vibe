#!/usr/bin/env node
const { runCommand } = require("../src/commands");

runCommand(process.argv.slice(2));
