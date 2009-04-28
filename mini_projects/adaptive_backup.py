#!/usr/bin/python
# Filename : adaptive_backup.py

import os
import time
import tarfile

#List of directories and files to backup
bk_src = ['/home/pshah/Documents', 
          '/home/pshah/Templates']

#Directory where the backup will be stored
bk_dest = '/home/pshah/bk/'

bk_fn = bk_dest + time.strftime('%Y%m%d%H%M%S') + '.tgz'
zip_cmd = "zip -qr '%s' %s" % (bk_fn, ' '.join(bk_src))

tar_file = tarfile.open(bk_fn, 'w:gz')
for file in bk_src:
  tar_file.add(file)
tar_file.close()

