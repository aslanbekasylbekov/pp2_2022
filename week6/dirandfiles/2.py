import os
print('Exist:', os.access('C:\PP2\week6\dirandfiles', os.F_OK))
print('Readable:', os.access('C:\PP2\week6\dirandfiles', os.R_OK))
print('Writable:', os.access('C:\PP2\week6\dirandfiles', os.W_OK))
print('Executable:', os.access('C:\PP2\week6\dirandfiles', os.X_OK))