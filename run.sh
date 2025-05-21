#!/usr/bin/env bash

rm -Rf .conan2
conan profile detect
(cd base && conan create .)
(cd foo && conan create .)
