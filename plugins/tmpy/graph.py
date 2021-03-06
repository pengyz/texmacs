#!/usr/bin/env python
###############################################################################
##
## MODULE      : graph.py
## DESCRIPTION : An abstract Graph class
## COPYRIGHT   : (C) 2019  Darcy Shen
##
## This software falls under the GNU general public license version 3 or later.
## It comes WITHOUT ANY WARRANTY WHATSOEVER. For details, see the file LICENSE
## in the root directory or <http://www.gnu.org/licenses/gpl-3.0.html>.

import os
from .protocol import *


class Graph(object):
    name = ""
    message = ""
    height = 0
    width = 0

    def set_height(self, h):
        self.height = h

    def set_width(self, w):
        self.width = w

    def greet(self):
        for x in self.message.split("\n"):
            if len(x) == 0:
                pass
            else:
                flush_verbatim (x + "\n")
                flush_prompt (self.name + "] ")

    def available(self):
        return len(self.message) > 0

    def evaluate(self, code):
        pass

    def get_tmp_dir(self):
        return os.getenv("TEXMACS_HOME_PATH") + "/system/tmp/"

    def get_png_path(self):
        png = self.get_tmp_dir() + self.name + ".png" +\
            "?" + "width=" + str(self.width) +\
            "&" + "height=" + str(self.height)
        if os.path.isfile(png):
            os.remove(png)
        return png

    def get_eps_path(self):
        return self.get_tmp_dir() + self.name + ".eps"

    def get_eps(self):
        return self.get_eps_path() +\
            "?" + "width=" + str(self.width) +\
            "&" + "height=" + str(self.height)
