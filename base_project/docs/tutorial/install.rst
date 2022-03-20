.. _install-software:

Install the software
=====================

The next step is to install the software. Raspberry PiOS Bullseye Lite has been tested.

The BrachioGraph library requires a few additional components. It needs to be run in a Python 3 environment, using
Python 3.6 or later. Raspberry PiOS Bullseye will provide Python 3.9 or later.


Install system packages
-----------------------

You may have some of these installed already, but that shouldn't matter.

::

    sudo apt install -y python3-venv python3-tk pigpiod libjbig0 libjpeg-dev liblcms2-2 libopenjp2-7 libtiff5 libwebp6 libwebpdemux2 libwebpmux3 libzstd1 libatlas3-base libgfortran5 git

The packages include:

* ``venv``, for managing virtual environments under Python 3
* `PIGPIO <http://abyz.me.uk/rpi/pigpio/index.html>`_, an excellent library that provides hardware control of the
  Pi's GPIO pins - important for accurate timing of pulses. It comes with a Python interface to the lower-level code.
* various system libraries required by the Pillow Python imaging library
* ``libatlas3-base`` and ``libgfortran5``, required by the Numpy Python mathematics library
* ``python3-tk``, for the Turtle graphics integration
* Git

.. _set-up-venv:

Set up a virtual environment
----------------------------

Create and activate a `Python virtual environment <https://docs.python.org/3/library/venv.html>`_ to work in::

    python3 -m venv env
    source env/bin/activate

The environment needs to be active whenever you are using the plotter. You can tell when the virtual environment is
active from the bash prompt::

    (env) pi@raspberrypi:~ $

If you need to reactivate the environment, run ``source env/bin/activate`` once again, in this directory,


Clone the BrachioGraph repository
---------------------------------

Use Git to clone the ``BrachioGraph`` repository from https://github.com/evildmp/brachiograph::

    git clone git@github.com:evildmp/BrachioGraph.git

You will need to have set up a public key using ``ssh-keygen`` and `added your public key to your GitHub account
<https://github.com/settings/ssh/new>`_ for this to work. Or, you can use HTTPS instead::

    git clone https://github.com/evildmp/BrachioGraph.git


Install Python packages
-----------------------

Pinned versions of the Python packages are listed in ``requirements.txt`` in the BrachioGraph directory. Install them
by running::

    cd BrachioGraph
    pip install -r requirements.txt

This will install:

* `Numpy <numpy>`_, a Python mathematics library
* PIGPIO's Python library
* `Pillow <http://pillow.readthedocs.io>`_, the most widely-used Python imaging library.
* ``tqdm``, for the progress indicator while drawing
* ``readchar``, to allow the ``BrachioGraph.drive()`` methods to accept user input
* ``pytest``, to run the test suite

You only need to install them once in your virtual environment. Next time you activate the virtual environment, you'll
find that they're still there.
