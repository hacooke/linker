#include <pybind11/pybind11.h>
#include "main.h"

PYBIND11_MODULE(importworld, m) {
    m.doc() = "LinkerMC importworld module";
    m.def("hello", &hello, "say hello");
}
