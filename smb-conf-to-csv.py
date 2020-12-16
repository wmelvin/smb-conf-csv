#!/usr/bin/env python3

#----------------------------------------------------------------------
# smb-conf-to-csv.py
#
# Extract some fields from a smb.conf file and output in CSV format.
# This is a manual edit-and-run tool with hard-coded paths, for now.
# 
#
# 2020-12-16
#----------------------------------------------------------------------

from pathlib import Path

smb_file = Path.cwd() / "smb.conf.copy-20201216.txt"

p = Path(smb_file).resolve()

if not p.exists():
 	raise SystemExit(f"File not found: {p}")

with open(p, 'r') as f:
    lines = f.readlines()

for line in lines:
    print(line)


# def get_option_entries(opt_section, opt_content):
#     result = []
#     in_section = False
#     for line in opt_content:
#         s = line.strip()
#         if len(s) == 0:
#             in_section = False
#         else:
#             if in_section:
#                 # Handle new section w/o blank lines between.
#                 if s.startswith('['):
#                     in_section = False
#                 # Support whole-line comments identified by '#' (ignore them).
#                 elif not s.startswith('#'):
#                     result.append(s)
#             if s == opt_section:
#                 in_section = True
#     return result
