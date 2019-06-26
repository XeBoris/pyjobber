"""
.. module:: example_module
   :platform: Unix
   :synopsis: An example module to show how a basic module is designed

.. moduleauthor:: Boris Bauermeister <Boris.Bauermeister@gmail.com>

"""

import logging
from pyjobber.interfaces.decorator import Collector


@Collector
class ExampleModule():

    def __init__(self):
        """ExampleModule:__init__()

        Setup your example module as you wish.
        The __init__() construct acts mainly as class name collector.
        Limit your variables in this function will safe memory in case of
        heavy calculations.        
        """

        self.list_arguments = {'example': {'type': str, 'default': "./"}}
        self.def_arguments = {}
        self.init_arguments = False

    def arg_eval(self, args):
        for arg in vars(args):
            if arg in list(self.list_arguments.keys()) and type(getattr(args, arg)) == self.list_arguments[arg]['type']:
                self.def_arguments[arg] = getattr(args, arg)

        if list(self.def_arguments.keys()) == list(self.list_arguments.keys()):
            self.init_arguments = True
        else:
            logging.warning(
                "Discrepancy between requiered inputs from the terminal:")
            logging.warning(" -> {0}".format(list(self.list_arguments.keys())))
            logging.warning("and arguments which are handed over:")
            logging.warning(" -> {0}".format(list(self.def_arguments.keys())))

    def init(self, args):
        """ExampleModule:init()

        The init module which should hold all variable declarations and class constructors.

        :param args: Parse some arguments from the commandline
        """
        logging.info(f"Running module: {self.__class__.__name__}")
        self.arg_eval(args)

    def run(self):
        """ExampleModule:run()

        Run your ExampleModule!
        The run memberfunction can hold code itself or complicated calculations
        are distributed along several memberfunctions of this module class
        For example: self.do_something()

        :return 0: Hint: You can change it but keep in mind: 0 for success and 1 for failure.
        """

        logging.info("Start your example process")
        if self.init_arguments == False:
            return 1  # not ok!

        self.do_something()
        # return 0 if you reach the end of the run() memberfunction
        return 0

    def do_something(self):
        """ExampleModule:do_something()

        Here goes your code in if you have complicated calculations to run.

        """

        logging.info("Do something...")
