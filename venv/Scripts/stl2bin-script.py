#!C:\Users\cdog2\PycharmProjects\STLGen\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'numpy-stl==2.10.1','console_scripts','stl2bin'
__requires__ = 'numpy-stl==2.10.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('numpy-stl==2.10.1', 'console_scripts', 'stl2bin')()
    )
