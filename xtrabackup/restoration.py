"""Xtrabackup script

Usage:
    pyxtrabackup-restore --base-archive=<base_archive_path> --incremental-archive=<incremental_archive_path> --user=<user> [--password=<pwd>] [--data-dir=<data_dir>] [--restart] [--tmp-dir=<tmp>] [--log-file=<log>] [--backup-threads=<threads>]
    pyxtrabackup-restore (-h | --help)
    pyxtrabackup --version


Options:
    -h --help                                           Show this screen.
    --version                                           Show version.
    --user=<user>                                       MySQL user.
    --password=<pwd>                                    MySQL password.
    --base-archive=<base_archive_path>                  Base backup.
    --incremental-archive=<incremental_archive_path>    Incremental archive target.
    --data-dir=<data_dir>                               MySQL server data directory [default: /var/lib/mysql]
    --restart                                           Restart the server after backup restoration.
    --tmp-dir=<tmp>                                     Temp folder [default: /tmp].
    --log-file=<log>                                    Log file [default: /var/log/pyxtrabackup-restore.log].
    --backup-threads=<threads>                          Threads count [default: 1].

"""
from docopt import docopt
import sys
import logging
from xtrabackup.tools import BackupTool


def main():
    arguments = docopt(__doc__, version='1.0')
    try:
        pass
    except Exception:
        logger = logging.getLogger(__name__)
        logger.error("An error occured during the restoration process.",
                     exc_info=True)
        exit(1)
    exit(0)


if __name__ == '__main__':
    sys.exit(main())
