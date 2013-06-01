from setuptools import setup, find_packages
import pyrenfe

setup(
    name=pyrenfe.__uname__,
    version=pyrenfe.__version__,
    description='Train timetable checker (Renfe Cercanias, Spain)',
    long_description='\n'.join([open('README.rst').read()]),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords='timetable,train,cercanias,renfe,spain',

    author=pyrenfe.__author__,
    author_email=pyrenfe.__email__,
    url=pyrenfe.__url__,
    license=pyrenfe.__license__,

    packages=find_packages(),
    py_modules=['pyrenfe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests', 'lxml'],
    entry_points={
        'console_scripts': ['pyrenfe = pyrenfe:main']
    },
)

# vim: ai ts=4 sts=4 et sw=4
