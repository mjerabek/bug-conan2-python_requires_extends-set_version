from conan import ConanFile
from conan.errors import ConanException


class ConanBase:
    def set_version(self):
        self.version = '1.2.3'


class Pkg(ConanFile):
    name = "conan_base"
    version = "1.0.0"
    package_type = "python-require"
