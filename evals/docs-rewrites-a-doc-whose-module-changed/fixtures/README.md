# widgetcli

A tiny CLI to manage widgets from the command line.

## About this project

Widgetcli started as a personal weekend project to learn how to package small CLI tools; this paragraph is maintained entirely by hand and must never be rewritten by any tooling, no matter what else changes in this file.

## Features

<!-- vibe:begin:features -->
- Add widgets and list them from the command line
- Output your widget list as JSON for scripting
- Choose where your widget data is stored
<!-- vibe:end:features -->

## Installation

<!-- vibe:begin:install -->
Requires Node.js. From a checkout of this repository:

```sh
npm install -g .
```

Check it with `widgetcli list`. Remove it with `npm uninstall -g widgetcli`.
<!-- vibe:end:install -->

## Usage

<!-- vibe:begin:usage -->
```sh
widgetcli add "My widget"
widgetcli list
widgetcli list --json
```
<!-- vibe:end:usage -->

## Documentation

<!-- vibe:begin:docs-index -->
- [docs/architecture.md](docs/architecture.md) — how the commands and the storage fit together.
<!-- vibe:end:docs-index -->
