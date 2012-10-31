#!/usr/bin/env python
# encoding: utf-8
'''
src.pingex -- shortdesc

src.pingex is a description

It defines classes_and_methods

@author:     Kazushige TAKEUCHI
            
@copyright:  2012 Kazushige TAKEUCHI. All rights reserved.
            
@license:    original license 

@contact:    kazushige.takeuchi@gmail.com
@deffield    updated: Updated
'''

import sys
import os

from optparse import OptionParser
from ui.pingexui import Ui_Form

__all__ = []
__version__ = 0.1
__date__ = '2012-11-01'
__updated__ = '2012-11-01'

DEBUG = 1
TESTRUN = 0
PROFILE = 0



class PingEx(QtGui.QMainWindow):
    def __init__(self):
        self.helper = Ui_Form()
        self.helper.setupUi(self)
        
    pass


def main(argv=None):
    '''Command line options.'''
    
    program_name = os.path.basename(sys.argv[0])
    program_version = "v0.1"
    program_build_date = "%s" % __updated__
 
    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
    #program_usage = '''usage: spam two eggs''' # optional - will be autogenerated by optparse
    program_longdesc = '''''' # optional - give further explanation about what the program does
    program_license = "Copyright 2012 user_name (organization_name)                                            \
                Licensed under the Apache License 2.0\nhttp://www.apache.org/licenses/LICENSE-2.0"
 
    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
        parser.add_option("-i", "--in", dest="infile", help="set input path [default: %default]", metavar="FILE")
        parser.add_option("-o", "--out", dest="outfile", help="set output path [default: %default]", metavar="FILE")
        parser.add_option("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %default]")
        
        # set defaults
        parser.set_defaults(outfile="./out.txt", infile="./in.txt")
        
        # process options
        (opts, args) = parser.parse_args(argv)
        
        if opts.verbose > 0:
            print("verbosity level = %d" % opts.verbose)
        if opts.infile:
            print("infile = %s" % opts.infile)
        if opts.outfile:
            print("outfile = %s" % opts.outfile)
            
        # MAIN BODY #
        
        import PySide
        from PySide.QtGui import QApplication
        import ui.pingexui.Ui_Form

        
        qapp = QApplication(sys.argv)
        qmain = Ui_Form()
        qmain.show()
        exit(qapp._exec())
        
        
        
    except Exception, e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'src.pingex_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())