#!/bin/sh
# Prints the widgets listed in the file given as first argument, one per line.
tr ',' '\n' < "$1"
