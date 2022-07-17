
DIS2RBED LUA reference
========================

There are multiple namespaces & types in the current DIS2RBED LUA framework, each with their own set of functions.

.. _lua_types:

Types in LUA Engine
######################

Types in LUA Engine are defined in the following order:

* :ref:`hash` (uint64)
* :ref:`Entity` (int)
* :ref:`Ped` (int)
* :ref:`Player` (int)
* :ref:`Cam` (int)
* :ref:`Blip` (int)
* :ref:`Any` (int)
* :ref:`Vehicle` (int)

.. _Hash:

Hash
----------------------
Hash definition here

.. _Entity:

Entity
----------------------
Entity definition here

.. _Ped:

Ped
----------------------
Ped definition here

.. _Player:

Player
----------------------
Player definition here

.. _Cam:

Cam
----------------------
Cam definition here

.. _Blip:

Blip
----------------------
Blip definition here

.. _Any:

Any
----------------------
Any type definition here

.. _Vehicle:

Vehicle
----------------------
Vehicle definition here

..

   # with overline, for chapters
   = for sections
   - for subsections
   ^ for subsubsections
   " for paragraph

.. _namespaces:

Namespaces in LUA Engine
###########################

Function namespaces in LUA Engine are defined in the following order:


* :ref:`system`
* :ref:`menu`
* :ref:`stats`   
* :ref:`notify`
* :ref:`script`
* :ref:`globals`
* :ref:`locals`
* :ref:`render`
* :ref:`self`
* :ref:`lobby`
* :ref:`text`
* :ref:`fs`
* :ref:`playerNS`
* :ref:`pedNS`
* :ref:`vehicleNS`
* :ref:`entityNS`
* :ref:`object`
* :ref:`weapon`
* :ref:`streaming`
* :ref:`ui`
* :ref:`draw`
* :ref:`camNS`
* :ref:`gameplay`
* :ref:`fire`
* :ref:`network`
* :ref:`cutscene`
* :ref:`controls`
* :ref:`graphics`
* :ref:`time`
* :ref:`ai`
* :ref:`decorator`
* :ref:`interior`
* :ref:`audio`
* :ref:`rope`


.. _system:

System namespace
----------------------

Functions here

.. _menu:

Menu namespace
----------------------

Functions here

.. _stats:

Stats namespace
----------------------

Functions here

.. _notify:

Notify namespace
----------------------

Functions here

.. _script:

Script namespace
----------------------

Functions here

.. _globals:

Globals namespace
----------------------

Functions here

.. _locals:

Locals namespace
----------------------

Functions here

.. _render:

Render namespace
----------------------

Functions here

.. _self:

Self namespace
----------------------

Functions here

.. _lobby:

Lobby namespace
----------------------

Functions here

.. _text:

Text namespace
----------------------

Functions here

.. _fs:

FS namespace
----------------------

dir_exist(string *``dir``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if directory exists.

**Parameters:**

* ``dir`` (*string*``) -- Directory to check

**Returns:**

* ``bool`` -- ``True`` if directory exists, ``false`` otherwise

file_exist(string *``file``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if file exists.

**Parameters:**

* ``file`` (*string*) -- File to check

**Returns:**

* ``bool`` -- ``True`` if file exists, ``false`` otherwise


file_remove(string *``file``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a file.

**Parameters:**

* ``file`` (*string*) -- File to remove

**Returns:**

* ``bool`` -- ``True`` if file was removed, ``false`` otherwise (e.g. file was not found)

file_validate(string *``file``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Validate file.

**Parameters:**

* ``file`` (*string*) -- File to validate

**Returns:**

* ``bool`` -- ``True`` if file is valid, ``false`` otherwise (e.g. file was not found)

is_file_empty(string *``file``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if file is empty.

**Parameters:**

* ``file`` (*string*) -- File to check

**Returns:**

* ``bool`` -- ``True`` if file is empty, ``false`` otherwise

dir_check(string *``dir``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if directory exists, and if not, create it.

**Parameters:**

* ``dir`` (*string*) -- Directory to check

**Returns:**

``void``

dir_create(string *``dir``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a directory.

**Parameters:**

* ``dir`` (*string*) -- Directory to create

**Returns:**

``void``

file_copy(string *``source``, string ``dest``*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy a file.

**Parameters:**

* ``source`` (*string*) -- Path to source file
* ``dest`` (*string*) -- Path to destination file

**Returns:**

``void``

.. _playerNS:

Player namespace
----------------------

Functions here

.. _pedNS:

Ped namespace
----------------------

Functions here

.. _vehicleNS:

Vehicle namespace
----------------------

Functions here

.. _entityNS:

Entity namespace
----------------------

Functions here

.. _object:

Object namespace
----------------------

Functions here

.. _weapon:

Weapon namespace
----------------------

Functions here

.. _streaming:

Streaming namespace
----------------------

Functions here

.. _ui:

UI namespace
----------------------

Functions here

.. _draw:

Draw namespace
----------------------

Functions here

.. _camNS:

Cam namespace
----------------------

Functions here

.. _gameplay:

Gameplay namespace
----------------------

Functions here

.. _fire:

Fire namespace
----------------------

Functions here

.. _network:

Network namespace
----------------------

Functions here

.. _cutscene:

Cutscene namespace
----------------------

Functions here

.. _controls:

Controls namespace
----------------------

Functions here

.. _graphics:

Graphics namespace
----------------------

Functions here

.. _time:

Time namespace
----------------------

Functions here

.. _ai:

AI namespace
----------------------

Functions here

.. _decorator:

Decorator namespace
----------------------

Functions here

.. _interior:

Interior namespace
----------------------

Functions here

.. _audio:

Audio namespace
----------------------

Functions here

.. _rope:

Rope namespace
----------------------

Functions here