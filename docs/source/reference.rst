..   
   DIS2RBED LUA reference
   ========================
   ..
      There are multiple namespaces in the current DIS2RBED LUA framework:
      * :ref:`System namespace` - contains functions for system management
      * :ref:
   System namespace
   -----------------


      .. [log_chat] Sample funciton


      .. |name| replace:: replacement *text*


      def my_function(my_arg, my_other_arg):
         """A function just for me.

         :param my_arg: The first of my arguments.
         :param my_other_arg: The second of my arguments.

         :returns: A message (just for me, of course).
         """

      .. rst-class:: with-border
         Test
         Test

   

Usage
=====

.. _installation:

Installation
------------

To use Lumache, first install it using pip:
.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:
.. lua:autoclass:: MyOrg.Car

.. lua:automodule:: cls:test
..
   .. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
