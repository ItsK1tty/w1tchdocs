General Information
=====

.. _installation:

Installation path
------------

To install LUA scripts, you need to drop them into a directory that is ``%appdata%\DIS2RBED\Lua``:

.... code-block:: console
..
..   (.venv) $ pip install lumache
..
You can edit scripts with any editor you want, but DIS2RBED will only scan for them during initialization.

Small LUA guide we recommend for new developers: `LUA guide`_. Credits to Tyler Neylon.

.. _LUA guide: https://tylerneylon.com/a/learn-lua/

Found a mistake in documentation?
------------------------------

Feel free to contact us:

* `Issues`_
* `Pull Requests`_
* `Official website`_ 

.. _Issues: https://github.com/ItsK1tty/w1tchdocs/issues
.. _Pull Requests: https://github.com/ItsK1tty/w1tchdocs/pulls
.. _Official website: https://w1tch.net
..Creating recipes
..----------------

..To retrieve a list of random ingredients,
..you can use the ``lumache.get_random_ingredients()`` function:

.... autofunction:: lumache.get_random_ingredients

..The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
..or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
..will raise an exception.

.... autoexception:: lumache.InvalidKindError

..For example:

..>>> import lumache
..>>> lumache.get_random_ingredients()
..['shells', 'gorgonzola', 'parsley']

