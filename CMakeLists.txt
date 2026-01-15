cmake_minimum_required(VERSION 3.17...4.0)
project(linkermc)

# find python
find_package(Python3 REQUIRED COMPONENTS Development.Module)
#if (CMAKE_CROSSCOMPILING AND NOT (APPLE AND "$ENV{CIBUILDWHEEL}" STREQUAL "1"))
#    find_package(Python3 REQUIRED COMPONENTS Development.Module)
#else()
#    find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
#endif()

# find pybind11
if (NOT USE_GLOBAL_PYBIND11 AND Python3_EXECUTABLE)
    if (NOT pybind11_ROOT OR NOT EXISTS ${pybind11_ROOT})
        message(STATUS "Detecting pybind11 CMake location")
        execute_process(COMMAND ${Python3_EXECUTABLE}
            -m pybind11 --cmakedir
            OUTPUT_VARIABLE PY_BUILD_PYBIND11_ROOT
            OUTPUT_STRIP_TRAILING_WHITESPACE
            RESULT_VARIABLE PY_BUILD_CMAKE_PYBIND11_RESULT)
        # If it was successful
        if (PY_BUILD_CMAKE_PYBIND11_RESULT EQUAL 0)
            message(STATUS "pybind11 CMake location: ${PY_BUILD_PYBIND11_ROOT}")
            set(pybind11_ROOT ${PY_BUILD_PYBIND11_ROOT}
                CACHE PATH "Path to the pybind11 CMake configuration." FORCE)
        else()
            unset(pybind11_ROOT CACHE)
        endif()
    endif()
endif()
find_package(pybind11 ${ARGN} REQUIRED CONFIG CMAKE_FIND_ROOT_PATH_BOTH)

pybind11_add_module(importworld
    src/linkermc/importworld/bindings.cpp
    src/linkermc/importworld/main.cpp
)

target_include_directories(importworld PRIVATE
  ${CMAKE_CURRENT_SOURCE_DIR}/src/linkermc/importworld
)

## Find the Python interpreter and the development files
#if (CMAKE_CROSSCOMPILING AND NOT (APPLE AND "$ENV{CIBUILDWHEEL}" STREQUAL "1"))
#    find_package(Python3 REQUIRED COMPONENTS Development.Module)
#else()
#    find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
#endif()
#
## Find the pybind11 package
#include(cmake/QueryPythonForPybind11.cmake)
#find_pybind11_python_first()
#
## Compile the example Python module
#pybind11_add_module(_add_module MODULE "src/ext/add_module.cpp")
#set_target_properties(_add_module PROPERTIES
#    DEBUG_POSTFIX "${CMAKE_DEBUG_POSTFIX}${PYTHON_MODULE_DEBUG_POSTFIX}")
#target_compile_definitions(_add_module PRIVATE
#    MODULE_NAME=$<TARGET_FILE_BASE_NAME:_add_module>
#    VERSION_INFO="${PY_FULL_VERSION}"
#)
## Hide all symbols by default (including external libraries on Linux)
#set_target_properties(_add_module PROPERTIES
#    CXX_VISIBILITY_PRESET "hidden"
#    VISIBILITY_INLINES_HIDDEN true)
#if (CMAKE_SYSTEM_NAME MATCHES "Linux")
#    target_link_options(_add_module PRIVATE "LINKER:--exclude-libs,ALL")
#endif()
#
## Install the Python module
#install(TARGETS _add_module
#        EXCLUDE_FROM_ALL
#        COMPONENT python_modules
#        DESTINATION ${PY_BUILD_CMAKE_IMPORT_NAME})
#
## Generate stubs for the Python module
#set(WITH_PY_STUBS_DEFAULT On)
#if (CMAKE_CROSSCOMPILING)
#    set(WITH_PY_STUBS_DEFAULT Off)
#endif()
#option(WITH_PY_STUBS
#    "Generate Python stub files (.pyi) for the Python module."
#    ${WITH_PY_STUBS_DEFAULT})
#if (WITH_PY_STUBS)
#    include(cmake/Pybind11Stubgen.cmake)
#    pybind11_stubgen(_add_module
#        PACKAGE ${PY_BUILD_CMAKE_IMPORT_NAME}
#        COMPONENT python_stubs)
#endif()
