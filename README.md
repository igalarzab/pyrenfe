# pyrenfe

## What it does.

This script helps you to know when there is a train (Renfe, Spain) next to
leave the configured station. Also, you can query the timetable of an specific
route.

Nothing more, nothing less... :D


## What I need.

To use ``pyrenfe``, you only need:

* python >= 2.7 (compatible with Python 3)
* requests (python module)
* lxml (python module)


## How to install it.

The package is uploaded to PyPI, so you just have to install the package with
``pip`` or ``easy_install``.

```sh
$ sudo pip install pyrenfe
```


## How to use

To run it, you only need to execute the program with the proper parameters.
Here you have some examples:

See the help of the program.

```sh
$ pyrenfe --help
```

Check the next train between Atocha and Principe Pio (when it will leave and
when will it arrive).

```sh
$ pyrenfe --origin 18000 --destine 10000
```

Show the same information, but inside a formatted table.

```sh
$ pyrenfe -o 18000 -d 10000 -p table
```

Check the timetable of all the trains between Atocha and Principe Pio for
today.

```sh
$ pyrenfe --origin 18000 --destine 10000 --timetable
```

As you can see the origin and the destine are provided with numbers. Those
numbers are the IDs of the stations. To take the IDs of your choice you have to
fill the [official form](http://www.renfe.com/viajeros/cercanias/madrid/index.html)
and then check in the POST which values are provided.

In the future I hope to add this functionality to the script (pull requests are
accepted :D).


# Author

* [Jose Ignacio Galarza (igalarzab)](http://github.com/igalarzab)
