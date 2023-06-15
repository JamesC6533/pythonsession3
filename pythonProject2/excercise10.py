import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# Use glob.glob() to obtain filenames
filenames = glob.glob(pattern)

# Print the filenames
for filename in filenames:
    size = os.path.getsize(filename)
    if size > 0:
        basename = os.path.basename(filename)
        print(f"{filename}: {size} bytes: {basename}")