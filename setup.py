from setuptools import setup

setup(
	name='ClassAttendanceRegister',
	version='1.0',
	py_modules=['class_attendance'],
	install_requires=[
		'Click',
		'colorama',
        'termcolor',
        'pyfiglet'
	],
	entry_points='''
		[console_scripts]
		class_attendance=class_attendance:cli
	'''
)