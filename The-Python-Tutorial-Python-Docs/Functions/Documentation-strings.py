"""
The first line should always be a short, concise summary of the s purpose. For brevity, it should not explicitly state the s name or type, since these are available by other means (except if the name happens to be a verb describing a s operation). This line should begin with a capital letter and end with a period.

If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the s calling conventions, its side effects
"""
def my_function():
     """Do nothing, but document it.

     No, really, it doesn't do anything.
     """
     pass

print(my_function.__doc__)
