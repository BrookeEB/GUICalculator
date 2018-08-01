from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(windows=[{'script': 'filename.py'}], \
            options={"py2exe": {"includes": ["decimal", "Tkinter", \
            "tkFileDialog", "csv", "xml.dom.minidom", "os"], \
            'bundle_files': 1, 'compressed': False}}, \
            zipfile = None)

self.dlls_in_exedir = [python_dll,
                       "w9xpopen%s.exe" % (is_debug_build and "_d" or ""),
                       "msvcr71%s.dll" % (is_debug_build and "d" or ""),
                       "tcl85.dll",
                       "tk85.dll"]