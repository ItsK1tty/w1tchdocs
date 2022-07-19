DIS2RBED LUA reference
========================

There are multiple namespaces & types in the current DIS2RBED LUA framework, each with their own set of functions.

.. _lua_types:

Types in the LUA Engine
######################

Types in the LUA Engine are defined in the following order:

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

================================

.. _Hash:

Hash
----------------------
Hash definition here

================================

.. _Entity:

Entity
----------------------
Entity definition here

================================

.. _Ped:

Ped
----------------------
Ped definition here

================================

.. _Player:

Player
----------------------
Player definition here

================================

.. _Cam:

Cam
----------------------
Cam definition here

================================

.. _Blip:

Blip
----------------------
Blip definition here

================================

.. _Any:

Any
----------------------
Any type definition here

================================

.. _Vehicle:

Vehicle
----------------------
Vehicle definition here

================================

.. _Vector2:

Vector2
----------------------
Vector2 definition here

================================

.. _Vector3:

Vector3
----------------------
Vector3 definition here

================================

.. _ColorRGB:

ColorRGB
----------------------
ColorRGB definition here

================================

.. _ColorRGBA:

ColorRGBA
----------------------
ColorRGBA definition here

================================

.. _gvars:

Global Variables
###########################

* ``int`` ``chatSenderId`` -- Last chat message sender ID
* ``string`` ``chatSenderName`` -- Last chat message sender name
* ``string`` ``chatMessage`` -- Last chat message

================================

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
* :ref:`scripting`
* * :ref:`scripting_functions`
* * :ref:`playerNSS`
* * :ref:`pedNSS`
* * :ref:`entityNSS`
* * :ref:`vehicleNSS`
* * :ref:`online`
* * :ref:`networkNSS`
* * :ref:`spawn`
* * :ref:`weaponNSS`
* * :ref:`teleport`
* * :ref:`world`
* :ref:`rage`
* * :ref:`playerNSR`
* * :ref:`pedNSR`
* * :ref:`vehicleNSR`
* * :ref:`entityNSR`
* * :ref:`object`
* * :ref:`weaponNSR`
* * :ref:`streaming`
* * :ref:`ui`
* * :ref:`draw`
* * :ref:`camNS`
* * :ref:`gameplay`
* * :ref:`fire`
* * :ref:`networkNSR`
* * :ref:`cutscene`
* * :ref:`controls`
* * :ref:`graphics`
* * :ref:`time`
* * :ref:`ai`
* * :ref:`decorator`
* * :ref:`interior`
* * :ref:`audio`
* * :ref:`rope`

================================

.. _system:

System namespace
----------------------

This namespace contains functions that are used to interact with the DIS2RBED's task management and logging.

================================

