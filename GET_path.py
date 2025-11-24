def path():
    import os
    filepath = os.path.abspath(__file__)
    directory = os.path.dirname(filepath)
    return directory+"/"