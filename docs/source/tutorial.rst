Tutorial
================

.. _tutorial:

so the headlines dont exist here
they're called 'sections'

quick cheat sheet:

This will be first (and largest) type of section:


First section
##############

This will be the second (smaller) type of a section

Second section
=======================

it's important to note that that line should start from the newline right after the title, so this wouldn't work:

thiswouldntwork

======================

Third section (even smaller)
-------------------------------------

it is also important to note that the line should be equal or longer to the length of the section title, so this won't work:

ahfiouashfiuashfiuahfiushfiu
-----

Bullet lists
#######################

so bullet lists are quite simple you just need to do this:

* item 1
* item 2
* item 3

to add subitems, just do this:

* item 1
* * subitem 1
* * subitem 2
* * subitem 3

Classic inline formatting
#########################################################

* Bold text: **bold text**
* Italic text: *italic text* :pinching_fingers:
* idk how its called: ``this stuff``

code blocks:
near code-block word you can specify the language so the output will be highlighted
the :linenos: option will add line numbers to the code block


.. code-block:: lua
    :linenos:

    print("somestuff")

    if 1 then
        print("1")
    end

Warning:
=============

.. warning::
    this is a warning

Note:
==============

.. note::
    this is a note


Hyperlinks:
==============

this where fun at

so there are internal and external hyperlinks

internal hyperlinks mean hyperlinks between parts/sections of the same document or just a link to some other page

external hyperlinks mean hyperlinks to other pages on the internet

example

for internal hyperlinks, you first need to make a place holder. lemme show you:

``.. _name:`` this we use to make a place holder


* :ref:`test`



you can make a reference to another page:

:doc:`gettingstarted`

for external hyperlinks, see this

first we create a placeholder

.. _LUA guide: https://tylerneylon.com/a/learn-lua/

then we ref

Small LUA guide we recommend for new developers: `LUA guide`_. Credits to Tyler Neylon.

this basically it 

continuing samepage hyperlinks:

.. _test: 

test
----------------------
test definition here
