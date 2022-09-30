# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name and Extension
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# ------------------------
# getLogger => Return a Logger With the Specified Name

import logging

# print(dir(logging))

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("Shehab")

my_logger.warning("This Is Warning Message")