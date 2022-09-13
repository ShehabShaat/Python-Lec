# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] There's One Line and Multiple Line Doc Strings
# -------------------------------------------------
# doc for multiple line = """ """
# doc for single line = ''' '''
def shehab_function(name):
    """
  Shehab Function
    It Says Hello From Shehab
  Parameter:
    name => Person Name That Use Function
  Return:
    Return Hello Message To The Person
  """
    print(f"Hello {name} From Shehab")


shehab_function("Ahmed")

print(dir(shehab_function))

print(shehab_function.__doc__)

help(shehab_function)
