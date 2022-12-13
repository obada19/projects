cmake_minimum_required(VERSION 3.14)
project(assignment_4_1 C)

set(CMAKE_C_STANDARD 99)

add_executable(assignment_4_1 main.c)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 -Wall -pedantic -D__USE_MINGW_ANSI_STDIO")
