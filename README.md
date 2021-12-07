# smb-conf-csv #


**smb_conf_csv.py** is a command-line tool that reads a [Samba](https://www.samba.org/samba/) configuration file (smb.conf), or a copy of one, and writes some information about *shares* to CSV format. 

This tool serves the author's needs for documenting the shares on a few local file servers with fairly simple configurations. It **does not produce a comprehensive listing** of available configuration parameters for a file share. Doing so would produce a *very wide* (and hardly usable) CSV file. At the time of writing, there were over 140 share (S) parameters listed in the manpage for [smb.conf](https://www.samba.org/samba/docs/current/man-html/smb.conf.5.html).


## Command Line Help/Usage ##

```
Usage: smb_conf_csv.py  INPUT_FILE  [-o OUTPUT_NAME]

Reads a Samba configuration file (smb.conf) and writes
some information about the shares to CSV format.

INPUT_FILE
                Path to the smb.conf file to be read (Required).

-o OUTPUT_NAME
                Name of the CSV file to be written (Optional).
                The output_name is used to specify the base name.
                A date_time tag, and '.csv' extension are added.
                If no output_name is specified, output is written
                to the console.
```
