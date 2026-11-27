# billing-service

## Architecture

Ports & adapters. `src/core/` holds the domain and the application services and depends on nothing outside itself; `src/core/ports/` declares the interfaces the core needs; `src/adapters/` implements them. `src/app.py` is the composition root: every service is built there and receives its dependencies through its constructor.
