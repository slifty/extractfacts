#!D:\venv\cxf-35\Scripts\python.exe	

from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['bs4','difflib', 'psycopg2', 'hashlib', 'requests', 'pytz']}

setup(name = 'buster',
	version = '0.2',
	description = '',
	options = {'build.exe': build_exe_options},
	executables = [Executable('buster.py')])
