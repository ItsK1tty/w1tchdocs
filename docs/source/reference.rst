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
* :ref:`eSessionType` (int)

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

.. _eSessionType:

eSessionType
----------------------
eSessionType definition here


* ``PublicJoin`` = ``0``
* ``PublicStart`` = ``1``
* ``CrewClosed`` = ``2``
* ``Crew`` = ``3``
* ``FriendsClosed`` = ``6``
* ``FriendsFind`` = ``9``
* ``Solo`` = ``10``
* ``Invite`` = ``11``
* ``CrewJoin`` = ``12``


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

  * :ref:`scripting_functions`
  * :ref:`playerNSS`
  * :ref:`pedNSS`
  * :ref:`entityNSS`
  * :ref:`vehicleNSS`
  * :ref:`online`
  * :ref:`networkNSS`
  * :ref:`spawn`
  * :ref:`weaponNSS`
  * :ref:`teleport`
  * :ref:`world`
* :ref:`rage`

  * :ref:`playerNSR`
  * :ref:`pedNSR`
  * :ref:`vehicleNSR`
  * :ref:`entityNSR`
  * :ref:`object`
  * :ref:`weaponNSR`
  * :ref:`streaming`
  * :ref:`ui`
  * :ref:`draw`
  * :ref:`camNS`
  * :ref:`gameplay`
  * :ref:`fire`
  * :ref:`networkNSR`
  * :ref:`cutscene`
  * :ref:`controls`
  * :ref:`graphics`
  * :ref:`time`
  * :ref:`ai`
  * :ref:`decorator`
  * :ref:`interior`
  * :ref:`audio`
  * :ref:`rope`

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

  * Can be ``-1`` to execute the task again and again.
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

Checks whether the key is pressed

**Parameters:**

* ``key`` (``string``) -- The key to check.

**Returns:**

* ``bool``

  * ``True`` -- The key is pressed
  * ``false`` -- The key is not pressed

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

