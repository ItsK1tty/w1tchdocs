
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
* :ref:`Vector2` (float ``x``, float ``y``)
* :ref:`Vector3` (float ``x``, float ``y``, float ``z``)
* :ref:`ColorRGB` (int ``r``, int ``g``, int ``b``)
* :ref:`ColorRGBA` (int ``r``, int ``g``, int ``b``, int ``a``)


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

.. _Vector2:

Vector2
----------------------
Vector2 definition here

.. _Vector3:

Vector3
----------------------
Vector3 definition here

.. _ColorRGB:

ColorRGB
----------------------
ColorRGB definition here

.. _ColorRGBA:

ColorRGBA
----------------------
ColorRGBA definition here



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

draw_box(``hash``, ``draw``, ``x``, ``y``, ``w``, ``h``, ``color``, ``rounding`` = ``0``, ``rounding_flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draws a box with the given color and rounding.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the box to draw. Hash is used to identify the box, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the box or not. Pass ``true`` to draw the box, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``color`` (``vector<int>``) -- The color of the box. ``{R, G, B, A}``
*   ``rounding`` (``float``) -- The rounding rule of the box. Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. Default is ``0``.

More about rounding flags: :doc:`roundingflags`

**Returns:**

* ``None``


**Example:**

.. code-block:: lua
   :linenos:
   
   draw_box("MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 10, 0);


draw_box_filled(``hash``, ``draw``, ``x``, ``y``, ``w``, ``h``, ``color``, ``rounding`` = ``0``, ``rounding_flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draws a filled box with the given color and rounding.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the box to draw. Hash is used to identify the box, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the box or not. Pass ``true`` to draw the box, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``color`` (``vector<int>``) -- The color of the box. ``{R, G, B, A}``
*   ``rounding`` (``float``) -- The rounding rule of the box. Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. Default is ``0``.

More about rounding flags: :doc:`roundingflags`

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:
   
   draw_box_filled("MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 10, 0);

draw_box_border_filled(``hash``, ``draw``, ``x``, ``y``, ``w``, ``h``, ``borderSize``, ``color``, ``colorBorder``, ``borderFilled`` = ``true``, ``rounding`` = ``0``, ``rounding_flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Draws a filled border box with the given color and rounding.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the box to draw. Hash is used to identify the box, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the box or not. Pass ``true`` to draw the box, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``borderSize`` (``float``) -- The width of the border (in pixels)
*   ``color`` (``vector<int>``) -- The color of the box. ``{R, G, B, A}``
*   ``colorBorder`` (``vector<int>``) -- The color of the border. ``{R, G, B, A}``
*   ``borderFilled`` (``bool``) -- Whether to fill the border or not. Default is ``true``.
*   ``rounding`` (``float``) -- The rounding rule of the box. Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. Default is ``0``.

More about rounding flags: :doc:`roundingflags`

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:
   
   draw_box_border_filled("MyHash", true, 0, 0, 100, 100, 10, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true, 10, 0);

draw_circle(``hash``, ``draw``, ``x``, ``y``, ``radius``, ``color``, ``segments`` = ``16``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. warning::
    This function's documentation lacks testing and information. 

Draws a circle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the circle to draw. Hash is used to identify the circle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the circle or not. Pass ``true`` to draw the circle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``vector<int>``) -- The color of the circle. ``{R, G, B, A}``
*  ``segments`` (``int``) -- The number of segments of the circle. Default is ``16``. Better to keep between ``1-50``. Going further may cause the process to crash.

**Returns:**

* ``None``


**Example:**

.. code-block:: lua
   :linenos:
   
   draw_circle("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, 16);


draw_circle_filled(``hash``, ``draw``, ``x``, ``y``, ``radius``, ``color``, ``segments`` = ``16``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   This function's documentation lacks testing and information. 

Draws a filled circle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the circle to draw. Hash is used to identify the circle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the circle or not. Pass ``true`` to draw the circle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``vector<int>``) -- The color of the circle. ``{R, G, B, A}``
*  ``segments`` (``int``) -- The number of segments of the circle. Default is ``16``. Better to keep between ``1-50``. Going further may cause the process to crash.

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:

   draw_circle_filled("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, 16);


draw_circle_border_filled(``hash``, ``draw``, ``x``, ``y``, ``radius``, ``color``, ``colorBorder``, ``borderFilled`` = ``true``, ``segments`` = ``16``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   This function's documentation lacks testing and information. 

Draws a filled border circle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the circle to draw. Hash is used to identify the circle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the circle or not. Pass ``true`` to draw the circle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``vector<int>``) -- The color of the circle. ``{R, G, B, A}``
*  ``colorBorder`` (``vector<int>``) -- The color of the border. ``{R, G, B, A}``
*  ``borderFilled`` (``bool``) -- Whether to fill the border or not. Default is ``true``.
*  ``segments`` (``int``) -- The number of segments of the circle. Default is ``16``. Better to keep between ``1-50``. Going further may cause the process to crash.

**Returns:**

* ``None``


**Example:**

.. code-block:: lua
   :linenos:

   draw_circle_border_filled("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true, 16);

draw_triangle(``hash``, ``draw``, ``x``, ``y``, ``color``, ``size`` = ``1.1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   This function's documentation lacks testing and information. 

Draws a triangle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not. Pass ``true`` to draw the triangle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``size`` (``float``) -- The size of the triangle (in pixels). Default is ``1.1``.

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:
      
   draw_triangle("MyHash", true, 0, 0, { 255, 255, 255, 255 }, 1.1);


draw_triangle_filled(``hash``, ``draw``, ``x``, ``y``, ``color``, ``size`` = ``1.1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   This function's documentation lacks testing and information. 

Draws a filled triangle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not. Pass ``true`` to draw the triangle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``size`` (``float``) -- The size of the triangle (in pixels). Default is ``1.1``.

**Returns:**

* ``None``


**Example:**

.. code-block:: lua
   :linenos:

   draw_triangle_filled("MyHash", true, 0.f, 0.f, { 255, 255, 255, 255 }, 1.1);


draw_triangle_border_filled(``hash``, ``draw``, ``x``, ``y``, ``color``, ``colorBorder``, ``borderFilled`` = ``true``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   This function's documentation lacks testing and information. 

Draws a filled border triangle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not. Pass ``true`` to draw the triangle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``colorBorder`` (``vector<int>``) -- The color of the border. ``{R, G, B, A}``
*  ``borderFilled`` (``bool``) -- Whether to fill the border or not. Default is ``true``.

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:

   draw_triangle_border_filled("MyHash", true, 0, 0, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true);

draw_text(``hash``, ``draw``, ``text``, ``x``, ``y``, ``scale``, ``color``, ``flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
   This function's documentation lacks testing and information. 

Draws a text with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the text to draw. Hash is used to identify the text, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the text or not. Pass ``true`` to draw the text, ``false`` to do otherwise.
*  ``text`` (``string``) -- The text to draw.
*  ``x`` (``float``) -- The X coordinate of the text's center.
*  ``y`` (``float``) -- The Y coordinate of the text's center.
*  ``scale`` (``float``) -- The scale of the text. Default is ``1``.
*  ``color`` (``vector<int>``) -- The color of the text. ``{R, G, B, A}``
*  ``flags`` (``int``) -- The flags for the text. Default is ``0``.

More about text flags: :doc:`textflags`

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:

   draw_text("MyHash", true, "Hello World", 0, 0, 1, { 255, 255, 255, 255 }, 0);



is_color_picker_rendering()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if the color picker is active.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Returns ``True`` if the color picker is active, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:
      
   if is_color_picker_rendering() then
      system.log_warning("The color picker is active!"); -- Prints if the color picker is active.
   end

is_cursor_hover_menu()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if the cursor is hovering over the menu.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Returns ``True`` if the cursor is hovering over the menu, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   if is_cursor_hover_menu() then
      system.log_warning("The cursor is hovering over the menu!"); -- This will only be logged if the cursor is hovering over the menu.
   end

is_cursor_hover_option()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if the cursor is hovering over an option.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Returns ``True`` if the cursor is hovering over an option, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:
      
   if is_cursor_hover_option() then
      system.log_warning("The cursor is hovering over an option!"); -- This will only be logged if the cursor is hovering over an option.
   end

is_input_active();
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if the input window is active. (The input window is for example, the window that appears when you press the ` key in story mode)

**Parameters:**

* None

**Returns:**

* ``bool`` -- Returns ``True`` if the input window is active, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:
      
   if is_input_active() then
      system.log_warning("The input window is active!"); -- This will only be logged if the input window is active.
   end


get_border_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the process window's border size.

**Parameters:**

* None

**Returns:**

* ``float``

**Example:**

.. code-block:: lua
   :linenos:
      
   local borderSize = ; -- Gets the border size.
   system.log_warning("The border size is " .. borderSize .. "."); -- Prints the border size.

get_fps()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current FPS.

**Parameters:**

* None

**Returns:**

* ``float``

**Example:**

.. code-block:: lua
   :linenos:
      
   local fps = get_fps(); -- Gets the FPS.
   system.log_warning("The FPS is " .. fps .. "."); -- Prints the FPS.

get_menu_rounding();
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the menu's rounding.

**Parameters:**

* None

**Returns:**

* ``float``

**Example:**

.. code-block:: lua
   :linenos:
      
   local rounding = get_menu_rounding(); -- Gets the rounding.
   system.log_warning("The rounding is " .. rounding .. "."); -- Prints the rounding.


float get_menu_width();
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the menu's width.

**Parameters:**

* None

**Returns:**

* ``float``

**Example:**

.. code-block:: lua
   :linenos:
      
   local width = get_menu_width(); -- Gets the width.
   system.log_warning("The width is " .. width .. "."); -- Prints the width.



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

dir_exist(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if directory exists.

**Parameters:**

* ``dir`` (``string``) -- Directory to check

**Returns:**

* ``bool`` -- ``True`` if directory exists, ``false`` otherwise

file_exist(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if file exists.

**Parameters:**

* ``file`` (``string``) -- File to check

**Returns:**

* ``bool`` -- ``True`` if file exists, ``false`` otherwise


file_remove(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a file.

**Parameters:**

* ``file`` (``string``) -- File to remove

**Returns:**

* ``bool`` -- ``True`` if file was removed, ``false`` otherwise (e.g. file was not found)

file_validate(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if file is corrupted, checks if the permissions are correct, if it's readable and if it's writable.

**Parameters:**

* ``file`` (``string``) -- File to validate

**Returns:**

* ``bool`` -- ``True`` if file is valid, ``false`` otherwise (e.g. file was not found)

is_file_empty(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if file is empty.

**Parameters:**

* ``file`` (``string``) -- File to check

**Returns:**

* ``bool`` -- ``True`` if file is empty, ``false`` otherwise

dir_check(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if directory exists, and if not, create it.

**Parameters:**

* ``dir`` (``string``) -- Directory to check

**Returns:**

``None``

dir_create(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a directory.

**Parameters:**

* ``dir`` (``string``) -- Directory to create

**Returns:**

``None``

file_copy(``source``, ``dest``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copies a file.

**Parameters:**

* ``source`` (*string*) -- Path to source file
* ``dest`` (*string*) -- Path to destination file

**Example**

.. code-block:: lua
   :linenos:

   file_copy("source.txt", "dest.txt");

   file_copy("files/source.txt", "files/dest.txt");

**Returns:**

``None``

.. _playerNS:

Player namespace
----------------------

Functions here

.. _pedNS:

Ped namespace
----------------------

add_relationship_group(``name``, ``groupHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    This function's documentation lacks testing and information. It is not recommended to use this function.

Add a relationship group

**Parameters:**

* ``name`` (``string``) -- Name of the relationship group
* ``groupHash`` (``Hash``) -- Hash of the relationship group

**Returns:**

* ``None``

**Example:**

.. code-block:: lua
   :linenos:
   
   add_relationship_group("MyGroup", "MyHash")

can_create_random_cops()
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    This function's documentation lacks testing and information. It is not recommended to use this function.

Check if random cops can be created

**Parameters:**
* ``None``

**Returns:**
* ``bool`` -- ``True`` if random cops can be created, ``false`` otherwise

**Example:**

.. code-block:: lua
   :linenos:
   
   local fuckingshit = can_create_random_cops(); system.log_warning(fuckingshit);

can_ped_ragdoll(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    This function's documentation lacks testing and information. It is not recommended to use this function.

Check if a ped can ragdoll

**Parameters:**
* ``ped`` (``Ped``) -- Ped to check

**Returns:**
* ``bool`` -- ``True`` if ped can be ragdolled, ``false`` otherwise

**Example:**
.. code-block:: lua
   :linenos:
   
   can_ped_ragdoll(ped)

clear_all_ped_props(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    This function's documentation lacks testing and information. It is not recommended to use this function.

Clear all ped props

**Parameters:**
* ``ped`` (``Ped``) -- Ped to clear props from

**Returns:**
* ``None``

**Example:**
.. code-block:: lua
   :linenos:
   
   clear_all_ped_props(ped)

clear_ped_blood_damage(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    This function's documentation lacks testing and information. It is not recommended to use this function.

Clear ped blood damage

**Parameters:**
* ``ped`` (``Ped``) -- Ped to clear blood damage from

**Returns:**
* ``None``

**Example:**
.. code-block:: lua
   :linenos:
   
   clear_ped_blood_damage(ped)

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