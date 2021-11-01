#!/usr/bin/env python3

"""
This console application reads a Samba configuration file (smb.conf) and
writes some information about the shares to CSV format.
"""


import sys

from datetime import datetime
from pathlib import Path


class ShareInfo:
    def __init__(self, share_name: str, line_num: int):
        self.share_name = share_name
        self.line_num = line_num
        self.path = ""
        self.force_user = ""
        self.force_group = ""
        self.browseable = ""
        self.guest_ok = ""
        self.read_only = ""
        self.valid_users = ""
        self.write_list = ""

    def has_data(self):
        return 0 < len(self.path)

    def as_csv(self):
        return '"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",'.format(
            self.line_num,
            self.share_name,
            self.path,
            self.force_user,
            self.force_group,
            self.browseable,
            self.guest_ok,
            self.valid_users,
            self.read_only,
            self.write_list,
        )


def csv_header():
    return '"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",'.format(
        "line_num",
        "share_name",
        "path",
        "force_user",
        "force_group",
        "browseable",
        "guest_ok",
        "valid_users",
        "read_only",
        "write_list",
    )


def print_usage():
    print("\nUsage: smb_conf_csv.py  input_file  [-o output_name]")
    print("Where:")
    print("  input_file = Path to the smb.conf file to be read. (Required)")
    print("  output_name = Name of the CSV file to be written. (Optional)")
    print("    The output_name is used to specifiy the base name.")
    print("    A date_time tag, and '.csv' extension are added.")
    print("    If no output_name is specified, output is written")
    print("    to the console.\n")


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
        #  Only print this message when writing to a file.
        #  Not wanted if console output is being redirected.
        print(f"Reading '{in_path}'")

    with open(in_path, "r") as f:
        lines = f.readlines()

    out_list = []
    out_list.append(csv_header())

    share_info = None

    for line_num, line in enumerate(lines, start=1):
        s = line.strip()
        if len(s) > 0:
            if s.startswith("["):
                if share_info is not None and share_info.has_data():
                    out_list.append(share_info.as_csv())

                share_info = ShareInfo(
                    s.replace("[", "").replace("]", ""), line_num
                )

            elif "=" in s:
                a = s.split("=", 1)
                opt_name = a[0].strip().lower()
                opt_value = a[1].strip()
                if opt_name == "path":
                    share_info.path = opt_value
                elif opt_name == "valid users":
                    share_info.valid_users = opt_value
                elif opt_name == "force user":
                    share_info.force_user = opt_value
                elif opt_name == "force group":
                    share_info.force_group = opt_value
                elif opt_name == "guest ok":
                    share_info.guest_ok = opt_value
                elif opt_name == "read only":
                    share_info.read_only = opt_value
                elif opt_name == "write list":
                    share_info.write_list = opt_value
                elif opt_name == "browseable":
                    share_info.browseable = opt_value
                elif opt_name == "browsable":
                    share_info.browseable = opt_value

    #  Get the last one.
    if share_info is not None and share_info.has_data():
        out_list.append(share_info.as_csv())

    if out_path is None:
        for item in out_list:
            print(item)
    else:
        print(f"Writing '{out_path}'")
        with open(out_path, "w") as f:
            for item in out_list:
                f.write(f"{item}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
