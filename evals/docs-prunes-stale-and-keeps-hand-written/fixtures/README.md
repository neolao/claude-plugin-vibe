# widgetcli

A tiny CLI to manage widgets from the command line.

## About this project

Widgetcli grew out of a team hack day; the maintainers keep this paragraph by hand to explain where the project came from, and no generator is allowed to reword it.

## Features

<!-- vibe:begin:features -->
- Add widgets and list them from the command line
- Faster repeated listings thanks to an in-memory cache
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
- [docs/caching.md](docs/caching.md) — how widget listings are kept in memory between reads.
<!-- vibe:end:docs-index -->
