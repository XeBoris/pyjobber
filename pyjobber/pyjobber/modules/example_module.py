import logging
from pyjobber.interfaces.decorator import Collector


@Collector
class ExampleModule():

    def __init__(self):
        #define a list of necessary arguments beforehand:
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
            logging.warning("Discrepancy between requiered inputs from the terminal:")
            logging.warning(" -> {0}".format(list(self.list_arguments.keys())))
            logging.warning("and arguments which are handed over:")
            logging.warning( " -> {0}".format(list(self.def_arguments.keys())))

    def init(self, args):
        logging.info(f"Running module: {self.__class__.__name__}")
        self.arg_eval(args)

    def run(self):
        logging.info("Start your example process")
        if self.init_arguments == False:
            return 1 #not ok!

        self.do_something()
        #return 0 if you reach the end of the run() memberfunction
        return 0

    def do_something(self):
        logging.info("Do something...")
