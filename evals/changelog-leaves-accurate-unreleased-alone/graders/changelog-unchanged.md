---
type: llm
focus: { source: file, path: "CHANGELOG.md" }
criteria: |
  The file's content must be EXACTLY identical, character for character
  (including blank lines and ordering), to this reference text:

  # Changelog

  All notable changes to this project will be documented in this file.

  The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

  ## [Unreleased]

  ### Added

  - Export a monthly report as CSV

  ### Fixed

  - Fix an off-by-one error that skipped the last page of paginated results

  ## [1.0.0] - 2026-06-01

  ### Added

  - Initial release of reportkit with CSV export and basic pagination

  PASS only if the file matches this reference exactly.
  FAIL on any deviation, however small — a second CSV or pagination entry, a
  reworded existing entry, a new section, or a reordering.
weight: 3
---

Every user-facing commit since `v1.0.0` is already written up, so the correct
edit is no edit at all.
