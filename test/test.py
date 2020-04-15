import sys
sys.path.append("../")
from ini.core import INI

ini = INI("config.ini")

print(ini.section_count("jack"))
print(ini.find(0, None, "global"))
print(ini.find(0, "jack", "name"))
print(ini.find(0, "jack", "sex"))
print(ini.find(0, "jack", "test"))
print(ini.find(1, "jack", "name"))
