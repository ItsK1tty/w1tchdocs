DIS2RBED LUA reference
========================

There are multiple namespaces & types in the current DIS2RBED LUA framework, each with their own set of functions.

.. _lua_types:

Types in the LUA Engine
##########################

Types in the LUA Engine are defined in the following order:

* :ref:`hash` (uint64)
* :ref:`Entity` (int)
* :ref:`Ped` (int)
* :ref:`Player` (int)
* :ref:`Cam` (int)
* :ref:`Blip` (int)
* :ref:`Any`
* :ref:`Vehicle` (int)
* :ref:`Vector2` (float ``x``, float ``y``)
* :ref:`Vector3` (float ``x``, float ``y``, float ``z``)
* :ref:`ColorRGB` (int ``r``, int ``g``, int ``b``)
* :ref:`ColorRGBA` (int ``r``, int ``g``, int ``b``, int ``a``)
* :ref:`eSessionType` (int)
* :ref:`Pickup`

================================

.. _Hash:

Hash
----------------------

Hash is a hash of a string that is encrypted using the Jenkins hash function. 
It's an in-game identifier that is unique to each object and helps identify a gun or a vehicle.

You can find a hash key using this function: rage.gameplay.get_hash_key("string"), where string is a game object name.

You can find most of the game objects here:

Menu button, children and task hashes can be anything you want, but they have to be unique.

* `Weapons <https://wiki.rage.mp/index.php?title=Weapons>`__
* `Weapon Components <https://wiki.rage.mp/index.php?title=Weapons_Components>`__
* `Vehicles <https://wiki.rage.mp/index.php?title=Vehicles>`__
* `Peds <https://wiki.rage.mp/index.php?title=Peds>`__
* `Blips <https://wiki.rage.mp/index.php?title=Blips>`__
* `Props <https://cdn.rage.mp/public/odb/index.html>`__


================================

.. _Entity:

Entity
----------------------

