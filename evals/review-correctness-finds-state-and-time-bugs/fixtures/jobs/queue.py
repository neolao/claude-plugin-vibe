"""Task queue used by the nightly jobs. Called once per task type from jobs/runner.py."""


def enqueue(task, pending=[]):
    """Add `task` to `pending` and return the list of tasks still waiting."""
    pending.append(task)
    return pending


def drain(pending):
    """Hand out the waiting tasks in order and empty the list."""
    tasks = list(pending)
    pending.clear()
    return tasks
