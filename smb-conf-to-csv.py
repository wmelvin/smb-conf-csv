#!/usr/bin/env python3

#----------------------------------------------------------------------
# smb-conf-to-csv.py
#
# Extract some fields from a smb.conf file and output in CSV format.
# This is a manual edit-and-run tool with hard-coded paths, for now.
#
# ./smb-conf-to-csv.py > smb-conf-to-csv-output.csv
#
# 2020-12-16 
#----------------------------------------------------------------------

from pathlib import Path

#smb_file = Path.cwd() / "smb.conf.copy-20201216.txt"
smb_file = Path.cwd() / "smb.conf.copy-20210123.txt"

p = Path(smb_file).resolve()

if not p.exists():
 	raise SystemExit(f"File not found: {p}")

with open(p, 'r') as f:
    lines = f.readlines()

shares_list = []
shares_list.append('"SHARE","PATH"')
share_name = ''
share_path = ''

for line in lines:
    #print(line)
    s = line.strip()
    if len(s) > 0:
        if s.startswith('['):
            if len(share_path) > 0:
                shares_list.append('"{0}","{1}"'.format(share_name, share_path))
            share_name = s.replace('[', '').replace(']', '')
            share_path = ''
            #print(share_name)
        elif '=' in s:
            a = s.split('=')
            if a[0].strip().lower() == 'path':
                share_path = a[1].strip()
# Get last one.
if len(share_path) > 0:
    shares_list.append('"{0}","{1}"'.format(share_name, share_path))

for item in shares_list:
    print(item)



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
