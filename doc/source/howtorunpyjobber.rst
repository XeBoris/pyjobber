===================
How to run pyjobber
===================

Pyjobber uses argparse to cast several command line commands into pyjobber.

List modules
------------
After pyjobber is installed (e.g. with your new task), you can get a list modules by simply running pyjobber without any commands. 

.. code-block:: bash

    [~/]$ pyjobber
    INFO:Run the Jobber
    WARNING:Select from a list of modules:
    WARNING:-> ExampleModule
    WARNING:-> ScratchLoader
    
To run a specific module it is enough to select it in advance:

.. code-block:: bash

    [~/]$ pyjobber ExampleModule
    

You can get any time a help overview (--help)

.. code-block:: bash

    [~/]$ pyjobber ExampleModule --help


If you have a specific pyjobber adjustment it is suggested to move your argparse evulation into each module instead of the pyjobber.py main() function. 

Last but not least, you can choose to parameter option how often a certain task should be executed:

.. code-block:: bash

    [~/]$ pyjobber ExampleModule --once
    
The option --once runs the task only once

.. code-block:: bash

    [~/]$ pyjobber ExampleModule --sleep N
    
The option --sleep N defines the sleep time between executing tasks continously.