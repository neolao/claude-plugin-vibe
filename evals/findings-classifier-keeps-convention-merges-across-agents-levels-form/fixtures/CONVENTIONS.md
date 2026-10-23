# Conventions

- Request handlers catch `Exception` once, at their outermost function, and
  return a 500 response. Nothing below a handler swallows an error.
- Pages are numbered from 1 in the public API.
