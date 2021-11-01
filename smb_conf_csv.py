#!/usr/bin/env python3

"""
Read a Samba configuration file (smb.conf) and write share names and paths
as CSV format.
"""


import sys

from datetime import datetime
from pathlib import Path


def print_usage():
    print("Usage: smb_conf_csv.py  input_file [-o output_file]")
    print("Where:")
    print("  input_file = Path to the smb.conf file to be read.")
    print("  output_name = Name of the CSV file to be written.")
    print("    The output_name is used to specifiy the base name.")
    print("    A date_time tag, and '.csv' extension are added.")
    print("    If no output_name is specified, output is written")
    print("    to the console.")


def main(argv):

    if not len(argv) in [2, 4]:
        print_usage()
        return 2

    out_path = None
    if len(argv) == 4:
        if argv[2].lower() != "-o":
            print_usage()
            return 2
        out_path = Path(argv[3]).expanduser().resolve()
        suffix = f".{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        out_path = out_path.with_suffix(suffix)

    in_path = Path(argv[1]).expanduser().resolve()
    if not in_path.exists():
        print(f"ERROR: File not found: {in_path}")
        return 1

    if out_path is not None:
        #  Only print this message when writing to a file in case console
        #  output is being redirected.
        print(f"Reading '{in_path}'")

    with open(in_path, 'r') as f:
        lines = f.readlines()

    shares_list = []
    shares_list.append('"SHARE","PATH","CONF_LINE"')
    share_name = ''
    share_path = ''
    share_line = 0

    line_num = 0
    for line in lines:
        line_num += 1
        # print(line)
        s = line.strip()
        if len(s) > 0:
            if s.startswith('['):
                if len(share_path) > 0:
                    shares_list.append(
                        '"{0}","{1}",{2}'.format(
                            share_name, share_path, share_line
                        )
                    )
                share_name = s.replace('[', '').replace(']', '')
                share_path = ''
                share_line = line_num
                # print(share_name)
            elif '=' in s:
                a = s.split('=')
                if a[0].strip().lower() == 'path':
                    share_path = a[1].strip()

    #  Get the last one.
    if len(share_path) > 0:
        shares_list.append(
            '"{0}","{1}",{2}'.format(share_name, share_path, share_line)
        )

    if out_path is None:
        for item in shares_list:
            print(item)
    else:
        print(f"Writing '{out_path}'")
        with open(out_path, "w") as f:
            for item in shares_list:
                f.write(f"{item}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
