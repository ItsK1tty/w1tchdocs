Getting Started
================

.. _gettingstarted:

Is this your first time using the LUA Engine? This is the place to get started!

This page gives a brief introduction to the framework.

A Minimal script
----------

Let\’s make a script that responds to a specific key and walk you through it.

It looks something like this:

.. code-block:: lua
    :linenos:

    function my_script_function()
        -- Test key press
        bKeyPressed = system.is_key_pressed("F")
        if bKeyPressed then
            system.log_warning("Pressed F to pay respect!")
        end
    end
    system.add_task("My script task", "luaTestTaskHash", -1, my_script_function)

Let’s name this file ``example.lua``.

There’s a lot going on here, so let’s walk you through it step by step.

#. The first line defines the name of the function. It can be any name you want.
#. Next, there's the comment. Comments are started with -- and are a good way to explain what something does or keep a certain feature from executing.
#. We then check if the key is pressed. This is done by calling the ``system.is_key_pressed`` function. The first and only argument is the key name.
#. If the key is pressed, we send the "Pressed F to pay respect!" message to the console.
#. Finally, end keywords are used to end the function or a logic expression.
#. The last line of the script is to add the function to the main loop, or task list. The main loop runs the feature over and over, that's why we don't use a loop in the function itself.

Now that we've made a script, we have to *run* the script. Inject DIS2RBED, and the script will start running right after DIS2RBED is initialized.

You can now play around with your basic script.