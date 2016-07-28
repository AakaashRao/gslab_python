#! /usr/bin/env python
#****************************************************
# GET LIBRARY
#****************************************************
import subprocess, shutil, os
gslab_make_path = os.getenv('gslab_make_path')
subprocess.call('svn export --force -r 23124 ' + gslab_make_path + ' gslab_make', shell = True)
from gslab_make.py.get_externals import *
from gslab_make.py.make_log import *
from gslab_make.py.run_program import *
from gslab_make.py.dir_mod import *

#****************************************************
# MAKE.PY STARTS
#****************************************************

# SET DEFAULT OPTIONS
set_option(makelog = 'log/make.log', output_dir = './log', temp_dir = '')

clear_output_dirs()
start_make_logging()

# RUN ALL TESTS
run_python(program = 'test/run_all_tests.py', log = 'log/test.log', changedir = True)

end_make_logging()

shutil.rmtree('gslab_make')
raw_input('\n Press <Enter> to exit.')
