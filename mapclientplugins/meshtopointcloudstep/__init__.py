
"""
MAP Client Plugin - Generated from MAP Client v0.24.0
"""

__version__ = '0.1.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'MeshToPointCloud'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.meshtopointcloudstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.meshtopointcloudstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc