from conan import ConanFile
from conan.tools.cmake import cmake_layout


class FooRecipe(ConanFile):
    name = "foo"
    package_type = "application"
    python_requires = "conan_base/[>=1.0 <2.0]"
    python_requires_extend = "conan_base.ConanBase"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        cmake_layout(self)

    def set_version(self):
        # This doesn't work, because the inheritance is not yet done.
        super().set_version()
        # This works, which means that the python requires is already resolved.
        # self.python_requires["conan_base"].module.ConanBase.set_version(self)

        # If this whole method is missing here, we get "ERROR: conanfile didn't specify version".
