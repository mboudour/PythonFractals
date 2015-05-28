# Select a color from colorbrewer schemes

# Copyright (c) 2014 Ludger Sandig
# This file is part of apollon.

# Apollon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Apollon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Apollon.  If not, see <http://www.gnu.org/licenses/>.


import json

class ColorMap(object):
    """
    Map numbers to colors.
    """
    def __init__(self, default):
        """
        @param default: Is returned when a number can't be mapped.
        """
        self.pairs = []
        self.default = default

    def add_interval(self, left, right, color):
        """
        A number in interval [left,right] gets mapped to color.
        """
        self.pairs.append((left, right, color))

    def color_for(self, number):
        """
        Map number to color. If not found, return default value.
        """
        ret = self.default
        for p in self.pairs:
            if (number >= p[0]) and (number <= p[1]):
                ret = p[2]
                break
        return ret

class ColorScheme(object):
    """
    Color Scheme helper class.
    """
    def __init__(self, filename):
        """
        Load color scheme definitions from json file.
        """
        json_data = open(filename)

        self.schemes=json.load(json_data)
        json_data.close()

    def info(self):
        """
        Get information on available color schemes
        """
        infos = []
        for name in self.schemes:
            smallest = min(self.schemes[name], key=lambda k: len(self.schemes[name][k]))
            biggest = max(self.schemes[name], key=lambda k: len(self.schemes[name][k]))
            infos.append({"name" : name, "low" : int(smallest), "high" : int(biggest)})
        return infos

    def makeMap(self, frm, to, name, res):
        """
        Construct a L{ColorMap} that maps numbers between frm and to to color scheme name with resolution res.
        """
        # TODO: Proper error handling when name or res are not available
        delta = to-frm
        step = delta/res
        colors = self.schemes[name][str(res)]
        mp = ColorMap("none")
        # Items are (lower_bound, color)
        for n in range(res):
            mp.add_interval(frm + n*step, frm + (n+1)*step, colors[n])
        return mp
