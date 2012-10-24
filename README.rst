===============
renfe-notifier
===============

What it does.
==============

This script notifies you when there is a train (Renfe, Spain) next to leave the
configured station (in the next 10 to 15 minutes by default).

Nothing more, nothing less... :D


What I need.
=============

To use ``renfe-notifier``, you only need:

* Python
* Requests (python module)
* Mplayer (optional, to execute a sound with the notification)

To install the requirements (in a Debian GNU/Linux or derivate system) execute::

    $ sudo apt-get install mplayer python-pip
    $ sudo pip install requests


How to install it.
==================

There is no installation, just execute it :)


How to use
===========

To run it, you only need to execute the provided script::

  $ chmod +x renfe-notifier
  $ ./renfe-notifier

Previously you need to configure the route you want to be notified on. To do this,
open it and edit the global variables at the top of the file.

To find the correct values of the ``O``, ``D`` and ``DF`` variables you have
to check the request done in the renfe.com webpage after doing a search.

You can provide two parameters when executing the script. The high and low limit
to look for the trains. These parameters need to be written in minutes.


Author
=======
* `Jose Ignacio Galarza (igalarzab)`_

  .. _`Jose Ignacio Galarza (igalarzab)`: http://github.com/igalarzab
