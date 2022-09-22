# ----------------------------------
# -- Regular Expressions => Intro --
# ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# +972 597747241=> https://regex101.com/r/GHtySL/1
# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# -----------------------------------------------------------------------
# [0-9] : Number From 0 to 9
# [^0-9] : Anything Except 0-9
# [A-Z] : Characters Form A to Z
# [^A-Z] : Anything Except Characters From A  to Z
# [a-z]
# [^a-z]
# [A-z] : All Characters
# shabbinessSaat
# 0597747241
#  https://regex101.com/r/OcwAmK/1
# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$
# https://regex101.com/r/PoWbVs/1
# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
# \	  Escape Special Characters
# ()  Separate Groups
# -----------------------------

# (\d-|\d\)|\d>) (\w+)
# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$

