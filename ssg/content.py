import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$" # Raw string, so append with r
    __regex = re.compile(__delimiter, re.MULTILINE)