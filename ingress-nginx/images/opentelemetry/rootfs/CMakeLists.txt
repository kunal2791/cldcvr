#!/bin/bash

# Copyright 2021 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cmake_minimum_required(VERSION 3.11 FATAL_ERROR)

project(
  dependencies
  LANGUAGES CXX
  VERSION 0.0.1)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "-O2 -fpic")
set(CMAKE_VERBOSE_MAKEFILE ON CACHE BOOL "ON" FORCE)

set(CMAKE_BUILD_TYPE
    Release
    CACHE STRING "Build type" FORCE)

include(GNUInstallDirs)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY
    ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY
    ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY
    ${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_BINDIR})

set(INSTALL_LIBDIR
    ${CMAKE_INSTALL_LIBDIR}
    CACHE PATH "directory for libraries")
set(INSTALL_BINDIR
    ${CMAKE_INSTALL_BINDIR}
    CACHE PATH "directory for executables")
set(INSTALL_INCLUDEDIR
    ${CMAKE_INSTALL_INCLUDEDIR}
    CACHE PATH "directory for header files")

set(DEF_INSTALL_CMAKEDIR share/cmake/${PROJECT_NAME})
set(INSTALL_CMAKEDIR
    ${DEF_INSTALL_CMAKEDIR}
    CACHE PATH "directory for CMake files")

set_property(DIRECTORY PROPERTY EP_BASE ${CMAKE_BINARY_DIR}/subs)

set(STAGED_INSTALL_PREFIX ${CMAKE_BINARY_DIR}/stage)
message(STATUS "${PROJECT_NAME} staged install: ${STAGED_INSTALL_PREFIX}")

find_package(OpenSSL REQUIRED)
message("OpenSSL include dir: ${OPENSSL_INCLUDE_DIR}")
message("OpenSSL libraries: ${OPENSSL_LIBRARIES}")

find_package(Protobuf REQUIRED)
find_package(gRPC REQUIRED)
find_package(OpentelemetryCPP REQUIRED)

install(
  DIRECTORY ${STAGED_INSTALL_PREFIX}/
  DESTINATION .
  USE_SOURCE_PERMISSIONS)
