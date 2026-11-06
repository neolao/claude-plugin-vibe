# Module: adapters

**Role:** One module per delivery channel, each wrapping one provider SDK and registering its `send` function with the core registry under the channel name.
**Files:** `adapters/notify/__init__.py`, `adapters/notify/email.py`, `adapters/notify/push.py`
**Depends on:** core
