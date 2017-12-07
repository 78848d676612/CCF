cmake_minimum_required(VERSION 3.5)
project(CCF)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")

set(SOURCE_FILES distribution/distribution.c)
add_executable(CCF ${SOURCE_FILES})