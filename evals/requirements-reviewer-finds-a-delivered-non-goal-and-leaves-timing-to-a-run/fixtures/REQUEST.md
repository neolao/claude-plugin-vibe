# Backlog item 027 — Compress uploaded images

## Description
Photos uploaded by shop owners are stored as they come and fill the disk.

## Acceptance Criteria
1. An uploaded image is stored compressed at JPEG quality 80, under its original name.
2. The original size and the stored size are written to the application log.

## Constraints
- Out of scope: the gallery thumbnails keep their current width (120 px); this change does not touch them.
- Compressing a 5 MB image takes under 2 seconds.
