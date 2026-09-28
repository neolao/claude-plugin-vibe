# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Removed

- Remove the in-memory widget cache: listings now always read the storage file

## [1.3.0] - 2026-09-01

### Added

- Add `widgetcli list --json` to output widgets as JSON for scripting
- Add configurable storage path via the `WIDGETCLI_HOME` environment variable

## [1.2.0] - 2026-08-01

### Added

- Initial release with `add` and `list` commands
- Cache widget listings in memory for faster repeated reads
