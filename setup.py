from setuptools import setup, find_packages

__uname__ = 'pyrenfe'
__long_name__ = 'Train checker (Cercanias Renfe, Spain)'
__version__ = '2.0'
__author__ = 'Jose Ignacio Galarza'
__email__ = 'igalarzab@gmail.com'
__url__ = 'http://github.com/igalarzab/pyrenfe'
__license__ = 'MIT'

setup(
    name=__uname__,
    version=__version__,
    packages=find_packages(),

    author=__author__,
    author_email=__email__,
    description='Train timetable checker (Renfe Cercanias, Spain)',
    long_description='\n'.join([open('README.md').read()]),
    license=__license__,
    url=__url__,
    keywords='timetable,train,cercanias,renfe,spain',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],

    py_modules=['pyrenfe'],
    include_package_data=True,
    install_requires=['requests', 'lxml'],
    entry_points={
        'console_scripts': ['pyrenfe = pyrenfe:main']
    },
)

# vim: ai ts=4 sts=4 et sw=4
