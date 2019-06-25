==========================
How to write your own task
==========================

I will guide you through the basic concept of writing your own module in pyjobber to get your task done.

How is a module organized?
--------------------------

Each module consist of a Python class which you can find in

| pyjobber
| │
| ├──pyjobber
|       │
|       ├──interfaces
|       │   │
|       │   ├──decorator.py
|       │   ├──mongodb_interface.py
|       │   ├──your_interface.py
|       │  
|       ├──modules
|           │
|           ├──example_module.py
|           ├──your_task.py

    
The most straight forward way to build your module is to follow the example_module.py class. Each module looks like this:

.. code-block:: python
  :linenos:
  :emphasize-lines: 11,14,17

    your_task.py:

    import logging
    from pyjobber.interfaces.decorator import Collector
    #Further imports...

    @Collector
    class YOURTASK():
        def __init__(self):
            pass
        def init(self, arguments):
            #setup your module with arguments
            #if not needed
        def run(self, arguments):
            #Run Execute your task
            self.do_something()
        def do_something()
            #more complicated tasks are going in that member function
        
The most important member functions are 
  * __init__() - The Python constructor
  * init() - Set up your module with arguments and define variables
  * run()  - Execute your module. Run your calculations here and use further member functions if your workflow is more complicated

What is an interface?
---------------------
Each ETL has its own way to to communicate with files, databases or users and therefore it becomes important to write your interface class which matches the needs of your workflow and therefore your modules. Pyjobber comes with a simple interface for MongoDB database which is based on pymongo. Please check the code before going in production. The module is supposed to be an example.

Feel free to run and add your interfaces to pyjobber if you start to contribute to the project. By default are not code structure requierements foreseen besides that the interface is supposed to be a class with a valid constructor.

Module/Interface Compile
------------------------
Pyjobber is only a very simple ETL workflow manager and therefore you can get your new task working by simply install pyjobber in your Python environment. For installation help watch out here (:ref:'_Installation')