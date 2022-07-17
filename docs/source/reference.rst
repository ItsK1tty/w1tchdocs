
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

log_chat(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as [CHAT]. Has a purple color.

**Parameters:**

* ``text`` (``string``) - The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_chat("Hello World!")

log_debug(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as [DEBUG]. Has a grey color.

**Parameters:**

* ``text`` (``string``) - The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_debug("Hello World!")

log_info(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as [INFO]. Has a blue color.

**Parameters:**

* ``text`` (``string``) - The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_info("Hello World!")

log_online(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as [ONLINE]. Has a bright yellow color.

**Parameters:**

* ``text`` (``string``) - The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_online("Hello World!")


log_protex(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as [PROTEX]. Has a light blue color.

**Parameters:**

* ``text`` (``string``) - The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_protex("Hello World!")

log_warning(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as [WARNING]. Has a red color.

**Parameters:**

* ``text`` (``string``) - The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_warning("Hello World!")

wait(ms)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Waits for ``ms`` milliseconds.

**Parameters:**

* ``ms`` (``int``) - The number of milliseconds to wait. Can be `-1`, but not less.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.wait(10000) -- Waits for 10 seconds


add_task(``name``, ``hash``, ``ms``, ``fn``)

Adds a task into the process's main loop.

.. note::

   DO NOT USE ``system.wait()`` inside task functions! You can use it only in the options functions!

**Parameters:**

* ``name`` (``string``) - The name of the task.
* ``hash`` (``string``) - The hash of the task. Hash is used to identify the task, so it must be unique.
* ``ms`` (``int``) - The number of milliseconds to wait before calling the task. Can be `-1` to execute the task again and again.
* ``fn`` (``function``) - The function to call when the task is executed.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   function my_script_function()
        system.log_info("Hello World!")
   end
   system.add_task("My script task", "luaTestTaskHash", 1000, my_script_function)
   --or
   function my_script_function()
        -- Test key press
        bKeyPressed = system.is_key_pressed("F")
        if bKeyPressed then
            system.log_warning("Pressed F to pay respect!")
        end
   end
   system.add_task("My script task", "luaTestTaskHash", -1, my_script_function)

remove_task(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a task from the process's main loop.

**Parameters:**

* ``hash`` (``string``) - The hash of the task to remove.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   function my_script_function()
        system.log_info("Hello World!")
   end
   system.add_task("My script task", "luaTestTaskHash", 1000, my_script_function)
   system.remove_task("luaTestTaskHash")


add_chat_listener(``name``, ``hash``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Connects a chat listener that calls a task every time a message is sent in the chat.

.. note::

   Chat listener only reacts to other player's chat messages, not your own ones.

.. note::

   DO NOT USE ``system.wait()`` inside task functions! You can use it only in the options functions!


**Parameters:**

* ``name`` (``string``) - The name of the task.
* ``hash`` (``string``) - The hash of the task. Hash is used to identify the task, so it must be unique.
* ``fn`` (``function``) - The function to call when the task is executed.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   function my_script_function(text)
        system.log_info("Hello World!")
   end
   system.add_chat_listener("My script task", "luaTestTaskHash", my_script_function)

remove_chat_listener(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnects a chat listener for a certain task.

**Parameters:**

* ``hash`` (``string``) - The hash of the task to remove.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   function my_script_function(text)
        system.log_info("Hello World!")
   end
   system.add_chat_listener("My script task", "luaTestTaskHash", my_script_function)
   system.remove_chat_listener("luaTestTaskHash")


string_to_key(``key``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a string key to a key hash.

**Parameters:**

* ``key`` (``string``) - The key to convert.

**Returns:**

* ``int`` - The key hash. -1 if the key is not any special key or it doesn't exist at all

**Example:**
.. code-block:: lua
   :linenos:


   system.log_info(tostring(system.string_to_key("HOME"))) -- get "HOME" key hash

string key_to_string(``key``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a key hash to a string key.

**Parameters:**

* ``key`` (``int``) - The key hash to convert.

**Returns:**

* ``string`` - The key as string.

**Example:**

.. code-block:: lua
   :linenos:

   system.log_info(tostring(system.key_to_string(36))) -- get "HOME" key hash

   -- why 36, you ask? See this: https://www.oreilly.com/library/view/javascript-dhtml/9780596514082/apb.html



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

* ``void``


**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_box("MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 10, 0)


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

* ``void``

**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_box_filled("MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 10, 0)

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

* ``void``

**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_box_border_filled("MyHash", true, 0, 0, 100, 100, 10, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true, 10, 0)

draw_circle(``hash``, ``draw``, ``x``, ``y``, ``radius``, ``color``, ``segments`` = ``16``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



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

* ``void``


**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_circle("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, 16)


draw_circle_filled(``hash``, ``draw``, ``x``, ``y``, ``radius``, ``color``, ``segments`` = ``16``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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

* ``void``

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_circle_filled("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, 16)


draw_circle_border_filled(``hash``, ``draw``, ``x``, ``y``, ``radius``, ``color``, ``colorBorder``, ``borderFilled`` = ``true``, ``segments`` = ``16``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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

* ``void``


**Example:**

.. code-block:: lua
   :linenos:

   render.draw_circle_border_filled("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true, 16)

draw_triangle(``hash``, ``draw``, ``x``, ``y``, ``color``, ``size`` = ``1.1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draws a triangle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not. Pass ``true`` to draw the triangle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``size`` (``float``) -- The size of the triangle (in pixels). Default is ``1.1``.

**Returns:**

* ``void``

**Example:**

.. code-block:: lua
   :linenos:
      
   render.draw_triangle("MyHash", true, 0, 0, { 255, 255, 255, 255 }, 1.1)


draw_triangle_filled(``hash``, ``draw``, ``x``, ``y``, ``color``, ``size`` = ``1.1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Draws a filled triangle with the given color.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not. Pass ``true`` to draw the triangle, ``false`` to do otherwise.
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``size`` (``float``) -- The size of the triangle (in pixels). Default is ``1.1``.

**Returns:**

* ``void``


**Example:**

.. code-block:: lua
   :linenos:

   render.draw_triangle_filled("MyHash", true, 0.f, 0.f, { 255, 255, 255, 255 }, 1.1)


draw_triangle_border_filled(``hash``, ``draw``, ``x``, ``y``, ``color``, ``colorBorder``, ``borderFilled`` = ``true``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

* ``void``

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_triangle_border_filled("MyHash", true, 0, 0, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true)

draw_text(``hash``, ``draw``, ``text``, ``x``, ``y``, ``scale``, ``color``, ``flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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

* ``void``

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_text("MyHash", true, "Hello World", 0, 0, 1, { 255, 255, 255, 255 }, 0)



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
      
   if render.is_color_picker_rendering() then
      system.log_warning("The color picker is active!") -- Prints if the color picker is active.
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

   if render.is_cursor_hover_menu() then
      system.log_warning("The cursor is hovering over the menu!") -- This will only be logged if the cursor is hovering over the menu.
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
      
   if render.is_cursor_hover_option() then
      system.log_warning("The cursor is hovering over an option!") -- This will only be logged if the cursor is hovering over an option.
   end

is_input_active()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if the input window is active. (The input window is for example, the window that appears when you press the ` key in story mode)

**Parameters:**

* None

**Returns:**

* ``bool`` -- Returns ``True`` if the input window is active, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:
      
   if render.is_input_active() then
      system.log_warning("The input window is active!") -- This will only be logged if the input window is active.
   end


get_border_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the process window's border size.

**Parameters:**

* None

**Returns:**

* ``float`` -- The border size.

**Example:**

.. code-block:: lua
   :linenos:
      
   local borderSize = render.get_border_size() -- Gets the border size.
   system.log_warning("The border size is " .. tostring(borderSize) .. ".") -- Prints the border size.

get_fps()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current FPS.

**Parameters:**

* None

**Returns:**

* ``float`` -- The current FPS.

**Example:**

.. code-block:: lua
   :linenos:
      
   local fps = render.get_fps() -- Gets the FPS.
   system.log_warning("The FPS is " .. tostring(fps) .. ".") -- Prints the FPS.

get_menu_rounding()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the menu's rounding.

**Parameters:**

* None

**Returns:**

* ``float`` -- The menu's rounding.

**Example:**

.. code-block:: lua
   :linenos:
      
   local rounding = render.get_menu_rounding() -- Gets the rounding.
   system.log_warning("The rounding is " .. tostring(rounding) .. ".") -- Prints the rounding.


get_menu_width()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the menu's width.

**Parameters:**

* None

**Returns:**

* ``float`` -- The menu's width.

**Example:**

.. code-block:: lua
   :linenos:
      
   local width = render.get_menu_width() -- Gets the width.
   system.log_warning("The width is " .. tostring(width) .. ".") -- Prints the width.

get_font_header_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the font header size.

**Parameters:**

* None

**Returns:**

* ``int`` -- The font header size.

**Example:**

.. code-block:: lua
   :linenos:
      
   local headerSize = render.get_font_header_size() -- Gets the header size.
   system.log_warning("The header size is " .. tostring(headerSize) .. ".") -- Prints the header size.

get_font_helper_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the font helper size.

**Parameters:**

* None

**Returns:**

* ``int`` -- The font helper size.

**Example:**

.. code-block:: lua
   :linenos:
      
   local helperSize = render.get_font_helper_size() -- Gets the helper size.
   system.log_warning("The helper size is " .. tostring(helperSize) .. ".") -- Prints the helper size.


get_font_option_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the font option size.

**Parameters:**

* None

**Returns:**

* ``int`` -- The font option size.

**Example:**

.. code-block:: lua
   :linenos:
      
   local optionSize = render.get_font_option_size() -- Gets the option size.
   system.log_warning("The option size is " .. tostring(optionSize) .. ".") -- Prints the option size.

get_font_warning_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the font warning size.

**Parameters:**

* None

**Returns:**

* ``int`` -- The font warning size.

**Example:**

.. code-block:: lua
   :linenos:
      
   local warningSize = render.get_font_warning_size() -- Gets the warning size.
   system.log_warning("The warning size is " .. tostring(warningSize) .. ".") -- Prints the warning size.


get_menu_cursor_pos()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the cursor position.

**Parameters:**

* None

**Returns:**

``Vector2`` -- The cursor position.

**Example:**

.. code-block:: lua
   :linenos:
      
   local cursorPos = render.get_menu_cursor_pos() -- Gets the cursor position.
   system.log_warning("The cursor position is " .. tostring(cursorPos.x) .. ".") -- Prints the cursor X position coordinate.
   system.log_warning("The cursor position is " .. tostring(cursorPos.y) .. ".") -- Prints the cursor Y position coordinate.



get_menu_position()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the menu position.

**Parameters:**

* None

**Returns:**

``Vector2`` -- The menu position.

**Example:**

.. code-block:: lua
   :linenos:
      
   local menuPos = render.get_menu_position() -- Gets the menu position.
   system.log_warning("The menu position is " .. tostring(menuPos.x) .. ".") -- Prints the menu X position coordinate.
   system.log_warning("The menu position is " .. tostring(menuPos.y) .. ".") -- Prints the menu Y position coordinate.


get_menu_total_size()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the menu total size.

**Parameters:**

* None

**Returns:**

``Vector2`` -- The menu total size.

**Example:**

.. code-block:: lua
   :linenos:
      
   local totalSize = render.get_menu_total_size() -- Gets the menu total size.
   system.log_warning("The menu total size is " .. tostring(totalSize.x) .. ".") -- Prints the menu total X size.
   system.log_warning("The menu total size is " .. tostring(totalSize.y) .. ".") -- Prints the menu total Y size.


get_screen_resolution()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the screen resolution.

**Parameters:**

* None

**Returns:**

``Vector2`` -- The screen resolution.

**Example:**

.. code-block:: lua
   :linenos:
      
   local screenRes = render.get_screen_resolution() -- Gets the screen resolution.
   system.log_warning("The screen resolution is " .. tostring(screenRes.x) .. ".") -- Prints the screen X resolution.
   system.log_warning("The screen resolution is " .. tostring(screenRes.y) .. ".") -- Prints the screen Y resolution.

set_warning(``message``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Brings up a warning (as if a moderator was detected in a session)

**Parameters:**

   * ``message`` (``string``) -- The warning message.

**Returns:**

* None

**Example:**

   .. code-block:: lua
         :linenos:
         
         render.set_warning("This is a warning.") -- Brings up a warning.

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

**Example:**

.. code-block:: lua
   :linenos:
   
   if fs.dir_exist("C:\Users\") then
      system.log_warning("Directory exists.")

   end


file_exist(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if file exists.

**Parameters:**

* ``file`` (``string``) -- File to check

**Returns:**

* ``bool`` -- ``True`` if file exists, ``false`` otherwise

**Example:**

.. code-block:: lua
   :linenos:
   
   if not fs.file_exist("D:\NewFolder\BetterCallSaulS05E06.mp4") then
      system.log_warning("Better not to call Saul.")
   end


file_remove(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a file.

**Parameters:**

* ``file`` (``string``) -- File to remove

**Returns:**

* ``bool`` -- ``True`` if file was removed, ``false`` otherwise (e.g. file was not found)

**Example:**

.. code-block:: lua
   :linenos:
      
   local success = fs.file_remove("test.txt") -- Removes the file.
   if success then
      system.log_warning("File removed.") -- Prints a message if the file was removed.
   end

file_validate(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if file is corrupted, checks if the permissions are correct, if it's readable and if it's writable.

**Parameters:**

* ``file`` (``string``) -- File to validate

**Returns:**

* ``bool`` -- ``True`` if file is valid, ``false`` otherwise (e.g. file was not found)

**Example:**

.. code-block:: lua
   :linenos:
   
   if fs.file_validate("/test.txt") then
      system.log_warning("File is valid and ready.")
   end



is_file_empty(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if file is empty.

**Parameters:**

* ``file`` (``string``) -- File to check

**Returns:**

* ``bool`` -- ``True`` if file is empty, ``false`` otherwise

**Example:**

.. code-block:: lua
   :linenos:
   
   if fs.is_file_empty("test.txt") then
      system.log_warning("The file is empty.")
   else
      system.log_warning("The file is not empty.")
   end

dir_check(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if directory exists, and if not, creates it.

**Parameters:**

* ``dir`` (``string``) -- Directory to check

**Returns:**

``void``

**Example:**

.. code-block:: lua
   :linenos:
   
   fs.dir_check("D:\NewFolder") -- Creates the directory if it doesn't exist.

dir_create(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a directory.

**Parameters:**

* ``dir`` (``string``) -- Directory to create

**Returns:**

``void``

**Example**

.. code-block:: lua
   :linenos:
   
   fs.dir_create("D:\NewFolder") -- Creates a directory.

file_copy(``source``, ``dest``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copies a file.

**Parameters:**

* ``source`` (*string*) -- Path to source file
* ``dest`` (*string*) -- Path to destination file

**Returns:**

``void``

**Example**

.. code-block:: lua
   :linenos:

   fs.file_copy("source.txt", "dest.txt")
   -- or
   fs.file_copy("files/source.txt", "files/dest.txt")

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