log_chat(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as ``[CHAT]``. Has a purple color.

**Parameters:**

* ``text`` (``string``) -- The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_chat("Hello World!")

================================

log_debug(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as ``[DEBUG]``. Has a grey color.

**Parameters:**

* ``text`` (``string``) -- The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_debug("Hello World!")

================================

log_info(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as ``[INFO]``. Has a blue color.

**Parameters:**

* ``text`` (``string``) -- The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_info("Hello World!")

================================

log_online(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as ``[ONLINE]``. Has a bright yellow color.

**Parameters:**

* ``text`` (``string``) -- The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_online("Hello World!")

================================

log_protex(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as ``[PROTEX]``. Has a light blue color.

**Parameters:**

* ``text`` (``string``) -- The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_protex("Hello World!")

================================

log_warning(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a message to the log as ``[WARNING]``. Has a red color.

**Parameters:**

* ``text`` (``string``) -- The text to send to the log.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.log_warning("Hello World!")

================================

wait(``ms``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Waits for ``ms`` milliseconds.

**Parameters:**

* ``ms`` (``int``) -- The number of milliseconds to wait. If ``-1`` is set, skips ticks.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   system.wait(10000) -- Waits for 10 seconds

================================

add_task(``name``, ``hash``, ``ms``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a task into the process's main loop.

.. note::

   DO NOT USE ``system.wait()`` inside task functions! You can use it only in the options functions!

**Parameters:**

* ``name`` (``string``) -- The name of the task.
* ``hash`` (``string``) -- The hash of the task. Hash is used to identify the task, so it must be unique.
* ``ms`` (``int``) -- The number of milliseconds to wait before calling the task. 
* * Can be ``-1`` to execute the task again and again.
* ``fn`` (``function``) -- The function to call when the task is executed.

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
            system.log_info("Pressed F to pay respect!")
        end
   end
   system.add_task("My script task", "luaTestTaskHash", -1, my_script_function)

================================

remove_task(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a task from the process's main loop.

**Parameters:**

* ``hash`` (``string``) -- The hash of the task to remove.

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

================================

add_chat_listener(``name``, ``hash``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Connects a chat listener that calls a task every time a message is sent in the chat.

.. note::

   Chat listener only reacts to other player's chat messages, not your own ones.

.. note::

   DO NOT USE ``system.wait()`` inside task functions! You can use it only in the options functions!


**Parameters:**

* ``name`` (``string``) -- The name of the task.
* ``hash`` (``string``) -- The hash of the task. Hash is used to identify the task, so it must be unique.
* ``fn`` (``function``) -- The function to call when the task is executed.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   function my_script_function(text)
        system.log_info("Hello World!")
   end
   system.add_chat_listener("My script task", "luaTestTaskHash", my_script_function)

================================

remove_chat_listener(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnects a chat listener for a certain task.

**Parameters:**

* ``hash`` (``string``) -- The hash of the task to remove.

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

================================

string_to_key(``key``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a string key to a key hash.

**Parameters:**

* ``key`` (``string``) -- The key to convert.

**Returns:**

* ``int`` -- The key hash. -1 if the key is not any special key or it doesn't exist at all

**Example:**

.. code-block:: lua
   :linenos:

   system.log_info(tostring(system.string_to_key("HOME"))) -- get "HOME" key hash

================================

key_to_string(``key``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a key hash to a string key.

**Parameters:**

* ``key`` (``int``) -- The key hash to convert.

**Returns:**

* ``string`` -- The key as string.

**Example:**

.. code-block:: lua
   :linenos:

   system.log_info(tostring(system.key_to_string(36))) -- get "HOME" key hash

   -- why 36, you ask? See this: https://www.oreilly.com/library/view/javascript-dhtml/9780596514082/apb.html

================================

is_key_pressed(``key``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if key is pressed

**Parameters:**

* ``key`` (``string``) -- The key to check.

**Returns:**

* ``bool`` -- ``True`` if the key is pressed, ``false`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   function my_script_function(text)
      kPressed = system.is_key_pressed("F")
      if kPressed then
         system.log_info("Hello World!")
      end
   end

================================

.. _menu:

Menu namespace
----------------------

This namespace contains functions for creating and manipulating menu options and sections.

================================

Menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

======================

add_parent(``name``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a parent section into menu resolution.

**Parameters:**

* ``name`` (``string``) -- The name of the parent section.

**Returns:**

* ``int`` -- The ID of the parent section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_parent("My parent section")

======================

add_child(``name``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a child section to a parent section.

**Parameters:**

* ``name`` (``string``) -- The name of the child section.
* ``parent`` (``int``) -- The parent section.

**Returns:**

* ``int`` -- The ID of the child section.

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   child = menu.add_child("Child section of my parent section", parent)

======================

add_delimiter(``name``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a delimiter to a section.

**Parameters:**

* ``name`` (``string``) -- The name of the delimiter.
* ``parent`` (``int``) -- The parent section.

**Returns:**

* ``int`` -- The ID of the delimiter.

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_delimiter("Just a delimiter...", parent)

======================

add_option(``name``, ``hash``, ``parent``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a menu option button.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``parent`` (``int``) -- The parent section.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- A test function
   function test()
      log_info("Test function!")
   end
   
   parent = menu.add_parent("My parent section")

   menu.add_option("Lua Option", "luaOptHash", parent, test)

======================

add_option_toggle(``name``, ``hash``, ``parent``, ``fn``);
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable menu option button.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``parent`` (``int``) -- The parent section.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_toggle("Toggle Option", "luaOptDummyToggle", parent, function())

======================

add_option_slider(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``parent``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a slider menu option.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``parent`` (``int``) -- The parent section.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_slider("Slider Option", "luaOptDummyToggle", 10, 0, 100, 1, parent, function())

======================

add_option_slider_toggle(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``parent``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable slider menu option.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``parent`` (``int``) -- The parent section.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_slider_toggle("Toggable Slider Option", "luaOptDummyToggle", 10, 0, 100, 1, parent, function())

======================

add_option_value(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``parent``, ``valueSuffix``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a menu option with a pre-set value

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``parent`` (``int``) -- The parent section.
* ``valueSuffix`` (``string``) -- The value suffix text (e.g. ``m/s``)
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_value("Lua option with value", "luaOptDummyToggle", 10, 0, 100, 1, parent, "kb", function())

======================

add_option_value_toggle(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``parent``, ``valueSuffix``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable menu option with a pre-set value.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``parent`` (``int``) -- The parent section.
* ``valueSuffix`` (``string``) -- The value suffix text (e.g. ``m/s``)
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_value_toggle("Toggable Lua option with value", "luaOptDummyToggle", 10, 0, 100, 1, parent, "kb", function())

======================

add_option_value_str(``name``, ``hash``, ``value``, ``parent``, ``list``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a menu option with multiple values.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``parent`` (``int``) -- The parent section.
* ``list`` (``vector<string>``) -- The values list separated with a comma
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_value_str("Lua option with multiple values", "luaOptDummyToggle", 0, parent, { "One", "Two", "Three" }, function())

======================

add_option_value_str_toggle(``name``, ``hash``, ``value``, ``parent``, ``list``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable menu option with multiple values.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``parent`` (``int``) -- The parent section.
* ``list`` (``vector<string>``) -- The values list separated with a comma.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_value_str("Toggable Lua option with multiple values", "luaOptDummyToggle", 0, parent, { "One", "Two", "Three" }, function())

======================

add_option_teleport(``name``, ``coords``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a teleport option button.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``coords`` (``Vector3``) -- The teleport coordinates.
* ``parent`` (``int``) -- The parent section.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_teleport("Casino Entrance", { 922.680847, 47.205017, 81.106346 }, parent)

======================

add_option_spawn(``name``, ``model``, ``type``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a spawn option button.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``model`` (``Hash``) -- The vehicle hash.
* ``type`` (``int``) -- The vehicle spawn type.
* ``parent`` (``int``) -- The parent section.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_spawn("Spawn Zentorno", zentornoHash, 0, parent) -- 0 is vehicle_spawn type

======================

add_option_text(``name``, ``hash``, ``text``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a text option (e.g. a note).

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``text`` (``string``) -- The displayed text to the right of the name.
* ``parent`` (``int``) -- The parent section.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_text("Just a text option", "luaOptHashText", "Text", parent)

======================

add_option_info(``name``, ``hash``, ``info``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a text option. (e.g. a note).

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``info`` (``string``) -- Info to display to the right of the option name.
* ``parent`` (``int``) -- The parent section.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_text("Just a text option", "luaOptHashInfo", "Some info", parent)

======================

add_player_option(``name``, ``hash``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a player menu option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- Just a test function
   function test()
      log_info("Test function!")
   end

   menu.add_player_option("Lua Player Option", "luaOptHash", test)

======================

add_player_option_toggle(``name``, ``hash``, ``fn``);
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable player menu option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option_toggle("Toggle Player Option", "luaOptDummyToggle", function())

======================

add_player_option_slider(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a player menu slider option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_slider("Slider Player Option", "luaOptDummyToggle", 10, 0, 100, 1, function())

======================

add_player_option_slider_toggle(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable slider player menu option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_slider_toggle("Toggable Slider Player Option", "luaOptDummyToggle", 10, 0, 100, 1, function())

======================

add_player_option_value(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``valueSuffix``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a player menu option with a set value in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase
* ``valueSuffix`` (``string``) -- The value suffix text
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_value("Lua option with value", "luaOptDummyToggle", 10, 0, 100, 1, "kb", function())

======================

add_player_option_value_toggle(``name``, ``hash``, ``value``, ``min``, ``max``, ``mod``, ``valueSuffix``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable player menu option with a set value in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase
* ``valueSuffix`` (``string``) -- The value suffix text
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_value_toggle("Toggable Lua option with value", "luaOptDummyToggle", 10, 0, 100, 1, "kb", function())

======================

add_player_option_value_str(``name``, ``hash``, ``value``, ``list``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a player menu option with multiple values in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``list`` (``string``) -- The values list separed with a comma.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_value_str("Lua option with multiple values", "luaOptDummyToggle", 0, { "One", "Two", "Three" }, function())

======================

add_player_option_value_str_toggle(``name``, ``hash``, ``value``, ``list``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a toggable player menu option with multiple values in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``value`` (``float``) -- The option default value.
* ``list`` (``string``) -- The values list separed with a comma.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option_value_str("Toggable Lua option with multiple values", "luaOptDummyToggle", 0, { "One", "Two", "Three" }, function())

======================

add_player_option_text(``name``, ``hash``, ``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a player menu text option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``text`` (``string``) -- The option displayed text.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_text("Just a text option", "luaOptHashText", "Text")

======================

add_player_option_info(``name``, ``hash``, ``info``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a text menu option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``info`` (``string``) -- The option displayed info as text.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_text("Just a text option", "luaOptHashInfo", "Some info")

======================

update_root_parent(``keepActiveOption`` = ``false``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates the main section to display the created Lua section/option.

**Parameters:**

* ``keepActiveOption`` (``bool``) -- Keep the option active (``true`` / ``false``).

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   menu.update_root_parent(true)

======================

update_current_parent(``keepActiveOption`` = ``false``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates the current section to display the created Lua section/option.

**Parameters:**

* ``keepActiveOption`` (``bool``) -- Keep the option active (``true`` / ``false``).

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_current_parent(true)

======================

is_option_toggled(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if an option is toggled.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``bool`` -- Returns ``True`` if the option is toggled, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   -- Get option state
   optionToggled = "~rl~luaOptDummyToggle ~w~state is: ~g~" .. tostring(menu.is_option_toggled("luaOptDummyToggle"))

======================

is_option_visible(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if an option is visible.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``bool`` -- Returns ``True`` if the option is visible, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   optionVisible = "~rl~luaOptDummyToggle ~w~state is: ~g~" .. tostring(menu.is_option_visible("luaOptDummyToggle"))

======================

is_option_enabled(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if an option is enabled.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``bool`` -- Returns ``True`` if the option is enabled, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   optionEnabled = "~rl~luaOptDummyToggle ~w~state is: ~g~" .. tostring(menu.is_option_enabled("luaOptDummyToggle"))

======================

get_option_value(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the value of an option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``float`` -- Returns option value.

**Example:**

.. code-block:: lua
   :linenos:

   -- Get option value
   optionValue = "~rl~luaOptHashValue ~w~value is: ~g~" .. tostring(menu.get_option_value("luaOptHashValue"))

======================

remove_option(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes an option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.remove_option("luaOpt") --assuming there's an option with hash "luaOpt"

======================

.. _stats:

Stats namespace
----------------------

This namespace contains functions that are used to get and set certain stats in the game.

.. warning::

   These functions are meant to be used by experienced users only, as they can be used to break the character and the account.

   There are no examples for this namespace, as advanced users will know how to use it.

   *Sapienti sat*

================================

set_packed_bool(``index``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a packed boolean stat.

**Parameters:**

* ``index`` (``int``) -- The index of the packed bool stat.
* ``value`` (``bool``) -- The value to set.

**Returns:**

* None

================================

get_packed_bool(``index``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a packed boolean stat.

**Parameters:**

* ``index`` (``int``) -- The index of the packed bool stat.

**Returns:**

* ``bool`` -- The value of the packed bool stat.

================================

set_mass_packed_bool(``value``, ``min``, ``max``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a mass-packed boolean stat.

**Parameters:**

* ``value`` (``bool``) -- The value to set.
* ``min`` (``int``) -- The minimum value of the mass-packed bool stat.
* ``max`` (``int``) -- The maximum value of the mass-packed bool stat.

**Returns:**

* None

================================

get_mass_packed_bool(``min``, ``max``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not implemented yet.

Returns a mass-packed boolean stat.

**Parameters:**

* ``min`` (``int``) -- The minimum value of the mass-packed bool stat.
* ``max`` (``int``) -- The maximum value of the mass-packed bool stat.

**Returns:**

* None

================================

set_packed_int(``index``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a packed integer stat.

**Parameters:**

* ``index`` (``int``) -- The index of the packed integer stat.
* ``value`` (``int``) -- The value to set.

**Returns:**

* None

================================

get_packed_int(``index``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a packed integer stat.

**Parameters:**

* ``index`` (``int``) -- The index of the packed integer stat.

**Returns:**

* ``int`` -- The value of the packed integer stat.

================================

get_mass_packed_int(``min``, ``max``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not implemented yet.

Returns a mass-packed integer stat.

**Parameters:**

* ``min`` (``int``) -- The minimum value of the mass-packed integer stat.
* ``max`` (``int``) -- The maximum value of the mass-packed integer stat.

**Returns:**

* None

================================

set_stat_bit(string stat, int bit)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a bit in a stat.

**Parameters:**

* ``stat`` (``string``) -- The stat name.
* ``bit`` (``int``) -- The bit to set.

**Returns:**

* None

================================

clear_stat_bit(``stat``, ``bit``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clear a bit in a stat.

**Parameters:**

* ``stat`` (``string``) -- The stat name.
* ``bit`` (``int``) -- The bit to clear.

**Returns:**

* None

================================


stat_get_int(``stat``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns an integer stat.

**Parameters:**

* ``stat`` (``string``) -- The name of the stat.

**Returns:**

* ``int`` -- The value of the stat.

================================


stat_set_int(``stat``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Parameters:**

* ``stat`` (``string``) -- The name of the stat.
* ``value`` (``int``) -- The value to set.

**Returns:**

* None

================================

stat_get_bool(``stat``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a boolean stat.

**Parameters:**

* ``stat`` (``string``) -- The name of the stat.

**Returns:**

* ``bool`` -- The value of the stat.

================================

stat_set_bool(``stat``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a boolean stat.

**Parameters:**

* ``stat`` (``string``) -- The name of the stat.
* ``value`` (``bool``) -- The value to set.

**Returns:**

* None

================================

stat_get_float(``stat``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a float stat.

**Parameters:**

* ``stat`` (``string``) -- The name of the stat.

**Returns:**

* ``float`` -- The value of the stat.

================================

stat_set_float(``stat``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a float stat.

**Parameters:**

* ``stat`` (``string``) -- The name of the stat.
* ``value`` (``float``) -- The value to set.

**Returns:**

* None

================================


.. _notify:

Notify namespace
----------------------

This namespace contains functions for sending notifications.

================================

above_map(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a notification in the bottom-left corner of the screen.

**Parameters:**

* ``text`` (``string``) -- The text to display.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   notify.above_map("Hello world!")

================================

.. _script:

Script namespace
----------------------

This namespace contains functions for executing in-game events.

.. warning::

   These functions are meant to be used by experienced users only.

   *Sapienti sat*

================================

trigger_script_event(``eventGroup``, ``args``, ``playerId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Triggers a script event.

**Parameters:**

* ``eventGroup`` (``int``) -- The event group ID.
* ``args`` (``int64_t``) -- The arguments to pass to the event.
* ``playerId`` (``int``) -- The player ID to send the event to.

**Returns:**

* None

**Example:**


.. code-block:: lua
   :linenos:

   script.trigger_script_event(0x0000000, { 1234567, 7654321, 1234321 }, chatSenderId)

================================

.. _globals:

Globals namespace
----------------------

This namespace contains functions for accessing global in-game values.

.. warning::

   These functions are meant to be used by experienced users only.

   *Sapienti sat*


================================

set_global_int(``global``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new global integer value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.
* ``value`` (``int``) -- The value to set.

**Returns:**

* None

================================

set_global_float(``global``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new global float value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.
* ``value`` (``float``) -- The value to set.

**Returns:**

* None

================================

set_global_bool(``global``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new global boolean value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.
* ``value`` (``bool``) -- The value to set.

**Returns:**

* None

================================

set_global_string(``global``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new global string value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.
* ``value`` (``string``) -- The value to set.

**Returns:**

* None

================================

get_global_int(``global``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a global integer value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.

**Returns:**

* ``int`` -- The global value.

================================

get_global_float(``global``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a global float value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.

**Returns:**

* ``float`` -- The global value.

================================

get_global_bool(``global``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a global boolean value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.

**Returns:**

* ``bool`` -- The global value.

================================

get_global_string(``global``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a global string value.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.

**Returns:**

* ``string`` -- The global value.

================================

.. _locals:

Locals namespace
----------------------

This namespace contains functions for accessing local in-game values.

.. warning::

   These functions are meant to be used by experienced users only.

   *Sapienti sat*

================================

set_local_int(``scriptName``, ``local``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new local integer value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.
* ``value`` (``int``) -- The value to set.

**Returns:**

* None

================================

set_local_float(``scriptName``, ``local``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new local float value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.
* ``value`` (``float``) -- The value to set.

**Returns:**

* None

================================

set_local_bool(``scriptName``, ``local``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new local boolean value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.
* ``value`` (``bool``) -- The value to set.

**Returns:**

* None

================================

set_local_string(``scriptName``, ``local``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a new local string value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.
* ``value`` (``string``) -- The value to set.

**Returns:**

* None

================================

get_local_int(``scriptName``, ``local``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a local integer value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.

**Returns:**

* ``int`` -- The local value.

================================

get_local_float(``scriptName``, ``local``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a local float value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.

**Returns:**

* ``float`` -- The local value.

================================

get_local_bool(``scriptName``, ``local``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a local boolean value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.

**Returns:**

* ``bool`` -- The local value.

================================

get_local_string(``scriptName``, ``local``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a local string value.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.

**Returns:**

* ``string`` -- The local value.

================================

.. _render:

Render namespace
----------------------

This namespace contains functions that are used to render certain objects in the game 
and gathering certain objects' coordinates on screen.

================================

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

* None


**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_box("MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 10, 0)

================================

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

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_box_filled("MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 10, 0)

================================

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

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_box_border_filled("MyHash", true, 0, 0, 100, 100, 10, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true, 10, 0)

================================

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

* None


**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_circle("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, 16)

================================

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

* None

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_circle_filled("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, 16)

================================

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

* None


**Example:**

.. code-block:: lua
   :linenos:

   render.draw_circle_border_filled("MyHash", true, 0, 0, 100, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true, 16)

================================

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

* None

**Example:**

.. code-block:: lua
   :linenos:
      
   render.draw_triangle("MyHash", true, 0, 0, { 255, 255, 255, 255 }, 1.1)

================================

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

* None


**Example:**

.. code-block:: lua
   :linenos:

   render.draw_triangle_filled("MyHash", true, 0.f, 0.f, { 255, 255, 255, 255 }, 1.1)

================================

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

* None

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_triangle_border_filled("MyHash", true, 0, 0, { 255, 255, 255, 255 }, { 0, 0, 0, 255 }, true)

================================

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

* None

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_text("MyHash", true, "Hello World", 0, 0, 1, { 255, 255, 255, 255 }, 0)

================================

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
      system.log_info("The color picker is active!") -- Prints if the color picker is active.
   end

================================

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
      system.log_info("The cursor is hovering over the menu!") -- This will only be logged if the cursor is hovering over the menu.
   end

================================

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
      system.log_info("The cursor is hovering over an option!") -- This will only be logged if the cursor is hovering over an option.
   end

================================

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
      system.log_info("The input window is active!") -- This will only be logged if the input window is active.
   end

================================

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
      
   borderSize = render.get_border_size() -- Gets the border size.
   system.log_info("The border size is " .. tostring(borderSize) .. ".") -- Prints the border size.

================================

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
      
   fps = render.get_fps() -- Gets the FPS.
   system.log_info("The FPS is " .. tostring(fps) .. ".") -- Prints the FPS.

================================

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
      
   rounding = render.get_menu_rounding() -- Gets the rounding.
   system.log_info("The rounding is " .. tostring(rounding) .. ".") -- Prints the rounding.

================================

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
      
   width = render.get_menu_width() -- Gets the width.
   system.log_info("The width is " .. tostring(width) .. ".") -- Prints the width.

================================

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
      
   headerSize = render.get_font_header_size() -- Gets the header size.
   system.log_info("The header size is " .. tostring(headerSize) .. ".") -- Prints the header size.

================================

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
      
   helperSize = render.get_font_helper_size() -- Gets the helper size.
   system.log_info("The helper size is " .. tostring(helperSize) .. ".") -- Prints the helper size.

================================

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
      
   optionSize = render.get_font_option_size() -- Gets the option size.
   system.log_info("The option size is " .. tostring(optionSize) .. ".") -- Prints the option size.

================================

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
      
   warningSize = render.get_font_warning_size() -- Gets the warning size.
   system.log_info("The warning size is " .. tostring(warningSize) .. ".") -- Prints the warning size.

================================

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
      
   cursorPos = render.get_menu_cursor_pos() -- Gets the cursor position.
   system.log_info("The cursor position is " .. tostring(cursorPos.x) .. ".") -- Prints the cursor X position coordinate.
   system.log_info("The cursor position is " .. tostring(cursorPos.y) .. ".") -- Prints the cursor Y position coordinate.


================================

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
      
   menuPos = render.get_menu_position() -- Gets the menu position.
   system.log_info("The menu position is " .. tostring(menuPos.x) .. ".") -- Prints the menu X position coordinate.
   system.log_info("The menu position is " .. tostring(menuPos.y) .. ".") -- Prints the menu Y position coordinate.

================================

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
      
   totalSize = render.get_menu_total_size() -- Gets the menu total size.
   system.log_info("The menu total size is " .. tostring(totalSize.x) .. ".") -- Prints the menu total X size.
   system.log_info("The menu total size is " .. tostring(totalSize.y) .. ".") -- Prints the menu total Y size.

================================

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
      
   screenRes = render.get_screen_resolution() -- Gets the screen resolution.
   system.log_info("The screen resolution is " .. tostring(screenRes.x) .. ".") -- Prints the screen X resolution.
   system.log_info("The screen resolution is " .. tostring(screenRes.y) .. ".") -- Prints the screen Y resolution.

================================

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

================================

.. _self:

Self namespace
----------------------

This namespace contains functions that are related to the character of the menu user.

================================

is_alive()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns whether the user is alive.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Whether the user is alive.

**Example:**

.. code-block:: lua
   :linenos:
   
   if self.is_alive() then -- Checks if the user is alive.
      system.log_info("The user is alive.") 
   else
      system.log_info("The user is dead.")
   end

================================

is_in_vehicle()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the user is in a vehicle.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Whether the user is in a vehicle.

**Example:**

.. code-block:: lua
   :linenos:
   
   if self.is_in_vehicle() then -- Checks if the user is in a vehicle.
      system.log_info("The user is in a vehicle.") 
   else
      system.log_info("The user is not in a vehicle.")
   end

================================

is_valid()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is valid -- the player is alive, is fully loaded into the session, and has control of the character.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Whether the player is valid. Can also be ``true`` during cutscenes.

**Example:**

.. code-block:: lua
   :linenos:
   
   if self.is_valid() then -- Checks if the player is valid.
      system.log_info("The player is valid.") 
   else
      system.log_info("The player is invalid.")
   end

================================

get_online_index()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the online index of the user's character.

**Parameters:**

* None

**Returns:**

* ``int`` -- The online index of the user's character.
* * ``0`` -- The first character is used
* * ``1`` -- The second character is used

**Example:**

.. code-block:: lua
   :linenos:
   
   index = self.get_online_index() -- Returns the online index of the user's character.
   if index == 0 then -- Checks if the first character is used.
      system.log_info("The first character is used.")
   elseif index == 1 then -- Checks if the second character is used.
      system.log_info("The second character is used.")
   end

================================

get_ped()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the user's character's ped ID

**Parameters:**

* None

**Returns:**

* ``int`` -- The user's character's ped ID.

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   if rage.ped.is_ped_a_player(ped) then -- If the ped is a player.
      system.log_info("The ped is a player.")
   end

================================

get_id()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the user's character's ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The user's character's ID.

**Example:**

.. code-block:: lua
   :linenos:
   
   id = self.get_id() -- Gets the user's character's ID.
   system.log_info("The character ID is " .. tostring(id) .. ".")

======================

get_name()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns your own username.

**Parameters:**

* None

**Returns:**

* ``string``

**Example:**

.. code-block:: lua
   :linenos:

   selfUsername = self.get_name()
   system.log_info("My username is: " .. selfUsername)

======================

get_original_scid()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns your SCID (Social Club ID).

**Parameters:**

* None

**Returns:**

* ``uint32_t`` -- Original Social Club ID

**Example:**

.. code-block:: lua
   :linenos:

   selfOGscid = self.get_original_scid()
   system.log_info("My original SCID is: " .. tostring(selfOGscid))

======================

get_scid()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns your current SCID (Social Club ID).

**Parameters:**

* None

**Returns:**

* ``uint32_t`` -- Current Social Club ID

**Example:**

.. code-block:: lua
   :linenos:

   selfSCID = self.get_scid()
   system.log_info("My current SCID is: " .. tostring(selfSCID))

======================

get_saved_scid()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns your saved SCID (Social Club ID).

**Parameters:**

* None

**Returns:**

* ``uint64_t`` -- Saved Social Club ID

**Example:**

.. code-block:: lua
   :linenos:

   selfSavedSCID = self.get_saved_scid()
   system.log_info("My saved SCID is: " .. tostring(selfSavedSCID))

======================

get_coords()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns your character's coordinates.

**Parameters:**

* None

**Returns:**

* ``Vector3`` -- Coordinates

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords()
   system.log_info("I'm located at the following coords: " .. tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z) .. " .")

======================

get_coords_infront(``distance`` = ``5.0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns coordinates in front of your character.

**Parameters:**

* ``distance`` (``float``) -- Distance calculated starting from in front of self. Default value is ``5.0``.

**Returns:**

* ``Vector3`` -- Returns coordinates in Vector3 form.

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords_infront(5)
   system.log_info("The coords in front of me are: " .. tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z) .. " .")

======================

get_vehicle()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns your current vehicle's ID.

**Parameters:**

* None

**Returns:**

* ``Vehicle`` -- Returns vehicle ID.

**Example:**

.. code-block:: lua
   :linenos:

   selfVehicle = self.get_vehicle()
   system.log_info("You're riding vehicle ID: " .. tostring(selfVehicle))

======================

.. _lobby:

Lobby namespace
----------------------

This namespace contains functions related to the interaction with the online game session.

.. note::
   Functions from this namespace only work in online mode.

================================

is_player_active(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is in active, in the session, is fully loaded, 
connected, is in the same game mode as you (e.g. freemode)

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is active.

**Example:**

.. code-block:: lua
   :linenos:
   
   isActive = lobby.is_player_active(lobby.get_host()) -- Checks if the player is active.
   if isActive then -- If the player is active.
      system.log_info("The player is active.")
   end

================================

is_player_connected(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is connected.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is connected.

**Example:**

.. code-block:: lua
   :linenos:
   
   isConnected = lobby.is_player_connected(lobby.get_host()) -- Checks if the player is connected.
   if isConnected then -- If the player is connected.
      system.log_info("The player is connected.")
   end

================================

is_player_friend(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is a friend.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is a friend.

**Example:**

.. code-block:: lua
   :linenos:
   
   isFriend = lobby.is_player_friend(lobby.get_host()) -- Checks if the player is a friend.
   if isFriend then -- If the player is a friend.
      system.log_info("The player is a friend.")
   end

================================

is_player_host(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is the host.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is the host.

**Example:**

.. code-block:: lua
   :linenos:
   
   isHost = lobby.is_player_host(lobby.get_host()) -- Checks if the player is the host.
   if isHost then -- If the player is the host.
      system.log_info("The player is the host.")
   end

================================

is_player_host_next(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is the next script host.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is the next script host.

**Example:**

.. code-block:: lua
   :linenos:
   
   isHostNext = lobby.is_player_host_next(lobby.get_host()) -- Checks if the player is the next script host.
   if isHostNext then -- If the player is the next script host.
      system.log_info("The player is the next script host.")
   end

================================

is_player_in_vehicle(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is in a vehicle.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is in a vehicle.

**Example:**

.. code-block:: lua
   :linenos:
   
   isInVehicle = lobby.is_player_in_vehicle(lobby.get_host()) -- Checks if the player is in a vehicle.
   if isInVehicle then -- If the player is in a vehicle.
      system.log_info("The player is in a vehicle.")
   end


================================

is_player_modder(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is a modder.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is a modder.

**Example:**

.. code-block:: lua
   :linenos:
   
   isModder = lobby.is_player_modder(lobby.get_host()) -- Checks if the player is a modder.
   if isModder then -- If the player is a modder.
      system.log_info("The player is a modder.")
   end

================================

is_player_selected(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is selected in the menu's online section.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is selected.

**Example:**

.. code-block:: lua
   :linenos:
   
   isSelected = lobby.is_player_selected(lobby.get_host()) -- Checks if the player is selected.
   if isSelected then -- If the player is selected.
      system.log_info("The player is selected.")
   end

================================

is_player_staff(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is a Rockstar staff member.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is a Rockstar staff member.

**Example:**

.. code-block:: lua
   :linenos:
   
   isStaff = lobby.is_player_staff(lobby.get_host()) -- Checks if the player is a Rockstar staff member.
   if isStaff then -- If the player is a Rockstar staff member.
      system.log_info("The player is a Rockstar staff member.")
   end

================================

is_player_valid(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is valid - if it's connected to the session, fully loaded, and alive.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``bool`` -- Whether the player is valid.

**Example:**

.. code-block:: lua
   :linenos:
   
   isValid = lobby.is_player_valid(lobby.get_host()) -- Checks if the player is valid.
   if isValid then -- If the player is valid.
      system.log_info("The player is valid.")
   end

================================

is_session_started()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the session has started: returns true if it's fully loaded and you're not hanging in the clouds.

**Parameters:**

* None

**Returns:**

* ``bool`` -- Whether the session has started.

**Example:**

.. code-block:: lua
   :linenos:
   
   isStarted = lobby.is_session_started() -- Checks if the session has started.
   if isStarted then -- If the session has started.
      system.log_info("The session has started.")
   end

================================

get_active_players()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a number of all active players.

**Parameters:**

* None

**Returns:**

* ``int`` -- a number of all active players.

**Example:**

.. code-block:: lua
   :linenos:
   
   activePlayers = lobby.get_active_players() -- Gets a number of all active players.
   system.log_info("There are " .. tostring(activePlayers) .. " active players.")

================================

get_connected_players()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a number of connected players.

**Parameters:**

* None

**Returns:**

* ``int`` --  a number of connected players.

**Example:**

.. code-block:: lua
   :linenos:
   
   connectedPlayers = lobby.get_connected_players() -- Gets a number of connected players.
   system.log_info("There are " .. tostring(connectedPlayers) .. " connected players.")

================================

get_player_armour(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's armour health.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's armour health.

**Example:**

.. code-block:: lua
   :linenos:
   
   armour = lobby.get_player_armour(lobby.get_host()) -- Gets the player's armour ID.
   if armour == 0 then -- If the player has no armour.
      system.log_info("The player has no armour.")
   end

================================

get_player_health(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's health.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's health.

**Example:**

.. code-block:: lua
   :linenos:
   
   health = lobby.get_player_health(lobby.get_host()) -- Gets the host's health.
   if health == 100 then -- If the host has full health.
      system.log_info("The host has full health.")
   end


================================

get_player_max_health(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's maximum health.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's maximum health.

**Example:**

.. code-block:: lua
   :linenos:
   
   maxHealth = lobby.get_player_max_health(lobby.get_host()) -- Gets the host's maximum health.
   health = lobby.get_player_health(lobby.get_host()) -- Gets the host's health.
   if maxHealth == health then -- If the host has full health.
      system.log_info("The host has full health.")
   end

================================

get_player_team(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's team.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's team ID. -1 if the player is not in a team.

================================

get_player_ped(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's ped.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``Ped`` -- The player's ped.

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = lobby.get_player_ped(lobby.get_host()) -- Gets the host's ped.
   if rage.ped.is_ped_a_player(ped) then -- If the ped is a player.
      system.log_info("The ped is a player.")
   end

================================

get_host()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the host player ID.

**Parameters:**

* None

**Returns:**

* ``Player`` -- The host player ID.

**Example:**

.. code-block:: lua
   :linenos:
   
   host = lobby.get_host() -- Gets the host player ID.
   system.log_debug("The host is " .. get_player_name(host) .. ".")

================================

get_next_host()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the next host player ID.

**Parameters:**

* None

**Returns:**

* ``Player`` -- The next host player ID.

**Example:**

.. code-block:: lua
   :linenos:
   
   nextHost = lobby.get_next_host() -- Gets the next host player ID.
   system.log_debug("The next host is " .. get_player_name(nextHost) .. ".")

================================

get_selected_player()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the ID of a player that is currently selected in the Online section.

**Parameters:**

* None

**Returns:**

* ``Player`` -- The selected player ID.

================================

get_player_coords_str(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's coordinates as a string.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's coordinates

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = lobby.get_player_coords_str(lobby.get_host()) -- Gets the host's coordinates.
   system.log_debug("The host is at " .. coords .. ".")

================================

get_player_ip(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's IP.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's IP.

**Example:**

.. code-block:: lua
   :linenos:
   
   ip = lobby.get_player_ip(lobby.get_host()) -- Gets the host's IP.
   system.log_debug("The host's IP is " .. ip .. ".")

================================

get_player_name(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's name.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's name.

**Example:**

.. code-block:: lua
   :linenos:
   
   name = lobby.get_player_name(lobby.get_host()) -- Gets the host's name.
   system.log_debug("The host's name is " .. name .. ".")

================================

get_player_status(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's status.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's status.
* * ``H`` -- The player is the host.
* * ``NH`` -- The player is the next host.
* * ``F`` -- The player is a friend.
* * ``M`` -- The player is a modder.

**Example:**


.. code-block:: lua
   :linenos:
   
   status = lobby.get_player_status(lobby.get_selected_player()) -- Gets the selected player's status.
   system.log_debug("The selected player's status is " .. status .. ".")

===============================

get_player_vehicle_name(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's vehicle name.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's vehicle name. If the player is not in a vehicle, the string "None" is returned.

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicleName = lobby.get_player_vehicle_name(lobby.get_host()) -- Gets the host's vehicle name.
   system.log_debug("The host's vehicle name is " .. vehicleName .. ".")

================================

get_player_deaths(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the total player's deaths.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's deaths.

**Example:**

.. code-block:: lua
   :linenos:
   
   deaths = lobby.get_player_deaths(lobby.get_host()) -- Gets the host's deaths.
   system.log_debug("The host has died " .. tostring(deaths) .. " times.")

================================

get_player_kills(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the total player's kills.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's kills.

**Example:**

.. code-block:: lua
   :linenos:
   
   kills = lobby.get_player_kills(lobby.get_host()) -- Gets the host's kills.
   system.log_debug("The host has killed " .. tostring(kills) .. " people.")

================================

get_player_level(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's level.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's level.

**Example:**

.. code-block:: lua
   :linenos:
   
   level = lobby.get_player_level(lobby.get_host()) -- Gets the host's level.
   system.log_debug("The host's level is " .. tostring(level) .. ".")

================================

get_player_money_bank(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's bank money.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's bank money.

**Example:**

.. code-block:: lua
   :linenos:
   
   money = lobby.get_player_money_bank(lobby.get_host()) -- Gets the host's bank money.
   system.log_debug("The host has $" .. tostring(money) .. " in the bank.")

================================

get_player_money_wallet(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's wallet money.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's wallet money.

**Example:**

.. code-block:: lua
   :linenos:
   
   money = lobby.get_player_money_wallet(lobby.get_host()) -- Gets the host's wallet money.
   system.log_debug("The host has $" .. tostring(money) .. " in the wallet.")

================================

get_player_rp(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's RP points.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's RP.

**Example:**

.. code-block:: lua
   :linenos:
   
   rp = lobby.get_player_rp(lobby.get_host()) -- Gets the host's RP.
   system.log_debug("The host has " .. tostring(rp) .. " RP.")

================================

get_player_host_token(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's host token.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's host token.

**Example:**

.. code-block:: lua
   :linenos:
   
   token = lobby.get_player_host_token(lobby.get_host()) -- Gets the host's host token.
   system.log_debug("The host's host token is " .. token .. ".")

================================

get_player_original_scid(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's original SCID.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's original SCID.

**Example:**

.. code-block:: lua
   :linenos:
   
   scid = lobby.get_player_original_scid(lobby.get_host()) -- Gets the host's original SCID.
   system.log_debug("The host's original SCID is " .. scid .. ".")

================================

get_player_scid(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's SCID.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's SCID.

**Example:**

.. code-block:: lua
   :linenos:
   
   scid = lobby.get_player_scid(lobby.get_host()) -- Gets the host's SCID.
   system.log_debug("The host's SCID is " .. scid .. ".")

================================

get_player_coords(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's coordinates.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``Vector3`` -- The player's coordinates.

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = lobby.get_player_coords(lobby.get_host()) -- Gets the host's coordinates.
   system.log_debug("The host is at " .. tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z) .. " .")

================================

set_player_modder(``player``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the player's modder status.

**Parameters:**

* ``player`` (``Player``) -- The player ID.
* ``toggle`` (``bool``) -- The modder status.
* * ``true`` -- The player is a modder.
* * ``false`` -- The player is not a modder.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   lobby.set_player_modder(lobby.get_host(), true) -- Sets the host as a modder.
   system.log_debug("The host is a modder.")

================================

set_player_selected(``player``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the player as selected in the online menu.

**Parameters:**

* ``player`` (``Player``) -- The player ID.
* ``toggle`` (``bool``) -- The selected status.
* * ``true`` -- The player is set as selected.
* * ``false`` -- The player is set as not selected.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   lobby.set_player_selected(lobby.get_host(), true) -- Sets the host as selected.
   system.log_debug("The host is now selected.")

================================

set_player_staff(``player``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the player's staff status.

**Parameters:**

* ``player`` (``Player``) -- The player ID.
* ``toggle`` (``bool``) -- The staff status.
* * ``true`` -- The player is a staff member.
* * ``false`` -- The player is not a staff member.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   lobby.set_player_staff(lobby.get_host(), true) -- Sets the host as a staff member.
   system.log_debug("The host is a staff member.")


================================

.. _text:

Text namespace
----------------------

This namespace contains functions related to text manipulation.

================================

contains(``source``, ``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if string contains character/word.

**Parameters:**

* ``source`` (``string``) -- The string to check.
* ``data`` (``string``) -- The data to check for.

**Returns:**

* ``bool`` -- Returns ``True`` if data is found, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:
	
   loremIpsum = Lorem ipsum dolor sit amet
   Contains = text.contains(loremIpsum, "Lorem")
   system.log_debug(tostring(Contains))

======================

is_float(``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if string is ``float`` type.

**Parameters:**

* ``data`` (``string``) -- The data to check.

**Returns:**

* ``bool`` -- Returns ``True`` if data is float, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   isFloat = text.is_float("10.1")
   system.log_debug(tostring(isFloat))

======================

is_number(``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if string is a number.

**Parameters:**

* ``data`` (``string``) -- The data to check.

**Returns:**

* ``bool`` -- Returns ``True`` if data is number, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:

   isNumber = text.is_number("10")
   system.log_debug(tostring(isNumber))

======================

is_valid_ip4(``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if string is a valid IPv4.

**Parameters:**

* ``data`` (``string``) -- The data to check.

**Returns:**

* ``bool`` -- Returns ``True`` if data is a valid IPv4, ``False`` otherwise.

**Example:**

.. code-block:: lua
   :linenos:
   
   isValid = text.is_valid_ip4("1.1.1.1")
   system.log_debug(tostring(isValid))


======================

get_random_string(``length``, ``type``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generates a random string.

**Parameters:**

* ``length`` (``int``) -- Length of the string.
* ``type`` (``eRandomType``) -- Type of string generation: 
* * ``0`` -- Upper
* * ``1`` -- Lower
* * ``2`` -- Digits
* * ``3`` -- UpperLower
* * ``4`` -- UpperDigits
* * ``5`` -- LowerDigits

**Returns:**

* ``string`` -- The generated random string.

**Example:**

.. code-block:: lua
   :linenos:

   r = text.get_random_string(10, 2) -- Generates a random string made of digits
   system.log_debug(r)

======================

remove_characters(``data``, ``word``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes certain characters from string.

**Parameters:**

* ``data`` (``string``) -- The data to check.
* ``word`` (``string``) -- Word/Character to remove.

**Returns:**

* ``string`` -- The output string.

**Example:**

.. code-block:: lua
   :linenos:
   
   r = remove_characters("Road", "o")
   system.log_debug(r)

======================

replace_characters(``data``, ``first``, ``second``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replaces certain characters from string.

**Parameters:**

* ``data`` (``string``) -- The data to check.
* ``first`` (``string``) -- Word/Character to replace
* ``second`` (``string``) -- Replacement word/character

**Returns:**

* ``string`` -- The new, replaced string

**Example:**

.. code-block:: lua
   :linenos:
	
   r = replace_characters("Mr. White", "White", "Black")
   system.log_debug(r)
   
======================

resize_string_center(``data``, ``length``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuts string from center.

**Parameters:**

* ``data`` (``string``) -- The data to check.
* ``length`` (``int``) -- Length of the end string.

**Returns:**

* ``string`` -- The new string.

**Example:**

.. code-block:: lua
   :linenos:

   r = resize_string_center("Hello World", 5)
   system.log_debug(r)

**Output:**

.. code-block:: lua
   :linenos:

   He...ld
======================

resize_string_left(``data``, ``length``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuts string from the left

**Parameters:**

* ``data`` (``string``) -- The data to check.
* ``length`` (``int``) -- Length of the end string.

**Returns:**

* ``string`` -- Returns the new string.

**Example:**

.. code-block:: lua
   :linenos:

   r = resize_string_left("Hello World", 5)
   system.log_debug(r)
**Output:**

.. code-block:: lua
   :linenos:
   
   ...World
======================

resize_string_right(``data``, ``length``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuts string from the right.

**Parameters:**

* ``data`` (``string``) -- The data to check.
* ``length`` (``int``) -- Length of the end string.

**Returns:**

* ``string`` -- Returns the new string.

**Example:**

.. code-block:: lua
   :linenos:

   r = resize_string_right("Hello World", 5)
   system.log_debug(r)

**Output:**

.. code-block:: lua
   :linenos:
   
   Hello...



================================

.. _fs:

FS namespace
----------------------

This namespace contains functions that let you interact with the file system.

================================

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
      system.log_info("Directory exists.")

   end

================================

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
      system.log_info("Better not to call Saul.")
   end

================================

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

   success = fs.file_remove("test.txt") -- Removes the file.
   if success then
      system.log_info("File removed.") -- Prints a message if the file was removed.
   end

================================

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
      system.log_info("File is valid and ready.")
   end

================================

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
      system.log_info("The file is empty.")
   else
      system.log_info("The file is not empty.")
   end

================================

dir_check(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if directory exists, and if not, creates it.

**Parameters:**

* ``dir`` (``string``) -- Directory to check

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   fs.dir_check("D:\NewFolder") -- Creates the directory if it doesn't exist.

================================

dir_create(``dir``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a directory.

**Parameters:**

* ``dir`` (``string``) -- Directory to create

**Returns:**

* None

**Example**

.. code-block:: lua
   :linenos:
   
   fs.dir_create("D:\NewFolder") -- Creates a directory.

================================

file_copy(``source``, ``dest``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copies a file.

**Parameters:**

* ``source`` (``string``) -- Path to source file
* ``dest`` (``string``) -- Path to destination file

**Returns:**

* None

**Example**

.. code-block:: lua
   :linenos:

   fs.file_copy("source.txt", "dest.txt")
   -- or
   fs.file_copy("files/source.txt", "files/dest.txt")

================================

.. _scripting:

Scripting functions
#############################

Scripting functions are functions that let you interact with DIS2RBED's built-in options

================================

.. _scripting_functions:

Functions that are not included in any namespace
----------------------------------------------------

bool get_vehicle_bypass()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Not documented yet.

================================

void set_vehicle_bypass(bool ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Not documented yet.

================================

get_coords_infront_of_coords(``position``, ``rotation``, ``distance``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Not documented yet.

Returns the coordinates in front of the specified coordinates.

**Parameters:**

* ``position`` (``Vector3``) -- Position of the object
* ``rotation`` (``Vector3``) -- Rotation of the object
* ``distance`` (``float``) -- Distance to the object

**Returns:**

* ``Vector3`` -- Coordinates in front of the object

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = get_coords_infront_of_coords({0,0,0}, {0,0,0}, 10)
   system.log_debug(tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z))

================================

get_coords_above_of_coords(``position``, ``distance``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Not documented yet.

Returns the coordinates above of the specified coordinates.

**Parameters:**

* ``position`` (``Vector3``) -- Position of the object
* ``distance`` (``float``) -- Distance to the object

**Returns:**

* ``Vector3`` -- Coordinates above of the object

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = get_coords_above_of_coords({0,0,0}, 10)
   system.log_debug(tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z))

================================

.. _playerNSS:

Player namespace
----------------------

This namespace contains functions that are related to player and are used to execute built-in menu features

================================

set_clean()
^^^^^^^^^^^^^^^^^^^^

Cleans the character.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_clean()
   system.log_debug("Character cleaned.")

================================

set_force_field(``toggle``, ``type`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles and configures the force field.

**Parameters:**

* ``toggle`` (``bool``) -- ``true`` to enable the force field, ``false`` to disable it
* * ``true`` to enable the force field
* * ``false`` to disable it
* ``type`` (``int``) -- Type of the force field 
* * ``0`` for ``Normal`` (Default)
* * ``1`` for ``Lethal``



================================

.. _pedNSS:

Ped namespace
----------------------

Functions here

================================

.. _entityNSS:

Entity namespace
----------------------

Functions here

================================

.. _vehicleNSS:

Vehicle namespace
----------------------

Functions here

================================

.. _online:

Online namespace
----------------

Functions here

================================

.. _networkNSS:

Network namespace
----------------------

Functions here

================================

.. _spawn:

Spawn namespace
----------------

Functions here

================================

.. _weaponNSS:

Weapon namespace
----------------------

Functions here

================================

.. _teleport:

Teleport namespace
----------------------

Functions here

================================

.. _world:

World namespace
----------------------

Functions here

================================

.. _rage:

RAGE Functions
#################

This namespace contains native game functions.

================================

.. _playerNSR:

Player namespace
----------------------

Functions here

================================

.. _pedNSR:

Ped namespace
----------------------

Functions here

================================

.. _vehicleNSR:

Vehicle namespace
----------------------

Functions here

================================

.. _entityNSR:

Entity namespace
----------------------

Functions here

================================

.. _object:

Object namespace
----------------------

Functions here

================================

.. _weaponNSR:

Weapon namespace
----------------------

Functions here

================================

.. _streaming:

Streaming namespace
----------------------

Functions here

================================

.. _ui:

UI namespace
----------------------

Functions here

================================

.. _draw:

Draw namespace
----------------------

Functions here

================================

.. _camNS:

Cam namespace
----------------------

Functions here

================================

.. _gameplay:

Gameplay namespace
----------------------

Functions here

================================

.. _fire:

Fire namespace
----------------------

Functions here

================================

.. _networkNSR:

Network namespace
----------------------

Functions here

================================

.. _cutscene:

Cutscene namespace
----------------------

Functions here

================================

.. _controls:

Controls namespace
----------------------

Functions here

================================

.. _graphics:

Graphics namespace
----------------------

Functions here

================================

.. _time:

Time namespace
----------------------

Functions here

================================

.. _ai:

AI namespace
----------------------

Functions here

================================

.. _decorator:

Decorator namespace
----------------------

Functions here

================================

.. _interior:

Interior namespace
----------------------

Functions here

================================

.. _audio:

Audio namespace
----------------------

Functions here

================================

.. _rope:

Rope namespace
----------------------

Functions here

================================