Entity is an integer ID of an in-game object (don't mix up with the ``Hash``!). It's an integer that is unique to each object, and, unlike the ``Hash``, it only lasts one session.
Entity can be used to identify a ped, a vehicle, an animal, a character. Entity is everything.

================================

.. _Ped:

Ped
----------------------

Ped is an integer ID which represents the NPC in the game session. It's unique to each NPC, and it only lasts one session.
Ped can be converted to Entity, hence it can be used with methods that take Entity as a parameter.

Easiest way to acquire a ped handle is to call ``self.get_ped()`` function that returns a Ped object of your character. Or spawn it through ``rage.ped.create_ped()``.

* `Peds <https://wiki.rage.mp/index.php?title=Peds>`__

================================

.. _Player:

Player
----------------------

Player is an integer ID that represents Player in the game session. It ranges from 0 to 32.
Player ID helps identify a player in the game session. Always 0 in single player mode.

================================

.. _Cam:

Cam
----------------------

Cam ID represents the game camera. It's not used anywhere at the moment.

================================

.. _Blip:

Blip
----------------------

Blip is an Integer ID that represents the mark object on the game map. You can spawn and manage different types of blips.

You can find Blip types here:

* `Blips <https://wiki.rage.mp/index.php?title=Blips>`__

================================

.. _Any:

Any
----------------------

Any is a type that's used in native methods, whose parameters weren't completely figured out.
You can use ``false`` to represent it.

================================

.. _Vehicle:

Vehicle
----------------------

Vehicle is an Integer Vehicle ID which represents the Vehicle in the game session. It's unique to each vehicle, and it only lasts one session.
Vehicle can be converted to Entity, hence it can be used with methods that take Entity as a parameter.

Easiest way to acquire a vehicle handle is to call ``self.get_vehicle()`` function that returns a Vehicle object of your vehicle. Or spawn it through ``scripting.spawn.spawn_vehicle()``.

* `Vehicles <https://wiki.rage.mp/index.php?title=Vehicles>`__

================================

.. _Vector2:

Vector2
----------------------

Vector2 is a 2D vector, and is used to represent the coordinates on the screen. It contains two float variables: ``x`` and ``y``
Only used in :ref:`render` at the moment.

You can initialize a Vector3 object with following code:

``v2 = Vector2.new(x, y)``

================================

.. _Vector3:

Vector3
----------------------

Vector3 is a 3D vector, and is used to represent the coordinates in the game world. It contains three float variables: ``x``, ``y`` and ``z``

You can initialize vector3 with the following code:

``myV3 = Vector3.new(x, y, z)``

================================

.. _ColorRGB:

ColorRGB
----------------------

ColorRGB represents a color in RGB format. It contains three integer variables: ``r``, ``g`` and ``b``.

You can initialize a ColorRGB object with the following code:

``myColor = ColorRGB.new(r, g, b)``

================================

.. _ColorRGBA:

ColorRGBA
----------------------

ColorRGBA represents a color in RGBA format. It contains four integer variables: ``r``, ``g``, ``b`` and ``a``.

You can initialize a ColorRGBA object with the following code:

``myColor = ColorRGBA.new(r, g, b, a)``

================================

.. _eSessionType:

eSessionType
----------------------

eSessionType represents a session type that DIS2RBED uses to set up an online session.

Current available session types are:

* ``PublicJoin`` = ``0``
* ``PublicStart`` = ``1``
* ``CrewClosed`` = ``2``
* ``Crew`` = ``3``
* ``FriendsClosed`` = ``6``
* ``FriendsFind`` = ``9``
* ``Solo`` = ``10``
* ``Invite`` = ``11``
* ``CrewJoin`` = ``12``

===========================

.. _Pickup:

Pickup
----------------------

Used for money drops. It's not used anywhere at the moment.

===========================

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
* :ref:`web`
* :ref:`menu`
* :ref:`stats`   
* :ref:`notify`
* :ref:`script`
* :ref:`globals`
* :ref:`locals`
* :ref:`render`
* :ref:`self`
* :ref:`lobby`
* :ref:`vehicleNS`
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

add_script_event(``name``, ``eventId``, ``args`` = ``{}``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a script event into the protection blacklist.

**Parameters:**

* ``name`` (``string``) -- The name of the task.
* ``eventId`` (``int``) -- The event ID to add.
* ``args`` (``vector<int>``) -- The arguments to pass to the event. Default is an empty vector.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   system.add_script_event("CEO Kick", 1240068495)

================================

remove_script_event(``eventId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a script event from the protection blacklist.

**Parameters:**

* ``eventId`` (``int``) -- The event ID to remove.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   system.remove_script_event("CEO Kick")

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

   key = system.string_to_key("HOME")

   system.log_info(tostring(key)) -- get "HOME" key hash

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

   key = system.key_to_string(36)
   system.log_info(tostring(key)) -- get "HOME" key hash

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

.. _web:

Web namespace
----------------------

This namespace contains functions for sending web requests to external servers.

================================

get(``url``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a GET request to a web server.

**Parameters:**

* ``url`` (``string``) -- The URL to send the request to.

**Returns:**

* ``string`` -- The response from the server.

**Example:**

.. code-block:: lua
   :linenos:

   system.log_warning("Test HTTP request GET")
   result_get = web.get("http://ip-api.com/php/24.48.0.1")
   system.log_warning(result_get)

   --or

   system.log_warning("Test HTTPS request GET")
   result_get = web.get("https://ipapi.co/8.8.8.8/json/")
   system.log_warning(result_get)

================================

post(``url``, ``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a POST request to a web server.

**Parameters:**

* ``url`` (``string``) -- The URL to send the request to.
* ``data`` (``string``) -- The data to send.

**Returns:**

* ``string`` -- The response from the server.

**Example:**

.. code-block:: lua
   :linenos:

   system.log_warning("Test HTTPS request GET, get website page")
   result_get = web.get("https://www.w3.org/History/19921103-hypertext/hypertext/WWW/TheProject.html")
   system.log_warning(result_get)

   --or

   system.log_warning("Test HTTP request POST")
   json_request = "[ {\"query\": \"208.80.152.201\", \"fields\": \"city,country,countryCode,query\", \"lang\": \"eu\"},  \"8.8.8.8\",  \"24.48.0.1\" ]"
   result_post = web.post("http://ip-api.com/batch",json_request)
   system.log_warning(result_post)


================================

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
* ``mod`` (``float``) -- Delimeter of value increase.
* ``parent`` (``int``) -- The parent section.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_slider("Slider Option", "luaOptDummyToggle", 10, 0, 100, 3, parent, function()) -- makes a slider with 3 possible values: on 2, 4, and 6

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

   menu.add_option_slider_toggle("Toggable Slider Option", "luaOptDummyToggle", 10, 0, 100, 10, parent, function())  -- makes a slider with 10 possible values: on 10, 20, and so on.

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
* ``fn`` (``function``) -- Function to call. (optional)

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

   zentornoHash = rage.gameplay.get_hash_key("ZENTORNO")

   menu.add_option_spawn("Spawn Zentorno", zentornoHash, 0, parent) -- 0 is vehicle_spawn type

======================

add_option_text(``name``, ``hash``, ``text``, ``parent``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a text option (e.g. a note).

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``text`` (``string``) -- The displayed text to the right of the name.
* ``parent`` (``int``) -- The parent section.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_text("Just a text option", "luaOptHashText", "Text", parent, foo)

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


add_option_color(``name``, ``hash``, ``color``, ``parent``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a color selection button.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``color`` (``ColorRGBA``) -- The option default color.
* ``parent`` (``int``) -- The parent section ID.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   parent = menu.add_parent("My parent section")

   menu.add_option_color("Color option", "luaOptHashColor", {0, 0, 255, 255}, parent) -- Blue is the default color


======================
======================


update_option(``hash``, ``name``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a menu option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
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

   menu.update_option("luaOptHash", "Lua Option", test)

======================

update_option_toggle(``hash``, ``name``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a toggable option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
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

   menu.update_option_toggle("luaOptHash", "Lua Option", test)

======================

update_option_slider(``hash``, ``name``, ``value``, ``min``, ``max``, ``mod``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a slider option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Delimeter of value increase.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_slider("luaOptDummyToggle", "Slider Option", 10, 0, 100, 3, function())

======================

update_option_slider_toggle(``hash``, ``name``, ``value``, ``min``, ``max``, ``mod``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a slider toggable option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Delimeter of value increase.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_slider_toggle("luaOptDummyToggle", "Slider Toggable Option", 10, 0, 100, 3, function())

======================

update_option_value( ``hash``, ``name``, ``value``, ``min``, ``max``, ``mod``, ``valueSuffix``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a value option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``valueSuffix`` (``string``) -- The value suffix text (e.g. ``m/s``)
* ``fn`` (``function``) -- Function to call. (optional)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_value("luaOptDummyToggle", "Lua option with value", 10, 0, 100, 1, "kb", function())

======================

update_option_value_toggle( ``hash``, ``name``, ``value``, ``min``, ``max``, ``mod``, ``valueSuffix``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a toggable menu value option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``value`` (``float``) -- The option default value.
* ``min`` (``float``) -- Minimum slider value.
* ``max`` (``float``) -- Maximum slider value.
* ``mod`` (``float``) -- Step of value increase.
* ``valueSuffix`` (``string``) -- The value suffix text (e.g. ``m/s``)
* ``fn`` (``function``) -- Function to call. (optional)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_value_toggle("luaOptDummyToggle", "Toggable Lua option with value values", 10, 0, 100, 1, "kb", function())

======================

update_option_value_str(``hash``, ``name``, ``value``, ``list``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a value string option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``value`` (``float``) -- The option default value.
* ``list`` (``vector<string>``) -- The values list separated with a comma
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_value_str("luaOptDummyToggle", "Lua option with multiple values", 0, { "One", "Two", "Three" }, function())

======================

update_option_value_str_toggle(``hash``, ``name``, ``value``, ``list``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a toggable value string option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``value`` (``float``) -- The option default value.
* ``list`` (``vector<string>``) -- The values list separated with a comma
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_value_str_toggle("luaOptDummyToggle", "Toggable Lua option with multiple values", 0, { "One", "Two", "Three" }, function())

======================

update_option_text(``hash``, ``name``, ``text``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a text option (e.g. a note).

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``text`` (``string``) -- The displayed text to the right of the name.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_text("luaOptHashText", "Just a text option", "Text", fn())

======================

update_option_info(``hash``, ``name``, ``info``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates an info text option (e.g. a note).

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``text`` (``string``) -- The displayed text to the right of the name.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_info("luaOptHashText", "Just a text option", "Some Info")

======================

update_option_color(``hash``, ``name``, ``color``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates a color selection button.

**Parameters:**

* ``hash`` (``string``) -- The option hash.
* ``name`` (``string``) -- The name of the option.
* ``color`` (``ColorRGBA``) -- The option default color.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.update_option_color("luaOptHashColor", "Color option", {0, 0, 255, 255})

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

   menu.add_player_option_slider("Slider Player Option", "luaOptDummyToggle", 10, 0, 100, 10, function())  -- makes a slider with 10 possible values: on 10, 20, 30, and so on.

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

   menu.add_player_option_slider_toggle("Toggable Slider Player Option", "luaOptDummyToggle", 10, 0, 100, 10, function()) --  -- makes a slider with 10 possible values: on 10, 20, 30, and so on.

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

add_player_option_text(``name``, ``hash``, ``text``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a player menu text option in the selected player section.

**Parameters:**

* ``name`` (``string``) -- The name of the option.
* ``hash`` (``string``) -- The option hash.
* ``text`` (``string``) -- The option displayed text.
* ``fn`` (``function``) -- Function to call.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   menu.add_player_option_text("Just a text option", "luaOptHashText", "Text", foo)

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
   optionToggled = "Option toggled: " .. tostring(menu.is_option_toggled("luaOptDummyToggle"))

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

   optionVisible = "Option visibility state is: " .. tostring(menu.is_option_visible("luaOptDummyToggle"))

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

   optionEnabled = "Option state is: " .. tostring(menu.is_option_enabled("luaOptDummyToggle"))

======================

get_option_value(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the value of an option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``float`` -- Option value.

**Example:**

.. code-block:: lua
   :linenos:

   -- Get option value
   optionValue = "Option value is: " .. tostring(menu.get_option_value("luaOptHashValue"))

======================

get_option_value_str(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the value of an option as a string.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``string`` -- Option value.

======================

get_option_text(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the option text.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``string`` -- Option text.

**Example:**

.. code-block:: lua
   :linenos:
   
   -- Get option text
   optionText = "Option text is: " .. tostring(menu.get_option_text("luaOptHashText"))


======================

get_option_color(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the selected color of a color selection option.

**Parameters:**

* ``hash`` (``string``) -- The option hash.

**Returns:**

* ``ColorRGBA`` -- Option color.

**Example:**

.. code-block:: lua
   :linenos:
   
   
   parent = menu.add_parent("My parent section")

   menu.add_option_color("Color option", "luaOptHashColor", {0, 0, 255, 255}, parent) -- Blue is the default color

   optionColor = "Option color is: " .. tostring(menu.get_option_color("luaOptHashColor"))


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

section_online_all_players()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Online -> All Players section ID.

**Parameters:**

* None

**Returns:**

* ``int`` -- The ID of the menu section.

**Example:**

.. code-block:: lua
   :linenos:
   
   menu.add_option("All Online Players", "optAllOnlPlayers", menu.section_online_all_players(), function())

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

info(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a blue-colored notification in the bottom-right corner of the screen.

**Parameters:**

* ``text`` (``string``) -- The text to display.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   notify.info("Hello world!")

================================

success(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a green-colored notification in the bottom-right corner of the screen.


**Parameters:**

* ``text`` (``string``) -- The text to display.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   notify.success("Hello world!")

================================

warning(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a red-colored notification in the bottom-right corner of the screen.

**Parameters:**

* ``text`` (``string``) -- The text to display.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   notify.warning("Hello world!")

================================

lua(``text``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a lime-colored notification in the bottom-right corner of the screen.

**Parameters:**

* ``text`` (``string``) -- The text to display.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   notify.lua("Hello world!")

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

is_script_running(``scriptName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a script is running.

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.

**Returns:**

* ``bool`` -- True if the script is running, false otherwise.

================================

execute_as_script(``scriptName``, ``fn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute function as script

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``fn`` (``function``) -- The function to execute.

**Returns:**

* None

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

get_global_addr(``global``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the memory address of a global.

**Parameters:**

* ``global`` (``uint64_t``) -- The name of the global value.

**Returns:**

* ``uint64_t`` -- The memory address of the global.

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

get_local_addr(``scriptName``, ``local``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Parameters:**

* ``scriptName`` (``string``) -- The name of the script.
* ``local`` (``uint64_t``) -- The name of the local value.


**Returns:**

* ``uint64_t`` -- The memory address of the local.

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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the box to draw. Hash is used to identify the box, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the box or not.
* * ``True`` to draw the box
* * ``false`` to not draw the box 
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``color`` (``ColorRGBA``) -- The color of the box. ``{R, G, B, A}``
*   ``rounding`` (``float``) -- The rounding rule of the box.
* *  Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. 
* * Default is ``0``.

More about rounding flags: :doc:`things/roundingflags`

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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the box to draw. Hash is used to identify the box, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the box or not.
* * ``True`` to draw the box
* * ``false`` to not draw the box 
*  ``x`` (``float``) -- The X coordinate of the box's starting point.
*  ``y`` (``float``) -- The Y coordinate of the box's starting point.
*  ``w`` (``float``) -- The width of the box (in pixels)
*   ``h`` (``float``) -- The height of the box (in pixels)
*   ``color`` (``ColorRGBA``) -- The color of the box. ``{R, G, B, A}``
*   ``rounding`` (``float``) -- The rounding rule of the box. 
* * Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. 
* * Default is ``0``.

More about rounding flags: :doc:`things/roundingflags`

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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

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
*   ``color`` (``ColorRGBA``) -- The color of the box. ``{R, G, B, A}``
*   ``colorBorder`` (``ColorRGBA``) -- The color of the border. ``{R, G, B, A}``
*   ``borderFilled`` (``bool``)
* * ``True`` to fill the border
* * ``false`` to not fill the border
*   ``rounding`` (``float``) -- The rounding rule of the box. 
* * Default is ``0``.
*   ``rounding_flags`` (``int``) -- The rounding flags of the box. 
* * Default is ``0``.

More about rounding flags: :doc:`things/roundingflags`

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


.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   
**Parameters:**

*  ``hash`` (``string``) -- The hash of the circle to draw. Hash is used to identify the circle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the circle or not.
* * ``True`` to draw the circle
* * ``false`` to not draw the circle
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``ColorRGBA``) -- The color of the circle. ``{R, G, B, A}``
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Draws a filled circle with the given color.

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the circle to draw. Hash is used to identify the circle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the circle or not.
* * ``True`` to draw the circle
* * ``false`` to not draw the circle
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``ColorRGBA``) -- The color of the circle. ``{R, G, B, A}``
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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the circle to draw. Hash is used to identify the circle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the circle or not.
* * ``True`` to draw the circle
* * ``false`` to not draw the circle
*  ``x`` (``float``) -- The X coordinate of the circle's center.
*  ``y`` (``float``) -- The Y coordinate of the circle's center.
*  ``radius`` (``float``) -- The radius of the circle (in pixels).
*  ``color`` (``ColorRGBA``) -- The color of the circle. ``{R, G, B, A}``
*  ``colorBorder`` (``ColorRGBA``) -- The color of the border. ``{R, G, B, A}``
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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not.
* * ``True`` to draw the triangle
* * ``false`` to not draw the triangle
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``ColorRGBA``) -- The color of the triangle. ``{R, G, B, A}``
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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not.

* * ``True`` to draw the triangle
* * ``false`` to not draw the triangle
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``ColorRGBA``) -- The color of the triangle. ``{R, G, B, A}``
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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

**Parameters:**

*  ``hash`` (``string``) -- The hash of the triangle to draw. Hash is used to identify the triangle, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the triangle or not.
* * ``True`` to draw the triangle
* * ``false`` to not draw the triangle
*  ``x`` (``float``) -- The X coordinate of the triangle's center.
*  ``y`` (``float``) -- The Y coordinate of the triangle's center.
*  ``color`` (``ColorRGBA``) -- The color of the triangle. ``{R, G, B, A}``
*  ``colorBorder`` (``ColorRGBA``) -- The color of the border. ``{R, G, B, A}``
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

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

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
*  ``color`` (``ColorRGBA``) -- The color of the text. ``{R, G, B, A}``
*  ``flags`` (``int``) -- The flags for the text. 
* * Default is ``0``.

More about text flags: :doc:`things/textflags`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   render.draw_text("MyHash", true, "Hello World", 0, 0, 1, { 255, 255, 255, 255 }, 0)

================================

draw_image(``path``, ``hash``, ``draw``, ``x``, ``y``, ``w``, ``h``, ``color``, ``rounding`` = ``0.f``, ``rounding_flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.
   

Draws an image. Supports PNG & JPEG files.

**Parameters:**

*  ``path`` (``string``) -- The path of the image to draw.
*  ``hash`` (``string``) -- The hash of the image to draw. Hash is used to identify the image, so it must be unique.
*  ``draw`` (``bool``) -- Whether to draw the image or not.
* * ``True`` to draw the image
* * ``false`` to not draw the image
*  ``x`` (``float``) -- The X coordinate of the image's center.
*  ``y`` (``float``) -- The Y coordinate of the image's center.
*  ``w`` (``float``) -- The width of the image.
*  ``h`` (``float``) -- The height of the image.
*  ``color`` (``ColorRGBA``) -- The color of the image. ``{R, G, B, A}``
*  ``rounding`` (``float``) -- The rounding of the image.
* * Default is ``0``.
*  ``rounding_flags`` (``int``) -- The flags for the rounding.
* * Default is ``0``.
* * More about rounding flags: :doc:`things/roundingflags`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.draw_image("/path/to/image.png", "MyHash", true, 0, 0, 100, 100, { 255, 255, 255, 255 }, 0.f, 0)

================================

draw_atlas_frame(``hash``, ``atlasHash``, ``frameName``, ``draw``, ``x``, ``y``, ``w``, ``h``, ``color``, ``rounding`` = ``0.0``, ``rounding_flags`` = ``0``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draw an atlas texture frame.

.. note::

   This doesn't have to be called every frame, only if you have to constantly change its parameters.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the atlas texture frame to draw.
*  ``atlasHash`` (``string``) -- The hash of the atlas texture.
*  ``frameName`` (``string``) -- The name of the frame to draw.
*  ``draw`` (``bool``) -- Whether to draw the atlas texture frame or not.
* * ``True`` to draw the atlas texture frame
* * ``false`` to not draw the atlas texture frame
*  ``x`` (``float``) -- The X coordinate of the atlas texture frame
*  ``y`` (``float``) -- The Y coordinate of the atlas texture frame
*  ``w`` (``float``) -- The width of the atlas texture frame.
*  ``h`` (``float``) -- The height of the atlas texture frame.
*  ``color`` (``ColorRGBA``) -- The color of the atlas texture frame. ``{R, G, B, A}``
*  ``rounding`` (``float``) -- The rounding of the atlas texture frame.
* * Default is ``0``.
*  ``rounding_flags`` (``int``) -- The flags for the rounding.
* * Default is ``0``.
* * More about rounding flags: :doc:`things/roundingflags`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   --assuming there's a texture named "test" in the atlas
   render.load_atlas("/path/to/atlas.png", "MyAtlas")
   render.draw_atlas_frame("MyFrameHash", "MyAtlas", "test", true, 240, 15, 0, 0, { 255, 255, 255, 255 }, 0, 0)

================================

remove_draw_task(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a draw task.

**Parameters:**

*  ``hash`` (``string``) -- The hash of the task to remove.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.remove_draw_task("MyTask")

================================

remove_draw_tasks_by_mask(``mask``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove multiple draw tasks with the same masks.

**Parameters:**

*  ``mask`` (``string``) -- The mask of the tasks to remove.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.remove_draw_tasks_by_mask("Task_*") -- Remove all tasks with the hash that starts with "Task_"



================================

load_atlas(``path``, ``atlasHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Load a texture atlas.

**Parameters:**

*  ``path`` (``string``) -- The path of the atlas to load.
*  ``atlasHash`` (``string``) -- The atlas hash.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.load_atlas("/path/to/atlas.png", "MyAtlas")


================================

remove_atlas(``atlasHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unload a texture atlas.

**Parameters:**
 
*  ``atlasHash`` (``string``) -- The atlas hash.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   render.load_atlas("/path/to/atlas.png", "MyAtlas")
   render.remove_atlas("MyAtlas")


===============================

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
      
   borderSize = render.get_border_size() -- Returns the border size.
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
      
   fps = render.get_fps() -- Returns the FPS.
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
      
   rounding = render.get_menu_rounding() -- Returns the rounding.
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
      
   width = render.get_menu_width() -- Returns the width.
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
      
   headerSize = render.get_font_header_size() -- Returns the header size.
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
      
   helperSize = render.get_font_helper_size() -- Returns the helper size.
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
      
   optionSize = render.get_font_option_size() -- Returns the option size.
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
      
   warningSize = render.get_font_warning_size() -- Returns the warning size.
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
      
   cursorPos = render.get_menu_cursor_pos() -- Returns the cursor position.
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
      
   menuPos = render.get_menu_position() -- Returns the menu position.
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
      
   totalSize = render.get_menu_total_size() -- Returns the menu total size.
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
      
   screenRes = render.get_screen_resolution() -- Returns the screen resolution.
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
   
   id = self.get_id() -- Returns the user's character's ID.
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

* ``Vector3`` -- Coordinates in front of self.

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

* ``Vehicle`` -- Vehicle handle.

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
   
   activePlayers = lobby.get_active_players() -- Returns a number of all active players.
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
   
   connectedPlayers = lobby.get_connected_players() -- Returns a number of connected players.
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
   
   armour = lobby.get_player_armour(lobby.get_host()) -- Returns the player's armour ID.
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
   
   health = lobby.get_player_health(lobby.get_host()) -- Returns the host's health.
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
   
   maxHealth = lobby.get_player_max_health(lobby.get_host()) -- Returns the host's maximum health.
   health = lobby.get_player_health(lobby.get_host()) -- Returns the host's health.
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
   
   ped = lobby.get_player_ped(lobby.get_host()) -- Returns the host's ped.
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
   
   host = lobby.get_host() -- Returns the host player ID.
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
   
   nextHost = lobby.get_next_host() -- Returns the next host player ID.
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
   
   coords = lobby.get_player_coords_str(lobby.get_host()) -- Returns the host's coordinates.
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
   
   ip = lobby.get_player_ip(lobby.get_host()) -- Returns the host's IP.
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
   
   name = lobby.get_player_name(lobby.get_host()) -- Returns the host's name.
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
   
   status = lobby.get_player_status(lobby.get_selected_player()) -- Returns the selected player's status.
   system.log_debug("The selected player's status is " .. status .. ".")

===============================

get_player_vehicle_name(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's vehicle name.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's vehicle name. If the player is not in a vehicle, the string "None" is returned.

**Example:**

.. code-block:: lua
   :linenos:
   
   vehicleName = lobby.get_player_vehicle_name(lobby.get_host()) -- Returns the host's vehicle name.
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
   
   deaths = lobby.get_player_deaths(lobby.get_host()) -- Returns the host's deaths.
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
   
   kills = lobby.get_player_kills(lobby.get_host()) -- Returns the host's kills.
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
   
   level = lobby.get_player_level(lobby.get_host()) -- Returns the host's level.
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
   
   money = lobby.get_player_money_bank(lobby.get_host()) -- Returns the host's bank money.
   system.log_debug("The host has $" .. tostring(money) .. " in the bank.")

================================

get_player_money_wallet(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's wallet money.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``int`` -- The player's wallet money.

**Example:**

.. code-block:: lua
   :linenos:
   
   money = lobby.get_player_money_wallet(lobby.get_host()) -- Returns the host's wallet money.
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
   
   rp = lobby.get_player_rp(lobby.get_host()) -- Returns the host's RP.
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
   
   token = lobby.get_player_host_token(lobby.get_host()) -- Returns the host's host token.
   system.log_debug("The host's host token is " .. token .. ".")

================================

get_player_original_scid(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the player's original SCID.

**Parameters:**

* ``player`` (``Player``) -- The player ID.

**Returns:**

* ``string`` -- The player's original SCID.

**Example:**

.. code-block:: lua
   :linenos:
   
   scid = lobby.get_player_original_scid(lobby.get_host()) -- Returns the host's original SCID.
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
   
   scid = lobby.get_player_scid(lobby.get_host()) -- Returns the host's SCID.
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
   
   coords = lobby.get_player_coords(lobby.get_host()) -- Returns the host's coordinates.
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _vehicleNS:

Vehicle namespace
-----------------------

This namespace contains functions related to vehicle manipulation

================================

get_vehicle_handling(``vehicle``, ``param``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the value for the specified handling parameter.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID.
* ``param`` (``string``) -- The handling parameter.

  * You can find a list of handling parameters here: :doc:`things/handling`.

**Returns:**

* ``float`` -- The value for the specified handling parameter.

**Example:**

.. code-block:: lua
   :linenos:
   
   handling = lobby.get_vehicle_handling(self.get_vehicle(), "fBrakeForce") -- Returns the brake force of the vehicle.
   system.log_debug("The player's vehicle has " .. tostring(handling) .. " brake force.")

================================

set_vehicle_handling(``vehicle``, ``param``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the value for the specified handling parameter.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID.
* ``param`` (``string``) -- The handling parameter.

  * You can find a list of handling parameters here: :doc:`things/handling`.
* ``value`` (``float``) -- The value for the specified handling parameter.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   lobby.set_vehicle_handling(self.get_vehicle(), "fAcceleration", 100) -- Sets the acceleration of the vehicle to 100 points.
   system.log_debug("The player's vehicle has been set to have 100 acceleration points.")


================================


.. _text:

Text namespace
----------------------

This namespace contains functions related to text manipulation.

================================

contains(``source``, ``data``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a string contains character/word.

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

Checks whether a string is ``float`` type.

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

Checks whether a string is a number.

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

* ``string`` -- The new string.

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

* ``string`` -- The new string.

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

get_dis2rbed_dir()
^^^^^^^^^^^^^^^^^^^^^

Returns the filepath for the DIS2RBED home directory.

**Parameters:**

* None

**Returns:**

* ``string`` -- The filepath for the DIS2RBED home directory

**Example:**

.. code-block:: lua
   :linenos:
   
   path = fs.get_dis2rbed_dir()
   system.log_debug(path)

================================

get_fonts_dir()
^^^^^^^^^^^^^^^^^

Returns the filepath for the DIS2RBED fonts directory.

**Parameters:**

* None

**Returns:**

* ``string`` -- The filepath for the DIS2RBED fonts directory

**Example:**

.. code-block:: lua
   :linenos:
   
   path = fs.get_fonts_dir()
   system.log_debug(path)

================================

get_themes_dir()
^^^^^^^^^^^^^^^^^

Returns the filepath for the DIS2RBED themes directory.

**Parameters:**

* None

**Returns:**

* ``string`` -- The filepath for the DIS2RBED themes directory

**Example:**

.. code-block:: lua
   :linenos:
   
   path = fs.get_themes_dir()
   system.log_debug(path)

================================

get_locales_dir()
^^^^^^^^^^^^^^^^^

Returns the filepath for the DIS2RBED locales directory.

**Parameters:**

* None

**Returns:**

* ``string`` -- The filepath for the DIS2RBED locales directory

**Example:**

.. code-block:: lua
   :linenos:
   
   path = fs.get_locales_dir()
   system.log_debug(path)

================================

get_lua_dir()
^^^^^^^^^^^^^

Returns the filepath for the DIS2RBED lua directory.

**Parameters:**

* None

**Returns:**

* ``string`` -- The filepath for the DIS2RBED lua directory

**Example:**

.. code-block:: lua
   :linenos:
   
   path = fs.get_lua_dir()
   system.log_debug(path)

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

get_blip_coords(``sprite``, ``color``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the coordinates of the specified :ref:`blip`.

**Parameters:**

* ``sprite`` (``int``) -- Sprite of the blip
* ``color`` (``int``) -- Color of the blip

**Returns:**

* ``Vector3`` -- Coordinates of the blip

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = scripting.get_blip_coords(1, 1)
   system.log_debug(tostring(coords.x) .. ", " .. tostring(coords.y) .. ", " .. tostring(coords.z))

================================

get_ground_z(``coords``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the ground Z coordinate (height) of the specified coordinates.

**Parameters:**

* ``coords`` (``Vector3``) -- Coordinates to check

**Returns:**

* ``float`` -- Ground Z coordinate

**Example:**

.. code-block:: lua
   :linenos:
   
   coords = self.get_coords()
   z = scripting.get_ground_z(coords)
   system.log_debug(tostring(z))


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


get_nearby_peds()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the array of the nearby peds' IDs

**Parameters:**

* None

**Returns:**

* ``vector<Ped>`` -- The array of the nearby peds' IDs

**Example:**

.. code-block:: lua
   :linenos:
   
   peds = scripting.ped.get_nearby_peds()
   for i, ped in ipairs(peds) do
      system.log_debug("Ped " .. i .. ": " .. ped)
   end

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

get_nearby_entities()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the array of the nearby entities' IDs

**Parameters:**

* None

**Returns:**

* ``vector<Entity>`` -- The array of the nearby entities' IDs

**Example:**

.. code-block:: lua
   :linenos:
   
   entities = scripting.entity.get_nearby_entities()
   for i, entity in ipairs(entities) do
      system.log_debug("Entity " .. i .. ": " .. entity)
   end

================================

.. _vehicleNSS:

Vehicle namespace
----------------------

This namespace contains functions that are related to vehicle mods and are used to execute built-in menu features

================================


get_name_from_hash(``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the name of the vehicle based on its hash.

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

Returns the personal vehicle ID.

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

  * For door IDs, see this: :doc:`things/doors`

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

  * For color IDs, see this: :doc:`things/headlightcolor`
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set vehicle color (primary, secondary, pearlescence, wheels)

**Parameters:**

* ``v`` (``Vehicle``) -- Vehicle hash
* ``primary`` (``int``) -- Primary `color ID <https://wiki.rage.mp/index.php?title=Vehicle_Colors>`__
* ``secondary`` (``int``) -- Secondary `color ID <https://wiki.rage.mp/index.php?title=Vehicle_Colors>`__
* ``pearl`` (``int``) -- Pearlescence `color ID <https://wiki.rage.mp/index.php?title=Vehicle_Colors>`__ (if applicable)
* ``wheel`` (``int``) -- Wheel `color ID <https://wiki.rage.mp/index.php?title=Vehicle_Colors>`__

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

  * For window IDs, see this: :doc:`things/windows`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   personal_vehicle = scripting.vehicle.get_personal_vehicle()

   scripting.vehicle.set_windows_opened(personal_vehicle, true, 1)

================================

get_nearby_vehicles()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the array of the nearby vehicles' IDs

**Parameters:**

* None

**Returns:**

* ``vector<Vehicle>`` -- Array of nearby vehicles' IDs

**Example:**

.. code-block:: lua
   :linenos:

   vehicles = scripting.vehicle.get_nearby_vehicles()
   for i, veh in ipairs(vehicles) do
      system.log_debug("Vehicle " .. i .. ": " .. veh)
   end


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

* ``Vehicle`` -- The spawned vehicle handle.

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

* ``Vehicle`` -- The spawned vehicle handle.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

   scripting.weapon.give_weapon_self(rage.gameplay.get_hash_key("weapon_microsmg")) -- Gives self the MicroSMG

================================

give_weapon(``ped``, ``weaponHash``, ``maxAmmo`` = ``true``, ``maxComponents`` = ``true``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

   scripting.weapon.give_weapon(lobby.get_player_ped(lobby.get_host()), rage.gameplay.get_hash_key("weapon_microsmg"), true, true) -- Gives session host a fully loaded and upgraded MicroSMG

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

   scripting.weapon.give_ammo_for_weapon(lobby.get_player_ped(lobby.get_host()), rage.gameplay.get_hash_key("weapon_microsmg")) -- Gives ammo to session host's MicroSMG

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

  * You can read more about explosion IDs here: :doc:`things/exptypes`

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

  * For weather types, see this: :doc:`things/weathertypes`

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

  * For weather types, see this: :doc:`things/weathertypes`
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns whether the wasted/busted screen is visible or not.

**Parameters:**

* ``player`` (``Player``) -- The player ID

**Returns:**

* ``bool``

  * ``true`` -- the wasted/busted screen is visible
  * ``false`` -- the wasted/busted screen is not visible

================================

is_player_pressing_horn(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

This namespace contains ped-related game functions.

================================

add_relationship_group(``name``, ``groupHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a new ped relationship group.

**Parameters:**

* ``name`` (``string``) -- The name of the relationship group
* ``groupHash`` (``Hash``) -- The hash of the created relationship group is output in the second parameter.  

**Returns:**

* ``Any`` -- This function returns nothing.

**Example:**

.. code-block:: lua
   :linenos:

   groupHash = 0
   rage.ped.add_relationship_group("COPS", groupHash)
   system.log_debug("Group hash: " .. tostring(groupHash))

================================

can_create_random_cops()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a Ped can summon random cops.

**Parameters:**

* None

**Returns:**

* ``bool``
  
  * ``true`` -- Ped can summon random cops
  * ``false`` -- Ped can't summon random cops

**Example:**

.. code-block:: lua
   :linenos:

   system.log_debug(tostring(rage.ped.can_create_random_cops()))

================================

can_ped_ragdoll(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if ragdoll is enabled for this ped

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``bool``
  
  * ``true`` -- Ped ragdoll on
  * ``false`` -- Ped ragdoll off

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.can_ped_ragdoll(ped)

   system.log_debug(tostring(data))

================================

clear_all_ped_props(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clears all ped's props.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ped.clear_all_ped_props(ped)

================================

clear_ped_blood_damage(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clears the blood on a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ped.clear_ped_blood_damage(ped)

================================

clear_ped_tasks_immediately(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clears all ped's tasks.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ped.clear_ped_tasks_immediately(ped)

================================

clear_relationship_between_groups(``relationship``, ``group1``, ``group2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clears the relationship between two groups. This should be called twice (once for each group).

**Parameters:**

* ``relationship`` (``int``) -- Relationship ID
  
  * Relationship types here: :doc:`things/relationship`

* ``group1`` (``Hash``) -- Group 1 hash
* ``group2`` (``Hash``) -- Group 2 hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ped.clear_relationship_between_groups((2, rage.gameplay.get_hash_key("GANG_1"), rage.gameplay.get_hash_key("COP")))
   rage.ped.clear_relationship_between_groups((2, rage.gameplay.get_hash_key("COP"), rage.gameplay.get_hash_key("GANG_1")))

================================

clone_ped(``ped``, ``isNetwork``, ``bScriptHostPed``, ``copyHeadBlendFlag``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a copy of the passed ped, optionally setting it as local and/or shallow-copying the head blend data.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``isNetwork`` (``bool``) -- Whether or not the ped should be registered as a network object
* ``bScriptHostPed`` (``bool``) -- Script host flag
* ``copyHeadBlendFlag`` (``bool``) -- If true, head blend data is referenced, not copied

**Returns:**

* ``Ped`` -- A new ped handle representing the ped's copy

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ped.clone_ped(ped, false, false, true)

================================

create_group(``unused``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a new ped group. Note: groups can contain up to 8 peds.

.. note::

   Groups can contain up to 8 peds.

**Parameters:**

* ``unused`` (``int``) -- The parameter is unused

**Returns:**

* ``int`` -- A handle to the created group, or 0 if a group couldn't be created

**Example:**

.. code-block:: lua
   :linenos:

   rage.ped.create_group()

================================

create_ped(``pedType``, ``modelHash``, ``x``, ``y``, ``z``, ``heading``, ``isNetwork``, ``bScriptHostPed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Spawns a ped (biped character, pedestrian, actor) with the specified model at the specified position and heading. This ped will initially be owned by the creating script as a mission entity, and the model should be loaded already (e.g. using streaming.request_model).

**Parameters:**

* ``pedType`` (``int``) -- Unused. Peds get set to CIVMALE/CIVFEMALE/etc. no matter the value specified
* ``modelHash`` (``Hash``) -- The model of ped to spawn

  * `Ped Models <https://wiki.rage.mp/index.php?title=Peds>`__
* ``x`` (``float``) -- Spawn coordinate X component
* ``y`` (``float``) -- Spawn coordinate Y component
* ``z`` (``float``) -- Spawn coordinate Z component
* ``heading`` (``float``) -- Heading to face towards, in degrees
* ``isNetwork`` (``bool``) -- Whether to create a network object for the ped

  * ``true`` -- A network object is created for the ped
  * ``false`` -- The ped exists only locally

* ``bScriptHostPed`` (``bool``) -- Whether to register the ped as pinned to the script host in the R* network model

**Returns:**

* ``Ped`` -- A script handle for the ped

  * ``0`` -- The ped spawn failed

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords_infront(20)

   rage.ped.create_ped(rage.gameplay.get_hash_key("csb_mp_agent14"), coords.x, coords.y, coords.z, 90, true, true)

================================

does_group_exist(``groupId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a group exists.

**Parameters:**

* ``groupId`` (``int``) -- The group ID

**Returns:**

* ``bool`` -- Group status
  
  * ``true`` -- Group exists
  * ``false`` -- Group does not exist

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ped.can_ped_ragdoll(ped)

================================

does_relationship_group_exist(groupHash)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a relationship group exists.

**Parameters:**

* ``groupHash`` (``Hash``) -- The group hash

**Returns:**

* ``bool`` -- Group status
  
  * ``true`` -- Group exists
  * ``false`` -- Group does not exist

**Example:**

.. code-block:: lua
   :linenos:

   data1 = rage.ped.does_relationship_group_exist(rage.gameplay.get_hash_key("PLAYER") -- true
   data2 = rage.ped.does_relationship_group_exist(0x6F0783F5) -- true
   data3 = rage.ped.does_relationship_group_exist("") -- false

   system.log_debug(tostring(data1)))
   system.log_debug(tostring(data2))
   system.log_debug(tostring(data3))


================================

get_current_ped_weapon(``ped``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns hash of the ped's active weapon


**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``p2`` (``bool``) -- Always seems to be ``true``


**Returns:**

* ``Hash`` -- The current weapon hash

  * Find out more about weapon hashes `here <https://wiki.rage.mp/index.php?title=Weapons>`__

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   
   data = rage.ped.get_current_ped_weapon(ped, true)

   system.log_debug(tostring(data))

================================

get_group_size(``groupId``, ``unknown``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns ped group size.

**Parameters:**

* ``groupId`` (``int``) -- The group ID
* ``unknown`` (``Any``) -- Unknown, seems to be a boolean that represents if the group exists at all

**Returns:**

* ``int`` -- The group member count

**Example:**


.. note::

   This example was not tested.

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   ped = rage.ped.clone_ped(entity, false, false, true)
   group = rage.ped.create_group()
   rage.ped.set_ped_as_group_leader(entity, group)
   rage.ped.set_ped_as_group_member(ped, group)
   data = rage.ped.get_group_size(group, true)
   system.log_debug(tostring(data)) -- should return 2

================================

get_number_of_ped_drawable_variations(``ped``, ``componentID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of drawable variations for the specified body part.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID / body part ID

  * You can find the component IDs here: :doc:`things/pedCompID`

**Returns:**

* ``int`` -- The number of drawable variations

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_number_of_ped_drawable_variations(ped, 0)
   system.log_debug(tostring(data)) -- drawable variations number for head

================================

get_number_of_ped_prop_drawable_variations(``ped``, ``propID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of drawable variations for the specified prop.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``propID`` (``int``) -- The prop ID

  * You can find the prop IDs here: :doc:`things/pedPropID`

**Returns:**

* ``int`` -- The number of drawable variations

**Example:**


.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   -- делать так:

   data = tostring(rage.ped.get_number_of_ped_prop_drawable_variations(ped, 0))
   system.log_debug(data)

   -- или вот так?

   data = rage.ped.get_number_of_ped_prop_drawable_variations(ped, 0)
   system.log_debug(tostring(data))

================================

get_number_of_ped_prop_texture_variations(``ped``, ``propID``, ``drawableID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
      
   this funciton is not yet documented.

================================

get_number_of_ped_texture_variations(``ped``, ``componentID``, ``drawableID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a number of possible texture variations for the specified component

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID / body part ID

  * You can find the component IDs here: :doc:`things/pedPropID`
* ``drawableID`` (``int``) -- The drawable ID

**Returns:**

* ``int`` -- The number of texture variations

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_number_of_ped_texture_variations(ped, 0, 0)
   system.log_debug(tostring(data)) -- texture variations number for head

================================

get_ped_bone_index(``ped``, ``boneID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the bone name for the specified bone ID.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``boneID`` (``int``) -- The bone ID

  * You can find the bone IDs here: :doc:`things/bones`

**Returns:**

* ``string`` -- The bone name

**Example:**

.. code-block:: lua
   :linenos:

   data1 = rage.ped.get_ped_bone_index(entity, 0)
   data2 = rage.ped.get_ped_bone_index(entity, 1356)
   data3 = rage.ped.get_ped_bone_index(entity, 2108)

   system.log_debug(tostring(data)) -- 0
   system.log_debug(tostring(data)) -- -1
   system.log_debug(tostring(data)) -- 5

================================

get_ped_drawable_variation(``ped``, ``componentID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get variation ID based on component ID.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID / body part ID

  * You can find the component IDs here: :doc:`things/pedCompID`

**Returns:**

* ``int`` -- The variation ID

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_drawable_variation(ped, 0) -- variations count for head
   system.log_debug(tostring(data))

================================

get_ped_eye_color(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the eye color of the specified ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``int`` -- The eye color

  * For eye colors list, see this: :doc:`things/eyecolors`

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_eye_color(ped)
   system.log_debug(tostring(data))

================================

get_ped_group_index(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the group id of which the specified ped is a member of.  

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``int`` -- The group id

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   group = rage.ped.create_group()
   rage.ped.set_ped_as_group_leader(entity, group)
   rage.ped.get_ped_group_index(entity)
   system.log_debug(tostring(data))

================================

get_ped_head_blend_data(``ped``, ``headBlendData``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not yet documented and is not yet available to use in Lua.

Returns face shape data of the specified ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``headBlendData`` (``int``) -- The head blend data

  * ``shapeFirst`` -- dad shape
  * ``shapeSecond`` -- mom shape
  * ``shapeThird`` -- third shape (unused)
  * ``skinFirst`` -- dad skin color
  * ``skinSecond`` -- mom skin color
  * ``skinThird`` -- third skin color (unused)
  * ``shapeMix`` -- shape mix
  * ``skinMix`` -- skin mix
  * ``thirdMix`` -- third mix (unused)

**Returns:**

* ``bool`` -- Unknown



================================


get_ped_head_overlay_value(``ped``, ``overlayID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the setting of the specified head part (makeup, complexion, etc.)

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``overlayID`` (``int``) -- The overlay ID

  * You can find the overlay IDs here: :doc:`things/pedOverlayID`

**Returns:**

* ``int`` -- The overlay value

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_head_overlay_value(ped, 0) -- get Blemishes overlay value
   system.log_debug(tostring(data))

================================

get_ped_max_health(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the maximum health of the specified ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``int`` -- The maximum health

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_max_health(ped)
   system.log_debug(tostring(data))


================================

get_ped_prop_index(``ped``, ``componentID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Returns a ped's prop index (identifier) based on component ID.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID / body part ID

  * You can find the component IDs here: :doc:`things/pedPropID`

**Returns:**

* ``int`` -- The prop index

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_prop_index(ped, 0) -- get helmet prop index
   system.log_debug(tostring(data))

================================

get_ped_prop_texture_index(``ped``, ``componentID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Returns a ped's prop texture index (identifier) based on component ID.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID / body part ID

  * You can find the component IDs here: :doc:`things/pedPropID`

**Returns:**

* ``int`` -- The prop texture index

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_prop_texture_index(ped, 0) -- get helmet prop texture index
   system.log_debug(tostring(data))

================================

get_ped_relationship_group_hash(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a ped's relationship group hash.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``int`` -- The relationship group hash

  * You can find the relationship group hashes here: :doc:`things/relationship`

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_relationship_group_hash(ped)
   system.log_debug(tostring(data))

================================

get_ped_texture_variation(``ped``, ``componentID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a ped's texture variation (identifier) based on component ID.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID / body part ID

  * You can find the component IDs here: :doc:`things/pedCompID`


**Returns:**

* ``int`` -- The texture variation ID

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_ped_texture_variation(ped, 0) -- get helmet texture variation
   system.log_debug(tostring(data))

================================

get_vehicle_ped_is_using(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the vehicle that the specified ped is in.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``Vehicle`` -- The vehicle handle

  * If the ped is not in a vehicle, the handle will be 0.

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.get_vehicle_ped_is_using(ped)
   platetext = rage.vehicle.get_vehicle_number_plate_text(data)
   system.log_debug(tostring(platetext))

================================

is_ped_a_player(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the specified ped is a player.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``bool`` 

  * ``true`` -- the ped is a player
  * ``false`` -- the ped is not a player

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.is_ped_a_player(ped)
   system.log_debug(tostring(data))

================================

is_ped_group_member(``ped``, ``group``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``group`` (``Group``) -- The group ID

**Returns:**

* ``bool`` 

  * ``true`` -- the ped is a member of the group
  * ``false`` -- the ped is not a member of the group

**Example:**   

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   group = rage.ped.create_group()
   data = rage.ped.is_ped_group_member(ped, group)
   if data then
      system.log_debug("Ped is a member of group " .. tostring(group))
   else
      system.log_debug("Ped is not a member of group " .. tostring(group))
   end

================================

is_ped_in_any_vehicle(``ped``, ``atGetIn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whether or not the specified ped is in any vehicle.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``atGetIn`` (``bool``) -- Whether or not to check if the ped is currently in the process of entering a vehicle

  * ``true`` -- Check if the ped is in the process of entering a vehicle
  * ``false`` -- Check if the ped is in any vehicle

**Returns:**


* ``bool``

  * ``true`` -- the ped is in any vehicle (or is in the process of entering a vehicle)
  * ``false`` -- the ped is not in any vehicle (or is not in the process of entering a vehicle)

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.is_ped_in_any_vehicle(ped, true)
   if data then
      system.log_debug("Ped is going to enter or already is in the vehicle")
   else
      system.log_debug("Ped is not going to enter or is not in the vehicle")
   end

================================

is_ped_ragdoll(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the ragdoll is currently active for this ped

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``bool`` 

  * ``true`` -- the ragdoll is active
  * ``false`` -- the ragdoll is inactive

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.is_ped_ragdoll(ped)
   if data then
      system.log_debug("Ped ragdoll active")
   else
      system.log_debug("Ragdoll inactive")
   end

================================

is_ped_shooting(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the specified ped is shooting.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``bool`` 

  * ``true`` -- the ped is shooting
  * ``false`` -- the ped is not shooting

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.is_ped_shooting(ped)
   if data then
      system.log_debug("Ped is shooting")
   else
      system.log_debug("Ped is not shooting")
   end

================================

is_ped_wimming(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the specified ped is swimming.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``bool`` 

  * ``true`` -- the ped is swimming
  * ``false`` -- the ped is not swimming

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.is_ped_wimming(ped)
   if data then
      system.log_debug("Ped is swimming")
   else
      system.log_debug("Ped is not swimming")
   end

================================

is_ped_using_any_scenario(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the specified ped is using any scenario.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* ``bool`` 

  * ``true`` -- the ped is using any scenario
  * ``false`` -- the ped is not using any scenario

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   data = rage.ped.is_ped_using_any_scenario(ped)
   if data then
      system.log_debug("Ped is using any scenario")
   else
      system.log_debug("Ped is not using any scenario")
   end

================================

remove_group(``groupId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a ped group from the game session.

**Parameters:**

* ``groupId`` (``Group``) -- The group ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   group = rage.ped.create_group()
   rage.ped.remove_group(group)
   system.log_debug("Group " .. tostring(group) .. " removed")

================================

remove_ped_from_group(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a ped from its group.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.remove_ped_from_group(ped)
   system.log_debug("Ped " .. tostring(ped) .. " removed from group")

================================

remove_relationship_group(``groupHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a relationship group from the game session.

**Parameters:**

* ``groupHash`` (``Hash``) -- The relationship group hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ped.remove_relationship_group(0xA49E591C)
   system.log_debug("Relationship group COP removed")

================================

reset_group_formation_default_spacing(``group``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets group formation settings.

**Parameters:**

* ``group`` (``Group``) -- The group ID

**Returns:**

* None

.. note::

   This example was not tested.

**Example:**

.. code-block:: lua
   :linenos:

   group = rage.ped.create_group()
   rage.ped.reset_group_formation_default_spacing(group)
   system.log_debug("Group formation settings reset")

================================

reset_ped_movement_clipset(``ped``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets the ped movement clip set (walking animation set).

.. note::

   Seems to only work with player peds. Needs more testing with ordinary peds.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``p1`` (``float``) -- Unknown
   
  * If ``p1`` is ``0.0``, you are back to normal.
  * If ``p1`` is ``1.0``, it looks like you can only rotate the ped, not walk.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.reset_ped_movement_clipset(ped, 0.0)
   system.log_debug("Ped movement clipset reset")

================================

resurrect_ped(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resurrects a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   deadPed = rage.ped.clone_ped(ped, false, false, true)

   -- imagine your clone gets killed

   rage.ped.resurrect_ped(deadPed)
   system.log_debug("Clone resurrected")

================================


set_can_attack_friendly(``ped``, ``bool``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether the ped can attack friendly peds.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``bool`` (``bool``) -- Whether the ped can attack friendly peds
* ``p2`` (``bool``) -- Unknown. Use ``false``, as setting it to ``true`` doesn't let you attack friends.

**Returns:**

* None

.. note::

   This example was not tested.


**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_can_attack_friendly(ped, true, false)
   system.log_debug("Ped can now attack friendly peds")

====================================

set_create_random_cops(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether random cops can be summoned

**Parameters:**

* ``toggle`` (``bool``) -- Whether random cops can be summoned

  * ``true`` -- random cops can be summoned
  * ``false`` -- random cops can't be summoned

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ped.set_create_random_cops(true)
   system.log_debug("Random cops can now be summoned")

====================================

set_group_formation(``group``, ``formationType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the group formation type.

**Parameters:**

* ``group`` (``Group``) -- The group ID
* ``formationType`` (``int``) -- The formation type

  * You can find formation types here: :doc:`things/formation`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   group = rage.ped.create_group()
   rage.ped.set_group_formation(group, 1)
   system.log_debug("Group formation set to formation type Circle Around Leader")

====================================

set_group_formation_spacing(``group``, ``p1``, ``p2``, ``p3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the group formation spacing.

**Parameters:**

* ``group`` (``Group``) -- The group ID
* ``p1`` (``float``) -- The spacing between members (in meters)
* ``p2`` (``float``) -- Unknown. Seen to be ``-1``
* ``p3`` (``float``) -- Unknown. Seen to be ``-1``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   group = rage.ped.create_group()
   rage.ped.set_group_formation_spacing(group, 10, -1, -1)
   system.log_debug("Group formation spacing set to 10 meters")

====================================

set_ped_accuracy(``ped``, ``accuracy``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the ped shooting accuracy.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``accuracy`` (``int``) -- Accuracy rate (0-100)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_accuracy(ped, 100)
   system.log_debug("Ped accuracy set to 100")

====================================

set_ped_as_group_leader(``ped``, ``groupId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the ped as a ped group leader.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``groupId`` (``int``) -- The group ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   group = rage.ped.create_group()
   ped = self.get_ped()
   rage.ped.set_ped_as_group_leader(ped, group)
   system.log_debug("Ped set as group leader")

====================================

set_ped_as_group_member(``ped``, ``groupId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the ped as a ped group member.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``groupId`` (``int``) -- The group ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   group = rage.ped.create_group()
   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_as_group_leader(ped, group)
   rage.ped.set_ped_as_group_member(clone, group)
   system.log_debug("Clone set as group member")

====================================

set_ped_can_ragdoll(``ped``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles the ragdoll for a ped

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``toggle`` (``bool``) -- Ragdoll toggle

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_can_ragdoll(clone, true)
   system.log_debug("Clone's ragdoll is now on")

====================================

set_ped_combat_ability(``ped``, ``abilityLevel``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets combat ability level for a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``abilityLevel`` (``int``) -- The ability level

  * ``100`` = attack
  * less than ``50`` -ish would mean run away

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_combat_ability(Clone, 100)
   system.log_debug("Clone combat ability set to Trevor level")

====================================

set_ped_combat_attributes(``ped``, ``attributeId``, ``enabled``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configures various combat attributes for a ped

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``attributeId`` (``int``) -- The attribute ID

  * You can find attribute IDs here: :doc:`things/combat_attributes`
* ``enabled`` (``bool``) -- Whether the attribute is enabled

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_combat_attributes(clone, 1, true)
   system.log_debug("Clone combat attributes set to 1 (BF_CanUseVehicles)")


====================================

set_ped_combat_movement(``ped``, ``combatMovement``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the combat movement rule for a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``combatMovement`` (``int``) -- The combat movement rule

  * You can find combat movement rules here: :doc:`things/combat_movements`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_combat_movement(clone, 2)
   system.log_debug("Clone combat movement set to 2 (Offensive)")

====================================

set_ped_combat_range(``ped``, ``combatRange``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the combat range for a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``combatRange`` (``int``) -- The combat range

  * You can find combat ranges here: :doc:`things/combat_ranges`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_combat_range(clone, 1)
   system.log_debug("Clone combat range set to 1 (Medium)")

====================================

set_ped_component_variation(``ped``, ``componentId``, ``drawableId``, ``textureId``, ``paletteId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the component variation for a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentId`` (``int``) -- The component ID

  * You can find component IDs here: :doc:`things/pedCompID`
* ``drawableId`` (``int``) -- The drawable ID
* ``textureId`` (``int``) -- The texture ID
* ``paletteId`` (``int``) -- The palette ID
  
  * Can be from ``0`` to ``3``.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   componentID = 0  -- face
   drawableId = rage.ped.get_number_of_ped_drawable_variations(ped, componentID) -- face drawable count
   textureId = rage.ped.get_number_of_ped_texture_variations(ped, componentID, 0) -- face texture count
   rage.ped.set_ped_component_variation(ped, componentID, drawableId, textureId, 2)

   system.log_debug("Manipulated face components.")

====================================

set_ped_config_flag(``ped``, ``flagId``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a ped config flag.

.. note::

   #. When ``flagId`` is set to ``33`` and the bool value to ``true``, peds will die by ragdolling, so you should set this flag to false when you resurrect a ped.
   #. When ``flagId`` is set to ``62`` and the bool value to ``false``, peds may jump out of their vehicles and never return.

   Config flags changes during game session:

  * Jumping: changes ``60``, ``61``, ``104`` to ``false``.
  * Being in water (swimming): changes ``60``, ``61`` to ``false`` and ``65``, ``66``, ``168`` to ``true``.
  * Falling: changes ``60``, ``61``, ``104``, ``276`` to ``false`` and ``76`` to ``true``.
  * Dying: changes ``60``, ``61``, ``104``, ``276`` to ``false``.
  * Being in a car: changes ``60``, ``79``, ``104`` to ``false`` and ``62`` to ``true``.

   Maximum value for ``flagId`` is 426. FlagId ``240`` appears to be somewhat special.



**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``flagId`` (``int``) -- The flag ID

  * You can find flag IDs here: :doc:`things/pedConfigs`
* ``value`` (``bool``) -- The flag value

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_config_flag(ped, 149, false)
   system.log_debug("Damage reduced for self.")

====================================

set_ped_default_component_variation(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets ped clothes to default

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   rage.ped.set_ped_default_component_variation(clone)
   system.log_debug("Clone's clothes set to default.")

====================================

set_ped_density_multiplier_this_frame(``multiplier``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the ped density on the streets.

.. note::

   You have to call this every frame, so use this inside a loop.

**Parameters:**

* ``multiplier`` (``float``) -- The density multiplier (should be between ``0`` and ``1``)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   function nopeds()
      rage.ped.set_ped_density_multiplier_this_frame(0.0)
   end

   system.add_task("task", "t", -1, nopeds)

====================================

set_ped_eye_color(``ped``, ``index``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the eye color for a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``index`` (``int``) -- The eye color index

  * For eye colors list, see this: :doc:`things/eyecolors`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_eye_color(ped, 1)
   system.log_debug("Ped's eye color set to Emerald.")

====================================

set_ped_head_blend_data(``ped``, ``shapeFirst``, ``shapeSecond``, ``shapeThird``, ``skinFirst``, ``skinSecond``, ``skinThird``, ``shapeMix``, ``skinMix``, ``thirdMix``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the face shape settings for the selected ped.

.. note::

   This function is often called prior to ``set_ped_head_overlay_color`` and ``set_ped_head_overlay`` native functions.

**Parameters:**


* ``ped`` (``Ped``) -- The ped ID
* ``shapeFirst`` (``int``) -- dad shape
* ``shapeSecond`` (``int``) -- mom shape
* ``shapeThird`` (``int``) -- third shape (unused)
* ``skinFirst`` (``int``) -- dad skin color
* ``skinSecond`` (``int``) -- mom skin color
* ``skinThird`` (``int``) -- third skin color (unused)
* ``shapeMix`` (``float``) -- shape mix (``0.0`` - ``1.0`` of whose characteristics to take: Mother -> Father)
* ``skinMix`` (``float``) -- skin mix (``0.0`` - ``1.0`` of whose characteristics to take: Mother -> Father)
* ``thirdMix`` (``float``) -- third mix (unused)
* ``isParent`` (``bool``) -- usually ``false``

**Returns:**

* None

**Example:**

.. note::

   This example was not tested, and there are no lists of possible input values.

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_head_blend_data(ped, 0, 0, 0, 0, 0, 0, 0, 0, 0, false)

====================================

set_ped_head_overlay(``ped``, ``overlayID``, ``index``, ``opacity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the setting of the specified head part (makeup, complexion, etc.)

.. note::

   You may need to call ``set_ped_head_blend_data`` for this to work.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``overlayID`` (``int``) -- The overlay ID
* ``index`` (``int``) -- The overlay index

  * You can find overlay ID data here: :doc:`things/pedOverlayID`
* ``opacity`` (``float``) -- The overlay opacity (``0.0`` - ``1.0``)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_head_overlay(ped, 8, 1, 0.5)
   system.log_debug("Ped's lipstick set to 1, half opacity.")

====================================

set_ped_head_overlay_color(``ped``, ``overlayID``, ``colorType``, ``colorID``, ``secondColorID``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the color of the specified head part (lipstick, beards, eyebrows, chest hair.)

.. note:: 

   You may need to call ``set_ped_head_blend_data`` for this to work.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``overlayID`` (``int``) -- The overlay ID

  * You can find overlay ID data here: :doc:`things/pedOverlayID`
* ``colorType`` (``int``) -- The color type

  * ``1`` for eyebrows, beards and chest hair.
  * ``2`` for lipstick and blush.
* ``colorID`` (``int``) -- The color ID

  * For color ID list, see this: :doc:`things/pedOverlayID`
* ``secondColorID`` (``int``) -- The second color ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_head_overlay_color(ped, 8, 1, 1, 1)
   system.log_debug("Ped's lIpstick set to red.")

====================================

set_ped_into_vehicle(``ped``, ``vehicle``, ``seatIndex``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Warps the ped into a vehicle.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``seatIndex`` (``int``) -- The seat index

  * For seat index list, see this: :doc:`things/seattypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- assuming you are already in a vehicle
   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   vehicle = self.get_vehicle()
   rage.ped.set_ped_into_vehicle(clone, vehicle, 0)
   system.log_debug("Ped warped into vehicle, right front seat.")

====================================

set_ped_max_health(``ped``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the maximum health for the ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``value`` (``int``) -- The maximum health

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_max_health(ped, 100000)
   system.log_debug("Doomguy mode activated.")

====================================

set_ped_movement_clipset(``ped``, ``clipset``, ``transitionSpeed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the movement clipset (walking animation set) for the ped.

.. note::

   You have to request an animation set before using this.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``clipset`` (``string``) -- The movement clipset name

  * For a list of movement clipsets, see this: :doc:`things/pedMovements`
* ``transitionSpeed`` (``float``) -- The speed of transtition between two clipsets

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.streaming.request_anim_set("MOVE_M@DRUNK@VERYDRUNK")
   rage.ped.set_ped_movement_clipset(ped, "MOVE_M@DRUNK@VERYDRUNK", 5.0)

====================================

set_ped_never_leaves_group(``ped``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether the ped can leave a ped group or not.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``toggle`` (``bool``) -- Toggle
  
  * ``true`` to not let the ped be able leave the group
  * ``false`` to let him leave the group

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   clone = rage.ped.clone_ped(ped, false, false, true)
   group = rage.ped.create_group()

   rage.ped.set_ped_as_group_leader(ped, group)
   rage.ped.set_ped_as_group_member(clone, group)

   rage.ped.set_ped_never_leaves_group(clone, true)
   system.log_debug("Clone can't leave group.")

====================================

set_ped_prop_index(``ped``, ``componentID``, ``drawableID``, ``textureID``, ``attach``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set prop variation on a ped. Components, drawables and textures IDs are related to the ped model.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``componentID`` (``int``) -- The component ID

  * For component ID list, see this: :doc:`things/pedPropID`
* ``drawableID`` (``int``) -- The drawable ID
* ``textureID`` (``int``) -- The texture ID
* ``attach`` (``bool``) -- Attach the prop to the ped

**Returns:**

* None

**Example:**

.. note::

   This example was not tested.

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_prop_index(ped, 0, 51, 0, true) -- places a black helmet
   system.log_debug("Ped's helmet set to 0, 51, 0.")

====================================

set_ped_random_component_variation(``ped``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a random component variation for the ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``p1`` (``int``) -- Seems to be always 0, unused anyway.


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_random_component_variation(ped, 0)
   system.log_debug("Ped's component variation set.")

====================================

set_ped_relationship_group_hash(``ped``, ``hash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the relationship group for the ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``hash`` (``int``) -- The relationship group hash

  * For a list of relationship group hashes, see this: :doc:`things/relationship`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_relationship_group_hash(ped, 0xA49E591C)
   system.log_debug("Ped's relationship group set to COP.")

====================================

set_ped_to_ragdoll(``ped``, ``time1``, ``time2``, ``ragdollType``, ``p4``, ``p5``, ``p6``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forces the ped to ragdoll.

**Parameters:**

* ``ped`` (``Ped``) -- The ped ID
* ``time1`` (``int``) -- The time ped is in ragdoll state (in ms)
* ``time2`` (``int``) -- The time ped needs to stand up (in ms)
* ``ragdollType`` (``int``) -- The ragdoll type

  * ``0`` -- Normal ragdoll
  * ``1`` -- Falls with stiff legs/body
  * ``2`` -- Narrow leg stumble(may not fall)
  * ``3`` -- Wide leg stumble(may not fall)
* ``p4`` (``int``) -- Unknown, seems to be always ``true``
* ``p5`` (``int``) -- Unknown, seems to be always ``true``
* ``p6`` (``int``) -- Unknown, seen to be both ``true`` and ``false``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()
   rage.ped.set_ped_to_ragdoll(ped, 10000, 3000, 0, true, true, false)
   system.log_debug("Ped ragdolled.")


===================================

set_relationship_between_groups(``relationship``, ``group1``, ``group2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the relationship between two groups.

.. note::

   This should be called twice (once for each group).

**Parameters:**

* ``relationship`` (``int``) -- The relationship type
* ``group1`` (``Hash``) -- The first group hash
* ``group2`` (``Hash``) -- The second group hash

  * For relationship groups and types, see this: :doc:`things/relationship`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ped.set_relationship_between_groups(1, 0xA49E591C, 0x6F0783F5)
   rage.ped.set_relationship_between_groups(1, 0x6F0783F5, 0xA49E591C)
   system.log_debug("Set respect relationship between cops and player")

===================================

set_scenario_ped_density_multiplier_this_frame(``p0``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets ped density during scenarios

.. note::

   You have to call this every frame, so use this inside a loop.

**Parameters:**

* ``p0`` (``float``) -- The density multiplier (should be between ``0`` and ``1``)
* ``p1`` (``float``) -- Should be the same as ``p0``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   function halfpeds()
      rage.ped.set_scenario_ped_density_multiplier_this_frame(0.5, 0.5)-- thanos moment 
   end
   system.add_task("half", "thanos", -1, halfpeds)

================================

.. _vehicleNSR:

Vehicle namespace
----------------------

This namepsace contains vehicle-related game functions.

====================================

add_vehicle_phone_explosive_device(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a phone explosive device to the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.add_vehicle_phone_explosive_device(vehicle)

====================================

clear_vehicle_custom_primary_colour(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets the vehicle's primary custom colour to it's real primary one.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.clear_vehicle_custom_primary_colour(vehicle)
   system.log_debug("Vehicle's primary custom colour reset.")

====================================

clear_vehicle_custom_secondary_colour(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets the vehicle's secondary custom colour to it's real secondary one.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.clear_vehicle_custom_secondary_colour(vehicle)
   system.log_debug("Vehicle's secondary custom colour reset.")

====================================

control_landing_gear(``vehicle``, ``state``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Switches the landing gear of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``state`` (``int``) -- The gear state

  * ``0`` -- Deployed
  * ``1`` -- Closing  
  * ``2`` -- Opening
  * ``3`` -- Retracted

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- assuming you're in a plane or a helicopter
   vehicle = self.get_vehicle()
   rage.vehicle.control_landing_gear(vehicle, 0)
   system.log_debug("Landing gear deployed.")

====================================

create_vehicle(``modelHash``, ``x``, ``y``, ``z``, ``heading``, ``isNetwork``, ``bScriptHostVeh``, ``p7``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a vehicle.

.. note::

   You have to load the model first before creating a vehicle.

**Parameters:**

* ``modelHash`` (``Hash``) -- The vehicle model hash
* ``x`` (``float``) -- Spawn coordinate X component
* ``y`` (``float``) -- Spawn coordinate Y component
* ``z`` (``float``) -- Spawn coordinate Z component
* ``heading`` (``float``) -- Spawn heading (to face towards, degrees)
* ``isNetwork`` (``bool``) -- Whether to create a network object for the vehicle. 
  
  * ``true`` -- Create a network object for the vehicle. Other players will be able to see it.
  * ``false`` -- the vehicle exists only locally.
* ``bScriptHostVeh`` (``bool``) -- Whether to register the vehicle as pinned to the script host in the R* network model.
* ``p7`` (``bool``) -- Unknown

**Returns:**

* ``Vehicle`` -- The vehicle ID

  ``0`` -- The vehicle couldn't be created.


**Example:**

.. code-block:: lua
   :linenos:

   zentornoHash = rage.gameplay.get_hash_key("ZENTORNO")
   coords = self.get_coords_infront(10)

   rage.streaming.request_model(zentornoHash)
   vehicle = rage.vehicle.create_vehicle(zentornoHash, coords.x, coords.y, coords.z, 0, true, false, false)
   if not vehicle == 0 then
      system.log_debug("Created vehicle.")
   end
   rage.streaming.set_model_as_no_longer_needed(zentornoHash)

====================================

detonate_vehicle_phone_explosive_device()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Detonates a previously-added phone explosive device.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- assuming you're in a vehicle

   vehicle = self.get_vehicle()

   rage.vehicle.add_vehicle_phone_explosive_device(vehicle)
   rage.vehicle.detonate_vehicle_phone_explosive_device()
   system.log_debug("Detonated phone explosive device.")

====================================

does_extra_exist(``vehicle``, ``extraId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not yet documented.

====================================


explode_vehicle(``vehicle``, ``isAudible``, ``isInvisible``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Explode a vehicle

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``isAudible`` (``bool``) -- Whether the explosion is audible
* ``isInvisible`` (``bool``) -- Whether the explosion is invisible

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = scripting.spawn.spawn_vehicle(rage.gameplay.get_hash_key("ZENTORNO"), self.get_coords_infront(10), 30.0)
   rage.vehicle.explode_vehicle(vehicle, true, false)

====================================

get_all_vehicles()
^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not yet documented.

====================================

get_convertible_roof_state(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the state of the vehicle's convertible roof.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The roof state

  * For the list of roof states, see this: :doc:`things/roofstate`
  * ``0`` if not in a vehicle

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   roofState = rage.vehicle.get_convertible_roof_state(vehicle)
   system.log_debug("Vehicle's roof state is " .. roofState) --assuming the roof is closed, or you're on a bike

====================================

get_landing_gear_state(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the state of the vehicle's landing gear.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The gear state

* ``0`` - Down
* ``1`` - Raising
* ``3`` - Lowering 
* ``4`` - Up
* ``5`` - Broken


**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   gearState = rage.vehicle.get_landing_gear_state(vehicle)
   system.log_debug("Vehicle's gear state is " .. gearState)

================================

get_livery_name(``vehicle``, ``liveryIndex``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns vehicle livery name

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``liveryIndex`` (``int``) -- The livery index

**Returns:**

* ``string`` -- The livery name

**Example:**

.. note::

   Additionally, you can get localized livery name using ``get_label_text``

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   count = rage.vehicle.get_vehicle_livery_count(vehicle)
   for i = 0, count do
      liveryName = rage.vehicle.get_livery_name(vehicle, i)
      system.log_debug("Livery " .. i .. ": " .. liveryName)
   end

   -- or

   vehicle = self.get_vehicle()

   liveryIndex = rage.vehicle.get_vehicle_livery(vehicle)

   livery_name = rage.vehicle.get_livery_name(vehicle, liveryIndex)
   system.log_debug("Livery name: " .. livery_name)
   
   -- or

   vehicle = self.get_vehicle()

   liveryIndex = rage.vehicle.get_vehicle_livery(vehicle)

   livery_name = rage.vehicle.get_livery_name(vehicle, liveryIndex)

   livery_label = rage.vehicle.get_label_text(livery_name)

   system.log_debug("Livery name: " .. livery_label)

====================================

get_mod_slot_name(``vehicle``, ``modType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the name for the type of vehicle mod(Armour, engine etc)

.. note::

   Unrealiable. Sometimes returns "".

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The mod type

  * For the list of mod types, see this: :doc:`things/modTypes`

**Returns:**

* ``string`` -- The mod type name

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   modType = rage.vehicle.get_mod_slot_name(vehicle, 0)
   system.log_debug("Type: " .. modType)

====================================

get_mod_text_label(``vehicle``, ``modType``, ``modValue``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the label name for the type of vehicle mod(Armour, engine etc)

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The mod type

  * For the list of mod types, see this: :doc:`things/modTypes`
* ``modValue`` (``int``) -- The mod value

**Returns:**

* ``string`` -- The mod label name


**Example:**


.. note::

   Additionally, you can get localized mod name using ``get_label_text``

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   value = rage.vehicle.get_vehicle_mod(vehicle, 0) -- get spoiler installed
   modLabel = rage.vehicle.get_mod_text_label(vehicle, 0, value)
   system.log_debug("Spoiler: " .. modLabel)

====================================

get_num_vehicle_mods(``vehicle``, ``modType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of possible mod variations for the type of vehicle mod(Armour, engine etc)

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The mod type

  * For the list of mod types, see this: :doc:`things/modTypes`

**Returns:**

* ``int`` -- The number of mod variations

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   count = rage.vehicle.get_num_vehicle_mods(vehicle, 0) -- spoiler possible variations
   system.log_debug("Spoiler count: " .. count)

====================================

get_ped_in_vehicle_seat(``vehicle``, ``seat``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the Ped handle of the ped in the specified vehicle seat.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``seat`` (``int``) -- The seat ID

  * For the list of seat IDs, see this: :doc:`things/seattypes`
* ``p2`` (``int``) -- Unknown (unused)

**Returns:**

* ``Ped`` -- The ped handle

  * If no ped is in the seat, returns ``0``

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   ped = rage.vehicle.get_ped_in_vehicle_seat(vehicle, 0)
   system.log_debug("Ped in a right front seat: " .. ped)

====================================

get_vehicle_class(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the class of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The class of the vehicle

  * For vehicle classes, see this: :doc: `vehicleClasses`

**Example:**

.. note::

   Additionally, you can get localized class name using ``get_label_text``

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   class = rage.vehicle.get_vehicle_class(vehicle)
   className = rage.vehicle.get_label_text("VEH_CLASS_" .. tostring(class))
   system.log_debug("Vehicle class: " .. className)

====================================

get_vehicle_custom_primary_colour(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the custom primary colour of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``ColorRGB`` -- The custom primary colour

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   colour = rage.vehicle.get_vehicle_custom_primary_colour(vehicle)
   r = colour.r
   g = colour.g
   b = colour.b
   system.log_debug("Custom primary colour: " .. tostring(r) .. " " .. tostring(g) .. " " .. tostring(b))

====================================

get_vehicle_custom_secondary_colour(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the custom secondary colour of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``ColorRGB`` -- The custom secondary colour

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   colour = rage.vehicle.get_vehicle_custom_secondary_colour(vehicle)
   r = colour.r
   g = colour.g
   b = colour.b
   system.log_debug("Custom secondary colour: " .. tostring(r) .. " " .. tostring(g) .. " " .. tostring(b))

====================================

get_vehicle_doors_locked_for_player(``vehicle``, ``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns whether the vehicle doors are locked for the specified player.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``player`` (``Player``) -- The player handle

**Returns:**

* ``bool`` -- Whether the vehicle doors are locked

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   player = self.get_player()
   doorsLocked = rage.vehicle.get_vehicle_doors_locked_for_player(vehicle, player)
   system.log_debug("Vehicle doors locked: " .. tostring(doorsLocked)) -- 100% false if the vehicle is personal

====================================

get_vehicle_estimated_max_speed(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns max vehicle speed

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``float`` -- The estimated max speed of the vehicle

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   speed = rage.vehicle.get_vehicle_estimated_max_speed(vehicle)
   system.log_debug("Vehicle max speed: " .. tostring(speed))

====================================

get_vehicle_livery(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the livery index of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The livery index

  * ``-1`` means no livery

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   livery = rage.vehicle.get_vehicle_livery(vehicle)
   system.log_debug("Vehicle livery: " .. tostring(livery))

====================================

get_vehicle_livery_count(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of livery variations for the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The number of livery variations

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   count = rage.vehicle.get_vehicle_livery_count(vehicle)
   system.log_debug("Vehicle livery count: " .. tostring(count))

====================================

get_vehicle_max_number_of_passengers(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the maximum number of passengers for the vehicle.

.. note::

   This does not include a driver.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The maximum number of passengers

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   maxPassengers = rage.vehicle.get_vehicle_max_number_of_passengers(vehicle)
   system.log_debug("Vehicle max passengers: " .. tostring(maxPassengers))

====================================

get_vehicle_mod(``vehicle``, ``modType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the vehicle mod variation ID

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The mod type

  * For mod types, see this: :doc: `modTypes`

**Returns:**

* ``int`` -- The mod variation ID

  * ``-1`` means mod is stock

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   modValue = rage.vehicle.get_vehicle_mod(vehicle, 0) -- get spoiler installed
   system.log_debug("Vehicle engine mod: " .. tostring(modValue))

====================================

get_vehicle_model_number_of_seats(``modelHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of seats for the specified vehicle model.

**Parameters:**

* ``modelHash`` (``int``) -- The model hash

**Returns:**

* ``int`` -- The number of seats

**Example:**

.. code-block:: lua
   :linenos:

   modelHash = GetHashKey("ZENTORNO")
   seats = rage.vehicle.get_vehicle_model_number_of_seats(modelHash)
   system.log_debug("Vehicle seats: " .. tostring(seats)) -- 2

====================================

get_vehicle_number_of_passengers(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number of passengers for the vehicle, not including the driver.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The number of passengers

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   passengers = rage.vehicle.get_vehicle_number_of_passengers(vehicle)
   system.log_debug("Vehicle passengers: " .. tostring(passengers))

====================================

get_vehicle_number_plate_text(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the number plate text of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``string`` -- The number plate text

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   plate = rage.vehicle.get_vehicle_number_plate_text(vehicle)
   system.log_debug("Vehicle plate: " .. tostring(plate))

====================================

get_vehicle_roof_livery_count(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns a number of available rooftop liveries

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The number of available livery variations
  
  * ``-1`` if vehicle has no rooftop liveries available.

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   count = rage.vehicle.get_vehicle_roof_livery_count(vehicle)
   system.log_debug("Vehicle roof livery count: " .. tostring(count))


====================================

get_vehicle_wheel_type(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the wheel type of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The wheel type

  * For wheel types, see this: :doc: `wheelTypes`

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   wheelType = rage.vehicle.get_vehicle_wheel_type(vehicle)
   system.log_debug("Vehicle wheel type: " .. tostring(wheelType))

====================================

get_vehicle_window_tint(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the window tint color of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``int`` -- The window tint color

  * For window tint colors, see this: :doc: `windowTints`

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   tint = rage.vehicle.get_vehicle_window_tint(vehicle)
   system.log_debug("Vehicle window tint: " .. tostring(tint))

====================================

has_vehicle_phone_explosive_device(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle has a phone explosive device.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool``

  * ``true`` -- the vehicle has a phone explosive device
  * ``false`` -- the vehicle does not have a phone explosive device

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   hasDevice = rage.vehicle.has_vehicle_phone_explosive_device(vehicle)
   system.log_debug("Vehicle has explosive device: " .. tostring(hasDevice))

====================================

is_taxi_light_on(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the taxi light is on.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool`` -- ``true`` if the taxi light is on, ``false`` otherwise

  * ``true`` -- the taxi light is on
  * ``false`` -- the taxi light is off

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isOn = rage.vehicle.is_taxi_light_on(vehicle)
   system.log_debug("Taxi light is on: " .. tostring(isOn))

====================================

is_toggle_mod_on(``vehicle``, ``modType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle mod is turned on (xenon, for example)

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The mod type

  * For mod types, see this: :doc: `modTypes`

**Returns:**

* ``bool``

  * ``true`` -- the mod is turned on
  * ``false`` -- the mod is turned off

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   modType = 22 -- xenon
   isOn = rage.vehicle.is_toggle_mod_on(vehicle, modType)
   system.log_debug("Mod is on: " .. tostring(isOn))

====================================

is_vehicle_a_convertible(``vehicle``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle is a convertible.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``p1`` (``bool``) -- Unknown parameter

  * If ``false``, the function will only return true, when the roof is convertible while pressing ``INPUT_VEH_ROOF`` (roof switch button)
  * If ``true``, the function will always return true.

**Returns:**

* ``bool``

  * ``true`` -- the vehicle is a convertible
  * ``false`` -- the vehicle is not a convertible

====================================

get_is_vehicle_engine_running(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle engine is running.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool``

  * ``true`` -- the engine is running
  * ``false`` -- the engine is not running

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isRunning = rage.vehicle.get_is_vehicle_engine_running(vehicle)
   system.log_debug("Vehicle engine is running: " .. tostring(isRunning))

====================================

is_vehicle_extra_turned_on(``vehicle``, ``extraId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not yet documented.

====================================

is_vehicle_model(``vehicle``, ``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model specified is a vehicle model.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``model`` (``Hash``) -- The model hash

**Returns:**

* ``bool``

  * ``true`` -- the model is a vehicle model
  * ``false`` -- the model is not a vehicle model

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   model = rage.gameplay.get_hash_key("ZENTORNO")
   isModel = rage.vehicle.is_vehicle_model(vehicle, model) -- true
   system.log_debug("Vehicle model is: " .. tostring(isModel))

====================================

is_vehicle_neon_light_enabled(``vehicle``, ``index``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the neon light is enabled on the specified vehicle and side.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``index`` (``int``) -- The vehicle side index

  * ``0`` = Left
  * ``1`` = Right
  * ``2`` = Front
  * ``3`` = Back

**Returns:**

* ``bool``

  * ``true`` -- the neon light is enabled
  * ``false`` -- the neon light is not enabled

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isOn = rage.vehicle.is_vehicle_neon_light_enabled(vehicle, 0) -- left
   system.log_debug("Vehicle neon light is on: " .. tostring(isOn)) -- a stock car will always return false

====================================

is_vehicle_on_all_wheels(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle is on all wheels.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool``

  * ``true`` -- the vehicle is on all wheels
  * ``false`` -- the vehicle is not on all wheels

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isOnWheels = rage.vehicle.is_vehicle_on_all_wheels(vehicle)
   system.log_debug("Is vehicle on all wheels: " .. tostring(isOnWheel))

====================================

get_is_vehicle_primary_colour_custom(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not yet documented.

====================================

is_vehicle_rocket_boost_active(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle rocket boost is active.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool``

  * ``true`` -- the rocket boost is active
  * ``false`` -- the rocket boost is not active

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isActive = rage.vehicle.is_vehicle_rocket_boost_active(vehicle)
   system.log_debug("Rocket boost is active: " .. tostring(isActive))

====================================

get_is_vehicle_secondary_colour_custom(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This function is not yet documented.

====================================

is_vehicle_stopped(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle is stopped, not moving.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool``

  * ``true`` -- the vehicle is stopped
  * ``false`` -- the vehicle is not stopped

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isStopped = rage.vehicle.is_vehicle_stopped(vehicle)
   system.log_debug("Vehicle is stopped: " .. tostring(isStopped))


====================================

is_vehicle_stuck_on_roof(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the vehicle is stuck on the roof, upside down.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* ``bool``

  * ``true`` -- the vehicle is stuck on the roof
  * ``false`` -- the vehicle is not stuck on the roof

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   isStuck = rage.vehicle.is_vehicle_stuck_on_roof(vehicle)
   system.log_debug("Vehicle is stuck on roof: " .. tostring(isStuck))

====================================

modify_vehicle_top_speed(``vehicle``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the top speed of the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``value`` (``float``) -- The new top speed

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.modify_vehicle_top_speed(vehicle, 1000.0)

====================================

set_ambient_vehicle_range_multiplier_this_frame(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the density on vehicles that are pulling out of driveways and parking spots, crossroads too.

.. note::

   This function has to be called every frame. Use this in a looped function, or use add_task().

**Parameters:**

* ``value`` (``float``) -- The density multiplier

  * ``0.0`` = No cars
  * ``1.0`` = Normal density

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   function nocars()
      rage.vehicle.set_ambient_vehicle_range_multiplier_this_frame(0.0)
   end

   system.add_task("No Cars", "NC", -1, nocars)

====================================

set_convertible_roof(``vehicle``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extend or retract the roof of a convertible vehicle.

.. note::

   Seems to only extend the roof, not retract it.

   Has to be called every frame.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``p1`` (``bool``) -- Whether to extend or retract the roof (seems to be unused)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_convertible_roof(vehicle) -- Extend


====================================

set_heli_blades_full_speed(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the helicopter blades to full speed.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- assuming you're in a helicopter
   vehicle = self.get_vehicle()
   rage.vehicle.set_heli_blades_full_speed(vehicle)

====================================

set_heli_blades_speed(``vehicle``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the helicopter blades speed.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``speed`` (``float``) -- The speed of the blades (``0`` - ``100``)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   -- assuming you're in a helicopter

   vehicle = self.get_vehicle()
   rage.vehicle.set_heli_blades_speed(vehicle, 50.0) -- halfspeed 

====================================

set_parked_vehicle_density_multiplier_this_frame(``multiplier``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the density for parked vehicles.

.. note::

   This function has to be called every frame. Use this in a looped function, or use add_task().


**Parameters:**

* ``multiplier`` (``float``) -- The density multiplier

  * ``0.0`` = No cars parked
  * ``1.0`` = Normal density

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.vehicle.set_parked_vehicle_density_multiplier_this_frame(0.0) -- no cars

====================================

set_random_vehicle_density_multiplier_this_frame(``multiplier``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the density for random vehicles on the streets.

.. note::

   This function has to be called every frame. Use this in a looped function, or use add_task().


**Parameters:**

* ``multiplier`` (``float``) -- The density multiplier

  * ``0.0`` = No cars on the roads
  * ``1.0`` = Normal density

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.vehicle.set_random_vehicle_density_multiplier_this_frame(0.0) -- no cars

====================================

set_taxi_lights(``vehicle``, ``state``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the taxi lights for a vehicle.

.. note::

   Doesn't seem to work. 

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``state`` (``bool``)

  * ``true`` = On
  * ``false`` = Off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_taxi_lights(vehicle, true) -- taxi lights should be on now

====================================

set_vehicle_brake_lights(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the brake lights for a vehicle.

.. note::

   Doesn't seem to work. Should be used every frame.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``toggle`` (``bool``)

  * ``true`` = On
  * ``false`` = Off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   function lights()
      vehicle = self.get_vehicle()
      rage.vehicle.set_vehicle_brake_lights(vehicle, true)
      system.wait(-1)
   end

   parent = menu.add_parent("My Lua Script")
   menu.add_option("brake lights ON", "light", parent, lights)

====================================

set_vehicle_can_be_locked_on(``vehicle``, ``canBeLockedOn``, ``unk``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether a vehicle can be locked on.

.. note::

   Doesn't seem to work.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``canBeLockedOn`` (``bool``) -- Whether the vehicle can be locked on
* ``unk`` (``bool``) -- Unknown

**Returns:**

* None

====================================

set_vehicle_can_be_visibly_damaged(``vehicle``, ``state``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether the vehicle can be visibly damaged

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``state`` (``bool``) -- Whether the vehicle can be damaged

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_can_be_visibly_damaged(vehicle, false) -- vehicle can't be visibly damaged now

====================================

set_vehicle_custom_primary_colour(``vehicle``, ``r``, ``g``, ``b``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the primary custom colour for a vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``r`` (``int``) -- The red colour value
* ``g`` (``int``) -- The green colour value
* ``b`` (``int``) -- The blue colour value

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_custom_primary_colour(vehicle, 255, 0, 0) -- vehicle is now red

====================================

set_vehicle_custom_secondary_colour(``vehicle``, ``r``, ``g``, ``b``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the secondary custom colour for a vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``r`` (``int``) -- The red colour value
* ``g`` (``int``) -- The green colour value
* ``b`` (``int``) -- The blue colour value

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_custom_secondary_colour(vehicle, 0, 255, 0) -- secondary vehicle color is now green

====================================

set_vehicle_deformation_fixed(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle deformation to 0.

.. note::

   This does not repair a vehicle, only restore the texture to its original state.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_deformation_fixed(vehicle) -- vehicle deformation is now 0


====================================

set_vehicle_door_open(``vehicle``, ``door``, ``loose``, ``openInstantly``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a vehicle door to open.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``door`` (``int``) -- The door ID

  * You can find door IDs here: :doc:`things/doors`
* ``loose`` (``bool``) -- Whether the door is loose. In this case, the door won't close itself after a while.
* ``openInstantly`` (``bool``) -- Whether the door should open instantly.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_door_open(vehicle, 5, true, false) -- open the trunt

====================================

set_vehicle_doors_locked(``vehicle``, ``doorLockStatus``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle doors lock to a certain state.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``doorLockStatus`` (``int``) -- The door lock status

  * You can find door lock status here: :doc:`things/doors`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_doors_locked(vehicle, 1) -- vehicle doors are now unlocked

====================================

set_vehicle_doors_locked_for_all_players(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether the vehicle doors are locked for all players.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``toggle`` (``bool``) -- Whether the vehicle doors are locked for all players

  * ``true`` -- vehicle doors are locked for all players
  * ``false`` -- vehicle doors are not locked for all players

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_doors_locked_for_all_players(vehicle, true) -- vehicle doors are now locked for all players

====================================

set_vehicle_doors_locked_for_non_script_players(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets whether the vehicle doors are locked for non-script players.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``toggle`` (``bool``) -- Whether the vehicle doors are locked for non-script players

  * ``true`` -- vehicle doors are locked for non-script players
  * ``false`` -- vehicle doors are not locked for non-script players

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_doors_locked_for_non_script_players(vehicle, true) -- vehicle doors are now locked for non-script players

====================================

set_vehicle_doors_locked_for_player(``vehicle``, ``player``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lokcs or unlocks the vehicle doors for a certain player.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``player`` (``Player``) -- The player ID
* ``toggle`` (``bool``) -- Whether the vehicle doors are locked for the player

  * ``true`` -- vehicle doors are locked for the player
  * ``false`` -- vehicle doors are not locked for the player

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   player = self.get_player()
   rage.vehicle.set_vehicle_doors_locked_for_player(vehicle, player, true) -- vehicle doors are now locked for the self

====================================

set_vehicle_doors_locked_for_team(``vehicle``, ``team``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locks or unlocks the vehicle doors for a certain team.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``team`` (``int``) -- The team ID
* ``toggle`` (``bool``) -- Whether the vehicle doors are locked for the team

  * ``true`` -- vehicle doors are locked for the team
  * ``false`` -- vehicle doors are not locked for the team

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   team = self.get_player_team()
   rage.vehicle.set_vehicle_doors_locked_for_team(vehicle, team, false) -- vehicle doors are now unlocked for your team

====================================

set_vehicle_doors_shut(``vehicle``, ``closeInstantly``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Closes all vehicle doors.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``closeInstantly`` (``bool``) -- Whether the doors should close instantly.

  * ``true`` -- doors close instantly
  * ``false`` -- doors don't close instantly

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_doors_shut(vehicle, true) -- vehicle doors are now closed

====================================

set_vehicle_engine_health(``vehicle``, ``health``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle engine health.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``health`` (``float``) -- The engine health value

  * For health values, see this: :doc:`things/vehicleHealth`


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_engine_health(vehicle, -4000) -- vehicle engine is now broken

====================================

set_vehicle_engine_on(``vehicle``, ``value``, ``instantly``, ``disableAutoStart``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle engine is on.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``value`` (``bool``) -- Whether the engine is on
* ``instantly`` (``bool``) -- Whether the engine should be turned on instantly
* ``disableAutoStart`` (``bool``) -- Disable the engine's ability to autostart.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_engine_on(vehicle, false, false, true) -- vehicle engine is now false

====================================

set_vehicle_extra(``vehicle``, ``extraId``, ``disable``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: 

   This function is not yet documented.

====================================

set_vehicle_fixed(``vehicle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Repairs the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_fixed(vehicle) -- vehicle is now fixed

====================================

set_vehicle_forward_speed(``vehicle``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle forward speed (boost).

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``speed`` (``float``) -- The vehicle forward speed value

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_forward_speed(vehicle, 1000.0) -- vehicle forward speed is now 1000

====================================

set_vehicle_fullbeam(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Switches the vehicle's lights to fullbeam.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``toggle`` (``bool``) -- Toggle 

  * ``true`` -- vehicle lights are in fullbeam mode
  * ``false`` -- vehicle lights are in normal mode


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_fullbeam(vehicle, true) -- vehicle lights are now in fullbeam mode

====================================

set_vehicle_has_been_owned_by_player(``vehicle``, ``owned``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle as owned by the played

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``owned`` (``bool``) -- Whether the vehicle is owned by the player

  * ``true`` -- vehicle is owned by the player
  * ``false`` -- vehicle is not owned by the player

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_has_been_owned_by_player(vehicle, true) -- vehicle is now flagged as owned by the player

====================================

set_vehicle_indicator_lights(``vehicle``, ``turnSignal``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets vehicle's indicator lights on/off

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``turnSignal`` (``int``) -- The turn signal to set

  * ``1`` -- Left turn signal
  * ``0`` -- Right turn signal
* ``toggle`` (``bool``) -- Toggle 
   
  * ``true`` -- turn signal is on
  * ``false`` -- turn signal is off

**Returns:**

* None

====================================


set_vehicle_livery(``vehicle``, ``livery``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle livery.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``livery`` (``int``) -- The livery ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   livNum = rage.vehicle.get_vehicle_livery_count()
   livery = math.random(livNum)
   rage.vehicle.set_vehicle_livery(vehicle, livery) -- Random livery set

====================================

set_vehicle_mod(``vehicle``, ``modType``, ``modIndex``, ``customTires``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modifies the vehicle.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The modification type

  * For modification types, see this: :doc:`things/modTypes`
* ``modIndex`` (``int``) -- The modification variation
* ``customTires`` (``bool``) -- Whether the mod is a custom tire

**Returns:**

* None

**Example:**

.. note::

   There's no mod variation list. Test, explore.

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_mod(vehicle, 0, 2, false) -- Vehicle spoiler variation 2 is now installed.

====================================

set_vehicle_neon_light_enabled(``vehicle``, ``index``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles neon light on/off

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``index`` (``int``) -- The vehicle side index

  * ``0`` = Left
  * ``1`` = Right
  * ``2`` = Front
  * ``3`` = Back
* ``toggle`` (``bool``) -- Toggle

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_neon_light_enabled(vehicle, 0, true) -- Left neon light is now on

====================================

set_vehicle_number_plate_text(``vehicle``, ``plateText``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle number plate text.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``plateText`` (``string``) -- The number plate text

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_number_plate_text(vehicle, "JOHN117") -- Vehicle number plate is now "JOHN117"

====================================

set_vehicle_on_ground_properly(``vehicle``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a vehicle on the ground on all wheels.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``p1`` (``float``) -- Unknown. Set to ``5.0``.

**Returns:**

* ``bool`` -- Whether the vehicle was set on the ground succesfully

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_on_ground_properly(vehicle, 5.0) -- Vehicle is now on the ground

====================================

set_vehicle_out_of_control(``vehicle``, ``killDriver``, ``explodeOnImpact``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle out of control.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``killDriver`` (``bool``) -- Whether to kill the driver
* ``explodeOnImpact`` (``bool``) -- Whether to explode the vehicle on impact

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_out_of_control(vehicle, true, true) -- Vehicle is now out of control with dead driver, set to explode on impact.

====================================

set_vehicle_parachute_active(``vehicle``, ``active``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's parachute active. Ruiner 2000 is the only vehicle with the parachute.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``active`` (``bool``) -- Whether the parachute is active

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_parachute_active(vehicle, true) -- Parachute is now active

====================================

set_vehicle_parachute_model(``vehicle``, ``modelHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets parachute model for a vehicle

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modelHash`` (``Hash``) -- The model hash

  * ``sr_prop_specraces_para_s_01``
  * ``imp_prop_impexp_para_s`` (SecuroServ; Default)
  * Plus, many more props can be used as vehicle parachutes, like umbrellas (``prop_beach_parasol_03``)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_parachute_model(vehicle, rage.gameplay.get_hash_key("prop_beach_parasol_03")) -- Parachute is now an umbrella

====================================

set_vehicle_reduce_grip(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's grip to be significantly reduced.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``toggle`` (``bool``) -- Whether to reduce the grip or not

  * ``true`` = Reduce the grip
  * ``false`` = Don't reduce the grip

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_reduce_grip(vehicle, true) -- Vehicle grip is now reduced

====================================

set_vehicle_rocket_boost_active(``vehicle``, ``active``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's rocket boost active.

.. note::

   Can only be used on the vehicles with rocket boosters.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``active`` (``bool``) -- Boost toggle

  * ``true`` = Boost is active
  * ``false`` = Boost is inactive

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_rocket_boost_active(vehicle, true) -- Rocket boost is now active

====================================

set_vehicle_rocket_boost_percentage(``vehicle``, ``percentage``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's rocket boost fill percentage.
.. note::

   Can only be used on the vehicles with rocket boosters.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``percentage`` (``float``) -- The percentage of boost "progress"

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_rocket_boost_percentage(vehicle, 0.5) -- Rocket boost is now 50% filled

====================================

set_vehicle_rocket_boost_refill_time(``vehicle``, ``seconds``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's rocket boost refill time.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``seconds`` (``float``) -- Time in seconds

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_rocket_boost_refill_time(vehicle, 0.5) -- Rocket boost will refill in a half a second

====================================

set_vehicle_steer_bias(``vehicle``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locks the vehicle's steering to the desired angle.

.. note::

   Needs to be called every frame.

   Steering is unlocked the moment the function stops being called on the vehicle.  

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``value`` (``float``) -- The steering angle

  * ``-1.0`` -- full right  
  * ``0.0`` -- centered steering  
  * ``1.0`` -- full left  


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_steer_bias(vehicle, 1.0) -- Vehicle steering set to full left.

====================================

set_vehicle_timed_explosion(``vehicle``, ``ped``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a timed explosion for a vehicle

.. note::

   Doesn't seem to work.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``ped`` (``Ped``) -- The ped ID, probably driver
* ``toggle`` (``bool``) -- Toggle timed explosion

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_timed_explosion(vehicle, self.get_ped(), true)

====================================

set_vehicle_undriveable(``vehicle``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets a vehicle as undriveable.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``toggle`` (``bool``) -- Toggle

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_undriveable(vehicle, true) -- Vehicle is now undriveable

====================================

set_vehicle_wheel_type(``vehicle``, ``wheelType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's wheel type.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``wheelType`` (``int``) -- The wheel type

  * For wheel types, see :doc:`things/wheelTypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_wheel_type(vehicle, 0) -- vehicle now has sport wheel type

====================================

set_vehicle_window_tint(``vehicle``, ``tint``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's window tint.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``tint`` (``int``) -- The tint ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.set_vehicle_window_tint(vehicle, 6) -- vehicle now has green tint

====================================

start_vehicle_horn(``vehicle``, ``duration``, ``mode``, ``forever``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sounds the horn for the specified vehicle.  

.. note::

   If a player is in the vehicle, it will only sound briefly. 

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``duration`` (``float``) -- The duration of the horn in seconds
* ``mode`` (``Hash``) -- The horn mode

  * ``NORMAL`` -- Normal horn
  * ``HELDDOWN``
  * ``0``
* ``forever`` (``bool``) -- If ``true``, the horn will sound forever

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.start_vehicle_horn(vehicle, 10.0, rage.gameplay.get_hash_key("NORMAL"), false) -- vehicle now sounds its horn for 10 seconds

====================================

toggle_vehicle_mod(``vehicle``, ``modType``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles a vehicle mod on/off.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``modType`` (``int``) -- The mod type

  * For mod types, see :doc:`things/modTypes`
* ``toggle`` (``bool``) -- Toggle

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   vehicle = self.get_vehicle()
   rage.vehicle.toggle_vehicle_mod(vehicle, 22, true) -- xenon headlights on

====================================

set_vehicle_cheat_power_increase(``vehicle``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the vehicle's torque value.

.. note::

   Negative values will cause the vehicle to go backwards instead of forwards while accelerating.

   This has to be called every frame.

**Parameters:**

* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``value`` (``float``) -- The torque value

  * Less than ``1.0`` -- Decreased torque
  * ``1.0`` -- Default torque
  * More than ``1.0`` -- Increased torque


**Returns:**

====================================

.. _entityNSR:

Entity namespace
----------------------

This namespace contains entity-related game functions.

================================

apply_force_to_entity(``entity``, ``forceFlags``, ``x``, ``y``, ``z``, ``offX``, ``offY``, ``offZ``, ``boneIndex``, ``isDirectionRel``, ``ignoreUpVec``, ``isForceRel``, ``p12``, ``p13``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Applies a force to the specified entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity handle
* ``forceFlags`` (``int``) -- Commonly used values:

  * ``MinForce`` = ``0``
  * ``MaxForceRot`` = ``1``
  * ``MinForce2`` = ``2``
  * ``MaxForceRot2`` = ``3``
  * ``ForceNoRot`` = ``4``
  * ``ForceRotPlusForce`` = ``5``

* ``x`` (``float``) -- Force amount (X)
* ``y`` (``float``) -- Force amount (Y)
* ``z`` (``float``) -- Force amount (Z)
* ``offX`` (``float``) -- Rotation/offset force (X)
* ``offY`` (``float``) -- Rotation/offset force (Y)
* ``offZ`` (``float``) -- Rotation/offset force (Z)
* ``boneIndex`` (``int``) -- Entity bone index (Often ``0``) 
* ``isDirectionRel`` (``bool``) -- Vector defined in local (body-fixed) coordinate frame (Usually ``false``)
* ``ignoreUpVec`` (``bool``) -- Usually ``true``
* ``isForceRel`` (``bool``)

  * ``true`` -- Force Returns multiplied with the objects mass and different objects will have the same acceleration
  * ``false`` -- Otherwise

* ``p12`` (``bool``) -- Unknown, usually ``false``
* ``p13`` (``bool``) -- Unknown, usually ``true``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.apply_force_to_entity(entity, 1, 10, 10, 10, 0, 0, 0, 0, false, true, true, false, true)

================================

attach_entity_to_entity(``entity1``, ``entity2``, ``boneIndex``, ``xPos``, ``yPos``, ``zPos``, ``xRot``, ``yRot``, ``zRot``, ``p9``, ``useSoftPinning``, ``collision``, ``isPed``, ``vertexIndex``, ``fixedRot``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attach an entity to the specified entity.

**Parameters:**

* ``entity1`` (``Entity``) -- The entity handle.
* ``entity2`` (``Entity``) -- Entity ID to attach entity1 with.
* ``boneIndex`` (``int``) -- This is different to boneID, use ``get_ped_bone_index`` to get the index from the ID. use the index for attaching to specific bones. entity1 will be attached to the center of entity2 if bone index given doesn't correspond to bone indexes for that entity type.
* ``xPos`` (``float``) -- X-axis offset from the center of entity2.
* ``yPos`` (``float``) -- Y-axis offset from the center of entity2.
* ``zPos`` (``float``) -- Z-axis offset from the center of entity2.
* ``xRot`` (``float``) -- X-axis rotation.
* ``yRot`` (``float``) -- Y-axis rotation.
* ``zRot`` (``float``) -- Z-axis rotation.
* ``p9`` (``bool``) -- Unknown. Does not seem to have any effect.
* ``useSoftPinning`` (``bool``) -- If set to ``false`` attached entity will not detach when fixed.
* ``collision`` (``bool``) -- Controls collision between the two entities
  
  * ``true`` -- Collision enabled
  * ``false`` -- Collision disabled

* ``isPed`` (``bool``) -- Pitch doesnt work when ``false`` and roll will only work on negative numbers (only peds)
* ``vertexIndex`` (``int``) -- The order in which the rotation is applied.
* ``fixedRot`` (``bool``) -- If ``false``, it ignores entity vector.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   entity2 = lobby.get_player_ped(lobby.get_host())

   boneIndex = get_ped_bone_index(entity2, 1)

   rage.entity.attach_entity_to_entity(entity, entity2, boneIndex, 10, 10, 10, 1, 1, 0, false, true, true, 1, true)

================================

delete_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes a specified entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.delete_entity(entity)

================================

detach_entity(``entity``, ``dynamic``, ``collision``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Detaches a specified entity, with toggable options.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``dynamic`` (``bool``) -- no effect
* ``collision`` (``bool``)

  * ``true`` -- both entities won't collide with each other until the distance between is 4 meters or more. (may not work with some entities)
  * ``false`` -- entities will collide with each other.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.detach_entity(entity, false, true)

================================

does_entity_have_drawable(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has a drawable (weapon?).

.. note::

   Seems to be always returning 0 no matter what the entity is or does it have a weapon (could be even a car, still ``true``.)

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity drawable (weapon?) status

  * ``true`` -- Entity has a drawable weapon (always?)
  * ``false`` -- Entity does not have a drawable weapon

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.does_entity_have_drawable(entity)

   system.log_debug(tostring(data))

================================

does_entity_have_physics(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has physics enabled.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity physics status

  * ``true`` -- Entity has physics enabled
  * ``false`` -- Entity does not have physics enabled

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.does_entity_have_physics(entity)
   system.log_debug(tostring(data))

================================

freeze_entity_position(``entity``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles freeze entity position.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Freeze entity position on
  * ``false`` -- Freeze entity position off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.freeze_entity_position(entity, true)

================================

get_entity_attached_to(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity that this entity is attached to.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``Entity`` -- The attached entity handle. ``0`` returned if the entity is not attached.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_attached_to(entity)

   system.log_debug(tostring(data))

================================

get_entity_bone_index_by_name(``entity``, ``boneName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity bone ID by name.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``boneName`` (``string``) -- Bone identifier

  * You can find out more about bones here: :ref:`bones`

**Returns:**

* ``int`` -- The index of the bone.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_bone_index_by_name(entity, "SKEL_L_Forearm")

   system.log_debug(tostring(data))

================================

get_entity_coords(``entity``, ``alive``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current coordinates for a specified entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``alive`` (``bool``) -- Checks whether an entity is alive

  * ``true`` -- Entity is alive (optional)
  * ``false`` -- Entity is dead

**Returns:**

* ``Vector3`` -- The current entity coordinates.

**Example:**

.. code-block:: lua
   :linenos:

   coords = rage.entity.get_entity_coords(self.get_ped())
   system.log_debug(tostring(coords.x) .. " " .. tostring(coords.y) .. " " .. tostring(coords.z))



================================

get_entity_forward_vector(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's forward vector.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``Vector3`` -- The forward vector. ``X``, ``Y`` and ``Z`` range from ``-1`` to ``1``.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_forward_vector(entity)

   system.log_debug(tostring(data))

================================

get_entity_heading(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's heading.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``float`` -- The entity's heading. 

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_heading(entity)

   system.log_debug(tostring(data))

================================

get_entity_physics_heading(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's physics heading.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``float`` -- The entity's physics heading. 

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_physics_heading(entity)

   system.log_debug(tostring(data))

================================

get_entity_pitch(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's pitch.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``float`` -- The entity's pitch.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_pitch(entity)

   system.log_debug(tostring(data))

================================

get_entity_population_type(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's population type.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``int`` -- the entity's population type

  * ``POPTYPE_UNKNOWN`` = ``0``
  * ``POPTYPE_RANDOM_PERMANENT`` = ``1``
  * ``POPTYPE_RANDOM_PARKED`` = ``2``
  * ``POPTYPE_RANDOM_PATROL`` = ``3``
  * ``POPTYPE_RANDOM_SCENARIO`` = ``4``
  * ``POPTYPE_RANDOM_AMBIENT`` = ``5``
  * ``POPTYPE_PERMANENT`` = ``6``
  * ``POPTYPE_MISSION`` = ``7``
  * ``POPTYPE_REPLAY`` = ``8``
  * ``POPTYPE_CACHE`` = ``9``
  * ``POPTYPE_TOOL`` = ``10``
**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_population_type(entity)

   system.log_debug(tostring(data))

================================

get_entity_roll(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's roll.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``float`` -- The entity's roll


**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_roll(entity)

   system.log_debug(tostring(data))

================================

get_entity_rotation(``entity``, ``rotationOrder``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity rotation.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``rotationOrder`` (``int``) -- The order yaw, pitch and roll is applied. Usually ``2``.

**Returns:**

* ``Vector3`` -- A vector where the Z coordinate is the yaw.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rot = rage.entity.get_entity_rotation(entity, 2)

   system.log_debug(tostring(rot.x) .. " " .. tostring(rot.y) .. " " .. tostring(rot.z))

================================

get_entity_rotation_velocity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity rotation velocity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``Vector3`` -- A vector where the Z coordinate is the rotation velocity.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rot = rage.entity.get_entity_rotation_velocity(entity, 2)
   
   system.log_debug(tostring(rot.x) .. " " .. tostring(rot.y) .. " " .. tostring(rot.z))

================================

get_entity_speed(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's speed.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``float`` -- The entity's speed

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.get_entity_speed(entity)

   system.log_debug(tostring(data))

================================

get_entity_submerged_level(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity's submerged level.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``float`` -- The entity's submerged level

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.get_entity_submerged_level(entity)
   system.log_debug(tostring(data))

================================

get_entity_type(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity type.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``int`` -- The entity type ID as following:

  * ``0`` = no entity
  * ``1`` = ped
  * ``2`` = vehicle
  * ``3`` = object

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.get_entity_type(entity)

   system.log_debug(tostring(data))

================================

get_entity_velocity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the entity velocity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``Vector3`` -- A vector where the Z coordinate is the velocity.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.get_entity_velocity(entity)

   system.log_debug(tostring(data.x) .. " " .. tostring(data.y) .. " " .. tostring(data.z))

================================

has_entity_been_damaged_by_any_object(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has been damaged by any object.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- The entity damage status
  
  * ``true`` -- Entity has been damaged by an object
  * ``false`` -- Entity has not been damaged by an object

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.has_entity_been_damaged_by_any_object(entity)
   system.log_debug(tostring(data))

================================

has_entity_been_damaged_by_any_ped(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has been damaged by any ped.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- The entity damage status
  
  * ``true`` -- Entity has been damaged by a ped
  * ``false`` -- Entity has not been damaged by a ped

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   data = rage.entity.has_entity_been_damaged_by_any_ped(entity)

   system.log_debug(tostring(data))

================================

has_entity_been_damaged_by_any_vehicle(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has been damaged by any vehicle.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity damage status
  
  * ``true`` -- Entity has been damaged by a vehicle
  * ``false`` -- Entity has not been damaged by a vehicle

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.has_entity_been_damaged_by_any_vehicle(entity)

   system.log_debug(tostring(data))

================================

has_entity_been_damaged_by_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has been damaged by another entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity damage status
  
  * ``true`` -- Entity has been damaged by another entity
  * ``false`` -- Entity has not been damaged by another entity

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.has_entity_been_damaged_by_entity(entity)
   system.log_debug(tostring(data))

================================

has_entity_collided_with_anything(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity has collided with anything.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity collision status
  
  * ``true`` -- Entity has collided with anything
  * ``false`` -- Entity has not collided with anything

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.has_entity_collided_with_anything(entity)

   system.log_debug(tostring(data))

================================

is_an_entity(``handle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an ScrHandle is an entity.

**Parameters:**

* ``handle`` (``ScrHandle``) -- The handle ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- The ScrHandle is an entity
  * ``false`` -- The ScrHandle is not an entity

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_an_entity(entity)

   system.log_debug(tostring(data))

================================

is_entity_a_ped(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is a ped.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is a ped
  * ``false`` -- Entity is not a ped

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_a_ped(entity)

   system.log_debug(tostring(data))


================================

is_entity_a_vehicle(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is a vehicle.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is a vehicle
  * ``false`` -- Entity is not a vehicle

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_a_vehicle(entity)

   system.log_debug(tostring(data))

================================

is_entity_an_object(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is an object.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is an object
  * ``false`` -- Entity is not an object

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_an_object(entity)

   system.log_debug(tostring(data))

================================

is_entity_attached(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is attached to anything.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is attached
  * ``false`` -- Entity is not attached

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_attached(entity)

   system.log_debug(tostring(data))

================================

is_entity_dead(``entity``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is dead.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``p1`` (``bool``) -- Unknown

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is dead
  * ``false`` -- Entity is alive

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_dead(entity, true)

   system.log_debug(tostring(data))

================================

is_entity_in_air(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is in air.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is in air
  * ``false`` -- Entity is not in air

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_in_air(entity)

   system.log_debug(tostring(data))


================================

is_entity_in_water(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is in water.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is in water
  * ``false`` -- Entity is not in water

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_in_water(entity)

   system.log_debug(tostring(data))

================================

is_entity_in_zone(``entity``, ``zone``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is in a specified zone

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``zone`` (``string``) -- The zone name

  * You can read more about zone names here: :doc:`things/zones`

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is in the specified zone
  * ``false`` -- Entity is not in the specified zone

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_in_zone(entity, "AirP")

   system.log_debug(tostring(data))


================================

is_entity_on_fire(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is on fire.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is on fire
  * ``false`` -- Entity is not on fire

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_on_fire(entity)

   system.log_debug(tostring(data))

================================

is_entity_static(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is static.

.. note::

   A static ped will not react to native functions like ``rage.entity.apply_force_to_entity`` or ``rage.entity.set_entity_velocity``. The only way to make them react to something is to ragdoll them or use ``rage.ped.clear_ped_tasks_immediately``.
   Static peds include almost all far-away peds, beach-combers, peds in certain scenarios, peds crossing a crosswalk, peds walking to get back into their cars, and others.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is static
  * ``false`` -- Entity is not static

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_static(entity)

   system.log_debug(tostring(data))


================================

is_entity_upright(``entity``, ``angle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is upright a specified angle.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``angle`` (``float``) -- The angle value

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is upright at the specified angle
  * ``false`` -- Entity is not upright at the specified angle

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   data = rage.entity.is_entity_upright(entity, 0.0)

   system.log_debug(tostring(data))

================================

is_entity_visible(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an entity is visible.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``bool`` -- Entity status
  
  * ``true`` -- Entity is visible
  * ``false`` -- Entity is not visible

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   system.log_debug(tostring(rage.entity.is_entity_visible(entity)))

================================

reset_entity_alpha(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets given entity alpha.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.reset_entity_alpha(entity)

================================

set_entity_alpha(``entity``, ``alphaLevel``, ``skin``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the entity's alpha level.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``alphaLevel`` (``int``) -- The alpha level ranges from ``0`` to ``255``, but changes occur every 20% (every 51).
* ``skin`` (``bool``) -- Whether or not to change the alpha of the entity's skin.

  * ``true`` -- Change alpha of the entity's skin
  * ``false`` -- Do not change alpha of the entity's skin

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_alpha(entity, 51, false)

================================

set_entity_as_mission_entity(``entity``, ``p1``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the specified entity (ped, vehicle or object) persistent. Persistent entities will not automatically be removed by the engine.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``p1`` (``bool``) -- Unknown. Doesn't seem to do anything.
* ``p2`` (``bool``) -- Unknown. Doesn't seem to do anything.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_as_mission_entity(entity)

================================

set_entity_as_no_longer_needed(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Marks the specified entity (ped, vehicle or object) as no longer needed.  

.. note::

   Entities marked as no longer needed, will be deleted as the engine sees fit.  


**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``xPos`` (``float``) -- The X coordinate
* ``yPos`` (``float``) -- The Y coordinate
* ``zPos`` (``float``) -- The Z coordinate
* ``xAxis`` (``bool``) -- Toggle X axis on/off
* ``yAxis`` (``bool``) -- Toggle Y axis on/off
* ``zAxis`` (``bool``) -- Toggle Z axis on/off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_as_no_longer_needed(entity)

================================

set_entity_heading(``entity``, ``heading``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the heading of an entity in degrees also known as "Yaw".

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``xPos`` (``float``) -- The heading in degrees.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_heading(entity, 90)

================================

set_entity_lights(``entity``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles entity's lights on/off.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``toggle`` (``bool``) -- Toggle
  
  * ``true`` -- Lights on
  * ``false`` -- Lights off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_lights(entity, true)

================================

set_entity_max_speed(``entity``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the entity's max speed.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``speed`` (``float``) -- The max speed to set for the entity

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_max_speed(entity, 250)

================================

set_entity_no_collision_entity(``entity1``, ``entity1``, ``thisFrameOnly``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets disabled collision between two entities.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``speed`` (``Entity``) -- The max speed to set for the entity
* ``thisFrameOnly`` (``bool``) -- Decides when to disable the collision

  * ``true`` -- Disabled until it is turned back on
  * ``false`` -- Disabled just this frame

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   entity2 = lobby.get_player_ped(lobby.get_host())

   rage.entity.set_entity_no_collision_entity(entity, entity2, true)

================================

set_entity_rotation(``entity``, ``pitch``, ``roll``, ``yaw``, ``rotationOrder``, ``p5``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the entity's rotation with customizable options.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``pitch`` (``float``) -- Rotation pitch
* ``roll`` (``float``) -- Rotation roll
* ``yaw`` (``float``) -- Rotation yaw
* ``rotationOrder`` (``int``) -- Rotation order
* ``p5`` (``bool``) -- Unknown, usually set to ``true``

.. note::

   What you use for rotationOrder when setting must be the same as rotationOrder when getting the rotation. 
   For the most part R* uses 1 or 2 as the order, overall value ranges from 0 to 5.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_rotation(entity, 10, 2, 5, 1)

================================

set_entity_velocity(``entity``, ``x``, ``y``, ``z``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the entity velocity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``x`` (``float``) -- The ``X`` vector coordinate
* ``y`` (``float``) -- The ``Y`` vector coordinate
* ``z`` (``float``) -- The ``Z`` vector coordinate
 
  * Note that ``z`` is "up and down" with positive numbers encouraging upwards movement.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_velocity(entity, 420.82, 69.53, 58, true, true, true)

================================

set_entity_visible(``entity``, ``toggle``, ``unk``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggles the visibility of a given entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID
* ``toggle`` (``bool``) -- Whether or not the entity will be visible
  
  * ``true`` -- Entity is visible
  * ``false`` -- Entity is not visible

* ``unk`` (``bool``) -- Always 0 in scripts

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.entity.set_entity_visible(entity, true)

================================

get_entity_model(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the model hash of the given entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity ID

**Returns:**

* ``Hash`` -- The model hash

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   model = rage.entity.get_entity_model(entity)
   freemodeModel = rage.gameplay.get_hash_key("mp_f_freemode_01")

   if model == freemodeModel then
      system.log_debug("This entity has a freemode model")
   end

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

Gets ped max ammo for a weapon.

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

   rage.weapon.get_max_ammo(lobby.get_player_ped(lobby.get_host()), rage.gameplay.get_hash_key("weapon_microsmg")) -- Gives session host a fully loaded MicroSMG

================================

get_ped_ammo_type_from_weapon(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets ammo type from a specific weapon of a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``Hash`` -- Ammo type hash

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.get_ped_ammo_type_from_weapon(ped, rage.gameplay.get_hash_key("weapon_microsmg")) -- Returns ammo type from session's host MicroSMG

================================

get_ped_weapon_tint_index(``ped``, ``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets weapon tint ID from a ped.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``int`` -- Weapon tint ID

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.get_ped_weapon_tint_index(ped, rage.gameplay.get_hash_key("weapon_microsmg")) -- Returns weapon tint ID from session's host MicroSMG

================================

get_ped_weapon_tint_count(``weaponHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets weapon tint count.

**Parameters:**

* ``weaponHash`` (``Hash``) -- Weapon `Whash`_ 
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* ``int`` -- Weapon tint count

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())

   rage.weapon.get_ped_weapon_tint_count(rage.gameplay.get_hash_key("weapon_microsmg")) -- Returns weapon tint count from session's host MicroSMG

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
  * ``false`` -- Don't equip
  
.. _Whash: https://wiki.rage.mp/index.php?title=Weapons

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   
   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

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
   
   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

   rage.weapon.give_delayed_weapon_to_ped(ped, weapon, rage.gameplay.get_hash_key("COMPONENT_MICROSMG_CLIP_02")) -- Gives extended clip component to session host's MicroSMG

================================

has_ped_got_weapon(``ped``, ``weaponHash``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a ped has got a weapon.

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
   
   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

   rage.weapon.has_ped_got_weapon(ped, weapon, true) -- Checks whether the session host has got MicroSMG

================================

has_ped_got_weapon_component(``ped``, ``weaponHash``, ``componentHash``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a ped's weapon has got a component.

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
   
   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

   rage.weapon.has_ped_got_weapon_component(ped, weapon, rage.gameplay.get_hash_key("COMPONENT_MICROSMG_CLIP_02")) -- Checks whether the session host's MicroSMG has got Extended Clip

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

   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

   rage.weapon.remove_weapon_component_from_ped(ped, weapon, rage.gameplay.get_hash_key("COMPONENT_MICROSMG_CLIP_02")) -- Removes Extended Clip from session host's MicroSMG

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

   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

   rage.weapon.remove_weapon_from_ped(ped, weapon) -- Removes MicroSMG from session host

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

   weapon = rage.gameplay.get_hash_key("weapon_microsmg")

   rage.weapon.set_ped_ammo(ped, weapon, 100, true)

================================

set_ped_ammo_by_type(``ped``, ``ammoTypeHash``, ``ammo``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set ped ammo by type.

.. note::

   This function is still in development.

**Parameters:**

* ``ped`` (``Ped``) -- The ped
* ``ammoTypeHash`` (``Hash``) -- Weapon ammo hash

  * You can read more about ammo types here: :doc:`things/ammotypes`
* ``ammo`` (``int``) -- Ammo Type


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = lobby.get_player_ped(lobby.get_host())
   self = lobby.get_player_ped(self.get_ped)

   ammoType = rage.weapon.get_ped_ammo_type_from_weapon(ped, rage.gameplay.get_hash_key("weapon_microsmg")) -- Get ammo type from session host's MicroSMG

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

   tint = rage.weapon.get_ped_weapon_tint_index(ped, rage.gameplay.get_hash_key("weapon_microsmg")) -- Returns weapon tint ID from session's host MicroSMG

   rage.weapon.set_ped_weapon_tint_index(self, rage.gameplay.get_hash_key("weapon_microsmg"), tint) -- Sets self weapon tint

================================

.. _streaming:

Streaming namespace
----------------------

This namespace contains ui-related game functions.

================================

has_anim_dict_loaded(``animDict``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an animation dictionary is loaded.

**Parameters:**

* ``animDict`` (``string``) -- Animation dictionary

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* ``bool`` -- Animation dictionary status
  
  * ``true`` -- Animation dictionary is loaded
  * ``false`` -- Animation dictionary is not loaded

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.streaming.has_anim_dict_loaded("move_f@injured")

   system.log_debug(tostring(data))

================================

has_anim_set_loaded(``animSet``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether an animation set is loaded.

**Parameters:**

* ``animSet`` (``string``) -- Animation set

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* ``bool`` -- Animation set status
  
  * ``true`` -- Animation set is loaded
  * ``false`` -- Animation set is not loaded

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.streaming.has_anim_set_loaded("idle_intro")

   system.log_debug(tostring(data))

================================

has_model_loaded(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a specified model has loaded into memory.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is loaded
  * ``false`` -- Model is not loaded

**Example:**

.. code-block:: lua
   :linenos:

   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.has_model_loaded(hashKey)

   system.log_debug(tostring(data))

================================

has_named_ptfx_asset_loaded(``fxName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a particles effect is loaded.

**Parameters:**

* ``fxName`` (``string``) -- Effect name

**Returns:**

* ``bool`` -- Effect status
  
  * ``true`` -- Effect is loaded
  * ``false`` -- Effect is not loaded

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.streaming.has_named_ptfx_asset_loaded("blood_stab")

   system.log_debug(tostring(data))

================================

is_this_model_a_bicycle(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a bicycle.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a bicycle
  * ``false`` -- Model is not a bicycle

**Example:**

.. code-block:: lua
   :linenos:

   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_bicycle(hashKey)

   system.log_debug(tostring(data))

================================

is_this_model_a_bike(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a bike.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a bike
  * ``false`` -- Model is not a bike

**Example:**

.. code-block:: lua
   :linenos:

   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_bike(hashKey)

   system.log_debug(tostring(data))

================================

is_this_model_a_boat(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a boat.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a boat
  * ``false`` -- Model is not a boat

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_boat(hashKey)

   system.log_debug(tostring(data))

================================

is_this_model_a_car(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a car.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a car
  * ``false`` -- Model is not a car

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_car(hashKey)

   system.log_debug(tostring(data)) -- Returns true

================================

is_this_model_a_heli(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a helicopter.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a helicopter
  * ``false`` -- Model is not a helicopter

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_heli(hashKey)

   system.log_debug(tostring(data))

================================

is_model_a_ped(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a ped.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a ped
  * ``false`` -- Model is not a ped

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_model_a_ped(hashKey)

   system.log_debug(tostring(data))

================================

is_this_model_a_plane(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a plane.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a plane
  * ``false`` -- Model is not a plane

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_plane(hashKey)

   system.log_debug(tostring(data))

================================

is_this_model_a_quadbike(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a quadbike.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a quadbike
  * ``false`` -- Model is not a quadbike

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_quadbike(hashKey)

   system.log_debug(tostring(data))

================================

is_this_model_a_train(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a train.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a train
  * ``false`` -- Model is not a train

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_this_model_a_train(hashKey)

   system.log_debug(tostring(data))

================================

is_model_a_vehicle(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is a vehicle.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is a vehicle
  * ``false`` -- Model is not a vehicle

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_model_a_vehicle(hashKey)

   system.log_debug(tostring(data))

================================

is_model_in_cdimage(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the model is in cdimage (rpf).

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is in cdimage
  * ``false`` -- Model is not in cdimage

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   rage.streaming.is_model_in_cdimage(hashKey)

================================

is_model_valid(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the specified model exists in the game.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* ``bool`` -- Model status
  
  * ``true`` -- Model is valid
  * ``false`` -- Model is not valid

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   data = rage.streaming.is_model_valid(hashKey)

   system.log_debug(tostring(data))

================================

remove_anim_dict(``animDict``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the animation dictionary.

**Parameters:**

* ``animDict`` (``string``) -- Animation dictionary

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.remove_anim_dict("move_f@injured")

================================

remove_anim_set(``animSet``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the animation set.

**Parameters:**

* ``animSet`` (``string``) -- Animation set

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.has_anim_set_loaded("idle_intro")

================================

remove_ipl(``iplName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the IPL.

**Parameters:**

* ``iplName`` (``string``) -- IPL name

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.remove_ipl("gr_case10_bunkerclosed")

================================

remove_named_ptfx_asset(``fxName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes the named particle effects asset.

**Parameters:**

* ``fxName`` (``string``) -- Effect name

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.remove_named_ptfx_asset("blood_stab")

================================

request_anim_dict(``animDict``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests the animation dictionary.

**Parameters:**

* ``animDict`` (``string``) -- Animation dictionary

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.request_anim_dict("move_f@injured")

================================

request_anim_set(``animSet``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rquests the animation set.

**Parameters:**

* ``animSet`` (``string``) -- Animation set

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.request_anim_set("idle_intro")

================================

request_ipl(``iplName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests the IPL.

**Parameters:**

* ``iplName`` (``string``) -- IPL name

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.request_ipl("gr_case10_bunkerclosed")

================================

request_model(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests a model to be loaded into memory.

**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   rage.streaming.request_model(hashKey)

================================

request_named_ptfx_asset(``fxName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Requests the named particle effects asset.

**Parameters:**

* ``fxName`` (``string``) -- Effect name

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.streaming.request_named_ptfx_asset("blood_stab")

================================

set_model_as_no_longer_needed(``model``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the model as no longer needed.

.. note::

   Unloads model from memory. Engine unloads this later as seems fit.


**Parameters:**

* ``model`` (``Hash``) -- Model hash

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   hashKey = rage.gameplay.get_hash_key("ZENTORNO")

   rage.streaming.set_model_as_no_longer_needed(hashKey)

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

* ``Blip`` -- A blip object at the specified coordinates.

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

* ``Blip`` -- A blip object at the specified entity.

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

* ``pickup`` (``Pickup``) -- Pickup item to add the blip to

**Returns:**

* ``Blip`` -- A blip object

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

* ``Blip`` -- A blip object

**Example:**

.. code-block:: lua
   :linenos:

   coords = lobby.get_player_coords(lobby.get_host())

   rage.ui.add_blip_for_radius(coords.x, coords.y, coords.z, 20)

================================

get_blip_coords(``blip``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets coordinates for a blip.

**Parameters:**

* ``blip`` (``Blip``) -- Blip object

**Returns:**

* ``Vector3`` -- Blip coords

**Example:**

.. code-block:: lua
   :linenos:

   blip = rage.ui.add_blip_for_entity(self.get_ped())

   rage.ui.get_blip_coords(blip) -- Returns coords of precedently created self ped's blip

================================

get_blip_from_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets blip from entity.

**Parameters:**

* ``entity`` (``Entity``) -- Entity to get the blip from

**Returns:**

* ``Blip`` -- A blip ID

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.ui.get_blip_from_entity(entity)

================================

get_label_text(``labelName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets label text from label name.

**Parameters:**

* ``string`` (``labelName``) -- Label name to get text from

**Returns:**

* ``string`` -- Label text

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

Checks whether specified HUD (Heads-up Display) component is active.

**Parameters:**

* ``id`` (``int``) -- Hud component ID

**Returns:**

* ``bool`` -- Rerturns hud component status

  * ``true`` -- Hud component is active
  * ``false`` -- Hud component is inactive

**Example:**

.. code-block:: lua
   :linenos:

   rage.ui.is_hud_component_active(19) -- Checks whether the Weapon Wheel is active

================================

is_mission_creator_blip(``blip``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a blip is a mission creator.

**Parameters:**

* ``blip`` (``Blip``) -- Blip

**Returns:**

* ``bool`` -- Blip status

  * ``true`` -- Blip is a mission creator
  * ``false`` -- Blip is not a mission creator

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
  * ``false`` -- Don't set blip as mission creator blip / remove mission creator blip

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
* ``color`` (``int``) -- Blip `Color ID <https://wiki.rage.mp/index.php?title=Blips#Blip_colors>`__ 


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

   coords = lobby.get_player_coords(lobby.get_host()) -- Returns host's coordinates

   rage.ui.set_blip_coords(blip, coords.x, coords.y, coords.z)

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
  * ``false`` -- Text is not aligned

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draw a 2D sprite on the screen.  

**Parameters:**

* ``textureDict`` (``string``) -- Name of texture dictionary to load texture from (e.g. "CommonMenu", "MPWeaponsCommon", etc.)  
* ``textureName`` (``string``) -- Name of texture to load from texture dictionary (e.g. "last_team_standing_icon", "tennis_icon", etc.)  
* ``screenX`` (``float``) -- Screen offset (0.5 = center)  
* ``screenY`` (``float``) -- Screen offset (0.5 = center)  
* ``width`` (``float``) -- Texture scaling. Negative values can be used to flip the texture on that axis. (0.5 = half)  
* ``height`` (``float``) -- Texture scaling. Negative values can be used to flip the texture on that axis. (0.5 = half)  
* ``heading`` (``float``) -- Texture rotation in degrees. Positive is clockwise, measured in degrees
* ``red`` (``int``) -- Sprite R color
* ``green`` (``int``) -- Sprite G color
* ``blue`` (``int``) -- Sprite B color
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

Gets gameplay camera relative pitch.

**Parameters:**

* None

**Returns:**

* ``float`` -- Cam's relative pitch value

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

Gets gameplay camera rotation

**Parameters:**

* ``rotationOrder`` (``int``) -- Rotation order.

  * Experiments show that this doesn't seem to make a difference. 

  * 0-Pitch(X): -70.000092  
  * 0-Roll(Y): -0.000001  
  * 0-Yaw(Z): -43.886459  
  * 1-Pitch(X): -70.000092  
  * 1-Roll(Y): -0.000001  
  * 1-Yaw(Z): -43.886463  
  * 2-Pitch(X): -70.000092  
  * 2-Roll(Y): -0.000002  
  * 2-Yaw(Z): -43.886467  


**Returns:**

* ``Vector3`` -- Camera rotation data

**Example:**

.. code-block:: lua
   :linenos:

   ggcr = rage.cam.get_gameplay_cam_rot(0) -- Returns the rotation of the camera with the first rotation order.
   system.log_debug("LocalPlayer pitch: " .. tostring(ggcr.x) .. " roll: " .. tostring(ggcr.y) .. " yaw: " .. tostring(ggcr.z))

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

  * You can read more about cloud types here: :doc:`things/cloudtypes`

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

  * You can read more about cloud types here: :doc:`things/cloudtypes`

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

  * You can read more about cloud types here: :doc:`things/cloudtypes`

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

  * You can read more about weather types here: :doc:`things/weathertypes`

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
   rage.gameplay.shoot_single_bullet_between_coords(coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords2.z, 1000, true, rage.gameplay.get_hash_key("WEAPON_SAWNOFFSHOTGUN"), self.get_ped(), true, true, 50.0) -- shoot a bullet from player coords to 10 meters in front of them with a damage of 1000, with pinpoint accuracy, using the shotgun, the bullet owner is the player, the bullet is audible and invisible, and the bullet speed is 50.0


update_onscreen_keyboard()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the current status of the onscreen input window

**Parameters:**

* None

**Returns:**

* ``int`` -- Status code

  * ``-1`` The onscreen input window is not active
  * ``0`` User still editing
  * ``1`` User has finished editing
  * ``2`` -- User has canceled editing

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

  * Read more about explosion types    here: :doc:`things/exptypes`
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

``int`` -- A value which represents how many times the fire was applied

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

Gets friend count.

**Parameters:**

* None

**Returns:**

* ``int`` -- Friend count

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_get_friend_count()

================================

network_get_host_of_this_script()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets ID of the player host of this script.

**Parameters:**

* None

**Returns:**

* ``Player`` -- Player ID

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_get_host_of_this_script()

================================

network_get_max_friends()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets max friends.

**Parameters:**

* None

**Returns:**

* ``int`` -- Max friends

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

Checks whether a friend is in multiplayer.

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

Checks whether a friend is online by friend index.

**Parameters:**

* ``friendIndex`` (``int``) -- The friend index to check

**Returns:**

* ``bool``

  * ``true`` -- Friend is online
  * ``false`` -- Friend isn't online


================================

network_is_friend_online(``name``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a friend is online.

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

Checks whether a session has started - you're fully connected, can control your character, and not hanging in the clouds.

**Parameters:**

* None

**Returns:**

* ``bool``

  * ``true`` --  Session has started
  * ``false`` -- Session hasn't started

**Example:**

.. code-block:: lua
   :linenos:

   rage.network.network_is_session_started()

================================

network_hash_from_player_handle(``player``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets hash from player handle.

**Parameters:**

* ``player`` (``Player``) -- The Player ID

**Returns:**

* ``Hash`` -- Hash from player handle.

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

network_get_network_id_from_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns netId from the given entity.

**Parameters:**

* ``entity`` (``Entity``) -- The Entity ID

**Returns:**

* ``int`` -- NetId

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   id = rage.network.network_get_network_id_from_entity(entity)

   system.log_debug("NetID = " .. id)

================================

.. _cutscene:

Cutscene namespace
----------------------

This namespace contains cutscene-related game functions.

================================

is_cutscene_active()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a cutscene is active.

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

Checks whether a cutscene is playing.

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

   This function needs more testing.

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

   This function needs more testing.


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

   This function needs more testing.

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

Checks whether a disabled control is just pressed.

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

Checks whether a disabled control is pressed.

**Parameters:**

* ``padIndex`` (``int``) -- Control `padIndex`_  
* ``control`` (``int``) -- Control `Ctypes`_  

.. _padIndex: https://docs.fivem.net/docs/game-references/controls/#controls
.. _Ctypes: https://docs.fivem.net/docs/game-references/controls/#control-types

**Returns:**

* ``bool`` -- Control status

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

   This function needs more testing.

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

animpostfx_is_running(``effectName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a postFX effect is running.

**Parameters:**

* ``effectName`` (``string``) -- Name of the animation postFX

**Returns:**

* ``bool``

  * ``true`` -- Animation postFX is running
  * ``false`` -- Animation postFX is not running

**Example:**

.. code-block:: lua
   :linenos:

   if rage.graphics.animpostfx_is_running("FocusIn") then
      system.log_debug("Drugs effect is running")
   end

================================

animpostfx_play(``effectName``, ``duration``, ``looped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Launches a postFX effect.

**Parameters:**

* ``effectName`` (``string``) -- Name of the postFX effect
* ``duration`` (``int``) -- Duration of the postFX effect in milliseconds
* ``looped`` (``bool``) -- If the postFX effect should be looped

  * ``true`` -- PostFX effect will be looped
  * ``false`` -- PostFX effect will not be looped

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.graphics.animpostfx_play("FocusIn", 10000, false) -- plays the FocusIn postFX for 10 seconds

================================

animpostfx_stop(``effectName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stops a postFX effect.

**Parameters:**

* ``effectName`` (``string``) -- Name of the postFX effect

  * ``true`` -- PostFX effect will be stopped
  * ``false`` -- PostFX effect will not be stopped

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.graphics.animpostfx_stop("FocusIn") -- stops the FocusIn postFX

================================

animpostfx_stop_all()
^^^^^^^^^^^^^^^^^^^^^^^^

Stops all postFX effects.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

    rage.graphics.animpostfix_stop_all() -- stops all postFX effects

================================

begin_scaleform_movie_method(``scaleform``, ``methodName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Display a scaleform.

.. note::
   
   This has to be called every frame.

**Parameters:**

* ``scaleform`` (``int``) -- Scaleform ID
* ``methodName`` (``string``) -- Name of the scaleform method

For scaleform IDs and methods, go here: :doc:`things/scaleforms`

**Returns:**

* ``bool``

  * ``true`` -- Scaleform is displayed
  * ``false`` -- Scaleform is not displayed

**Example:**

.. note::

   This should be called each frame.

   request_scaleform_movie() should be called to prepare a scaleform.

.. code-block:: lua
   :linenos:

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie(scaleform, 0.5, 0.5, 0.5, 0.5, 255, 255, 255, 255)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return
   

================================

create_checkpoint(``type``, ``posX1``, ``posY1``, ``posZ1``, ``posX2``, ``posY2``, ``posZ2``, ``diameter``, ``red``, ``green``, ``blue``, ``alpha``, ``reserved``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a checkpoint.

.. note::

   20/03/17 : Attention, checkpoints are already handled by the game itself, so you must not loop it like markers.

**Parameters:**

* ``type`` (``int``)-- The type of checkpoint to create.

  * ``0-4`` -- Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``5-9`` -- Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``10-14`` -- Ring: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``15-19`` -- 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``20-24`` -- Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``25-29`` -- Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``30-34`` -- Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker
  * ``35-38`` -- Ring: Airplane Up, Left, Right, UpsideDown
  * ``39`` -- ?
  * ``40`` -- Ring: just a ring
  * ``41`` -- ?
  * ``42-44`` -- Cylinder w/ number (uses 'reserved' parameter)
  * ``45-47`` -- Cylinder no arrow or number
* ``posX1`` (``float``) -- The X coordinate of the first checkpoint.
* ``posY1`` (``float``) -- The Y coordinate of the first checkpoint.
* ``posZ1`` (``float``) -- The Z coordinate of the first checkpoint.
* ``posX2`` (``float``) -- The X coordinate of the second checkpoint.
* ``posY2`` (``float``) -- The Y coordinate of the second checkpoint.
* ``posZ2`` (``float``) -- The Z coordinate of the second checkpoint.
* ``diameter`` (``float``) -- The diameter of the checkpoint.
* ``red`` (``int``) -- The red color level of the checkpoint.
* ``green`` (``int``) -- The green color level of the checkpoint.
* ``blue`` (``int``) -- The blue color level of the checkpoint.
* ``alpha`` (``int``) -- The transparency level of the checkpoint.
* ``reserved`` -- Special parameter

  * ``0-99`` -- Just numbers (0-99)
  * ``100-109`` -- Arrow (0-9)
  * ``110-119`` -- Two arrows (0-9)
  * ``120-129`` -- Three arrows (0-9)
  * ``130-139`` -- Circle (0-9)
  * ``140-149`` -- CycleArrow (0-9)
  * ``150-159`` -- Circle (0-9)
  * ``160-169`` -- Circle w/ pointer (0-9)
  * ``170-179`` -- Perforated ring (0-9)
  * ``180-189`` -- Sphere (0-9)

Checkpoint types with images `here <https://docs.fivem.net/docs/game-references/checkpoints/>`__.

**Returns:**

* ``int`` -- The handle of the checkpoint

**Example:**

.. code-block:: lua
   :linenos:

   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(100)

   checkpoint = rage.graphics.create_checkpoint(42, coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords2.z, 50, 255, 0, 0, 255, 120)
 

================================

delete_checkpoint(``checkpoint``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes a checkpoint.

**Parameters:**

* ``checkpoint`` (``int``) -- The handle of the checkpoint

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(100)
   checkpoint = rage.graphics.create_checkpoint(42, coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords2.z, 50, 255, 0, 0, 255, 120)
   rage.graphics.delete_checkpoint(checkpoint)

================================

draw_line(``x1``, ``y1``, ``z1``, ``x2``, ``y2``, ``z2``, ``red``, ``green``, ``blue``, ``alpha``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draws a line from ``x1``, ``y1``, ``z1`` to ``x2``, ``y2``, ``z2``.

.. note::

   This has to be called every frame.

**Parameters:**

* ``x1`` (``float``) -- The X coordinate of the first point.
* ``y1`` (``float``) -- The Y coordinate of the first point.
* ``z1`` (``float``) -- The Z coordinate of the first point.
* ``x2`` (``float``) -- The X coordinate of the second point.
* ``y2`` (``float``) -- The Y coordinate of the second point.
* ``z2`` (``float``) -- The Z coordinate of the second point.
* ``red`` (``int``) -- The red color level of the line.
* ``green`` (``int``) -- The green color level of the line.
* ``blue`` (``int``) -- The blue color level of the line.
* ``alpha`` (``int``) -- The transparency level of the line.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(100)
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_marker(1, coords1.x, coords1.y, coords1.z, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 5.0, 255, 0, 0, 255, true, true, 2, true, "mpmissmarkers256", "capture_the_flag_base_icon", true)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   return

================================

draw_marker(``type``, ``posX``, ``posY``, ``posZ``, ``dirX``, ``dirY``, ``dirZ``, ``rotX``, ``rotY``, ``rotZ``, ``scaleX``, ``scaleY``, ``scaleZ``, ``red``, ``green``, ``blue``, ``alpha``, ``reserved``)

Draws a marker with the specified appearance at the target location.

.. note::

   This has to be called every frame.

**Parameters:**

* ``type`` (``int``) -- The marker type to draw.

  * You can read more about marker types `here <https://docs.fivem.net/docs/game-references/markers/>`__.
* ``posX`` (``float``) -- The X coordinate to draw the marker at.
* ``posY`` (``float``) -- The Y coordinate to draw the marker at.
* ``posZ`` (``float``) -- The Z coordinate to draw the marker at.
* ``dirX`` (``float``) -- The X component of the direction vector for the marker, or 0.0 to use rotX/Y/Z.
* ``dirY`` (``float``) -- The Y component of the direction vector for the marker, or 0.0 to use rotX/Y/Z.
* ``dirZ`` (``float``) -- The Z component of the direction vector for the marker, or 0.0 to use rotX/Y/Z.
* ``rotX`` (``float``) -- The X rotation for the marker. Only used if the direction vector is 0.0.
* ``rotY`` (``float``) -- The Y rotation for the marker. Only used if the direction vector is 0.0.
* ``rotZ`` (``float``) -- The Z rotation for the marker. Only used if the direction vector is 0.0.
* ``scaleX`` (``float``) -- The scale for the marker on the X axis.
* ``scaleY`` (``float``) -- The scale for the marker on the Y axis.
* ``scaleZ`` (``float``) -- The scale for the marker on the Z axis.
* ``red`` (``int``) -- The red component of the marker color, on a scale from 0-255.
* ``green`` (``int``) -- The green component of the marker color, on a scale from 0-255.
* ``blue`` (``int``) -- The blue component of the marker color, on a scale from 0-255.
* ``alpha`` (``int``) -- The alpha component of the marker color, on a scale from 0-255.
* ``bobUpAndDown`` (``bool``) -- Whether or not the marker should slowly animate up/down.
* ``faceCamera`` (``bool``) -- Whether the marker should be a 'billboard', as in, should constantly face the camera.
* ``p19`` (``int``) -- Typically set to 2. Does not seem to matter directly.
* ``rotate`` (``bool``) -- Rotations only apply to the heading.
* ``textureDict`` (``string``) -- A texture dictionary to draw the marker with, or NULL. Example: 'GolfPutting'
* ``textureName`` (``string``) -- A texture name in textureDict to draw the marker with, or NULL. Example: 'PuttingMarker'
* ``drawOnEnts`` (``bool``) -- Whether or not the marker should draw on intersecting entities.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(100)
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_line(coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords2.z, 255, 0, 0, 255)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end

================================

draw_rect(``x``, ``y``, ``width``, ``height``, ``red``, ``green``, ``blue``, ``alpha``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draws a rectangle on the screen. Similar to render.draw_box()

.. note::

   The total number of rectangles to be drawn in one frame is apparently limited to 399.

.. note::

   This has to be called every frame.

**Parameters:**

* ``x`` (``float``) -- The X coordinate of the top-left corner. (``0.0`` - ``1.0``, ``0.0`` is the left edge of the screen, ``1.0`` is the right edge of the screen) 
* ``y`` (``float``) -- The Y coordinate of the top-left corner. (``0.0`` - ``1.0``, ``0.0`` is the top edge of the screen, ``1.0`` is the bottom edge of the screen)
* ``width`` (``float``) -- The width of the rectangle. (``0.0`` - ``1.0``, ``1.0`` means the whole screen width)
* ``height`` (``float``) -- The height of the rectangle. (``0.0`` - ``1.0``, ``1.0`` means the whole screen height)
* ``red`` (``int``) -- The red part of the rectangle color (``0`` - ``255``)
* ``green`` (``int``) -- The green part of the rectangle color (``0`` - ``255``)
* ``blue`` (``int``) -- The blue part of the rectangle color (``0`` - ``255``)
* ``alpha`` (``int``) -- The transparency of the rectangle color (``0`` - ``255``)

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_rect(0.5, 0.5, 0.5, 0.5, 255, 255, 255, 100)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end

================================


draw_scaleform_movie(``scaleformHandle``, ``x``, ``y``, ``width``, ``height``, ``red``, ``green``, ``blue``, ``alpha``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draw scaleform in the selected dimensions

.. note::
   
   This has to be called every frame.

**Parameters:**

* ``scaleformHandle`` (``int``) -- The scaleform handle to draw.
* ``x`` (``float``) -- The X coordinate to draw the scaleform at. (``0.0`` - ``1.0``, ``0.0`` is the left edge of the screen, ``1.0`` is the right edge of the screen)
* ``y`` (``float``) -- The Y coordinate to draw the scaleform at. (``0.0`` - ``1.0``, ``0.0`` is the top edge of the screen, ``1.0`` is the bottom edge of the screen)
* ``width`` (``float``) -- The width of the scaleform. (``0.0`` - ``1.0``, ``1.0`` means the whole screen width)
* ``height`` (``float``) -- The height of the scaleform. (``0.0`` - ``1.0``, ``1.0`` means the whole screen height)
* ``red`` (``int``) -- The red part of the scaleform color (``0`` - ``255``)
* ``green`` (``int``) -- The green part of the scaleform color (``0`` - ``255``)
* ``blue`` (``int``) -- The blue part of the scaleform color (``0`` - ``255``)
* ``alpha`` (``int``) -- The transparency of the scaleform color (``0`` - ``255``)


For scaleform IDs and methods, go here: :doc:`things/scaleforms`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie(scaleform, 0.5, 0.5, 0.5, 0.5, 255, 255, 255, 255)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return

================================

draw_scaleform_movie_fullscreen(``scaleformHandle``, ``red``, ``green``, ``blue``, ``alpha``, ``unk``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Draw a scaleform in fullscreen.

.. note::
   
   This has to be called every frame.

**Parameters:**

* ``scaleformHandle`` (``int``) -- The scaleform handle to draw.
* ``red`` (``int``) -- The red part of the scaleform color (``0`` - ``255``)
* ``green`` (``int``) -- The green part of the scaleform color (``0`` - ``255``)
* ``blue`` (``int``) -- The blue part of the scaleform color (``0`` - ``255``)
* ``alpha`` (``int``) -- The transparency of the scaleform color (``0`` - ``255``)
* ``unk`` (``int``) -- Unknown. Not used.

For scaleform IDs and methods, go here: :doc:`things/scaleforms`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie_fullscreen(scaleform, 255, 255, 255, 255, 0)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return
   
================================

enable_alien_blood_vfx(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a motion-blur sort of effect. Doesn't seem to work, but if you use animpostfx_play() with ``DrugsMichaelAliensFight`` animfx, you should be able to get the intended effect

**Parameters:**

* ``toggle`` (``boolean``) -- Whether to enable the effect or not.

  * ``true`` -- Enable the effect
  * ``false`` -- Disable the effect

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   enable_alien_blood_vfx(true)
   system.wait(1000)
   enable_alien_blood_vfx(false)

================================

enable_clown_blood_vfx(``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates cartoon effect when Michel smokes the weed.

**Parameters:**

* ``toggle`` (``boolean``) -- Whether to enable the effect or not.

  * ``true`` -- Enable the effect
  * ``false`` -- Disable the effect

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   enable_clown_blood_vfx(true)
   system.wait(1000)
   enable_clown_blood_vfx(false)

================================

end_scaleform_movie_method()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finishes all scaleforms that are currently drawn.

**Parameters:**

* None

**Returns:**

* None

**Example:**

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie_fullscreen(scaleform, 255, 255, 255, 255, 0)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return
   
================================

has_scaleform_movie_loaded(``scaleformHandle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a scaleform was loaded.

**Parameters:**

* ``scaleformHandle`` (``int``) -- The scaleform handle to check.

**Returns:**

* ``boolean`` -- ``true`` if the scaleform was loaded, ``false`` otherwise.

**Example:**

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   if rage.graphics.has_scaleform_movie_loaded(scaleform) then
      print("scaleform loaded")
   else
      print("scaleform not loaded")
   end

================================

remove_particle_fx(``ptfxHandle``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removes a particle effect.

**Parameters:**

* ``ptfxHandle`` (``int``) -- The particle effect handle to remove.
* ``p1`` (``bool``) -- Unknown. Seen to be ``false``.

**Returns:**

* None

.. note::

   PTFX spawning is not implemented yet, therefore no example.

================================

request_scaleform_movie(``scaleformName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request a scaleform handle.

**Parameters:**

* ``scaleformName`` (``string``) -- The name of the scaleform to request.

  * You can find the names of the scaleforms in :doc:`things/scaleforms`

**Returns:**

* ``int`` -- The scaleform handle.

**Example:**

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   system.log_debug(scaleform)

================================


scaleform_movie_method_add_param_bool(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pass a bool param to scaleform. The scaleform should be initialiazed already.

**Parameters:**

* ``value`` (``boolean``) -- The value to add.

**Returns:**

* None

**Example:**

.. note::

   I wasn't able to come up with a good example. If somebody can, please make a pull request.

================================

scaleform_movie_method_add_param_float(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pass a float param to scaleform. The scaleform should be initialized already.

**Parameters:**

* ``value`` (``float``) -- The value to add.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie(scaleform, 0.5, 0.5, 0.5, 0.5, 255, 255, 255, 255)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_float(5.0)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return

================================

scaleform_movie_method_add_param_int(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pass an int param to scaleform. The scaleform should be initialized already.

**Parameters:**

* ``value`` (``int``) -- The value to add.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie(scaleform, 0.5, 0.5, 0.5, 0.5, 255, 255, 255, 255)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return

================================

scaleform_movie_method_add_param_texture_name_string(``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pass a string param to scaleform. The scaleform should be initialized already.

**Parameters:**

* ``value`` (``string``) -- The value to add.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie(scaleform, 0.5, 0.5, 0.5, 0.5, 255, 255, 255, 255)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return

================================

set_checkpoint_cylinder_height(``checkpoint``, ``nearHeight``, ``farHeight``, ``radius``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the height of the cylindrical checkpoint.

**Parameters:**

* ``checkpoint`` (``int``) -- The checkpoint handle.
* ``nearHeight`` (``float``) -- The height of the checkpoint when inside of the radius.  
* ``farHeight`` (``float``) -- The height of the checkpoint when outside of the radius.  
* ``radius`` (``float``) -- The radius of the checkpoint.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(100)
   checkpoint = rage.graphics.create_checkpoint(45, coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords2.z, 50, 255, 0, 0, 255, 120)
   rage.graphics.set_checkpoint_cylinder_height(checkpoint, 0.0, 100.0, 50.0)

================================

set_checkpoint_rgba(``checkpoint``, ``red``, ``green``, ``blue``, ``alpha``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the RGBA of the checkpoint.

**Parameters:**

* ``checkpoint`` (``int``) -- The checkpoint handle.
* ``red`` (``int``) -- The red value.
* ``green`` (``int``) -- The green value.
* ``blue`` (``int``) -- The blue value.
* ``alpha`` (``int``) -- The alpha value.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:


   coords1 = self.get_coords()
   coords2 = self.get_coords_infront(100)
   checkpoint = rage.graphics.create_checkpoint(45, coords1.x, coords1.y, coords1.z, coords2.x, coords2.y, coords2.z, 50, 255, 0, 0, 255, 120)
   rage.graphics.set_checkpoint_rgba(checkpoint, 0, 255, 0, 255)

================================

set_scaleform_movie_as_no_longer_needed(``scaleformHandle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deinitializes a scaleform object.

**Parameters:**

* ``scaleformHandle`` (``int``) -- The scaleform handle.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   scaleform = rage.graphics.request_scaleform_movie("MP_BIG_MESSAGE_FREEMODE")
   rage.graphics.end_scaleform_movie_method()
   kPressed = system.is_key_pressed("K")
   while not kPressed do
      rage.graphics.draw_scaleform_movie(scaleform, 0.5, 0.5, 0.5, 0.5, 255, 255, 255, 255)
      rage.graphics.begin_scaleform_movie_method(scaleform, "SHOW_SHARD_WASTED_MP_MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("BIG MESSAGE")
      rage.graphics.scaleform_movie_method_add_param_texture_name_string("small message")
      rage.graphics.scaleform_movie_method_add_param_int(5)
      kPressed = system.is_key_pressed("K")
      system.wait(-1)
   end
   rage.graphics.set_scaleform_movie_as_no_longer_needed(scaleform)
   return


================================

.. _time:

Time namespace
----------------------

This namespace contains time-related game functions.

================================

get_clock_hours()
^^^^^^^^^^^^^^^^^^^^^^

Returns the current in-game hour

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

Returns the current in-game minute

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

Returns the current in-game second

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

This namespace contains ai-related game functions. 

================================

does_scenario_group_exist(``scenarioGroup``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a scenario group exists.

**Parameters:**

* ``scenarioGroup`` (``string``) -- Scenario group name
  
  * You can read more about scenario groups here: :doc:`things/scenariogroups`

**Returns:**

* ``bool`` -- Scenario group status check
  
  * ``true`` -- Scenario group exists
  * ``false`` -- Scenario group does not exist

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.ai.does_scenario_group_exist("SOLOMON_GATE")

   system.log_debug(tostring(data))

================================

is_ped_active_in_scenario(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the ped is currently in any scenario.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object

**Returns:**

* ``bool`` -- Check status
  
  * ``true`` -- If the ped is currently in any scenario.
  * ``false`` -- If the ped is not in any scenario.

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   data = rage.ai.is_ped_active_in_scenario(ped)

   system.log_debug(tostring(data))

================================

is_scenario_group_enabled(``scenarioGroup``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the scenario group is enabled.

**Parameters:**

* ``scenarioGroup`` (``string``) -- Scenario group name
  
  * You can read more about scenario groups here: :doc:`things/scenariogroups`

**Returns:**

* ``bool`` -- Scenario group status
  
  * ``true`` -- Scenario group is enabled.
  * ``false`` -- Scenario group is not enabled.

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.ai.is_scenario_group_enabled("SOLOMON_GATE")

   system.log_debug(tostring(data))

================================

is_scenario_type_enabled(``scenarioType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the scenario type is enabled.

**Parameters:**

* ``scenarioType`` (``string``) -- Scenario type name
  
  * You can read more about scenario groups here: :doc:`things/scenariotypes`

**Returns:**

* ``bool`` -- Scenario type status check
  
  * ``true`` -- Scenario type is enabled.
  * ``false`` -- Scenario type is not enabled.

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.ai.is_scenario_type_enabled("WORLD_HUMAN_DRINKING")

   system.log_debug(tostring(data))

================================

get_is_task_active(``ped``, ``taskIndex``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether the task is active.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``taskIndex`` (``int``) -- Task index enum

**Returns:**

* ``bool`` -- Task status check
  
  * ``true`` -- Task is active.
  * ``false`` -- Task is not active.

**Example:**

.. code-block:: lua
   :linenos:

   data = rage.ai.get_is_task_active(self.get_ped(), 127)  -- Checks whether the CTaskCrouch is active
   system.log_debug(tostring(data))

================================

play_anim_on_running_scenario(``ped``, ``animDict``, ``animName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play the animation on any running scenario.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``animDict`` (``string``) -- Animation dictionary
* ``animName`` (``string``) -- Animation (clip) name

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.play_anim_on_running_scenario(ped, "move_f@injured", "idle_intro")

================================

reset_exclusive_scenario_group()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reset the exclusive scenario group.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.reset_exclusive_scenario_group()

================================

reset_scenario_groups_enabled()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reset all the enabled scenario groups.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.reset_scenario_groups_enabled()

================================

reset_scenario_types_enabled()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reset all the enabled scenario types.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.reset_scenario_types_enabled()

================================

set_exclusive_scenario_group(``scenarioGroup``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the scenario group as exclusive.

**Parameters:**

* ``scenarioGroup`` (``string``) -- Scenario group name
  
  * You can read more about scenario groups here: :doc:`things/scenariogroups`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.set_exclusive_scenario_group("SOLOMON_GATE")

================================

reset_exclusive_scenario_group()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reset the exclusive scenario group(s).

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.reset_exclusive_scenario_group()

================================

set_parachute_task_target(``ped``, ``x``, ``y``, ``z``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make ped parachute to target

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``string``) -- The ``X`` coordinate
* ``y`` (``string``) -- The ``Y`` coordinate
* ``z`` (``string``) -- The ``Z`` coordinate

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.set_parachute_task_target(ped, 60, 118, 12)

================================

set_parachute_task_thrust(``ped``, ``thrust``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the parachute task thrust.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``thrust`` (``float``) -- The thrust value

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.set_parachute_task_thrust(ped, 10)

================================

set_scenario_group_enabled(``scenarioGroup``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set scenario group as enabled.

**Parameters:**

* ``scenarioGroup`` (``string``) -- Scenario group name
  
  * You can read more about scenario groups here: :doc:`things/scenariogroups`

* ``p1`` (``bool``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.set_scenario_group_enabled("SOLOMON_GATE")

================================

set_scenario_type_enabled(``scenarioType``, ``toggle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Toggle the scenario type.

**Parameters:**

* ``scenarioType`` (``string``) -- Scenario type name
  
  * You can read more about scenario groups here: :doc:`things/scenariotypes`

* ``toggle`` (``bool``) -- Toggle

  * ``true`` -- Scenario type enabled
  * ``false`` -- Scenario type not enabled

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.ai.set_scenario_type_enabled("WORLD_HUMAN_DRINKING", true)

================================

stop_anim_task(``ped``, ``animDictionary``, ``animationName``, ``p3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stop animation task.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``animDictionary`` (``string``) -- Animation dictionary
* ``animationName`` (``string``) -- Animation (clip) name

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

* ``p3`` (``float``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.stop_anim_task(ped, "move_f@injured", "sprint")

================================

task_aim_gun_at_coord(``ped``, ``x``, ``y``, ``z``, ``time``, ``p5``, ``p6``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aim gun at coordinates.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``string``) -- The ``X`` coordinate
* ``y`` (``string``) -- The ``Y`` coordinate
* ``z`` (``string``) -- The ``Z`` coordinate
* ``time`` (``int``) -- The time value
* ``p5`` (``bool``) -- Unknown
* ``p6`` (``bool``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.task_aim_gun_at_coord(ped, 60.12, 118.40, 12.28, 5)

================================

task_aim_gun_at_entity(``ped``, ``entity``, ``duration``, ``p3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aim gun at entity.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``entity`` (``Entity``) -- The entity ID
* ``duration`` (``int``) -- The duration value
* ``p3`` (``bool``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   entity = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_aim_gun_at_entity(ped, entity, 5)

================================

task_combat_ped(``ped``, ``targetPed``, ``p2``, ``p3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the specified ped attack the target ped.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``targetPed`` (``Ped``) -- Target ped object
* ``p2`` (``int``) -- The duration value
* ``p3`` (``int``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   targetPed = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_combat_ped(ped, targetPed) -- Self's ped will attack lobby host's ped

================================

task_enter_vehicle(``ped``, ``vehicle``, ``timeout``, ``seat``, ``speed``, ``flag``, ``p6``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the specified ped enter the vehicle.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- Vehicle ID
* ``timeout`` (``int``) -- Animation timeout
* ``seat`` (``int``) -- Seat type ID

  * You can read more about seat types here: :doc:`things/seattypes`

* ``speed`` (``float``) -- Ped speed
  
  * ``1.0`` = walk
  * ``2.0`` = run

* ``flag`` (``int``) -- Entering type
  
  * ``1`` = normal
  * ``3`` = teleport to vehicle
  * ``8`` = normal/carjack ped from seat
  * ``16`` = teleport directly into vehicle

* ``p6`` (``Any``) -- Always 0

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   vehicle = rage.gameplay.get_hash_key("ZENTORNO")

   rage.ai.task_enter_vehicle(ped, vehicle, 0, -1, 2.0, 1, 0) --  Ped will enter the Zentorno walking and sitting on driver seat.

================================

task_follow_to_offset_of_entity(``ped``, ``entity``, ``offsetX``, ``offsetY``, ``offsetZ``, ``movementSpeed``, ``timeout``, ``stoppingRange``, ``persistFollowing``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow to offset of the entity.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``entity`` (``Entity``) -- The entity ID
* ``offsetX`` (``float``) -- Offset ``X`` position
* ``offsetY`` (``float``) -- Offset ``Y`` position
* ``offsetZ`` (``float``) -- Offset ``Z`` position
* ``movementSpeed`` (``float``) -- Movement speed
* ``timeout`` (``int``) -- Timeout
* ``stoppingRange`` (``float``) -- Stopping range

* ``persistFollowing`` (``bool``) -- Toggle persist following
  
  * ``true`` -- Persist following on
  * ``false`` -- Persist following off

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   entity = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_follow_to_offset_of_entity(ped, entity, 5, 5, 1, 2, 0, 1, true)

================================

task_go_to_coord_while_aiming_at_coord(``ped``, ``x``, ``y``, ``z``, ``aimAtX``, ``aimAtY``, ``aimAtZ``, ``moveSpeed``, ``p8``, ``p9``, ``p10``, ``p11``, ``flags``, ``p13``, ``firingPattern``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ped move to a coordinate while aiming (and optionally shooting) at given coordinates.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``float``) -- Destination ``X`` position
* ``y`` (``float``) -- Destination ``Y`` position
* ``z`` (``float``) -- Destination ``Z`` position
* ``aimAtX`` (``float``) -- Aim at target ``X`` position
* ``aimAtY`` (``float``) -- Aim at target ``Y`` position
* ``aimAtZ`` (``float``) -- Aim at target ``Z`` position
* ``moveSpeed`` (``float``) -- Movement speed

* ``p8`` (``bool``) -- Toggle ped shooting
  
  * ``true`` -- Ped will shoot
  * ``false`` -- Ped will not shoot
  
* ``p9`` (``float``) -- seen to be 2.0
* ``p10`` (``float``) -- seen to be 0.5
* ``p11`` (``bool``) 

  * ``true`` -- ped will stay still
  * ``false`` -- will not stay still
* ``flags`` (``Any``) -- ``0`` / ``512`` / ``513``
* ``p13`` (``bool``) -- Unknown
* ``firingPattern`` (``Hash``) -- Firing pattern hash
  
  * Firing patterns can be found here: :doc:`things/firingpatterns`


**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.task_go_to_coord_while_aiming_at_coord(ped, 5, 5, 1, 10, 10, 1, 2, true)

================================

task_go_to_coord_while_aiming_at_entity(``p0``, ``p1``, ``p2``, ``p3``, ``p4``, ``p5``, ``p6``, ``p7``, ``p8``, ``p9``, ``p10``, ``p11``, ``p12``, ``p13``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ped move to a coordinate while aiming (and optionally shooting) at given coordinates.

**Parameters:**

* ``p0`` (``Any``) -- Ped ID
* ``p1`` (``float``) -- X coordinate to go to
* ``p2`` (``float``) -- Y coordinate to go to
* ``p3`` (``float``) -- Z coordinate to go to
* ``p4`` (``Any``) -- Ped to aim on
* ``p5`` (``float``) -- Unknown always seems to be ``2.0``
* ``p6`` (``bool``) -- Unknown -- seen to be both ``false`` and ``true``
* ``p7`` (``float``) -- Unknown -- let it be ``1.5``
* ``p8`` (``float``) -- Unknown -- let it be ``1.5``
* ``p9`` (``bool``) -- Unknown -- seen to be ``false``
* ``p10`` (``Any``) -- Unknown -- seen to be ``false``
* ``p11`` (``bool``) -- Unknown -- probably ``false``?
* ``p12`` (``Any``) -- Firing pattern

  * Firing patterns can be found here: :doc:`things/firingpatterns`
* ``p13`` (``Any``) -- Unknown -- let it be 20000, noone knows what that is

**Returns:**

* None

**Example:**

   .. note::

      This example was not tested.

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   ped2 = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_go_to_coord_while_aiming_at_entity(ped, 119.73, 65.30, 420.12, ped2, 2.0, false, 1.5, 1.5, false, false, false)

================================

task_go_to_entity_while_aiming_at_entity(``ped``, ``entityToWalkTo``, ``entityToAimAt``, ``speed``, ``shootatEntity``, ``p5``, ``p6``, ``p7``, ``p8``, ``firingPattern``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ped move to an entity while aiming and optionally shooting and optionally killing it.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``entityToWalkTo`` (``Entity``) -- Entity to walk to
* ``entityToAimAt`` (``Entity``) -- Entity to aim at
* ``speed`` (``float``) -- Speed
* ``shootatEntity`` (``bool``) -- Toggle shoot at entity

  * ``true`` -- Peds will shoot at Entity till it is dead.
  * ``false`` -- Peds will just walk till they reach the entity and will cease shooting.

* ``p5`` (``float``) -- Unknown
* ``p6`` (``float``) -- Unknown
* ``p7`` (``bool``) -- Unknown
* ``p8`` (``bool``) -- Unknown
* ``firingPattern`` (``Hash``) -- Firing pattern hash

  * Firing patterns can be found here: :doc:`things/firingpatterns`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   entity = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_go_to_entity_while_aiming_at_entity(ped, entity, 5, 5, 1, 2, 0, 1, true)

================================

task_go_to_entity(``entity``, ``target``, ``duration``, ``distance``, ``speed``, ``p5``, ``p6``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the entity move to a target until time is over (duration) or get in target's range (distance).

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``target`` (``Entity``) -- Target object
* ``duration`` (``int``) -- Time available to complete the task

  * ``duration`` = ``-1`` -- The task duration will be ignored

* ``distance`` (``float``) -- Target's range
* ``speed`` (``float``) -- Speed
* ``p5`` (``float``) -- Unknown but can leave it ``1073741824`` or ``100`` or even ``0`` (no difference noticed)
* ``p6`` (``bool``) -- Unknown but can leave it ``0``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   pedHandle = self.get_ped()
   coords = self.get_coords_infront(10)

   vehicleHandle = scripting.spawn.spawn_vehicle(rage.gameplay.get_hash_key("ZENTORNO"), coords, 30.0)

   rage.ai.task_go_to_entity(pedHandle, vehicleHandle, 5000, 4.0, 100, 1073741824, 0) 
   -- Ped will run towards the vehicle for 5 seconds and stop when time is over or when he Returns 4 meters(?) around the vehicle

================================

task_leave_vehicle(``ped``, ``vehicle``, ``flags``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ped leave the vehicle with customizable flags.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- Vehicle ID
* ``flags`` (``int``) -- Vehicle leaving flags
  
  * ``0`` = normal exit and closes door
  * ``1`` = normal exit and closes door
  * ``16`` = teleports outside, door kept closed. (This flag does not seem to work for the front seats in buses, NPCs continue to exit normally)
  * ``64`` = normal exit and closes door
  * ``256`` = normal exit but does not close the door
  * ``4160`` = ped is throwing himself out, even when the vehicle is still
  * ``262144`` = ped moves to passenger seat first, then exits normally 
  * Others to be tried out: ``320``, ``512``, ``131072``

**Returns:**

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   vehicle = self.rage.ped.get_vehicle_ped_is_using(ped)

   rage.ai.task_leave_vehicle(ped, vehicle, 1)

================================

task_open_vehicle_door(``ped``, ``vehicle``, ``timeOut``, ``seat``, ``speed``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ped open the vehicle door of a specific seat, at given speed.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- Vehicle ID
* ``timeOut`` (``int``) -- Task timeout
* ``seat`` (``int``) -- Seat Index

  * You can read more about seat indexes here: :doc:`things/seattypes`

* ``speed`` (``float``) -- Speed to open the door

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   vehicle = scripting.spawn.spawn_vehicle(rage.gameplay.get_hash_key("ZENTORNO"), self.get_coords_infront(10), 30.0)

   rage.ai.task_open_vehicle_door(ped, vehicle, 100, 1, 2.0)

================================

task_parachute(``ped``, ``p1``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the ped do a parachute jump

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``p1`` (``bool``) -- Unknown (unused)
* ``p1`` (``bool``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_parachute(ped)

================================

task_parachute_to_target(``ped``, ``x``, ``y``, ``z``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped parachute to given coordinates.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``float``) -- The ``X`` position
* ``y`` (``float``) -- The ``Y`` position
* ``z`` (``float``) -- The ``Z`` position

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_parachute_to_target(ped, 69.5, 420.10, 57.91)

================================

task_play_anim(``ped``, ``animDictionary``, ``animationName``, ``blendInSpeed``, ``blendOutSpeed``, ``duration``, ``flag``, ``playbackRate``, ``lockX``, ``lockY``, ``lockZ``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped play an animation with custom duration and flags.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``animDictionary`` (``string``) -- Animation dictionary
* ``animationName`` (``string``) -- Animation (clip) name

  * You can read more about animations dicts and names here: :doc:`things/animtypes`

* ``blendInSpeed`` (``float``) -- Normal speed is ``8.0``
* ``blendOutSpeed`` (``float``) -- Normal speed is ``8.0``
* ``duration`` (``int``) -- Time in millisecond
* ``flag`` (``int``) -- enum eAnimationFlags:
  
  * ANIM_FLAG_NORMAL = ``0``
  * ANIM_FLAG_REPEAT = ``1``
  * ANIM_FLAG_STOP_LAST_FRAME = ``2``
  * ANIM_FLAG_UPPERBODY = ``16``
  * ANIM_FLAG_ENABLE_PLAYER_CONTROL = ``32``
  * ANIM_FLAG_CANCELABLE = ``120``

* ``playbackRate`` (``float``) -- Values are between ``0.0`` and ``1.0``
* ``lockX`` (``bool``) -- ``0`` in most case
* ``lockY`` (``bool``) -- ``0`` in most case
* ``lockZ`` (``bool``) -- ``0`` for singleplayer, can be ``1`` in multiplayer

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.task_play_anim(ped, "move_f@injured", "sprint", 8.0, 8.0, 5000, 0, 0.0, 0, 0, 1)

================================

task_rappel_from_heli(``ped``, ``minHeightAboveGround``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped rappel from helicopter, with settable minimum height above the ground.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``minHeightAboveGround`` (``float``) -- Minimum helicopter height above the ground

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   ped = self.get_ped()

   rage.ai.task_rappel_from_heli(ped, 100)

================================

task_shoot_at_entity(``entity``, ``target``, ``duration``, ``firingPattern``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make the entity shoot at an entity targeted for a given duration and with custom firing pattern.

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``target`` (``Entityt``) -- Target entity object
* ``duration`` (``int``) -- Duration in milliseconds
* ``firingPattern`` (``Hash``) -- Firing pattern hash

  * Firing patterns can be found here: :doc:`things/firingpatterns`

**Returns:**

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   targetEntity = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_shoot_at_entity(entity, targetEntity, 5000, 1)

================================

task_sky_dive(``ped``, ``p1``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped sky-dive.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``p1`` (``bool``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_sky_dive(ped)

================================

task_stand_guard(``ped``, ``x``, ``y``, ``z``, ``heading``, ``scenarioName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped parachute to given coordinates.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``float``) -- The ``X`` position
* ``y`` (``float``) -- The ``Y`` position
* ``z`` (``float``) -- The ``Z`` position
* ``heading`` (``float``) -- The heading direction
* ``scenarioName`` (``string``) -- The scenario name

  * You can read more about scenario groups here: :doc:`things/scenariogroups`

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_parachute_to_target(ped, 69.5, 420.10, 57.91, 1, "WORLD_HUMAN_GUARD_STAND")

================================

task_start_scenario_at_position(``ped``, ``scenarioName``, ``x``, ``y``, ``z``, ``heading``, ``duration``, ``sittingScenario``, ``teleport``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped start the scenario at a given position.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``scenarioName`` (``string``) -- The scenario name

  * You can read more about scenario groups here: :doc:`things/scenariogroups`

* ``x`` (``float``) -- The ``X`` position
* ``y`` (``float``) -- The ``Y`` position
* ``z`` (``float``) -- The ``Z`` position
* ``heading`` (``float``) -- The heading direction
* ``duration`` (``int``) -- Duration in milliseconds
* ``sittingScenario`` (``bool``) -- Toggle sitting scenario

  * ``true`` -- Sitting scenario on
  * ``false`` -- Sitting scenario off

* ``teleport`` (``bool``) -- Toggle teleport ped to the given position
  
  * ``true`` -- Teleport ped to coordinates
  * ``false`` -- Do not teleport ped

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_start_scenario_at_position(ped, "WORLD_HUMAN_GUARD_STAND", 69.5, 420.10, 57.91, 1, 5000, false, )

================================

task_start_scenario_in_place(``ped``, ``scenarioName``, ``unkDelay``, ``playEnterAnim``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plays a scenario on a Ped at their current location.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``scenarioName`` (``string``) -- The scenario name

  * You can read more about scenario groups here: :doc:`things/scenariogroups`

* ``unkDelay`` (``int``) -- Usually 0 or -1, doesn't seem to have any effect.
* ``playEnterAnim`` (``bool``) -- Scenarios that don't have any "Enter" anims won't play if this is set to true.

  * ``true`` -- Plays the "Enter" anim
  * ``false`` -- Plays the "Exit" anim

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_start_scenario_in_place(ped, "WORLD_HUMAN_GUARD_STAND", 0, true)

================================

task_stay_in_cover(``ped``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes the ped stay in cover.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_stay_in_cover(ped)

================================

task_turn_ped_to_face_entity(``ped``, ``entity``, ``duration``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Turn the ped to face towards the entity.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``entity`` (``Entity``) -- Entityd object
* ``duration`` (``int``) -- The amount of time in milliseconds to do the task. 
  
  * ``-1`` will keep the task going until either another task is applied, or CLEAR_ALL_TASKS() is called with the ped

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   entity = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_turn_ped_to_face_entity(ped, entity, 500)

================================

task_vehicle_aim_at_coord(``ped``, ``x``, ``y``, ``z``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped vehicle aim at given coordinates.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``float``) -- The ``X`` position
* ``y`` (``float``) -- The ``Y`` position
* ``z`` (``float``) -- The ``Z`` position

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   rage.ai.task_vehicle_aim_at_coord(ped, 69.5, 420.10, 57.91)

================================

task_vehicle_aim_at_ped(``ped``, ``target``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped vehicle aim at a given ped.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``target`` (``Ped``) -- Target ped object

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   target = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_vehicle_aim_at_ped(ped, target)

================================

task_vehicle_chase(``driver``, ``targetEnt``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped driver chase a target entity.

**Parameters:**

* ``driver`` (``Ped``) -- Ped object (vehicle driver)
* ``targetEnt`` (``Entity``) -- Target entity

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   targetEnt = lobby.get_player_ped(lobby.get_host())

   rage.ai.task_vehicle_chase(ped, targetEnt)

================================

task_vehicle_drive_to_coord(``ped``, ``vehicle``, ``x``, ``y``, ``z``, ``speed``, ``p6``, ``vehicleModel``, ``drivingMode``, ``stopRange``, ``p10``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped drive the vehicle to given coordinates.

**Parameters:**

* ``driver`` (``Ped``) -- Ped object (vehicle driver)
* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``x`` (``float``) -- The ``X`` position
* ``y`` (``float``) -- The ``Y`` position
* ``z`` (``float``) -- The ``Z`` position
* ``speed`` (``float``) -- The driving speed
* ``p6`` (``Any``) -- Unknown
* ``vehicleModel`` (``Hash``) -- The vehilemde ash 
* ``drivingMode`` (``int``) -- Driving mode
* ``stopRange`` (``float``) -- Stops in the specific range near the destination. ``20.0`` works fine.
* ``p10`` (``float``) -- Unknown

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   zentornoHash = rage.gameplay.get_hash_key("ZENTORNO")

   rage.ai.task_vehicle_drive_to_coord(ped, 69.5, 420.10, 57.91, 100, zentornoHash, 1, 5)

================================



task_vehicle_drive_to_coord_longrange(``ped``, ``vehicle``, ``x``, ``y``, ``z``, ``speed``, ``driveMode``, ``stopRange``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped drive to the destination at set speed and driving style.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``x`` (``float``) -- The ``X`` position
* ``y`` (``float``) -- The ``Y`` position
* ``z`` (``float``) -- The ``Z`` position
* ``speed`` (``float``) -- The driving speed
* ``driveMode`` (``int``) -- Driving mode, `Driving Style calculator`_  
* ``stopRange`` (``float``) -- Stops in the specific range near the destination. ``20.0`` works fine

.. _Driving Style calculator: https://vespura.com/fivem/drivingstyle/

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   zentornoHash = rage.gameplay.get_hash_key("ZENTORNO")

   rage.ai.task_vehicle_drive_to_coord_longrange(ped, 69.5, 420.10, 57.91, 100, zentornoHash, 1, 5)

================================

task_vehicle_drive_wander(``ped``, ``vehicle``, ``speed``, ``drivingStyle``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped drive randomly with no destination set.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``speed`` (``float``) -- The driving speed
* ``drivingStyle`` (``int``) -- Driving mode, `Driving Style calculator`_  

.. _Driving Style calculator: https://vespura.com/fivem/drivingstyle/

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   vehicle = rage.gameplay.get_hash_key("ZENTORNO")

   rage.ai.task_vehicle_drive_wander(ped, vehicle, 50, 6)

================================

task_vehicle_escort(``ped``, ``vehicle``, ``targetVehicle``, ``mode``, ``speed``, ``drivingStyle``, ``minDistance``, ``p7``, ``noRoadsDistance``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes a ped follow the targetVehicle with <minDistance> in between.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``targetVehicle`` (``Vehicle``) -- The target vehicle ID
* ``mode`` (``int``) -- The mode defines the relative position to the targetVehicle. The ped will try to position its vehicle there.

  * ``-1`` = behind  
  * ``0`` = ahead  
  * ``1`` = left  
  * ``2`` = right  
  * ``3`` = back left  
  * ``4`` = back right  

* ``speed`` (``float``) -- The driving speed
* ``drivingStyle`` (``int``) -- Driving mode, `Driving Style calculator`_  
* ``minDistance`` (``float``) -- The minimum distance between ped vehicle and target vehicle

  * ``minDistance`` is ignored if drivingstyle is Avoiding Traffic, but Rushed is fine.  

* ``p7`` (``int``) -- Unknwn
* ``noRoadsDistance`` (``float``) -- If the target is closer than noRoadsDistance, the driver will ignore pathing/roads and follow it direct.

.. _Driving Style calculator: https://vespura.com/fivem/drivingstyle/

**Returns:**

* None

**Example:**

.. note::
   
   This example was not tested. It assumes that the host and the player are driving vehicles.

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   veh = self.get_vehicle()

   pedTarget = lobby.get_player_ped(lobby.get_host())
   targetVehicle = rage.ped.get_vehicle_ped_is_using(pedTarget)
   
   rage.ai.task_vehicle_escort(ped, veh, targetVehicle, -1, 50, 6, 100) -- player will follow host with 100m in betweentask_vehicle_escorttargetVehicle, -150, 6, 10, 20

================================

task_vehicle_follow(``ped``, ``vehicle``, ``targetEntity``, ``speed``, ``drivingStyle``, ``minDistance``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes a ped in a vehicle follow an entity.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``vehicle`` (``Vehicle``) -- The vehicle ID
* ``targetEntity`` (``Entity``) -- The target entity ID
* ``speed`` (``float``) -- The driving speed
* ``drivingStyle`` (``int``) -- Driving mode, `Driving Style calculator`_  
* ``minDistance`` (``float``) -- The minimum distance between ped vehicle and target vehicle

  * ``minDistance`` is ignored if drivingstyle is Avoiding Traffic, but Rushed is fine.  

.. _Driving Style calculator: https://vespura.com/fivem/drivingstyle/

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()

   target =  lobby.get_player_ped()
   
   vehicle = rage.gameplay.get_hash_key("ZENTORNO")

   rage.ai.task_vehicle_follow(ped, vehicle, target, 100, 6, 10)

================================

task_vehicle_shoot_at_coord(``ped``, ``x``, ``y``, ``z``, ``p4``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes a ped shoot at a coord from vehicle

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``x`` (``float``) -- X coord
* ``y`` (``float``) -- Y coord
* ``z`` (``float``) -- Z coord
* ``p4`` (``int``) -- Unknown -- seen to be ``0.5``

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   coords = self.get_coords_infront(10)
   coords2 = self.get_coords_infront(100)
   veh = scripting.spawn.spawn_vehicle(rage.gameplay.get_hash_key("ANNIHILATOR"), coords, 30)
   clone = rage.ped.clone_ped(self.get_ped(), true, true, false)
   rage.ai.task_enter_vehicle(clone, veh, 0, -1, 2.0, 1, 0)
   rage.ai.task_vehicle_shoot_at_coord(clone, coords2.x, coords2.y, coords2.z, 0.5)
   

================================

task_vehicle_shoot_at_ped(``ped``, ``target``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes a ped shoot another ped from vehicle.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``target`` (``Ped``) -- Target ped object
* ``p2`` (``int``) -- either ``1101004800``, ``100``, or ``5``

**Returns:**

* None

**Example:**

.. note::

  This example was not tested.


.. code-block:: lua
  :linenos:
  
  coords = self.get_coords_infront(10)
  veh = scripting.spawn.spawn_vehicle(rage.gameplay.get_hash_key("ANNIHILATOR"), coords, 30)
  clone = rage.ped.clone_ped(self.get_ped(), true, true, false)
  rage.ai.task_enter_vehicle(clone, veh, 0, -1, 2.0, 1, 0)
  rage.ai.task_vehicle_shoot_at_ped(clone, self.get_ped(), 100)

================================

task_wander_standard(``ped``, ``p1``, ``p2``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Makes ped walk around the area.

**Parameters:**

* ``ped`` (``Ped``) -- Ped object
* ``p1`` (``float``) -- Unknown
* ``p2`` (``int``) -- Unknown

.. note::

  if ``p1`` and ``p2`` are ``10``, the ped will walk around the area without a duration, anywhere.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:
   
   ped = self.get_ped()
   
   rage.ai.task_wander_standard(ped, 10, 10) -- walk around the area without a duration, anywhere

================================

.. _decorator:

Decorator namespace
----------------------

This namespace contains decoration-related game functions

.. warning::

  These functions are meant to be used by experienced users only.

  There are no examples for this namespace, as advanced users will know how to use it.

  *Sapienti sat*

================================

decor_get_bool(``entity``, ``propertyName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name

**Returns:**

* ``bool`` -- The value of the property

================================

decor_get_float(``entity``, ``propertyName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name

**Returns:**

* ``float`` -- The value of the property

================================

decor_get_int(``entity``, ``propertyName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name

**Returns:**

* ``int`` -- The value of the property

================================

decor_register(``propertyName``, ``type``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Register a property with the specified name and type.

**Parameters:**

* ``propertyName`` (``string``) -- Property name
* ``type`` (``int``) -- Property type

  * You can read more about property types here: :doc:`things/decor`

**Returns:**

* None

================================

decor_remove(``entity``, ``propertyName``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove a property.

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name

**Returns:**

* ``bool`` -- Whether the property was removed

  * ``true`` -- the property was removed
  * ``false`` -- the property was not found/was not removed/etc.

================================

decor_set_bool(``entity``, ``propertyName``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a boolean property.

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name
* ``value`` (``bool``) -- Value to set

**Returns:**

* ``bool`` -- Whether the value was succesfully set
  
  * ``true`` -- the value was set
  * ``false`` -- the value was not set.

================================

decor_set_float(``entity``, ``propertyName``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a float property.

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name
* ``value`` (``float``) -- Value to set

**Returns:**

* ``bool`` -- Whether the value was succesfully set
  
  * ``true`` -- the value was set
  * ``false`` -- the value was not set.

================================


decor_set_int(``entity``, ``propertyName``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set an integer property.

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name
* ``value`` (``int``) -- Value to set

**Returns:**

* ``bool`` -- Whether the value was succesfully set
  
  * ``true`` -- the value was set
  * ``false`` -- the value was not set.

  
================================

decor_set_time(``entity``, ``propertyName``, ``value``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a time property.

**Parameters:**

* ``entity`` (``Entity``) -- Entity object
* ``propertyName`` (``string``) -- Property name
* ``value`` (``int``) -- Value to set

**Returns:**

* ``bool`` -- Whether the value was succesfully set
  
  * ``true`` -- the value was set
  * ``false`` -- the value was not set.

================================

.. _interior:

Interior namespace
----------------------

This namespace contains interior-related game functions. 

================================

get_interior_at_coords_with_type(``x``, ``y``, ``z``, ``interiorType``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns the interior ID representing the requested interior at that location (if found?). The supplied interior string is not the same as the one used to load the interior.  

**Parameters:**

* ``x`` (``float``) -- The X position
* ``y`` (``float``) -- The Y position
* ``z`` (``float``) -- The Z position
* ``interiorType`` (``string``) -- The interior type

  * You can read more about interior types here: :doc:`things/inttypes`

**Returns:**

* ``int`` -- Interior ID.

**Example:**

.. code-block:: lua
   :linenos:

   rage.interior.get_interior_at_coords_with_type(-163.3628, -2385.161, 5.999994, "v_lesters")

================================

get_interior_from_entity(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the handle of the interior that the entity is in. Returns 0 if outside.  

**Parameters:**

* ``entity`` (``Entity``) -- The entity

**Returns:**

* ``int`` -- Interior ID.

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.interior.get_interior_from_entity(entity)

================================

refresh_interior(``interior``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Refresh a given interior.

**Parameters:**

* ``interior`` (``int``) -- The interior ID.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   interior = rage.interior.get_interior_from_entity(entity)

   rage.interior.refresh_interior(interior) -- Refreshes interior that the self's ped is in.

================================

.. _audio:

Audio namespace
----------------------

This namespace contains audio-related game functions. 

=================================

play_sound(``soundId``, ``audioName``, ``audioRef``, ``p3``, ``p4``, ``p5``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play a specified sound.

**Parameters:**

* ``soundId`` (``int``) -- Sound ID, it seems
* ``audioName`` (``string``) -- Sound name
* ``audioRef`` (``string``) -- Sound reference 
* ``p3`` (``bool``) -- Unknown
* ``p4`` (``Any``) -- Unknown
* ``p5`` (``bool``) -- Unknown

  * You can read more about audio names & refs `here <https://wiki.rage.mp/index.php?title=Sounds>`__.
  * `Also here <https://pastebin.com/A8Ny8AHZ>`__
   
**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.audio.play_sound(v_18, "Garage_Open", "CAR_STEAL_2_SOUNDSET", 1, 0, 1) -- Plays garage opening sound

=================================

play_sound_from_coord(``soundId``, ``audioName``, ``x``, ``y``, ``z``, ``audioRef``, ``isNetwork``, ``range``, ``p8``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play a specified sound from a given position.

**Parameters:**

* ``soundId`` (``int``) -- Sound ID, it seems
* ``audioName`` (``string``) -- Sound name
* ``x`` (``float``) -- X position
* ``y`` (``float``) -- Y position
* ``z`` (``float``) -- Z position
* ``audioRef`` (``string``) -- Sound reference
* ``isNetwork`` (``bool``) -- Make it networked so other players could also hear it (untested)
* ``range`` (``int``) -- Range of the sound
* ``p8`` (``bool``) -- Unknown

**Returns:**

* None

**Useful links:**

* `This <https://pastebin.com/eeFc5DiW>`__
* `This <https://gtaforums.com/topic/795622-audio-for-mods>`__

**Example:**

.. code-block:: lua
   :linenos:

   coords = self.get_coords_infront(100)
   rage.audio.play_sound_from_coord(-1, "Gas_Explosion", coords.x, coords.y, coords.z, "ARM_2_REPO_SOUNDS", 0, 0, 0) -- Plays gas explosion sound from 100m in front of the player.

=================================

play_sound_from_entity(``soundId``, ``audioName``, ``entity``, ``audioRef``, ``isNetwork``, ``p5``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play a specified sound from a given entity.

**Parameters:**

* ``soundId`` (``int``) -- Sound ID, it seems
* ``audioName`` (``string``) -- Sound name
* ``entity`` (``Entity``) -- Entity to play sound from
* ``audioRef`` (``string``) -- Sound reference
* ``isNetwork`` (``bool``) -- Make it networked so other players could also hear it (untested)
* ``p5`` (``int``) -- Unknown

**Returns:**

* None

**Useful links:**

* `This <https://pastebin.com/f2A7vTj0>`__
* `This <https://gtaforums.com/topic/795622-audio-for-mods>`__

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()
   rage.audio.play_sound_from_entity(-1, "Gas_Tanker_Explosion", entity, "BIG_SCORE_3A_SOUNDS", 0, 0)

================================

play_sound_frontend(``soundId``, ``audioName``, ``audioRef``, ``p3``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Play a specified sound from the frontend.

**Parameters:**

* ``soundId`` (``int``) -- Sound ID, it seems
* ``audioName`` (``string``) -- Sound name
* ``audioRef`` (``string``) -- Sound reference
* ``p3`` (``bool``) -- Unknown

**Returns:**

* None

**Useful links:**

* `This <https://pastebin.com/DCeRiaLJ>`__
* `This <https://gist.github.com/Sainan/021bd2f48f1c68d3eb002caab635b5a4>`__

**Example:**

.. code-block:: lua
   :linenos:

   rage.audio.play_sound_frontend(-1, "Garage_Door_Open", "GTAO_Script_Doors_Faded_Screen_Sounds", true) -- Plays garage opening sound

================================


stop_sound(``soundId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stop a specified sound.

**Parameters:**

* ``soundId`` (``int``) -- Sound ID, it seems

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.audio.stop_sound(v_18) -- Stops garage opening sound

=================================


.. _rope:

Rope namespace
----------------------

This namespace contains rope-related game functions. 

================================

activate_physics(``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activate physics for entity.

**Parameters:**

* ``entity`` (``Entity``) -- The entity

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   entity = self.get_ped()

   rage.rope.activate_physics(entity)

================================

add_rope(``x``, ``y``, ``z``, ``rotX``, ``rotY``, ``rotZ``, ``length``, ``ropeType``, ``maxLength``, ``minLength``, ``windingSpeed``, ``p11``, ``p12``, ``rigid``, ``p14``, ``breakWhenShot``, ``unkPtr``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a rope at the specific position, that extends in the specified direction when not attached to any entities.  

.. note::
   Rope does NOT interact with anything you attach it to, in some cases it make interact with the world AFTER it breaks (seems to occur if you set the type to -1).  
   Rope will sometimes contract and fall to the ground like you'd expect it to, but since it doesn't interact with the world the effect is just jaring.  

**Parameters:**

* ``x`` (``float``) -- Spawn coordinate X component.
* ``y`` (``float``) -- Spawn coordinate Y component.
* ``z`` (``float``) -- Spawn coordinate Z component.
* ``rotX`` (``float``) -- Rotation X component.
* ``rotY`` (``float``) -- Rotation Y component.
* ``rotZ`` (``float``) -- Rotation Z component.
* ``length`` (``float``) -- The initial length of the rope.
* ``ropeType`` (``int``) -- The rope type

  * ``0`` -- Thick, metal rope.
  * ``1`` -- Thin, twine rope.
  * ``2`` -- Thick , twine rope.
  * ``3`` -- See ``0``
  * ``4`` -- Thin, metal rope.
  * ``5`` -- Super thin, metal rope.
  * ``6`` -- See ``0``
  * ``7`` -- Game crashes
* ``maxLength`` (``float``) -- The maximum length the rope can drop.
* ``minLength`` (``float``) -- The minimum length the rope can be.
* ``windingSpeed`` (``float``) -- The speed in which the rope will wind if winding is started.
* ``p11`` (``bool``) -- Whether the rope should have collision. In original scripts this is followed by a LoadRopeData call when set.
* ``p12`` (``bool``) -- If max length is zero, and this is set to false the rope will become rigid (it will force a specific distance, what ever length is, between the objects).
* ``p14`` (``float``) -- The speed as which physics should run at. 1.0f is normal, 2.0f is twice as fast, -1.0f is time going backwards. This can affect gravity, etc.
* ``breakWhenShot`` (``bool``) -- Whether shooting the rope will break it.
* ``unkPtr`` (``Any``) -- Unknown parameter, always 0 in original scripts.

**Returns:**

* ``int`` -- Rope ID.

**Example:**

.. code-block:: lua
   :linenos:

   rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true) -- Creates a rope with a length of 100 meters, and a minimum length of 5 meters.

================================

attach_entities_to_rope(``ropeId``, ``ent1``, ``ent2``, ``ent1_x``, ``ent1_y``, ``ent1_z``, ``ent2_X``, ``ent2_Y``, ``ent2_Z``, ``length``, ``p10``, ``p11``, ``p12``, ``p13``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attaches entity 1 to entity 2 through a rope.

.. note::The position supplied can be anywhere, and the entity should anchor relative to that point from it's origin.  

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID
* ``ent1`` (``Entity``) -- Entity 1
* ``ent2`` (``Entity``) -- Entity 2
* ``ent1_x`` (``float``) -- Entity 1 ``X`` coordinate.
* ``ent1_y`` (``float``) -- Entity 1 ``Y`` coordinate.
* ``ent1_z`` (``float``) -- Entity 1 ``Z`` coordinate.
* ``ent2_x`` (``float``) -- Entity 2 ``X`` coordinate.
* ``ent2_y`` (``float``) -- Entity 2 ``Y`` coordinate.
* ``ent2_z`` (``float``) -- Entity 2 ``Z`` coordinate.
* ``length`` (``float``) -- The initial length of the rope.
* ``p10`` (``bool``) -- Unknown.
* ``p11`` (``bool``) -- Unknown.
* ``p12`` (``Any``) -- Unknown.
* ``p13`` (``Any``) -- Unknown.

**Returns:**

* None

**Example:**

.. note::

   This example was not tested.

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   entity1 = self.get_ped()

   entity2 = lobby.get_player_ped(lobby.get_host())

   rope = rage.rope.attach_entities_to_rope(rope, entity1, entity2, 79, 420, 69, 59, 420, 69, 10)

================================

delete_rope(``ropeId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a rope.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID to delete.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.delete_rope(rope)

================================

detach_rope_from_entity(``ropeId``, ``entity``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Detach a rope from entity.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID to delete.
* ``entity`` (``Entity``) -- The Entity to detach

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   entity = self.get_ped()

   rage.rope.detach_rope_from_entity(rope, entity)

================================

does_rope_exist(``ropeId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether a rope exists.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID to check.

**Returns:**

* ``bool`` -- The status of the check:

  * ``true`` -- Rope exists
  * ``false`` -- Rope does not exist

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.does_rope_exist(rope)

================================

rope_are_textures_loaded()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checks whether rope textures are loaded.

**Parameters:**

* None

**Returns:**

* ``bool`` -- The status of the check:

  * ``true`` -- Rope textures are loaded
  * ``false`` -- Rope textures are not loaded

**Example:**

.. code-block:: lua
   :linenos:

   rage.rope.rope_are_textures_loaded()

================================

rope_force_length(``ropeId``, ``length``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forces a rope to a certain length.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID
* ``length`` (``float``) -- The rope length

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.rope_force_length(rope, 50) -- Reduces the rope length from 100 to 50

================================

rope_load_textures()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Loads rope textures for all ropes in the current scene.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.rope.rope_load_textures()

================================

rope_unload_textures()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unloads rope textures for all ropes in the current scene.

**Parameters:**

* None

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rage.rope.rope_unload_textures()

================================

start_rope_unwinding_front(``ropeId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start rope unwinding from the front.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.start_rope_unwinding_front(rope)

================================

start_rope_winding(``ropeId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start rope winding.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.start_rope_winding(rope)

================================

stop_rope_unwinding_front(``ropeId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stop rope unwinding from the front.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.stop_rope_unwinding_front(rope)

================================

stop_rope_winding(``ropeId``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stop rope winding.

**Parameters:**

* ``ropeId`` (``int``) -- The rope ID.

**Returns:**

* None

**Example:**

.. code-block:: lua
   :linenos:

   rope = rage.rope.add_rope(69, 420, 69, 1, 1, 5, 10, 2, 100, 5, 1, true, true, 1.0, true)

   rage.rope.stop_rope_winding(rope)

================================
