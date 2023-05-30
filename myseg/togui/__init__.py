"""
GUI for myseg
"""
import sys

from myseg.global_var import user_global_var as gl

result = gl.load_config()
if result != 101:
    sys.exit()
result = gl.check_plat()
if result != 101:
    sys.exit()
