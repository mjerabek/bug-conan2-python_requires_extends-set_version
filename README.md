In `foo/conanfile.py`, `set_version` either tries to use inherited `set_version`, or use the method directly from the `python_require`d module.
The first doesn't work, the second does.
