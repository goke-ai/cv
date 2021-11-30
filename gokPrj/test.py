import os
srcPath = 'all_dataset'

for fname in os.listdir(srcPath):
    # if os.path.isdir(fname[1]):
    print(fname)

srcPaths = [srcPath + '/' + p for p in os.listdir(srcPath)]

print(srcPaths)