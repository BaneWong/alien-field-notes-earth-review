#!/usr/bin/env python3
"""Writes one original line of at most 200 characters:
a review of planet Earth written by an alien tourist."""

import os
import sys

ENTRY = (
    "4/5: The local species keeps tiny hairless apes in their homes "
    "and feeds them daily — I suspect those 'humans' are the pets. "
    "Would not recommend."
)

assert 1 <= len(ENTRY) <= 200, f"Entry length {len(ENTRY)} out of range"

OUTPUT_DIR = "/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Written {len(ENTRY)} characters to {OUTPUT_PATH}")
