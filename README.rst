=========
pytest-qr
=========

.. image:: https://img.shields.io/pypi/v/pytest-qr.svg
    :target: https://pypi.org/project/pytest-qr
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-qr.svg
    :target: https://pypi.org/project/pytest-qr
    :alt: Python versions

pytest plugin to generate test result QR codes

----

Features
--------

* prints a QR code :)


Requirements
------------

* `qrcode`


Installation
------------

You can install "pytest-qr" via `pip`_ from `PyPI`_::

    $ pip install pytest-qr


Usage
-----

Run `py.test` with `--qr`::

    $ py.test --qr
    …
        █▀▀▀▀▀█ █ █ ▀▄█ ██▄▀▄ █▀▀▀▀▀█    
        █ ███ █ ▄ ▀█▄█▄▄ ▄█▀▀ █ ███ █    
        █ ▀▀▀ █  █ ▀▄   █▀▀█▄ █ ▀▀▀ █    
        ▀▀▀▀▀▀▀ █ █ ▀ █ ▀▄▀ ▀ ▀▀▀▀▀▀▀    
        ▀ ██▄█▀█▄ █▀█▄▀ ▀▀▄█▄▄█▄▄█ █▀    
        ▄ ██▄▀▀▀█▀ █▀█▄ ▄▀ ▄█▀▄▄ ▄▀█     
        ██▄▀█ ▀ ██▄█▀▀▀█▀▄▄█ █▄   █ ▀    
        ▄▄▄▄▄▀▀▄██ ▀   ▄▄▀ ▀▀▀ ▀█▀ ▀█    
          ▄█ █▀  ▄▀▄█▀███▄▀▀█▄ ▄▀ ▄▀█    
        ▀  ██ ▀ █▄▄▄█ ▀▀▄██ ██▄█ ▀▄▄▄    
         ▀   ▀▀ ▄▄█ █ ▄ ███▀█▀▀▀█▀▀█▀    
        █▀▀▀▀▀█ █ ▀▀ ▄▀ ▀▀▄▀█ ▀ █ ▀▀     
        █ ███ █ ▄ ██▄▄▄█▄█▄ ▀▀▀▀█▀▄▀█    
        █ ▀▀▀ █ ▀▀▄█▄▀█▄▀ ▄  ▄ █▄█ ▄▀    
        ▀▀▀▀▀▀▀ ▀▀▀ ▀▀  ▀ ▀▀▀  ▀   ▀     


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-qr" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/evgeni/pytest-qr/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
