import os
import csv
import json
import datetime
import copy
import numpy
from pyjobber.interfaces.decorator import Collector
from pyjobber.interfaces.mongodb_interface import MongoDBapi

@Collector
class ScratchLoader(MongoDBapi):

    def __init__(self):
        #define a list of necessary arguments beforehand:
        self.list_arguments = {'scratch': {'type': str, 'default': "./"}}
        self.def_arguments = {}
        self.init_arguments = False

    def arg_eval(self, args):
        for arg in vars(args):
            if arg in list(self.list_arguments.keys()) and type(getattr(args, arg)) == self.list_arguments[arg]['type']:
                self.def_arguments[arg] = getattr(args, arg)

        if list(self.def_arguments.keys()) == list(self.list_arguments.keys()):
            self.init_arguments = True

    def init(self, args):
        print(f"Running module: {self.__class__.__name__}")
        self.arg_eval(args)

    def run(self):
        if self.init_arguments == False:
            return 1 #not ok!

        self.path = os.path.split(self.def_arguments['scratch'])[0]    #use everything before the last / (win/linux conform)
        self.base = os.path.split(self.path)[0]

        #Run an initial connect for the MongoDB interface:
        self.db = MongoDBapi()
        self.db.connect()

        # init an archiv folder for later clean up:
        self.init_archiv_path()

        # here we go:
        self.load_path()

        #return 0 if you reach this point.
        return 0

    def init_archiv_path(self):
        self.archive_folder = "{0}_archive".format(os.path.basename(os.path.normpath(self.path)))
        if not os.path.exists(os.path.join(self.base, self.archive_folder)):
            os.makedirs(os.path.join(self.base, self.archive_folder))

    def archiver(self, mfile):
        old_p = os.path.join(self.path, mfile)
        new_p = os.path.join(self.base, self.archive_folder, mfile)
        os.rename(old_p, new_p)

    def data_massage(self, df):
        #this code might be sorted into another class later
        #Aim: clean data, correct for types from csv files and deal with
        #     missing data

        #attention! Assuming pre knowledge about types here!

        dk = json.loads(df['content'])
        for ik in dk:
            for key, val in ik.items():
                if key != 'temperature' and len(val) == 0:
                    ik[key] = numpy.nan
                if key == 'skipped_beat' and len(val) != 0:
                    ik[key] = float(val)
                if key == 'at_risk' and len(val) != 0:
                    ik[key] = int(val)
                if key == 'price' and len(val) != 0:
                    ik[key] = float(val)

        df['content'] = dk
        return df

    def load_path(self):
        ### Assume no corruption

        for r, d, f in os.walk(self.path):
            # simple check to exclude hidden folders
            if '/.' in r:
                continue
            # run through csv files, create dataframes, append them
            if len(f) == 0:
                continue

            for file in f:

                dc_temp = {}
                dc_temp['filename'] = None
                dc_temp['date'] = None
                dc_temp['content'] = []

                #Analyse csv files along the input path (self.path)
                if '.csv' in file:
                    f_csv = open(os.path.join(r, file), 'rU')
                    reader = csv.DictReader( f_csv, delimiter=',')
                    reader_json = json.dumps([row for row in reader])
                    #define filename and date independent in case we want to change
                    #the file names later (important: date information must come from
                    #file name
                    dc_temp['filename'] = file
                    dc_temp['date'] = datetime.datetime.strptime(file.split("/")[-1].split(".")[0], '%Y-%m-%d')
                    dc_temp['content'] = reader_json

                    dc_temp_old = copy.deepcopy(dc_temp)
                    dc_temp = self.data_massage(dc_temp)


                    #decide if we add these data to our database:
                    try:
                        db_find_filename = list(self.db.find_one(dc_temp))[0]['filename']
                    except:
                        db_find_filename = None

                    if dc_temp['filename'] == db_find_filename:
                        print("File exist in db")
                        print(db_find_filename, dc_temp['filename'])

                        # Clean up path to avoid heavy I/O on the system
                        self.archiver(file)

                    else:
                        print("Not in the db: ", dc_temp['filename'], " -> Add it")
                        self.db.insert(dc_temp)


        print("Read:")
        self.db.read_all()


