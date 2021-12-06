# smb_conf_csv #

## Command Line Help/Usage ##

```
Usage: smb_conf_csv.py  INPUT_FILE  [-o OUTPUT_NAME]

Reads a Samba configuration file (smb.conf) and writes
some information about the shares to CSV format.

INPUT_FILE
                Path to the smb.conf file to be read (Required).

-o OUTPUT_NAME
                Name of the CSV file to be written (Optional).
                The output_name is used to specifiy the base name.
                A date_time tag, and '.csv' extension are added.
                If no output_name is specified, output is written
                to the console.
```
