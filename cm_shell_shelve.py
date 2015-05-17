from __future__ import print_function
import os
import subprocess
import shelve
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_shelve.command_shelve import command_shelve

class cm_shell_shelve:

    def activate_cm_shell_shelve(self):
        self.register_command_topic('mycommands', 'shelve')

    @command
    def do_shelve(self, args, arguments):
        """
        ::
cm
          Usage:
              shelve REQARG1 OPTARG1 OPTARG2 OPTARG3

          Performs various shelve functions explained below

          Arguments:

            REQARG1     Initial function to perform. Possible values: deploy, start, clear, set, delete, list
                        deploy : deploys shelve
                        start  : starts shelve, requires OPTARG1 to be the shelve filename (do not include '.db')
                        clear  : removes the shelve file, requires OPTARG1 to be the shelve filename (do not include '.db')
                        set    : adds data to a given index, requires OPTARG1 to be the shelve filename (do not include '.db'), OPTARG2 to be the index, and OPTARG3 to be the data
                        delete : removes the data at a given index, requires OPTARG1 to be the shelve filename (do not include '.db') and OPTARG2 to be in the index
                        list   : lists the contents, requires OPTARG1 to be the shelve filename (do not include '.db')

            OPTARG1     Set to shelve filename (do not include '.db') unless REQARG1 is
                        deploy : set to zero

            OPTARG2     Set to zero unless REQARG1 is
                        deploy : set to zero
                        set    : the index
                        delete : the index

            OPTARG3     Set to zero unless REQARG1 is
                        set    : the data

          Options:

        """

        if arguments["REQARG1"] == "deploy":

            subprocess.call(["pip", "install", "shelve2"])

        elif arguments["REQARG1"] == "start":

            shelveFilename = arguments["OPTARG1"]
            shelveFile = shelve.open(shelveFilename)

            Console.info("Database file " + shelveFilename + ".db created.")

        elif arguments["REQARG1"] == "clear":

            shelveFilename = arguments["OPTARG1"]

            subprocess.call(["rm", shelveFilename + ".db"])

            Console.info("Database file " + shelveFilename + ".db removed.")

        elif arguments["REQARG1"] == "set":

            shelveFilename = arguments["OPTARG1"]
            shelveFile = shelve.open(shelveFilename)

            index = arguments["OPTARG2"]
            data = arguments["OPTARG3"]

            shelveFile[index] = data

            Console.info(data + " has been written to index " + index)

        elif arguments["REQARG1"] == "delete":

            shelveFilename = arguments["OPTARG1"]
            shelveFile = shelve.open(shelveFilename)

            index = arguments["OPTARG2"]

            del shelveFile[index]

            Console.info("Data at index " + index + " has been deleted.")

        elif arguments["REQARG1"] == "list":

            shelveFilename = arguments["OPTARG1"]
            shelveFile = shelve.open(shelveFilename)

            keyList = shelveFile.keys()

            if not keyList:
                Console.info("No data in shelve file.")

            else:
                Console.info("Output format is Index : Data")

                for key in keyList:
                    Console.info(key + " : " + shelveFile[key])

        pass

if __name__ == '__main__':
    command = cm_shell_shelve()
    command.do_shelve()
