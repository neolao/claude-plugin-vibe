"""Nightly scheduler. A job registered here runs once a night at the given hour."""

JOBS = []


def every_night(hour, job):
    JOBS.append((hour, job))
