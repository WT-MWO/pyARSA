""""Space for useful functions not directly connected with RSA API"""


def write_list_to_file(list, path, filename):
    """Writes each item in list to new line in .txt file.
    Parameters:
        list(list): list with items
        path(string):  path for txt file
        filename(string): name for file
    """
    # Fix this function to write plain text without
    # parantesis always the same if its a set or list
    with open(path + filename, "w") as file:
        for item in list:
            file.write("{}\n".format(str(item)))
