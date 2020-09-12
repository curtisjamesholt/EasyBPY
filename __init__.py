#region INFO
'''
    == EasyBPY 0.0.1 ==
    Created by Curtis Holt
    https://curtisholt.online/links
    ---
    https://YouTube.com/CurtisHolt
    https://curtisholt.online
    https://twitter.com/curtisjamesholt
    https://instagram.com/curtisjamesholt
    ---
    This purpose of this module is to simplify the use of the Blender API
    (bpy) by creating an extra layer of abstraction that is more human-
    readable, memorizable and reduces the user's exposure to complex code
    paths.
    EasyBPY can be added to Blender by installing it into the:
                ../scripts/modules
    folder in the user preferences. The file can also be re-packaged with
    any other addon, so long as the developer respects the limitations of
    the GPL license, outlined below.
'''
'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#endregion

#region IMPORTS
import bpy
from mathutils import Vector
from math import radians

from .collections import *
from .cursor import *
from .materials import *
from .meshes import *
from .modifiers import *
from .nodes import *
from .objects import *
from .primitives import *
from .selection import *
from .shading import *
from .text import *
from .textures import *
from .transformations import *
from .utils import *
from .vertex_groups import *
from .visibility import *
#endregion
