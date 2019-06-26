# -*- coding: utf-8 -*-
"""Pyjobber

Author: Boris Bauermeister
Email: Boris.Bauermeister@gmail.com
"""

import argparse
import time
import logging

# load modules:
from pyjobber.interfaces.decorator import CallCollector, ClassCollector
# Load further modules if necessary:
from pyjobber.modules.example_module import ExampleModule
from pyjobber.modules.scratchloader import ScratchLoader
from pyjobber.interfaces.mongodb_interface import MongoDBapi

# setup a simple logger:
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def main(*args):
    logging.info("Run pyjobber")

    parser = argparse.ArgumentParser(description="A simple job pilot")
    # From here the input depends on the usage of the command
    parser.add_argument('module', nargs='?', default="default",
                        help="Select your work module")
    parser.add_argument('--once', dest="once", action='store_true',
                        help="Run pyjobber only once")
    parser.add_argument('--sleep', dest="sleep", type=int, default=10,
                        help="Usage:\n  --sleep N: Run each N seconds")

    # dedicated parser arguments for individual modules:
    parser.add_argument('--scratch', dest="scratch", type=str, default=None,
                        help="Path to scratch directory")

    # ready with parsing:
    args = parser.parse_args()

    # evaluate argparse:
    _once = args.once
    _sleep = args.sleep

    if _sleep < 1:
        _once = True

    # evaluate module choice:
    if args.module == "default" or args.module not in CallCollector:
        logging.warning("Select from a list of modules:")
        for i_module in CallCollector:
            logging.warning(str("-> " + i_module))
        exit()

    while True:

        if args.module != 'default' and args.module in ClassCollector:
            ClassCollector[args.module].init(args)
            status = ClassCollector[args.module].run()
            if status == 1:
                logging.error("Module did not start")

        if _once == True:
            break
        time.sleep(_sleep)


def version():
    import pyjobber
    print("----------------------------------------------")
    print("Hello world, my name is pyjobber!")
    print(" - I help you run tasks on single cores.")
    print(" - You are welcome to plug in in you own code.")
    print(f" - My version is: {pyjobber.__version__}")
    print("----------------------------------------------")


def ping():
    db = MongoDBapi()
    db.connect()
