from rootpy.io import open as ropen

with ropen('file.root') as f:
    myhist = f.somedirectory.histname

    # recursively walk through the file
    for path, dirs, objects in f.walk():
        # do something
        pass