add_option_toggle(``name``, ``hash``, ``parent``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

add_player_option_toggle(``name``, ``hash``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

* ``keepActiveOption`` (``bool``) 

  * ``true`` -- Save the cursor position
  * ``false`` -- Don't save the cursor position (default)

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

* ``keepActiveOption`` (``bool``) 

  * ``true`` -- Save the cursor position
  * ``false`` -- Don't save the cursor position (default)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_current_parent(true)

======================

is_option_toggled(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an option is toggled.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``bool``

  * ``True`` -- The option is toggled
  * ``False`` -- The option is not toggled

**Example:**

.. code-block:: lua
   :linenos:

   -- Get option state
   optionToggled = "~rl~luaOptDummyToggle ~w~state is: ~g~" .. tostring(menu.is_option_toggled("luaOptDummyToggle"))

======================

is_option_visible(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an option is visible.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``bool``

  * ``True`` -- The option is visible
  * ``False`` -- The option is invisible

**Example:**

.. code-block:: lua
   :linenos:

   optionVisible = "~rl~luaOptDummyToggle ~w~state is: ~g~" .. tostring(menu.is_option_visible("luaOptDummyToggle"))

======================

is_option_enabled(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an option is enabled.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``bool``

  * ``True`` -- The option is enabled
  * ``False`` -- The option is disabled

**Example:**

.. code-block:: lua
   :linenos:

   optionEnabled = "~rl~luaOptDummyToggle ~w~state is: ~g~" .. tostring(menu.is_option_enabled("luaOptDummyToggle"))

======================

get_option_value(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^

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



Menu sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

======================

section_self_mods()
^^^^^^^^^^^^^^^^^^^^

Returns the Self Mods section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add an option named "Useless Button" in the main Self Mods section.

   menu.add_option("Useless Button", "optUselessBtn", menu.section_self_mods(), function())

======================

section_self_mods_other()
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Self Mods -> Other section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add an option named "Other Option" in the Self Mods -> Other section.

   menu.add_option("Other Option", "optOtherOpt", menu.section_self_mods_other(), function())

======================

section_self_mods_no_clip()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Self Mods -> No Clip section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add an option named "No Clip Plus" in the Self Mods -> No Clip section.

   menu.add_option("No Clip Plus", "optNoclipPlus", menu.section_self_mods_no_clip(), function())

======================

section_self_mods_invincibility()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Self Mods -> Invincibility section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add an option named "Thanos Mode" in the Self Mods -> Invincibility section.

   menu.add_option("Thanos Mode", "optThanosMode", menu.section_self_mods_invincibility(), function())

======================

section_online()
^^^^^^^^^^^^^^^^^

Returns the Online section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add an option named "Useless Button" in the Online section.

   menu.add_option("Useless Button", "optUselessBtn2", menu.section_online(), function())

======================

section_online_player(``playerId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Online -> Player (specific) section ID.

**Parameters:**

* ``playerId`` (``int``) -- The player ID.

**Returns:**

* ``int`` -- The ID of the player's menu tab.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Look Player", "optLookPlayer", menu.section_online_player(23), function())

======================

section_online_players()
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Online -> Players section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("All Online Players", "optAllOnlPlayers", menu.section_online_players(), function())

======================

section_online_protex()
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Online -> Protections section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Super Protex", "optSuperPrtx", menu.section_online_protex(), function())

======================

section_online_other()
^^^^^^^^^^^^^^^^^^^^^^^

Returns the Online -> Other section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Other Button", "optOtherBtn", menu.section_online_other(), function())

======================

section_online_spoofer()
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Online -> Spoofing section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Spoof All", "optSpoofAll", menu.section_online_spoofer(), function())

======================

section_network()
^^^^^^^^^^^^^^^^^^^^

Returns the Online -> Network section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Disconnect", "optNtwrkDisconnect", menu.section_network(), function())

======================

section_recovery()
^^^^^^^^^^^^^^^^^^^^^

Returns the Recovery section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's integrate Heist Control LUA in the Recovery section.

   menu.add_delimiter("Heist Control v0.1", menu.section_recovery())

   -- Child section for Cayo Perico Heist options.

   CayoPericoHeist = menu.add_child("Cayo Perico Heist", menu.section_recovery())

======================

section_recovery_bunker()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Recovery -> Bunker Options section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Sell Everything", "optSellEvery", menu.section_recovery_bunker(), function())

======================

section_recovery_night_club()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Recovery -> NightClub Options section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add a toggable option in memory of the 6 Mil NC Safe Loop, we miss you.

   menu.add_option_toggle("Loop Nightclub Safe Cash", "optNcSafeLoop", menu.section_recovery_nightclub(), function())

======================

section_recovery_motorcycle_club()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Recovery -> Motorcycle Club Options section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Ride or Die", "optMcRideOrDie", menu.section_recovery_motorcycle_club(), function())

======================

section_recovery_casino()
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Recovery -> Casino Options section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   function casinoJackpot()
      log_warning("You hit the jackpot!!!")
   end

   menu.add_option("Jackpot", "optCasinoJckpt", menu.section_recovery_casino(), casinoJackpot)

======================

section_vehicle_spawn()
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Vehicle Spawn section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add Spawn Zentorno option to Vehicle Spawn section.

   spawn = menu.section_vehicle_spawn()

   zentornoHash = rage.gameplay.get_hash_key("ZENTORNO")

   menu.add_option_spawn("Spawn Zentorno", zentornoHash, 0, spawn)

======================

section_weapons()
^^^^^^^^^^^^^^^^^^^^^

Returns the Weapons section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Add Weapon", "optAddWeapon", menu.section_weapons(), function())

======================

section_weapons_ammo()
^^^^^^^^^^^^^^^^^^^^^^^

Returns the Weapons -> Weapons Ammo section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Add Ammo", "optAddAmmo", menu.section_weapons_ammo(), function())

======================

section_teleport()
^^^^^^^^^^^^^^^^^^^^^

Returns the Teleport section.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add a direct Casino Entrance teleport option, in the Teleport section.

   teleport = menu.section_teleport()

   menu.add_option_teleport("Casino Entrance", { 922.680847, 47.205017, 81.106346 }, teleport)

======================

section_teleport_ipl()
^^^^^^^^^^^^^^^^^^^^^^^

Returns the Teleport -> IPL section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Another IPL Teleport", "optAnotherIplTp", menu.section_teleport_ipl(), function())

======================

section_vehicle_mods()
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Vehicle Mods section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Full Upgrade", "optFullUpgrade", menu.section_vehicle_mods(), function())

======================

section_los_santos_customs()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the LSC Mods section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Rainbow Color", "optLscRainbowClrs", menu.section_los_santos_customs(), function())

======================

section_model_changer()
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Model Changer section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Turn into a cat", "optModelBecomeCat", menu.section_model_changer(), function())

======================

section_animations()
^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Animations section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Dance2", "optAnimDance2", menu.section_animations(), function())

======================

section_model_swapper()
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Model Swapper section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Swap Model", "optModelSwap", menu.section_model_swapper(), function())

======================

section_crafting_workshop()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Crafting Workshop section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   -- Let's add a child section in Crafting Workshop section named "Spawnable Custom Workshops"

   spawnables = menu.add_child("Spawnable Custom Workshops", menu.section_crafting_workshop())

   -- Inside we will have an option to spawn a custom made workshop preset.

   menu.add_option("Spawn Flying Kosatka (Custom 1)", "optCraftingSpawnCustom1", spawnables, function())

======================

section_outfit_store()
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns he Outfit Store section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Random Outfit", "optOutfitRandom", menu.section_outfit_store(), function())

======================

section_outfit_store()
^^^^^^^^^^^^^^^^^^^^^^^

Returns the Outfit Store section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Random Outfit", "optOutfitRandom", menu.section_outfit_store(), function())

======================

section_settings()
^^^^^^^^^^^^^^^^^^^

Returns the Settings section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Reset Settings", "optSettingsResetStngs", menu.section_settings(), function())

======================

section_settings_lua()
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Settings -> Lua section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Save Lua Settings", "optLuaSettingsSave", menu.section_settings_lua(), function())

======================

section_interface()
^^^^^^^^^^^^^^^^^^^^^^

Returns the Interface section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("Reset Theme", "optInterfaceResetTheme", menu.section_interface(), function())

======================

section_world()
^^^^^^^^^^^^^^^^^^^

Returns the World section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("World", "optWorld", menu.section_world(), function())

======================

section_about()
^^^^^^^^^^^^^^^^^^^

Returns the About section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the parent menu section.

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_option("About Me", "optAboutAbtMe", menu.section_about(), function())

======================

is_menu_active()
^^^^^^^^^^^^^^^^^^^

Checks whether the menu is active.

**Parameters:**

* None

**Returns:**

* ``bool``
  
  *  ``true`` -- The menu is opened
  *  ``false`` -- The menu is closed

**Example:**

.. code-block:: lua
   :linenos:

   isMenuOpened = menu.is_menu_active()

======================

is_menu_controls_active()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the menu controls are active.

**Parameters:**

* None

**Returns:**

* ``bool``
  
  *  ``true`` -- The menu controls are active
  *  ``false`` -- The menu controls are inactive

**Example:**

.. code-block:: lua
   :linenos:

   MenuControlsCheck = menu.is_menu_controls_active()

======================

is_menu_mouse_controls_active()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the menu mouse controls are active.

**Parameters:**

* None

**Returns:**

* ``bool``
  
  *  ``true`` -- The menu mouse controls are active
  *  ``false`` -- The menu mouse controls are inactive

**Example:**

.. code-block:: lua
   :linenos:

   MouseControlsCheck = menu.is_menu_mouse_controls_active()

======================

menu_set_controls(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles menu controls on/off.

**Parameters:**

* ``toggle`` (``bool``)

  * ``true`` to enable menu controls
  * ``false`` to disable them

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   controlsOn = menu.set_controls(true)

======================

menu_set_mouse_controls(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles menu mouse controls on/off.

**Parameters:**

* ``toggle`` (``bool``)

  * ``true`` to enable menu mouse controls
  * ``false`` to disable them

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   mouseControlsOn = menu.set_mouse_controls(true)

======================

menu_set_value()
^^^^^^^^^^^^^^^^^^^^

Menu action (Set Value).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   setValue = menu.set_value()

======================

menu_back()
^^^^^^^^^^^^^^

Menu navigation action (Back).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuBack = menu.menu_back()

======================

menu_back_mouse()
^^^^^^^^^^^^^^^^^^^

Menu mouse navigation action (Back).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuBackMouse = menu.menu_back_mouse()

======================

menu_down()
^^^^^^^^^^^^^^^^

Menu navigation action (Down).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuDown = menu.menu_down()

======================


menu_left()
^^^^^^^^^^^^^^^^^^^^^^^

Menu navigation action (Left).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuLeft = menu.menu_left()

======================

menu_remove_hotkey()
^^^^^^^^^^^^^^^^^^^^^^^

Menu action (Remove Hotkey).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuRemHotkey = menu.menu_remove_hotkey()

======================

menu_right()
^^^^^^^^^^^^^^^^^^^^^^^

Menu navigation action (Right).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuRight = menu.menu_right()

======================

menu_save()
^^^^^^^^^^^^^^^^^^^^^^^

Menu action (Save settings).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuSave = menu.menu_save()

======================

menu_select()
^^^^^^^^^^^^^^^^^^^^^^

Menu navigation action (Select).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuSelect = menu.menu_select()

======================

menu_select_mouse()
^^^^^^^^^^^^^^^^^^^^^^^^

Menu mouse navigation action (Select).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuSelectMouse = menu.menu_select_mouse()

======================

menu_toggle()
^^^^^^^^^^^^^^^^^^

Menu navigation action (Toggle).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuToggle = menu.menu_toggle()

======================

menu_up()
^^^^^^^^^^^^^

Menu navigation action (**Up**).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menuUp = menu.menu_up()

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
*  ``draw`` (``bool``) -- Whether to draw the box or not.
* * ``True`` to draw the box
* * ``false`` to not draw the box 
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``color`` (``vector<int>``) -- The color of the box. ``{R, G, B, A}``
*   ``rounding`` (``float``) -- The rounding rule of the box.
* *  Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. 
* * Default is ``0``.

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
*  ``draw`` (``bool``) -- Whether to draw the box or not.
* * ``True`` to draw the box
* * ``false`` to not draw the box 
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``color`` (``vector<int>``) -- The color of the box. ``{R, G, B, A}``
*   ``rounding`` (``float``) -- The rounding rule of the box. 
* * Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. 
* * Default is ``0``.

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
*  ``draw`` (``bool``) -- Whether to draw the box or not.
* * ``True`` to draw the box
* * ``false`` to not draw the box 
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``borderSize`` (``float``) -- The width of the border (in pixels)
*   ``color`` (``vector<int>``) -- The color of the box. ``{R, G, B, A}``
*   ``colorBorder`` (``vector<int>``) -- The color of the border. ``{R, G, B, A}``
*   ``borderFilled`` (``bool``)
* * ``True`` to fill the border
* * ``false`` to not fill the border
*   ``rounding`` (``float``) -- The rounding rule of the box. 
* * Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. 
* * Default is ``0``.

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
*  ``draw`` (``bool``) -- Whether to draw the circle or not.
* * ``True`` to draw the circle
* * ``false`` to not draw the circle
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``vector<int>``) -- The color of the circle. ``{R, G, B, A}``
*  ``segments`` (``int``) -- The number of segments of the circle. 
* * Default is ``16``. 
* * Better to keep between ``1-50``. Going further may cause the process to crash.

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
*  ``draw`` (``bool``) -- Whether to draw the circle or not.
* * ``True`` to draw the circle
* * ``false`` to not draw the circle
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``vector<int>``) -- The color of the circle. ``{R, G, B, A}``
*  ``segments`` (``int``) -- The number of segments of the circle. 
* * Default is ``16``. 
* * Better to keep between ``1-50``. Going further may cause the process to crash.

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
*  ``draw`` (``bool``) -- Whether to draw the circle or not.
* * ``True`` to draw the circle
* * ``false`` to not draw the circle
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``vector<int>``) -- The color of the circle. ``{R, G, B, A}``
*  ``colorBorder`` (``vector<int>``) -- The color of the border. ``{R, G, B, A}``
*  ``borderFilled`` (``bool``)
* * ``True`` to fill the border
* * ``false`` to not fill the border
*  ``segments`` (``int``) -- The number of segments of the circle. 
* * Default is ``16``. 
* * Better to keep between ``1-50``. Going further may cause the process to crash.

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
*  ``draw`` (``bool``) -- Whether to draw the triangle or not.
* * ``True`` to draw the triangle
* * ``false`` to not draw the triangle
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``size`` (``float``) -- The size of the triangle (in pixels). 
* * Default is ``1.1``.

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
*  ``draw`` (``bool``) -- Whether to draw the triangle or not.

* * ``True`` to draw the triangle
* * ``false`` to not draw the triangle
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``size`` (``float``) -- The size of the triangle (in pixels). 
* * Default is ``1.1``.

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
*  ``draw`` (``bool``) -- Whether to draw the triangle or not.
* * ``True`` to draw the triangle
* * ``false`` to not draw the triangle
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``vector<int>``) -- The color of the triangle. ``{R, G, B, A}``
*  ``colorBorder`` (``vector<int>``) -- The color of the border. ``{R, G, B, A}``
*  ``borderFilled`` (``bool``)

* * ``True`` to fill the border (Default)
* * ``false`` to not fill the border

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
*  ``draw`` (``bool``) -- Whether to draw the text or not.
* * ``True`` to draw the text
* * ``false`` to not draw the text
*  ``text`` (``string``) -- The text to draw.
*  ``x`` (``float``) -- The X coordinate of the text's center.
*  ``y`` (``float``) -- The Y coordinate of the text's center.
*  ``scale`` (``float``) -- The scale of the text.
*  ``color`` (``vector<int>``) -- The color of the text. ``{R, G, B, A}``
*  ``flags`` (``int``) -- The flags for the text. 
* * Default is ``0``.

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

Checks whether the color picker is active.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- The color picker is active
  * ``false`` -- The color picker is inactive

**Example:**

.. code-block:: lua
   :linenos:
      
   if render.is_color_picker_rendering() then
      system.log_info("The color picker is active!") -- Prints if the color picker is active.
   end

================================

is_cursor_hover_menu()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the cursor is hovering over the menu.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- The cursor is hovering over the menu
  * ``false`` -- The cursor is not hovering over the menu

**Example:**

.. code-block:: lua
   :linenos:

   if render.is_cursor_hover_menu() then
      system.log_info("The cursor is hovering over the menu!") -- This will only be logged if the cursor is hovering over the menu.
   end

================================

is_cursor_hover_option()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the cursor is hovering over an option.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- The cursor is hovering over an option
  * ``false`` -- The cursor is not hovering over an option

**Example:**

.. code-block:: lua
   :linenos:
      
   if render.is_cursor_hover_option() then
      system.log_info("The cursor is hovering over an option!") -- This will only be logged if the cursor is hovering over an option.
   end

================================

is_input_active()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the input window is active. (The input window is for example, the window that appears when you press the ` key in story mode)

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- The input window is active
  * ``false`` -- The input window is inactive

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
   
   if self.is_alive() then -- Checks whether the user is alive.
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
   
   if self.is_in_vehicle() then -- Checks whether the user is in a vehicle.
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

* ``bool`` -- Whether the player is valid. 

  * Can also be ``true`` during cutscenes.

**Example:**

.. code-block:: lua
   :linenos:
   
   if self.is_valid() then -- Checks whether the player is valid.
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

  * ``0`` -- The first character is used
  * ``1`` -- The second character is used

**Example:**

.. code-block:: lua
   :linenos:
   
   index = self.get_online_index() -- Returns the online index of the user's character.
   if index == 0 then -- Checks whether the first character is used.
      system.log_info("The first character is used.")
   elseif index == 1 then -- Checks whether the second character is used.
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
^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns coordinates in front of your character.

**Parameters:**

* ``distance`` (``float``) -- Distance calculated starting from in front of self. 

  * Default value is ``5.0``.

**Returns:**

* ``Vector3`` -- Returns coordinates in Vector3 form.

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords_infront(5)
   system.log_info("The coords in front of me are: " .. tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z) .. " .")

======================

get_vehicle()
^^^^^^^^^^^^^^^^^

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
   
   isActive = lobby.is_player_active(lobby.get_host()) -- Checks whether the player is active.
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
   
   isConnected = lobby.is_player_connected(lobby.get_host()) -- Checks whether the player is connected.
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
   
   isFriend = lobby.is_player_friend(lobby.get_host()) -- Checks whether the player is a friend.
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
   
   isHost = lobby.is_player_host(lobby.get_host()) -- Checks whether the player is the host.
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
   
   isHostNext = lobby.is_player_host_next(lobby.get_host()) -- Checks whether the player is the next script host.
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
   
   isInVehicle = lobby.is_player_in_vehicle(lobby.get_host()) -- Checks whether the player is in a vehicle.
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
   
   isModder = lobby.is_player_modder(lobby.get_host()) -- Checks whether the player is a modder.
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
   
   isSelected = lobby.is_player_selected(lobby.get_host()) -- Checks whether the player is selected.
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
   
   isStaff = lobby.is_player_staff(lobby.get_host()) -- Checks whether the player is a Rockstar staff member.
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
   
   isValid = lobby.is_player_valid(lobby.get_host()) -- Checks whether the player is valid.
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
   
   isStarted = lobby.is_session_started() -- Checks whether the session has started.
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

.. _lobby_get_player_team:

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

  * ``H`` -- The player is the host.
  * ``NH`` -- The player is the next host.
  * ``F`` -- The player is a friend.
  * ``M`` -- The player is a modder.

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

  * ``true`` -- The player is a modder.
  * ``false`` -- The player is not a modder.

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

  * ``true`` -- The player is set as selected.
  * ``false`` -- The player is set as not selected.

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

  * ``true`` -- The player is a staff member.
  * ``false`` -- The player is not a staff member.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if string contains character/word.

**Parameters:**

* ``source`` (``string``) -- The string to check.
* ``data`` (``string``) -- The data to check for.

**Returns:**

* ``bool``

  * ``true`` -- The string contains the data.
  * ``false`` -- The string does not contain the data.

**Example:**

.. code-block:: lua
   :linenos:
	
   loremIpsum = Lorem ipsum dolor sit amet
   Contains = text.contains(loremIpsum, "Lorem")
   system.log_debug(tostring(Contains))

======================

is_float(``data``)
^^^^^^^^^^^^^^^^^^^^^^^

Check if string is ``float`` type.

**Parameters:**

* ``data`` (``string``) -- The data to check.

**Returns:**

* ``bool``

  * ``true`` -- The data is a float.
  * ``false`` -- The data is not a float.

**Example:**

.. code-block:: lua
   :linenos:

   isFloat = text.is_float("10.1")
   system.log_debug(tostring(isFloat))

======================

is_number(``data``)
^^^^^^^^^^^^^^^^^^^^^

Check if string is a number.

**Parameters:**

* ``data`` (``string``) -- The data to check.

**Returns:**

* ``bool``

  * ``true`` -- The data is a number.
  * ``false`` -- The data is not a number.

**Example:**

.. code-block:: lua
   :linenos:

   isNumber = text.is_number("10")
   system.log_debug(tostring(isNumber))

======================

is_valid_ip4(``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the string is a valid IPv4.

**Parameters:**

* ``data`` (``string``) -- The data to check.

**Returns:**

* ``bool``

  * ``true`` -- The data is a valid IPv4.
  * ``false`` -- The data is not a valid IPv4.


**Example:**

.. code-block:: lua
   :linenos:
   
   isValid = text.is_valid_ip4("1.1.1.1")
   system.log_debug(tostring(isValid))


======================

get_random_string(``length``, ``type``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generates a random string.

**Parameters:**

* ``length`` (``int``) -- Length of the string.
* ``type`` (``eRandomType``) -- Type of string generation: 

  * ``0`` -- Upper
  * ``1`` -- Lower
  * ``2`` -- Digits
  * ``3`` -- UpperLower
  * ``4`` -- UpperDigits
  * ``5`` -- LowerDigits

**Returns:**

* ``string`` -- The generated random string.

**Example:**

.. code-block:: lua
   :linenos:

   r = text.get_random_string(10, 2) -- Generates a random string made of digits
   system.log_debug(r)

======================

remove_characters(``data``, ``word``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Checks whether the directory exists.

**Parameters:**

* ``dir`` (``string``) -- Directory to check

**Returns:**

* ``bool``

  * ``True`` -- directory exists
  * ``False`` -- directory does not exist

**Example:**

.. code-block:: lua
   :linenos:
   
   if fs.dir_exist("C:\Users\") then
      system.log_info("Directory exists.")

   end

================================

file_exist(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the file exists.

**Parameters:**

* ``file`` (``string``) -- File to check

**Returns:**

* ``bool``

  * ``True`` -- file exists
  * ``False`` -- file does not exist

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

* ``bool``

  * ``True`` -- The file was removed
  * ``False`` -- The file was not removed (e.g. file was not found)

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

Checks whether the file is corrupted, Checks whether the permissions are correct, if it's readable and if it's writable.

**Parameters:**

* ``file`` (``string``) -- File to validate

**Returns:**

* ``bool``

  * ``True`` -- The file is valid
  * ``False`` -- The file is invalid (e.g. file was not found)

**Example:**

.. code-block:: lua
   :linenos:
   
   if fs.file_validate("/test.txt") then
      system.log_info("File is valid and ready.")
   end

================================

is_file_empty(``file``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the file is empty.

**Parameters:**

* ``file`` (``string``) -- File to check

**Returns:**

* ``bool``

  * ``True`` -- The file is empty
  * ``False`` -- The file is not empty

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

Checks whether the directory exists, and if not, creates it.

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

Checks whether the bypass for spawning Online cars in SinglePlayer is enabled.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``True`` -- The bypass is enabled
  * ``False`` -- The bypass is disabled

**Example:**

.. code-block:: lua
   :linenos:
   
   if get_vehicle_bypass() then
      system.log_info("The bypass is enabled.")
   end   

================================

set_vehicle_bypass(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the bypass for spawning Online cars in SinglePlayer is enabled.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle the bypass

  * ``True`` -- Enable the bypass
  * ``False`` -- Disable the bypass

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   if not scripting.get_vehicle_bypass() then
      scripting.set_vehicle_bypass(true) -- Enables the bypass.
      system.log_info("The bypass is enabled.")
   end
   

================================

get_coords_infront_of_coords(``position``, ``rotation``, ``distance``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the coordinates in front of the specified coordinates.

**Parameters:**

* ``position`` (``Vector3``) -- Specified coordinates
* ``rotation`` (``Vector3``) -- Rotation to use
* ``distance`` (``float``) -- Distance to the object

**Returns:**

* ``Vector3`` -- Coordinates in front of the object

**Example:**

.. code-block:: lua
   :linenos:

   coords = scripting.get_coords_infront_of_coords(self.get_coords(), rage.entity.get_entity_rotation(self.get_ped(), 1), 10)
   system.log_debug(tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z))

================================

get_coords_above_of_coords(``position``, ``distance``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the coordinates above of the specified coordinates.

**Parameters:**

* ``position`` (``Vector3``) -- Specified coordinates
* ``distance`` (``float``) -- Distance from the coordinates

**Returns:**

* ``Vector3`` -- Coordinates above of the object

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = get_coords_above_of_coords(self.get_coords(), 10)
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

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable the force field
  * ``false`` to disable it
  
* ``type`` (``int``) -- Type of the force field 

  * ``0`` for ``Normal`` (Default)
  * ``1`` for ``Lethal``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_force_field(true, 1)
   system.log_debug("Lethal force field enabled.")

================================

set_god_mode(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles god mode.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable god mode
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_god_mode(true)
   system.log_debug("God mode enabled.")

================================

set_infinite_stamina(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles infinite stamina.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable infinite stamina
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_infinite_stamina(true)
   system.log_debug("Infinite stamina enabled.")

================================

set_invisibility(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles invisibility.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable invisibility
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_invisibility(true)
   system.log_debug("Invisibility enabled.")

================================

set_mobile_radio(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles mobile radio.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable mobile radio
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_mobile_radio(true)
   system.log_debug("Mobile radio enabled.")

================================

set_night_vision(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles night vision.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable night vision
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_night_vision(true)
   system.log_debug("Night vision enabled.")

================================

set_no_wanted_level()
^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the wanted level to 0.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_no_wanted_level()
   system.log_debug("Wanted level set to 0.")

================================

set_noclip(``toggle``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles noclip.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable noclip
  * ``false`` to disable it
  
* ``speed`` (``float``) -- Speed of the noclip

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_noclip(true, 1.0)
   system.log_debug("Noclip enabled.")

================================

set_ragdoll(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles ragdoll.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable ragdoll
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_ragdoll(true)
   system.log_debug("Ragdoll enabled.")

================================

set_regeneration(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the regeneration value.

**Parameters:**

* ``value`` (``float``) -- The regeneration value

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_regeneration(0.5)
   system.log_debug("Regeneration set to 0.5.")

================================

set_run_speed(``toggle``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles and configures the walk & run speed.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable speed hack
  * ``false`` to disable it

* ``value`` (``float``) -- Speed

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_run_speed(true, 1.0)
   system.log_debug("Run speed enabled.")


================================

set_seatbelt(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles seatbelt.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable seatbelt
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_seatbelt(true)
   system.log_debug("Seatbelt enabled.")



set_super_run(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles and configures super run mode.

**Parameters:**

* ``value`` (``float``) -- Speed

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_super_run(4.0)
   system.log_debug("Super run enabled.")

================================

set_swim_speed(``toggle``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles and configures the swim speed.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable swim hack
  * ``false`` to disable it

* ``value`` (``float``) -- Speed

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_swim_speed(true, 4.0)
   system.log_debug("Swim speed enabled.")

================================

set_thermal_vision(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles thermal vision.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable thermal vision
  * ``false`` to disable it

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_thermal_vision(true)
   system.log_debug("Thermal vision enabled.")

================================

set_walk_on_air(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles walk on air.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` to enable walk on air
  * ``false`` to disable it
   
================================

set_wanted_level(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the wanted level.

**Parameters:**

* ``value`` (``int``) -- The wanted level

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.player.set_wanted_level(5)
   system.log_debug("Wanted level set to 5.")

================================

.. _pedNSS:

Ped namespace
----------------------

This namespace contains functions that are related to ped and are used to execute built-in menu features

================================

clone_companion(``owner``, ``target``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clones the target ped and sets it as a companion of the owner.

**Parameters:**

* ``owner`` (``Entity``) -- The owner of the clone
* ``target`` (``Entity``) -- The target to clone
* ``weaponHash`` (``Hash``) -- The weapon hash to clone with

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   player = self.get_ped()
   scripting.ped.clone_companion(player, player, rage.gameplay.get_hash_key("Pistol"))
   system.log_debug("Cloned player.")
   
================================

kill_enemies()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kills all enemies.

**Parameters:**

* None

**Returns:**
   
* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.ped.kill_enemies()
   system.log_debug("Killed all enemies.")

================================

kill_nearby_peds()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kills all nearby peds.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.ped.kill_nearby_peds()
   system.log_debug("Killed all nearby peds.")


================================

.. _entityNSS:

Entity namespace
----------------------

This namespace contains functions that are related to Entities and are used to execute built-in menu features

================================

is_entity_in_whitelist(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is still in development.


Checks whether the entity is in the whitelist.

**Parameters:**

* ``entity`` (``Entity``) -- The entity to check

**Returns:**

* ``bool``

  * ``true`` -- The entity is in the whitelist
  * ``false`` -- The entity is not in the whitelist

**Example:**

.. code-block:: lua
      :linenos:
      
      entity = self.get_ped()
      scripting.entity.is_entity_in_whitelist(entity)
      system.log_debug("Entity is in whitelist: " .. tostring(entity_in_whitelist))


================================

entity_add_to_whitelist(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is still in development.

Adds the entity to the whitelist.

**Parameters:**

* ``entity`` (``Entity``) -- The entity to add

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   entity = self.get_ped()
   scripting.entity.entity_add_to_whitelist(entity)
   system.log_debug("Entity added to whitelist.")

================================


entity_remove_from_whitelist(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is still in development.

Removes the entity from the whitelist.

**Parameters:**

* ``entity`` (``Entity``) -- The entity to remove

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   entity = self.get_ped()
   scripting.entity.entity_remove_from_whitelist(entity)
   system.log_debug("Entity removed from whitelist.")

================================

set_proofs(``entity``, ``bulletProof``, ``fireProof``, ``explosionProof``, ``collisionProof``, ``meleeProof``, ``drownProof``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets resistance to certain damage.

**Parameters:**

* ``entity`` (``Entity``) -- The entity to set resistance to
* ``bulletProof`` (``bool``) -- Bullet resistance
* ``fireProof`` (``bool``) -- Fire resistance
* ``explosionProof`` (``bool``) -- Explosion resistance
* ``collisionProof`` (``bool``) -- Collision resistance
* ``meleeProof`` (``bool``) -- Melee resistance
* ``drownProof`` (``bool``) -- Drown resistance

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   entity = self.get_ped()
   scripting.entity.set_proofs(entity, true, true, true, true, true, true)
   system.log_debug("Nanomachines, son.")

================================

.. _vehicleNSS:

Vehicle namespace
----------------------

This namespace contains functions that are related to vehicle mods and are used to execute built-in menu features

================================


get_name_from_hash(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the name of the vehicle based on its hash.

**Parameters:**

* ``hash`` (``Hash``) -- The hash of the vehicle

**Returns:**

* ``string`` -- The name of the vehicle

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicle_name = scripting.vehicle.get_name_from_hash(rage.gameplay.get_hash_key("BMX"))
   system.log_debug("Vehicle name: " .. vehicle_name)

================================

get_personal_vehicle()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the personal vehicle ID.

**Parameters:**

* None

**Returns:**

* ``Vehicle`` -- The personal vehicle ID

**Example:**

.. code-block:: lua
   :linenos:
   
   personal_vehicle = scripting.vehicle.get_personal_vehicle()
   system.log_debug("Personal vehicle: " .. tostring(personal_vehicle))

================================

remove_nearby_vehicles()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes all nearby vehicles.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.remove_nearby_vehicles()
   system.log_debug("Removed all nearby vehicles.")

================================

set_air_vehicles_collision(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the air vehicles collision.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Enable the air vehicles collision
  * ``false`` -- Disable the air vehicles collision

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.set_air_vehicles_collision(true)
   system.log_debug("Air vehicles collision is now enabled.")

================================

set_boost(``vehicle``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the boost speed of the specified vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle to set the boost speed of
* ``speed`` (``float``) -- The boost speed

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicle = self.get_vehicle()
   scripting.vehicle.set_boost(vehicle, 50)
   system.log_debug("Boost speed set to 50 units.")

================================

set_bulletproof_tires(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the bulletproof tires.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Enable the bulletproof tires
  * ``false`` -- Disable the bulletproof tires

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.set_bulletproof_tires(true)
   system.log_debug("Bulletproof tires are now enabled.")

================================

set_clean(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cleans the specified vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle to clean

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicle = self.get_vehicle()
   scripting.vehicle.set_clean(vehicle)
   system.log_debug("Vehicle cleaned.")

================================

set_doors_opened(``vehicle``, ``toggle``, ``doorId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Opens or closes the doors of the specified vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle to open or close the doors of
* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Open the doors
  * ``false`` -- Close the doors

* doorId (``int``) -- The door ID

  * For door IDs, see this: :doc:`doors`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicle = self.get_vehicle()
   scripting.vehicle.set_doors_opened(vehicle, true, 0)
   system.log_debug("Door opened.")

================================

set_drift(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles the drift mode.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Enable the drift mode
  * ``false`` -- Disable the drift mode

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.set_drift(true)
   system.log_debug("Drift mode is now enabled.")

================================

set_drive_on_air(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles the Drive on Air mode.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle to toggle the Drive on Air mode of

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Enable the Drive on Air mode
  * ``false`` -- Disable the Drive on Air mode

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicle = self.get_vehicle()
   scripting.vehicle.set_drive_on_air(vehicle, true)
   system.log_debug("Drive on Air mode is now enabled.")

================================

set_force_jump(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles the vehicle force jump mode.


**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Enable the force jump mode
  * ``false`` -- Disable the force jump mode

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.set_force_jump(true)
   system.log_debug("Force jump mode is now enabled.")

================================

set_god_mode(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles the god mode for the vehicle.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Enable the god mode
  * ``false`` -- Disable the god mode

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.set_god_mode(true)
   system.log_debug("God mode is now enabled.")


================================

set_headlight_color(``color``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the headlight color of the specified vehicle.

**Parameters:**

* ``color`` (``int``) -- The headlight color ID

  * For color IDs, see this: :doc:`headlightcolor`
**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.vehicle.set_headlight_color(1)
   system.log_debug("Headlight color set to white.")

================================


set_license_plate_madness(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle license plate madness.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Toggle license plate madness on
  * ``false`` -- Toggle license plate madness off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_license_plate_madness(true)

================================

set_license_plate_scrolling(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle license plate scrolling.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Toggle license plate scrolling on
  * ``false`` -- Toggle license plate scrolling off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_license_plate_scrolling(true)

================================

set_license_plate_speedo(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle license plate speedo mode.

**Parameters:**

* ``toggle`` (``bool``)

  * ``true`` -- Toggle license plate speedo on
  * ``false`` -- Toggle license plate speedo off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_license_plate_speedo(true)

================================

set_rainbow_car(``type``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle rainbow car mode.

**Parameters:**

* ``type`` (``eRainbowCarType``) -- Car type

  * ``0`` -- Personal car
  * ``1`` -- All cars

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_rainbow_car(1) -- Sets all cars rainbow

================================

set_rainbow_headlights()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle rainbow headlights feature.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_rainbow_headlights()

================================

set_rainbow_neon()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle rainbow neon feature.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_rainbow_neon()

================================

set_rainbow_tires_smoke()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle rainbow tires smoke.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_rainbow_tires_smoke()

================================

set_repair()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Repairs vehicle.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_repair()
================================

set_stick_to_ground()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make a vehicle stick to the ground.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.vehicle.set_stick_to_ground()

================================

set_stop(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make a vehicle stop.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- Vehicle hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_stop(personal_vehicle)

================================

set_vehicle_clean_upgrade(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make a vehicle be max upgraded (only non-visible parts eg. engine, turbo...)

**Parameters:**

* ``vehicle`` (``Vehicle``) -- Vehicle hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_vehicle_clean_upgrade(personal_vehicle)

================================

set_vehicle_color(``v``, ``primary``, ``secondary``, ``pearl``, ``wheel``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set vehicle color (primary, secondary, pearlescence, wheels)

**Parameters:**

* ``v`` (``Vehicle``) -- Vehicle hash
* ``primary`` (``int``) -- Primary `color ID`_
* ``secondary`` (``int``) -- Secondary `color ID`_
* ``pearl`` (``int``) -- Pearlescence `color ID`_ (if applicable)
* ``wheel`` (``int``) -- Wheel `color ID`_
  
.. _color ID: https://wiki.rage.mp/index.php?title=Vehicle_Colors

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_vehicle_color(personal_vehicle, 12, 28, 12)

================================

set_vehicle_max_upgrade(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make a vehicle be max upgraded.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- Vehicle hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_vehicle_max_upgrade(personal_vehicle)

================================

set_waterproof(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a vehicle waterproof.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- Vehicle hash
* ``toggle`` (``bool``) -- Toggle waterproof on/off

  * ``true`` -- Vehicle is waterproof
  * ``false`` -- Vehicle is not waterproof

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_waterproof(personal_vehicle, true) -- Your vehicle can now swim

================================

set_windows_opened(``vehicle``, ``toggle``, ``windowId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set windows opened on a vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- Vehicle hash
* 
* ``toggle`` (``bool``) -- Toggle windows open/closed

  * ``true`` -- Windows open
  * ``false`` -- Windows closed

* ``windowId`` (``int``) -- Window ID to manipulate

  * For window IDs, see this: :doc:`windows`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_windows_opened(personal_vehicle, true, 1)

================================

.. _online:

Online namespace
----------------

This namespace contains functions that are related to online features and are used to execute built-in menu features

================================

reset_idle_kick_timer()
^^^^^^^^^^^^^^^^^^^^^^^^^

Resets the AFK kick timer.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.reset_idle_kick_timer()
   system.log_debug("Reset AFK kick timer.")

================================

set_off_radar(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle the off radar feature.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle the off radar feature

  * ``true`` -- Enable the off radar feature
  * ``false`` -- Disable the off radar feature

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.set_off_radar(true)
   system.log_debug("Off radar enabled.")

================================

set_passive_mode(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle the passive mode.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle the passive mode

  * ``true`` -- Enable the passive mode
  * ``false`` -- Disable the passive mode

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.set_passive_mode(true)
   system.log_debug("Passive mode enabled.")

================================

set_securoserv_bypass()
^^^^^^^^^^^^^^^^^^^^^^^^^

Activates the securoserv bypass.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.set_securoserv_bypass()
   system.log_debug("Securoserv bypass activated.")

================================

set_skip_cutscene()
^^^^^^^^^^^^^^^^^^^^^

Activates the skip cutscene feature.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.set_skip_cutscene()
   system.log_debug("Skip cutscene activated.")

================================

set_spectating_mode(``toggle``, ``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle and configure the spectating mode.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle the spectating mode

  * ``true`` -- Enable the spectating mode
  * ``false`` -- Disable the spectating mode
* ``player`` (``Player``) -- The player to spectate

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.set_spectating_mode(true, lobby.get_host())
   system.log_debug("Spectating mode enabled.")


================================

teleport_in_player_vehicle(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleports the player into specified player's vehicle.

**Parameters:**

* ``player`` (``Player``) -- The player to teleport to

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.teleport_in_player_vehicle(lobby.get_host())
   system.log_debug("Teleported into host's vehicle.")

================================

teleport_to_player(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleports the player to specified player.

**Parameters:**

* ``player`` (``Player``) -- The player to teleport to

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.teleport_to_player(lobby.get_host())
   system.log_debug("Teleported to host.")

================================

toggle_protex(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle the online protections.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle the online protections

  * ``true`` -- Enable the online protections
  * ``false`` -- Disable the online protections

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.online.toggle_protex(true)
   system.log_debug("Online protections enabled.")


================================

.. _networkNSS:

Network namespace
----------------------

This namespace contains functions that are related to session creation and are used to execute built-in menu features.

================================

session_choose_character()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends the player to the character selection screen.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.network.session_choose_character()
   system.log_debug("Sent to character selection screen.")

================================

session_leave_online()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends the player to the singleplayer mode.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.network.session_leave_online()
   system.log_debug("Sent to singleplayer mode.")

================================

session_manager(``id``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends the player to the specified session.

**Parameters:**

* ``id`` (``eSessionType``) -- The session to send the player to

  * Read more about eSessionType here -- :ref:`eSessionType`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.network.session_manager(0)
   system.log_debug("Sent to the open public session.")


================================

.. _spawn:

Spawn namespace
----------------

This namespace contains functions that are related to spawn and are used to execute built-in menu features.

================================

spawn_vehicle(``hash``, ``position``, ``heading``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Spawns a vehicle in a given position and heading.

**Parameters:**

* ``hash`` (``Hash``) -- Vehicle hash
* ``position`` (``Vector3``) -- Vehicle coordinates
* ``heading`` (``float``) -- Vehicle heading

**Returns:**

* ``Vehicle`` -- Returns the spawned vehicle.

**Example:**

.. code-block:: lua
   :linenos:
   
   zentornoHash = rage.gameplay.get_hash_key("ZENTORNO")

   scripting.spawn.spawn_vehicle(zentornoHash, self.get_coords(), 1)

================================

spawn_vehicle_personal(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Spawns a personal vehicle.

**Parameters:**

* ``hash`` (``Hash``)

**Returns:**

* ``Vehicle`` -- Returns the spawned vehicle.

**Example:**

.. code-block:: lua
   :linenos:

   scripting.spawn.spawn_vehicle_personal(rage.gameplay.get_hash_key("ZENTORNO"))

================================

.. _weaponNSS:

Weapon namespace
----------------------

This namespace contains functions that are related to weapons and are used to execute built-in menu features.

================================

give_all_weapons(``ped``, ``maxAmmo`` = ``true``, ``maxComponents`` = ``true``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Give all weapons to a ped with toggable max ammo and max components.

**Parameters:**

* ``ped`` (``Ped``) -- The ped to give all weapons to.

* ``maxAmmo`` (``bool``) -- Toggle Max Ammo

  * ``true`` -- Weapons will be given with max ammo (default)
  * ``false`` -- Weapons will be given without max ammo
  
* ``maxComponents`` -- Toggles Max Components

  * ``true`` -- Weapons will be given fully upgraded in components (default)
  * ``false`` -- Weapons will be given in their default form


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.give_all_weapons(lobby.get_player_ped(lobby.get_host()), true, true) -- Gives all maxed and upgraded weapons to the session host.

================================

remove_all_weapons_from_ped(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes all weapons from a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped to remove all weapons from.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.remove_all_weapons_from_ped(lobby.get_player_ped(lobby.get_host())) -- Removes all weapons from the session host

================================

give_weapon_self(``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives weapon to the player (self).

**Parameters:**

* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ to give to self.
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.give_weapon_self(rage.gameplay.get_hash_key("MicroSMG")) -- Gives self the MicroSMG

================================

give_weapon(``ped``, ``weaponHash``, ``maxAmmo`` = ``true``, ``maxComponents`` = ``true``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives a weapon to ped with toggable max ammo and max components.

**Parameters:**

* ``ped`` (``Ped``) -- The ped to give the weapon to.

* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ to give to the player.

* ``maxAmmo`` (``bool``) -- Toggles Max Ammo

  * ``true`` -- Weapon will be given with max ammo (default)
  * ``false`` -- Weapon will be given without max ammo
  
* ``maxComponents`` -- Toggles Max Components

  * ``true`` -- Weapon will be given fully upgraded in components (default)
  * ``false`` -- Weapon will be given in its default form

.. _Whash: https://wiki.rage.mp/index.php?title=Weapons


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.give_weapon(lobby.get_player_ped(lobby.get_host()), rage.gameplay.get_hash_key("MicroSMG"), true, true) -- Gives session host a fully loaded and upgraded MicroSMG

================================

give_ammo(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives ammo to a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped to ammo to.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.give_ammo(lobby.get_player_ped(lobby.get_host())) -- Gives ammo to session host's weapons

================================

give_ammo_for_weapon(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives ammo for a precise weapon to a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The targeted ped.

* ``weaponHash`` (``Hash``) -- Ped's weapon `Whash`_ to give ammo to.

.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.give_ammo_for_weapon(lobby.get_player_ped(lobby.get_host()), rage.gameplay.get_hash_key("MicroSMG")) -- Gives ammo to session host's MicroSMG

================================

ammo_infinite(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives infinite ammo to a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The targeted ped.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.ammo_infinite(lobby.get_player_ped(lobby.get_host())) -- Gives infinite ammo to session host

================================

ammo_enhanced(``ped``, ``explosionId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives enhanced ammo (ammo that generate a particular explosion) to a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The targeted ped.
  
* ``explosionId`` (``int``) -- The explosion ID determinates the type of explosion to assign to the ammo.

  * You can read more about explosion IDs here: :doc:`exptypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.ammo_enhanced(lobby.get_player_ped(lobby.get_host()), 7) -- Gives EXPLOSION_CAR type ammo to session host

================================

ammo_mega_damage(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives mega damage ammo to a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The targeted ped.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.weapon.ammo_mega_damage(lobby.get_player_ped(lobby.get_host())) -- Gives mega damage ammo to Trevor

================================

.. _teleport:

Teleport namespace
----------------------

This namespace contains functions that are related to teleport and are used to execute built-in menu features.

================================

to_blip(``sprite``, ``color`` = ``-1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to blip.

**Parameters:**

* ``sprite`` (``int``) -- The `blip <https://wiki.rage.mp/index.php?title=Blips>`__ sprite ID to use.
* ``color`` (``int``) -- The `blip <https://wiki.rage.mp/index.php?title=Blips>`__ color ID to use.

  * ``-1`` to use the default color



**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_blip(1, 1) -- red circle blip

================================

to_entity(``ent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to entity.

**Parameters:**

* ``ent`` (``Entity``) -- Targeted entity to teleport to.

**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_entity("prop_storagetank_02b") -- Teleport to the nearest fuel storage tank entity.

================================

to_player(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to player.

**Parameters:**

* ``player`` (``Player``) -- Targeted player to teleport to.

**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_player(lobby.get_host()) -- Teleport to the host player.

================================

to_position(``coords``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to position (through coordinates).

**Parameters:**

* ``coords`` (``Vector3``) -- Targeted coordinates (Vector3) to teleport to.

**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_position(lobby.get_player_coords(lobby.get_host())) -- Teleport to the host player's coordinates.

================================

to_waypoint()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to waypoint.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_waypoint()

================================

to_objective()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to objective.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_objective()

================================

to_nearest_vehicle()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to the nearest vehicle.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- Teleportation successful
  * ``false`` -- Teleportation failed

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_nearest_vehicle()

================================

to_personal_vehicle()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to personal vehicle.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.to_personal_vehicle()

================================

ipl_to_yankton()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to North Yankton (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_yankton()

================================

ipl_to_cargo_ship()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Cargo Ship (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_cargo_ship()

================================

ipl_to_hospital()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Hospital (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_hospital()

================================

ipl_to_yacht_sp()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to SinglePlayer Yacht (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_yacht_sp()

================================

ipl_to_yacht_online()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Online Yacht (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_yacht_online()

================================

ipl_to_morgue()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Morgue (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_morgue()

================================

ipl_to_ranch()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Ranch (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_ranch()

================================

ipl_to_jewelry()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Jewelry (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_jewelry()

================================

ipl_to_life_invader()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to Life Invader (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_life_invader()

================================

ipl_to_fib()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Teleport to FIB building (IPL location).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scripting.teleport.ipl_to_fib()

================================

.. _world:

World namespace
----------------------

This namespace contains functions that are related to world and are used to execute built-in menu features.

================================

set_weather(``weatherType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set weather type.

**Parameters:**

* ``weatherType`` (``string``) -- The weather type

  * For weather types, see this: :doc:`weathertypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.set_weather("RAIN") -- make it rain

================================

set_clouds(``cloudsType``, ``transitionTime``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set clouds type and their transition time.

**Parameters:**

* ``cloudsType`` (``string``)  -- The clouds type

  * For weather types, see this: :doc:`weathertypes`
* ``transitionTime`` (``float``)  -- The speed of clouds


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.set_clouds("RAIN")

================================

set_rain_intensity(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the rain intensity.

**Parameters:**

* ``value`` (``float``) -- Rain intensity value.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.set_rain_intensity(5.5)

================================

set_wind_speed(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the wind speed.

**Parameters:**

* ``value`` (``float``) -- Wind speed value.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.set_wind_speed(3)

================================

set_waves_height(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the waves height.

**Parameters:**

* ``value`` (``float``) -- Waves height value.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.set_waves_height(4)

================================

set_time(``hours``, ``minutes``, ``seconds``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the in-game time.

**Parameters:**

* ``hours`` (``int``) -- Hours
* ``minutes`` (``int``) -- Minutes
* ``seconds`` (``int``) -- Seconds

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.set_time(12, 30, 10) -- 12:30:10

================================

blackout(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle blackout on/off.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Toggle blackout on
  * ``false`` -- Toggle blackout off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.blackout(true) -- Blackout is on.

================================

angry_ufo()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activates Angry Ufo feature.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.angry_ufo()

================================

disable_phone(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disable phone option

**Parameters:**

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Toggle disable phone on
  * ``false`` -- Toggle disable phone off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.disable_phone(true) -- Disable phone option toggled on, phone is disabled.

================================

disable_recording()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disable GTA built-in recording feature.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.disable_recording() -- Disable recording

================================

disable_restricted_areas()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disable GTA restricted areas.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.disable_restricted_areas()

================================

disable_stunt_cameras()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disable GTA built-in stunt cameras.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scripting.world.disable_stunt_cameras()

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

This namespace contains player-related game functions.

================================

get_player_group(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the group ID the player is member of. Used for :ref:`ai`.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``int`` -- Group ID

**Example:**

.. code-block:: lua
   :linenos:
   
   group = rage.player.get_player_group(rage.player.player_id())
   system.log_debug("Player is member of group: " .. tostring(group))


================================

get_player_name(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player name.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``string`` -- Player name

**Example:**

.. code-block:: lua
   :linenos:
   
   name = rage.player.get_player_name(rage.player.player_id())
   system.log_debug("Player name: " .. tostring(name))

================================

get_player_parachute_model_override(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the hash of the parachute model.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``Hash`` -- Parachute model hash

**Example:**

.. code-block:: lua
   :linenos:
   
   parachute_model = rage.player.get_player_parachute_model_override(rage.player.player_id())
   system.log_debug("Player parachute model hash: " .. tostring(parachute_model))



================================

get_player_ped_script_index(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Ped ID of the player's character.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``Ped`` -- Ped ID

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = rage.player.get_player_ped_script_index(rage.player.player_id())
   system.log_debug("Player ped: " .. tostring(ped))

================================

get_player_team(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the team ID the player is member of. Almost like :ref:`lobby_get_player_team`.

.. note::

   Doesn't work in singleplayer. 

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``int`` -- Team ID

**Example:**

.. code-block:: lua
   :linenos:
   
   team = rage.player.get_player_team(rage.player.player_id())
   system.log_debug("Player is member of team: " .. tostring(team))

================================

get_player_wanted_level()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's wanted level.

**Parameters:**

* None

**Returns:**

* ``int`` -- Wanted level

================================

is_player_free_aiming(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns whether the player is aiming.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``bool``

  * ``true`` -- the player is aiming
  * ``false`` -- the player is not aiming
  
**Example:**

.. code-block:: lua
   :linenos:
   
   if rage.player.is_player_free_aiming(rage.player.player_id()) then
      system.log_debug("Player is aiming")
   end

================================

is_player_playing(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns whether the wasted/busted screen is visible or not.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``bool``

  * ``true`` -- the wasted/busted screen is visible
  * ``false`` -- the wasted/busted screen is not visible

================================

is_player_pressing_horn(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the player is pressing the horn.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``bool``

  * ``true`` -- Player is pressing the horn
  * ``false`` -- Player is not pressing the horn

**Example:**

.. code-block:: lua
   :linenos:
   
   if rage.player.is_player_pressing_horn(rage.player.player_id()) then
      system.log_debug("Player is pressing the horn")
   end

================================

player_id()
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player ID.

**Parameters:**

* None

**Returns:**

* ``Player`` -- Player ID

**Example:**

.. code-block:: lua
   :linenos:
   
   player = rage.player.player_id()
   system.log_debug("Player ID: " .. tostring(player))

================================

set_player_model(``player``, ``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the model for a specific player.

.. note::
   
   This will destroy the current Ped for the Player and create a new one.

**Parameters:**

* ``player`` (``Player``) -- The player ID
* ``model`` (``Hash``) -- The model hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   rage.player.set_player_model(rage.player.player_id(), rage.gameplay.get_hash_key(ig_floyd))


================================

set_player_parachute_model_override(``player``, ``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the parachute model for a player.

**Parameters:**

* ``player`` (``Player``) -- The player ID
* ``model`` (``Hash``) -- The model hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   rage.player.set_player_parachute_model_override(rage.player.player_id(), 73268708)

================================


set_player_targeting_mode(``targetMode``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets your targeting mode.

**Parameters:**

* ``targetMode`` (``int``) -- Targeting mode

  * ``0`` = Assisted Aim -- Full
  * ``1`` = Assisted Aim -- Partial
  * ``2`` = Free Aim -- Assisted
  * ``3`` = Free Aim

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   rage.player.set_player_targeting_mode(3)
   system.log_debug("Targeting mode: Free Aim")

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

This namespace contains object-related game functions.

================================


create_object(``modelHash``, ``x``, ``y``, ``z``, ``isNetwork``, ``bScriptHostObj``, ``dynamic``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates an object (prop) with the specified model at the specified position.

**Parameters:**

* ``modelHash`` (``Hash``) -- The model to spawn.

  * `Models here <https://gta-objects.xyz/objects>`__
* ``x`` (``float``) -- Spawn coordinate X component.
* ``y`` (``float``) -- Spawn coordinate Y component.
* ``z`` (``float``) -- Spawn coordinate Z component.
* ``isNetwork`` (``bool``) -- Whether to create a network object for the object.

  * ``true`` to create a network object for the object
  * ``false`` to create a local object for the object. In this case, the object exists only locally.
* ``bScriptHostObj`` (``bool``) -- Whether to register the object as pinned to the script host in the R* network model.
* ``dynamic`` (``bool``) -- False to create a door archetype (archetype flag bit 26 set) as a door. Required to be set to true to create door models in network mode.

**Returns:**

* ``Object`` -- An object ID.

**Example:**

.. code-block:: lua
   :linenos:
   
   object = rage.object.create_object(rage.gameplay.get_hash_key("apa_mp_apa_crashed_usaf_01a"), 0.0, 0.0, 0.0, true, false, false) -- Hash: 1925170211
   system.log_debug("Object ID: " .. tostring(object))


================================

.. _weaponNSR:

Weapon namespace
----------------------

This namespace contains weapon-related game functions.

================================

get_max_ammo(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get ped max ammo for a weapon.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 

.. _Whash: https://wiki.rage.mp/index.php?title=Weapons
**Returns:**

* ``bool``

  * ``true`` -- Max ammo has been given
  * ``false`` -- Max ammo hasn't been given

**Example:**

.. code-block:: lua
   :linenos:

   rage.weapon.get_max_ammo(lobby.get_player_ped(lobby.get_host()), rage.gameplay.get_hash_key("MicroSMG")) -- Gives session host a fully loaded MicroSMG

================================

get_ped_ammo_type_from_weapon(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get ammo type from a specific weapon of a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``Hash`` -- Returns ammo type hash

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.get_ped_ammo_type_from_weapon(ped, rage.gameplay.get_hash_key("MicroSMG")) -- Gets ammo type from session's host MicroSMG

================================

get_ped_weapon_tint_index(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get weapon tint ID from a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``int`` -- Returns weapon tint ID

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.get_ped_weapon_tint_index(ped, rage.gameplay.get_hash_key("MicroSMG"), ) -- Gets weapon tint ID from session's host MicroSMG

================================

get_ped_weapon_tint_count(``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get weapon tint count.

**Parameters:**

* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``int`` -- Returns weapon tint count

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.get_ped_weapon_tint_count(ped, rage.gameplay.get_hash_key("MicroSMG"), ) -- Gets weapon tint count from session's host MicroSMG

================================

give_delayed_weapon_to_ped(``ped``, ``weaponHash``, ``ammoCount``, ``bForceInHand``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gives a weapon to PED with a delay.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
* ``ammoCount`` (``int``) -- Ammo count

* ``bForceInHand`` (``bool``) -- Togglable force in hand

  * ``true`` -- Equip now
  * ``false`` -- Don't equp
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   
   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.give_delayed_weapon_to_ped(ped, weapon, 100, true)

================================

give_weapon_component_to_ped(``ped``, ``weaponHash``, ``componentHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Give a weapon component to a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
* ``componentHash`` (``Hash``) -- Weapon component `Chash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons
.. _Chash: https://wiki.rage.mp/index.php?title=Weapons_Components

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   
   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.give_delayed_weapon_to_ped(ped, weapon, "0x10E6BA2B") -- Gives extended clip component to session host's MicroSMG

================================

has_ped_got_weapon(``ped``, ``weaponHash``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if a ped has got a weapon.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_  
* ``p2`` (``bool``) -- Should always be ``false``, otherwise the function always returns ``false``
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``bool`` 

  * ``true`` -- Ped has got the weapon
  * ``false`` -- Ped doesn't have the weapon

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   
   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.has_ped_got_weapon(ped, weapon, true) -- Checks if session host has got MicroSMG

================================

has_ped_got_weapon_component(``ped``, ``weaponHash``, ``componentHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if a ped's weapon has got a component.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_  
* ``componentHash`` (``Hash``) -- Weapon component `Chash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons
.. _Chash: https://wiki.rage.mp/index.php?title=Weapons_Components

**Returns:**

* ``bool`` 

  * ``true`` -- Ped's weapon has got component
  * ``false`` -- Ped's weapon doesn't have the component

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   
   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.has_ped_got_weapon_component(ped, weapon, "0x10E6BA2B") -- Checks if session host's MicroSMG has got Extended Clip

================================

remove_all_ped_weapons(``ped``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove all ped's weapons.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``p1`` (``bool``) -- The value doesn't seem to matter.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.remove_all_ped_weapons(ped, true) -- Removes all session host's weapons

================================

remove_weapon_component_from_ped(``ped``, ``weaponHash``, ``componentHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove component from a ped's weapon.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_  
* ``componentHash`` (``Hash``) -- Weapon component `Chash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons
.. _Chash: https://wiki.rage.mp/index.php?title=Weapons_Components

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.remove_weapon_component_from_ped(ped, weapon, "0x10E6BA2B") -- Removes Extended Clip from session host's MicroSMG

================================

remove_weapon_from_ped(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a weapon from a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_  
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.remove_weapon_from_ped(ped, weapon, "0x10E6BA2B") -- Removes MicroSMG from session host

================================

set_ped_ammo(``ped``, ``weaponHash``, ``ammo``, ``p3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set ped ammo amount.

.. note::

   This function is still in development.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_  
* ``ammo`` (``int``) --
* ``p3`` (``bool``) --
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   weapon = rage.gameplay.get_hash_key("MicroSMG")

   rage.weapon.set_ped_ammo(ped, weapon, 100, true)

================================

set_ped_ammo_by_type(``ped``, ``ammoTypeHash``, ``ammo``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set ped ammo by type.

.. note::

   This function is still in development.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``ammoTypeHash`` (``Hash``) -- Weapon ammo `Ahash`_  
* ``ammo`` (``int``) -- Ammo Type
  
.. _Ahash: https://gist.github.com/root-cause/faf41f59f7a6d818b7db0b839bd147c1

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   self = lobby.get_player_ped(self.get_ped)

   ammoType = rage.weapon.get_ped_ammo_type_from_weapon(ped, rage.gameplay.get_hash_key("MicroSMG")) -- Get ammo type from session host's MicroSMG

   rage.weapon.set_ped_ammo_by_type(self, ammoType, 100) -- Set self ammo type

================================

set_ped_weapon_tint_index(``ped``, ``weaponHash``, ``tintIndex``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set ped weapon tint ID.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_  
* ``tintIndex`` (``int``) -- Weapon tint ID

  * ``tintIndex`` can be the following:

    * Default/Black = ``0``
    * Green = ``1``
    * Gold = ``2``
    * Pink = ``3``
    * Army = ``4``
    * LSPD = ``5``
    * Orange = ``6``
    * Platinum = ``7``
  * ``tineIndex`` for MK2 weapons:

    * Classic Black = ``0``
    * Classic Gray = ``1``  
    * Classic Two-Tone = ``2``
    * Classic White = ``3``
    * Classic Beige = ``4``
    * Classic Green = ``5``
    * Classic Blue = ``6``
    * Classic Earth = ``7``
    * Classic Brown & Black = ``8``
    * Red Contrast = ``9``
    * Blue Contrast = ``10``
    * Yellow Contrast = ``11``
    * Orange Contrast = ``12``
    * Bold Pink = ``13``
    * Bold Purple & Yellow = ``14``
    * Bold Orange = ``15``
    * Bold Green & Purple = ``16``
    * Bold Red Features = ``17``
    * Bold Green Features = ``18``
    * Bold Cyan Features = ``19``
    * Bold Yellow Features = ``20``
    * Bold Red & White = ``21``
    * Bold Blue & White = ``22``
    * Metallic Gold = ``23``
    * Metallic Platinum = ``24``
    * Metallic Gray & Lilac = ``25``
    * Metallic Purple & Lime = ``26``
    * Metallic Red = ``27``
    * Metallic Green = ``28``
    * Metallic Blue = ``29``
    * Metallic White & Aqua = ``30``
    * Metallic Orange & Yellow = ``31``
    * Mettalic Red and Yellow = ``32``


  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   self = lobby.get_player_ped(self.get_ped)

   tint = rage.weapon.get_ped_weapon_tint_index(ped, rage.gameplay.get_hash_key("MicroSMG")) -- Gets weapon tint ID from session's host MicroSMG

   rage.weapon.set_ped_weapon_tint_index(self, rage.gameplay.get_hash_key("MicroSMG"), tint) -- Sets self weapon tint

================================

.. _streaming:

Streaming namespace
----------------------

Functions here

================================

.. _ui:

UI namespace
----------------------

This namespace contains ui-related game functions.

================================

add_blip_for_coord(``x``, ``y``, ``z``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add blip for given coordinates.

**Parameters:**

* ``x`` (``float``) -- X position
* ``y`` (``float``) -- Y position
* ``z`` (``float``) -- Z position

**Returns:**

* ``Blip`` -- Returns a blip at the specified coordinates.

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.add_blip_for_coord(69.2, 54.8, 192.3)

================================

add_blip_for_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add blip for given entity.

**Parameters:**

* ``entity`` (``Entity``) -- Entity to add the blip to

**Returns:**

* ``Blip`` -- Returns a blip at the specified entity.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.ui.add_blip_for_entity(entity) -- Adds a blip to self's ped location.

================================

add_blip_for_pickup(``pickup``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add blip for given pickup.

**Parameters:**

* ``pickup`` (``Pickup``) -- Pickup to add the blip to

**Returns:**

* ``Blip`` -- Returns a blip at the specified pickup.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.ui.add_blip_for_pickup(entity)

================================

add_blip_for_radius(``posX``, ``posY``, ``posZ``, ``radius``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add blip for given coords with custom radius.

**Parameters:**

* ``posX`` (``float``) -- X position
* ``posY`` (``float``) -- Y position
* ``posZ`` (``float``) -- Z position
* ``radius`` (``float``) -- Radius

**Returns:**

* ``Blip`` -- Returns a blip at the specified pickup.

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.add_blip_for_radius(69.2, 54.8, 192.3, 20)

================================

get_blip_coords(``blip``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get coordinates for a blip.

**Parameters:**

* ``blip`` (``Blip``) -- Blip

**Returns:**

* ``Vector3`` -- Returns blip coords in Vector3 format

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped())

   rage.ui.get_blip_coords(blip) -- Returns coords of precedently created self ped's blip

================================

get_blip_from_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get blip from entity.

**Parameters:**

* ``entity`` (``Entity``) -- Entity to get the blip from

**Returns:**

* ``Blip`` -- Returns a blip

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.ui.get_blip_from_entity(entity)

================================

get_label_text(``labelName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get label text from label name.

**Parameters:**

* ``string`` (``labelName``) -- Label name to get text from

**Returns:**

* ``string`` -- Returns label text

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.get_label_text("Label")

================================

hide_hud_and_radar_this_frame()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hide HUD (Heads-up Display) and radar.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.hide_hud_and_radar_this_frame()

================================

hide_hud_component_this_frame(``id``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hide specified HUD (Heads-up Display) component.

**Parameters:**

* ``id`` (``int``) -- Hud component ID
  
  Hud component IDs:

  * ``1`` : WANTED_STARS
  * ``2`` : WEAPON_ICON
  * ``3`` : CASH
  * ``4`` : MP_CASH
  * ``5`` : MP_MESSAGE
  * ``6`` : VEHICLE_NAME
  * ``7`` : AREA_NAME
  * ``8`` : VEHICLE_CLASS
  * ``9`` : STREET_NAME
  * ``10`` : HELP_TEXT
  * ``11`` : FLOATING_HELP_TEXT_1
  * ``12`` : FLOATING_HELP_TEXT_2
  * ``13`` : CASH_CHANGE
  * ``14`` : RETICLE
  * ``15`` : SUBTITLE_TEXT
  * ``16`` : RADIO_STATIONS
  * ``17`` : SAVING_GAME
  * ``18`` : GAME_STREAM
  * ``19`` : WEAPON_WHEEL
  * ``20`` : WEAPON_WHEEL_STATS
  * ``21`` : HUD_COMPONENTS
  * ``22`` : HUD_WEAPONS

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.hide_hud_component_this_frame(19) -- Hides Weapon Wheel from the HUD.

================================

is_hud_component_active(``id``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if specified HUD (Heads-up Display) component is active.

**Parameters:**

* ``id`` (``int``) -- Hud component ID

**Returns:**

* ``bool`` -- Rerturns hud component status

  * ``true`` -- Hud component is active
  * ``false`` -- Otherwise

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.is_hud_component_active(19) -- Checks if Weapon Wheel is active

================================

is_mission_creator_blip(``blip``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if blip is mission creator.

**Parameters:**

* ``blip`` (``Blip``) -- Blip

**Returns:**

* ``bool`` -- Returns blip status

  * ``true`` -- Blip is mission creator
  * ``false`` -- Otherwise

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped())

   rage.ui.is_mission_creator_blip(blip)

================================

remove_blip(``blip``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a blip.

**Parameters:**

* ``blip`` (``Blip``) -- Blip

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped()) -- Adds a blip for self's ped

   rage.ui.remove_blip(blip) -- Removes precedently added blip
   
================================

set_blip_as_mission_creator_blip(``blip``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set blip as mission creator blip.

**Parameters:**

* ``blip`` (``Blip``) -- Blip
* ``toggle`` (``bool``) -- Toggles blip settings

  * ``true`` -- Set blip as mission creator blip
  * ``false`` -- Otherwise

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped()) -- Adds a blip for self's ped

   rage.ui.set_blip_as_mission_creator_blip(blip, true) -- Sets precedently added blip as mission creator blip
   
================================

set_blip_colour(``blip``, ``color``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set blip colour.

**Parameters:**

* ``blip`` (``Blip``) -- Blip
* ``color`` (``int``) -- Blip `Color ID`_  

.. _Color ID: https://wiki.rage.mp/index.php?title=Blips#Blip_colors

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped()) -- Adds a blip for self's ped

   rage.ui.set_blip_colour(blip, 38) -- Sets precedently added blip Blue
   
================================

set_blip_coords(``blip``, ``posX``, ``posY``, ``posZ``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set blip coordinates.

**Parameters:**

* ``blip`` (``Blip``) -- Blip
* ``posX`` (``float``) -- X position
* ``posY`` (``float``) -- Y position
* ``posZ`` (``float``) -- Z position

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped()) -- Adds a blip for self's ped

   rage.ui.set_blip_coords(blip, 69.2, 54.8, 192.3)

================================

set_blip_route(``blip``, ``enabled``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set blip route, toggable.

**Parameters:**

* ``blip`` (``Blip``) -- Blip
* ``enabled`` (``bool``) -- Toggle blip route
  
  * ``true`` -- Blip route enabled
  * ``false`` -- Blip route disabled

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped()) -- Adds a blip for self's ped

   rage.ui.set_blip_route(blip, true)

================================

set_blip_sprite(``blip``, ``spriteId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set blip sprite.

**Parameters:**

* ``blip`` (``Blip``) -- Blip
* ``spriteId`` (``int``) -- Blip `Sprite ID`_  

.. _Sprite ID: https://wiki.rage.mp/index.php?title=Blips

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped()) -- Adds a blip for self's ped

   rage.ui.set_blip_sprite(blip, 64) -- Sets radar_helicopter sprite to precedently created blip

================================

set_new_waypoint(``x``, ``y``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set new waypoint to given coordinates.

**Parameters:**

* ``x`` (``float``) -- X position
* ``y`` (``float``) -- Y position

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_new_waypoint(69.2, 420.1)

================================

set_text_centre(``align``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set text centre.

**Parameters:**

* ``align`` (``bool``) -- Toggle text alignment

  * ``true`` -- Text is aligned
  * ``false`` -- Otherwise

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_centre(true)

================================

set_text_font(``fontType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set text font.

**Parameters:**

* ``fontType`` (``int``) -- Font type ID
  
  * Font type IDs:

  * FontChaletLondon = ``0``
  * FontHouseScript = ``1``
  * FontMonospace = ``2``
  * FontWingDings = ``3``
  * FontChaletComprimeCologne = ``4``
  * FontPricedown = ``7``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_font(0) -- Font type 0, default (Chalet London)

================================

set_text_justification(``justifyType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set text justification.

**Parameters:**

* ``justifyType`` (``int``) -- Text justification ID
  
  * Justification types ID:

  * ``0`` = Center-Justify
  * ``1`` = Left-Justify
  * ``2`` = Right-Justify

.. note::

    Right-Justify requires ``set_text_wrap()``, otherwise it will draw to the far right of the screen.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_justification(1) -- Font justification left

================================

set_text_outline()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set text outline.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_outline()

================================

set_text_right_justify(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle set text right justify.

**Parameters:**

* ``toggle`` (``bool``) -- Toggle text right justify
  
  * ``true`` -- Toggle on
  * ``false`` -- Toggle off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_right_justify(true) -- Toggle on text right justify

================================

set_text_scale(``scale``, ``size``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set text scale.

**Parameters:**

* ``scale`` (``float``) -- Text scale
* ``size`` (``float``) -- Text size

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_scale(12, 10)

================================

set_text_wrap(``start``, ``end``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the text in a specified box and wrap the text if it exceeds the boundries. Both values are for X axis. Useful when positioning text set to center or aligned to the right.

**Parameters:**

* ``start`` (``float``) -- Left boundry on screen position (0.0 - 1.0)  
* ``end`` (``float``) -- Right boundry on screen position (0.0 - 1.0)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_text_wrap(0, 0)

================================

set_waypoint_off()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove the current waypoint from the map.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.set_waypoint_off(0, 0)

================================

show_hud_component_this_frame(``id``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Show specified HUD (Heads-up Display) component.

**Parameters:**

* ``id`` (``int``) -- Hud component ID
  
  Hud component IDs:

  * ``1`` : WANTED_STARS
  * ``2`` : WEAPON_ICON
  * ``3`` : CASH
  * ``4`` : MP_CASH
  * ``5`` : MP_MESSAGE
  * ``6`` : VEHICLE_NAME
  * ``7`` : AREA_NAME
  * ``8`` : VEHICLE_CLASS
  * ``9`` : STREET_NAME
  * ``10`` : HELP_TEXT
  * ``11`` : FLOATING_HELP_TEXT_1
  * ``12`` : FLOATING_HELP_TEXT_2
  * ``13`` : CASH_CHANGE
  * ``14`` : RETICLE
  * ``15`` : SUBTITLE_TEXT
  * ``16`` : RADIO_STATIONS
  * ``17`` : SAVING_GAME
  * ``18`` : GAME_STREAM
  * ``19`` : WEAPON_WHEEL
  * ``20`` : WEAPON_WHEEL_STATS
  * ``21`` : HUD_COMPONENTS
  * ``22`` : HUD_WEAPONS

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.show_hud_component_this_frame(19) -- Shows Weapon Wheel from the HUD.

================================

.. _draw:

Draw namespace
----------------------

This namespace contains drawing-related game functions.

================================

draw_sprite(``textureDict``, ``textureName``, ``screenX``, ``screenY``, ``width``, ``height``, ``heading``, ``red``, ``green``, ``blue``, ``alpha``, ``p11``, ``p12``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draw a 2D sprite on the screen.  

**Parameters:**

* ``textureDict`` (``string``) -- Name of texture dictionary to load texture from (e.g. "CommonMenu", "MPWeaponsCommon", etc.)  
* ``textureName`` (``string``) -- Name of texture to load from texture dictionary (e.g. "last_team_standing_icon", "tennis_icon", etc.)  
* ``screenX`` (``float``) -- Screen offset (0.5 = center)  
* ``screenY`` (``float``) -- Screen offset (0.5 = center)  
* ``width`` (``float``) -- Texture scaling. Negative values can be used to flip the texture on that axis. (0.5 = half)  
* ``height`` (``float``) -- Texture scaling. Negative values can be used to flip the texture on that axis. (0.5 = half)  
* ``heading`` (``float``) -- Texture rotation in degrees (default = 0.0) positive is clockwise, measured in degrees  
* ``red`` (``int``) -- Sprite R color (default = 255)  
* ``green`` (``int``) -- Sprite G color (default = 255)  
* ``blue`` (``int``) -- Sprite B color (default = 255)  
* ``alpha`` (``int``) -- Opacity level  
* ``p11`` (``bool``) -- Unknown
* ``p12`` (``Any``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.draw_sprite("CommonMenu", "shop_new_star", 0.5, 0.5, 0.5, 0.5, 0.0, 255, 255, 255, 255, false, false)

================================

.. _camNS:

Cam namespace
----------------------

This namespace contains draw-related game functions.

================================

get_gameplay_cam_relative_pitch()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get gameplay camera relative pitch.

**Parameters:**

* None

**Returns:**

* ``float`` -- Returns cam relative pitch value

**Example:**

.. code-block:: lua
   :linenos:

   pitch = rage.cam.get_gameplay_cam_relative_pitch()
   
   system.log_debug("LocalPlayer pitch: " .. pitch)

================================

get_gameplay_cam_rot(``rotationOrder``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function requires proper documentation & testing.

Get gameplay camera rotation

**Parameters:**

* ``rotationOrder`` (``int``) -- Rotation order.

0-Pitch(X): -70.000092  
0-Roll(Y): -0.000001  
0-Yaw(Z): -43.886459  
1-Pitch(X): -70.000092  
1-Roll(Y): -0.000001  
1-Yaw(Z): -43.886463  
2-Pitch(X): -70.000092  
2-Roll(Y): -0.000002  
2-Yaw(Z): -43.886467  


**Returns:**

* ``Vector3`` -- Returns coordinates in Vector3 form

**Example:**

.. code-block:: lua
   :linenos:


================================

.. _gameplay:

Gameplay namespace
----------------------

This namespace contains gameplay-related game functions.

================================

clear_area_of_cops(``x``, ``y``, ``z``, ``radius``, ``flags``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clear defined area of cops.

**Parameters:**

* ``x`` (``float``) -- X coordinate of the area center
* ``y`` (``float``) -- Y coordinate of the area center
* ``z`` (``float``) -- Z coordinate of the area center
* ``radius`` (``float``) -- Radius of the area
* ``flags`` (``int``) -- Flags

  * ``flags`` appears to always be ``0``.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords()

   rage.gameplay.clear_area_of_cops(coords.x, coords.y, coords.z, 100.0, 0) -- 100m cop purge

================================

clear_area_of_objects(``x``, ``y``, ``z``, ``radius``, ``flags``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clear defined area of props.

**Parameters:**

* ``x`` (``float``) -- X coordinate of the area center
* ``y`` (``float``) -- Y coordinate of the area center
* ``z`` (``float``) -- Z coordinate of the area center
* ``radius`` (``float``) -- Radius of the area
* ``flags`` (``int``) -- Flags

  * There seem to be some most used flags, though it's unknown what do they change.

    * ``0``
    * ``2``
    * ``6``
    * ``16``
    * ``17``
   
**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords()
   
   rage.gameplay.clear_area_of_objects(coords.x, coords.y, coords.z, 100.0, 0) -- 100m prop purge

================================

clear_area_of_peds(``x``, ``y``, ``z``, ``radius``, ``flags``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clear defined area of peds.

**Parameters:**

* ``x`` (``float``) -- X coordinate of the area center
* ``y`` (``float``) -- Y coordinate of the area center
* ``z`` (``float``) -- Z coordinate of the area center
* ``radius`` (``float``) -- Radius of the area
* ``flags`` (``int``) -- Flags

  * ``flags`` appears to always be ``1``.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords()
   
   rage.gameplay.clear_area_of_peds(coords.x, coords.y, coords.z, 100.0, 1) -- 100m ped purge

================================

clear_area_of_vehicles(``x``, ``y``, ``z``, ``radius``, ``p4``, ``p5``, ``p6``, ``p7``, ``p8``, ``p9``, ``p10``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clear defined area of vehicles.

**Parameters:**

* ``x`` (``float``) -- X coordinate of the area center
* ``y`` (``float``) -- Y coordinate of the area center
* ``z`` (``float``) -- Z coordinate of the area center
* ``radius`` (``float``) -- Radius of the area
* ``p4`` (``bool``) -- Unknown (Optional)
* ``p5`` (``bool``) -- Unknown (Optional)
* ``p6`` (``bool``) -- Unknown (Optional)
* ``p7`` (``bool``) -- Unknown (Optional)
* ``p8`` (``bool``) -- Unknown (Optional)
* ``p9`` (``bool``) -- Unknown (Optional)
* ``p10`` (``Any``) -- Unknown (Optional)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords()
   
   rage.gameplay.clear_area_of_vehicles(coords.x, coords.y, coords.z, 100.0) -- 100m vehicle purge


================================

clear_override_weather()
^^^^^^^^^^^^^^^^^^^^^^^^^

Clears the weather override.

.. note::

   This method only works if the weather using ``set_override_weather()``.

.. note::

   If the weather was previously set by scripting.world.set_weather(), the weather will be reset to that weather.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.gameplay.set_override_weather("RAIN") -- set rain weather
   rage.gameplay.clear_override_weather() -- clear the weather

================================

display_onscreen_keyboard(``p0``, ``windowTitle``, ``p2``, ``defaultText``, ``defaultConcat1``, ``defaultConcat2``, ``defaultConcat3``, ``maxInputLength``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Displays an onscreen input window.

**Parameters:**

* ``p0`` (``int``) -- Unknown

  * ``p0`` has to be ``6``, otherwise the method might not work as intended.
* ``windowTitle`` (``string``) -- Title of the window

  * All available window titles are listed here: ``windowtitles``
* ``p2`` (``string``) -- Unknown
* ``defaultText`` (``string``) -- Default text in the input box
* ``defaultConcat1`` (``string``) -- Unknown
* ``defaultConcat2`` (``string``) -- Unknown
* ``defaultConcat3`` (``string``) -- Unknown
* ``maxInputLength`` (``int``) -- Maximum length of the input box

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   function foo()
      data = nil
      rage.gameplay.display_onscreen_keyboard(6, "FMMC_KEY_TIP10", "", "Example Text", "", "", "", 30) -- display onscreen keyboard with the "Enter Synopsis" title and a maximum input length of 30 characters
      while data == "" or data == nil do
         data = rage.gameplay.get_onscreen_keyboard_result()
         system.wait(-1)
      end
      system.log_debug("The player entered " .. data .. ".")
   end

   parent = menu.add_parent("My Lua Script")
   menu.add_option("Get Data", "gd", parent, foo)
   menu.update_root_parent(true)

================================

find_spawn_point_in_direction(``posX``, ``posY``, ``posZ``, ``fwdVecX``, ``fwdVecY``, ``fwdVecZ``, ``distance``, ``spawnPoint``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Attempts to find a spawn point in the specified direction.

**Parameters:**

* ``posX`` (``float``) -- X coordinate of the spawn point
* ``posY`` (``float``) -- Y coordinate of the spawn point
* ``posZ`` (``float``) -- Z coordinate of the spawn point
* ``fwdVecX`` (``float``) -- X coordinate of the direction vector
* ``fwdVecY`` (``float``) -- Y coordinate of the direction vector
* ``fwdVecZ`` (``float``) -- Z coordinate of the direction vector
* ``distance`` (``float``) -- Limit the search to this distance
* ``spawnPoint`` (``vector3``) -- The found spawn point

**Returns:**

* ``bool``

  * ``true`` -- A spawn point was found
  * ``false`` -- No spawn point was found

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords()
   fwdVec = rage.entity.get_entity_rotation(self.get_ped(), 1)
   spawnP = coords
   rage.gameplay.find_spawn_point_in_direction(coords.x, coords.y, coords.z, fwdVec.x, fwdVec.y, fwdVec.z, 100.0, spawnP) -- find spawn point in 100m radius in the direction of the player

   if spawnP then
      system.log_debug(tostring(spawnP.x) .. " " .. tostring(spawnP.y) .. " " .. tostring(spawnP.z)) -- set the player's coords to the found spawn point
   end

================================

get_cloud_hat_opacity()
^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current clouds opacity.

**Parameters:**

* None

**Returns:**

* ``float`` -- The current clouds opacity

**Example:**

.. code-block:: lua
   :linenos:

   opacity = rage.gameplay.get_cloud_hat_opacity() -- get current clouds opacity
   system.log_debug("The clouds opacity is " .. tostring(opacity)) -- log the current clouds opacity

================================

get_frame_count()
^^^^^^^^^^^^^^^^^

Returns the current frame count.

**Parameters:**

* None

**Returns:**

* ``int`` -- The current frame count

**Example:**

.. code-block:: lua
   :linenos:

   frameCount = rage.gameplay.get_frame_count() -- get current frame count
   system.log_debug("The frame count is " .. tostring(frameCount)) -- log the current frame count

================================

get_frame_time()
^^^^^^^^^^^^^^^^

Returns the current frame time - the time it takes for a frame to be rendered.

**Parameters:**

* None

**Returns:**

* ``float`` -- The current frame time

**Example:**

.. code-block:: lua
   :linenos:

   frameTime = rage.gameplay.get_frame_time() -- get current frame time
   system.log_debug("The frame time is " .. tostring(frameTime)) -- log the current frame time

================================

get_hash_key(``string``)
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the hash key of the specified game object.

**Parameters:**

* ``string`` (``string``) -- The game object to get the hash key of

**Returns:**

* ``int`` -- The hash key of the specified string

**Example:**

.. code-block:: lua
   :linenos:

   hashKey = rage.gameplay.get_hash_key("ZENTORNO") -- get the hash key of "example"
   system.log_debug("The hash key of \"ZENTORNO\" is " .. tostring(hashKey)) -- log the hash key of "example"

================================

get_onscreen_keyboard_result()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the result of an onscreen input window.

**Parameters:**

* None

**Returns:**

* ``string`` -- The result of the onscreen input window

**Example:**

.. code-block:: lua
   :linenos:

   function foo()
      data = nil
      rage.gameplay.display_onscreen_keyboard(6, "FMMC_KEY_TIP10", "", "Example Text", "", "", "", 30) -- display onscreen keyboard with the "Enter Synopsis" title and a maximum input length of 30 characters
      while data == "" or data == nil do
         data = rage.gameplay.get_onscreen_keyboard_result()
         system.wait(-1)
      end
      system.log_debug("The player entered " .. data .. ".")
   end

   parent = menu.add_parent("My Lua Script")
   menu.add_option("Get Data", "gd", parent, foo)
   menu.update_root_parent(true)

================================

preload_cloud_hat(``name``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preloads the specified cloud hat.

**Parameters:**

* ``name`` (``string``) -- The cloud type

  * You can read more about cloud types here: :doc:`cloudtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.gameplay.preload_cloud_hat("altostratus") -- preload the altostratus cloud hat

================================

load_cloud_hat(``name``, ``transitionTime``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loads the specified cloud hat.

.. note::

   It appears that the cloud hat can be loaded without calling preload_cloud_hat(). 

**Parameters:**

* ``name`` (``string``) -- The cloud type

   * You can read more about cloud types here: :doc:`cloudtypes`

* ``transitionTime`` (``float``) -- The time to smoothly transit between the current cloud hat and the new cloud hat

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.gameplay.load_cloud_hat("altostratus", 1.0) -- load the altostratus cloud hat with a 1 second transition time

================================

unload_cloud_hat(``name``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unloads the specified cloud hat.

.. note::

   After unloading, it falls back to the previous cloud hat

**Parameters:**

* ``name`` (``string``) -- The cloud type

   * You can read more about cloud types here: :doc:`cloudtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.gameplay.unload_cloud_hat("altostratus") -- unload the altostratus cloud hat
   

================================

set_cloud_hat_opacity(``opacity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the opacity of the current cloud hat.

**Parameters:**

* ``opacity`` (``float``) -- The new opacity of the current cloud hat

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.gameplay.set_cloud_hat_opacity(5) -- set the current cloud hat opacity to 5

================================

set_override_weather(``weatherType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the weather to the specified weather type.

**Parameters:**

* ``weatherType`` (``string``) -- The weather type

  * You can read more about weather types here: :doc:`weathertypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.gameplay.set_override_weather("XMAS") -- set the weather to XMAS

================================

shoot_single_bullet_between_coords(``x1``, ``y1``, ``z1``, ``x2``, ``y2``, ``z2``, ``damage``, ``p7``, ``weaponHash``, ``ownerPed``, ``isAudible``, ``isInvisible``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shoots a bullet from the first coordinates to the second coordinates

**Parameters:**

* ``x1`` (``float``) -- The X coordinate to start the shot at
* ``y1`` (``float``) -- The Y coordinate to start the shot at
* ``z1`` (``float``) -- The Z coordinate to start the shot at
* ``x2`` (``float``) -- The X coordinate the shot should end up at
* ``y2`` (``float``) -- The Y coordinate the shot should end up at
* ``z2`` (``float``) -- The Z coordinate the shot should end up at
* ``damage`` (``int``) -- The amount of damage the bullet carries
* ``p7`` (``bool``) -- Whether the bullet should have pinpoint accuracy
* ``weaponHash`` (``Hash``) -- Hash of the weapon the bullet is used as ammunition for
* ``ownerPed`` (``Ped``) -- Owner of the bullet, e.g. if the bullet kills someone the kill feed shows 'X was shot by ownerPed.'
* ``isAudible`` (``bool``) -- Whether the bullet should be audible.
* ``isInvisible`` (``bool``) -- Whether the bullet should be invisible.
* ``speed`` (``float``) -- Speed the bullet should fly at.

**Returns:**

* None

**Example:**

.. note::
   
   This example is untested.

.. code-block:: lua
   :linenos:

   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(10)
   rage.gameplay.shoot_single_bullet_between_coords(coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords3.z, 1000, true, rage.gameplay.get_hash_key("WEAPON_SAWNOFFSHOTGUN"), self.get_ped(), true, true, 50.0) -- shoot a bullet from player coords to 10 meters in front of them with a damage of 1000, with pinpoint accuracy, using the shotgun, the bullet owner is the player, the bullet is audible and invisible, and the bullet speed is 50.0


update_onscreen_keyboard()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   
   This method is not documented yet.

================================

.. _fire:

Fire namespace
----------------------

This namespace contains fire-related game functions.

================================

add_explosion(``x``, ``y``, ``z``, ``explosionType``, ``damageScale``, ``isAudible``, ``isInvisible``, ``cameraShake``, ``noDamage``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add explosion in certain coordinates with multiple options.

**Parameters:**

* ``x`` (``float``) -- X position
* ``y`` (``float``) -- Y position
* ``z`` (``float``) -- Z position
* ``explosionType`` (``int``) -- Explosion types

  * Read more about explosion types    here: :doc:`exptypes`
* ``damageScale`` (``float``) -- Damage scale
* ``isAudible`` (``bool``) -- Toggle explosion sound

  * ``true`` -- Explosion is audible
  * ``false`` -- Explosion is silent  
* ``isInvisible`` (``bool``) -- Toggle explosion visibility

  * ``true`` -- Explosion is invisible
  * ``false`` -- Explosion is visible

* ``cameraShake`` (``float``) -- Camera shake intensity
* ``noDamage`` (``bool``) -- Toggle no damage

  * ``true`` -- Explosion doesn't cause damage
  * ``false`` -- Explosion causes damage

  
**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   c = self.get_coords()
   rage.fire.add_explosion(922.60430908203, 49.672721862793, 80.89803314209, 7, 10, true, false, 10, false)
   -- Adds a Car Explosion located at Casino Entrance, with 10 damage scale, audible, invisible, 10 camera shake intensity and damage toggled on

================================

start_entity_fire(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start fire on entity.

**Parameters:**

* ``entity`` (``Entity``) -- Entity ID

**Returns:**

``int`` -- Returns a value which represents how many times the fire was applied

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.fire.start_entity_fire(entity)

================================

stop_entity_fire(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stop fire on entity.

**Parameters:**

* ``entity`` (``Entity``) -- Entity ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.fire.stop_entity_fire(entity)

================================

.. _networkNSR:

Network namespace
----------------------

This namespace contains network-related game functions.

================================

network_get_friend_count()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get friend count.

**Parameters:**

* None

**Returns:**

* ``int`` -- Returns friend count

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_get_friend_count()

================================

network_get_host_of_this_script()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get ID of the player host of this script.

**Parameters:**

* None

**Returns:**

* ``Player`` -- Returns Player ID

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_get_host_of_this_script()

================================

network_get_max_friends()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get max friends.

**Parameters:**

* None

**Returns:**

* ``int`` -- Returns max friends

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_get_max_friends()

================================

network_has_control_of_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check network control of entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity to check

**Returns:**

* ``bool``     

  * ``true`` -- Network has control of the entity
  * ``false`` -- Network doesn't have control of the entity

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.network.network_has_control_of_entity(entity)

================================

network_is_friend_in_multiplayer(``friendName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if friend is in multiplayer.

**Parameters:**

* ``friendName`` (``string``) -- The friend name to check

**Returns:**

* ``bool``

  * ``true`` -- Friend is in multiplayer
  * ``false`` -- Friend isn't in multiplayer

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_is_friend_in_multiplayer("Bobby")

================================

network_is_friend_index_online(``friendIndex``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is poorly documented. It requires testing.

Check if friend is online by friend index.

**Parameters:**

* ``friendIndex`` (``int``) -- The friend index to check

**Returns:**

* ``bool``

  * ``true`` -- Friend is online
  * ``false`` -- Friend isn't online


================================

network_is_friend_online(``name``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if friend is online.

**Parameters:**

* ``name`` (``string``) -- The friend name to check

**Returns:**

* ``bool``

  * ``true`` -- Friend is online
  * ``false`` -- Friend isn't online

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_is_friend_online("Huginn5") -- stalking Huginn

================================

network_is_session_started()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if session has started.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` --  Session has started
  * ``false`` -- Otherwise

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_is_session_started()

================================

network_hash_from_player_handle(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get hash from player handle.

**Parameters:**

* ``player`` (``Player``) -- The Player ID

**Returns:**

* ``Hash`` -- Returns hash from player handle.

**Example:**

.. code-block:: lua
   :linenos:

   player = lobby.get_host()
   
   rage.network.network_hash_from_player_handle(player)

================================

network_is_host()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check host status.

**Parameters:**

* None

**Returns:**

* ``bool`` 

  * ``true`` --  Player is a host
  * ``false`` -- Player isn't a host

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_is_host()

================================

network_session_kick_player(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kick player out of the session.

**Parameters:**

* ``player`` (``Player``) -- The Player ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   player = lobby.get_host()

   rage.network.network_session_kick_player(player)

================================

network_request_control_of_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request control of entity.

**Parameters:**

* ``Entity`` (``Entity``) -- The Entity ID

**Returns:**

* ``bool``

  * ``true`` --  Request successful
  * ``false`` -- Request failed

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.network.network_request_control_of_entity(entity)

================================

.. _cutscene:

Cutscene namespace
----------------------

This namespace contains cutscene-related game functions.

================================

is_cutscene_active()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if a cutscene is active.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- Cutscene is active
  * ``false`` -- Cutscene is inactive

**Example:**

.. code-block:: lua
   :linenos:

   rage.cutscene.is_cutscene_active()

================================

is_cutscene_playing()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks if a cutscene is playing.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` -- Cutscene is playing
  * ``false`` -- Cutscene is not playing

**Example:**

.. code-block:: lua
   :linenos:

   rage.cutscene.is_cutscene_playing()

================================

remove_cutscene()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes cutscene.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.cutscene.remove_cutscene()

================================

stop_cutscene_immediately()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Immediately stop cutscene.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.cutscene.stop_cutscene_immediately()

================================

.. _controls:

Controls namespace
----------------------

This namespace contains controls-related game functions.

================================

disable_control_action(``padIndex``, ``control``, ``disable``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disable control action.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- `Control types`_  
* ``disable`` (``bool``) -- Toggle disable

  * ``true`` -- Disable control action
  * ``false`` -- Do not disable control action

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Control types: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.disable_control_action(21, 0, true)

================================

get_control_normal(``padIndex``, ``control``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is poorly documented. It needs more testing and information.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``float`` -- current control value

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.get_control_normal(71, 0) -- returns INPUT_VEH_ACCELERATE value (normalized)

================================

is_control_just_pressed(``padIndex``, ``control``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is poorly documented. It needs more testing and information.


**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``bool``

  * ``true`` -- Control was just pressed
  * ``false`` -- Control wasn't just pressed

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.is_control_just_pressed(21, 0)

================================

is_control_pressed(``padIndex``, ``control``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


   .. note::

   This function is poorly documented. It needs more testing and information.

.. note::

   ``inputGroup`` is always 2 for xbox 360 controller.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``bool``

  * ``true`` -- Control button is pressed
  * ``false`` -- Control button is not pressed

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.is_control_pressed(21, 0)

================================

is_disabled_control_just_pressed(``padIndex``, ``control``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if a disabled control is just pressed.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``bool``

  * ``true`` -- Control is pressed
  * ``false`` -- Control is not pressed

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.is_disabled_control_just_pressed(21, 0)

================================

is_disabled_control_pressed(``padIndex``, ``control``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if a disabled control is pressed.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``bool`` -- Returns control status

  * ``true`` -- Control is pressed
  * ``false`` -- Control is not pressed

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.is_disabled_control_pressed(21, 0)

================================

set_control_normal(``padIndex``, ``control``, ``amount``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This function simulates player input.

.. note::

   This function is poorly documented. It needs more testing and information.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  
* ``amount`` (``float``)

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``bool``

  * ``true`` -- input success
  * ``false`` -- input failed

**Example:**

.. code-block:: lua
   :linenos:

   rage.controls.set_control_normal(71, 0, 1) -- sets 1.0 to INPUT_VEH_ACCELERATE

================================

.. _graphics:

Graphics namespace
----------------------

Functions here

================================

.. _time:

Time namespace
----------------------

This namespace contains time-related game functions.

================================

get_clock_hours()
^^^^^^^^^^^^^^^^^^^^^^

Gets the current in-game hour

**Parameters:**

* None

**Returns:**

* ``int`` -- The current hour

**Example:**

.. code-block:: lua
   :linenos:

   hour = rage.time.get_clock_hours()
   system.log_debug("Current hour: " .. hour)

================================

get_current_minutes()
^^^^^^^^^^^^^^^^^^^^^^

Gets the current in-game minute

**Parameters:**

* None

**Returns:**

* ``int`` -- The current minute

**Example:**

.. code-block:: lua
   :linenos:

   minute = rage.time.get_current_minutes()
   system.log_debug("Current minute: " .. minute)

================================

get_current_seconds()
^^^^^^^^^^^^^^^^^^^^^^

Gets the current in-game second

**Parameters:**

* None

**Returns:**

* ``int`` -- The current second

**Example:**

.. code-block:: lua
   :linenos:

   second = rage.time.get_current_seconds()
   system.log_debug("Current second: " .. second)

================================

set_clock_time(``hour``, ``minute``, ``second``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the in-game time

**Parameters:**

* ``hour`` (``int``) -- The hour
* ``minute`` (``int``) -- The minute
* ``second`` (``int``) -- The second

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.time.set_clock_time(12, 30, 45) -- Sets in-game time to 12:30:45

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

This namespace contains audio-related game functions. 

=================================

================================

.. _rope:

Rope namespace
----------------------

Functions here

================================
