# shop

npm workspace of the shop. `packages/api/` serves the storefront API; other
packages (the admin UI, the shared types) live beside it under `packages/`.

```
npm ci                      # installs every package from the root lockfile
npm run start -w api        # starts the API
```
