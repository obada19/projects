# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.21

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = C:\Users\obada\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\213.7172.20\bin\cmake\win\bin\cmake.exe

# The command to remove a file.
RM = C:\Users\obada\AppData\Local\JetBrains\Toolbox\apps\CLion\ch-0\213.7172.20\bin\cmake\win\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/assignment_3_1.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/assignment_3_1.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/assignment_3_1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/assignment_3_1.dir/flags.make

CMakeFiles/assignment_3_1.dir/main.c.obj: CMakeFiles/assignment_3_1.dir/flags.make
CMakeFiles/assignment_3_1.dir/main.c.obj: ../main.c
CMakeFiles/assignment_3_1.dir/main.c.obj: CMakeFiles/assignment_3_1.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/assignment_3_1.dir/main.c.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/assignment_3_1.dir/main.c.obj -MF CMakeFiles\assignment_3_1.dir\main.c.obj.d -o CMakeFiles\assignment_3_1.dir\main.c.obj -c C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\main.c

CMakeFiles/assignment_3_1.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/assignment_3_1.dir/main.c.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\main.c > CMakeFiles\assignment_3_1.dir\main.c.i

CMakeFiles/assignment_3_1.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/assignment_3_1.dir/main.c.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\main.c -o CMakeFiles\assignment_3_1.dir\main.c.s

# Object files for target assignment_3_1
assignment_3_1_OBJECTS = \
"CMakeFiles/assignment_3_1.dir/main.c.obj"

# External object files for target assignment_3_1
assignment_3_1_EXTERNAL_OBJECTS =

assignment_3_1.exe: CMakeFiles/assignment_3_1.dir/main.c.obj
assignment_3_1.exe: CMakeFiles/assignment_3_1.dir/build.make
assignment_3_1.exe: CMakeFiles/assignment_3_1.dir/linklibs.rsp
assignment_3_1.exe: CMakeFiles/assignment_3_1.dir/objects1.rsp
assignment_3_1.exe: CMakeFiles/assignment_3_1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable assignment_3_1.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\assignment_3_1.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/assignment_3_1.dir/build: assignment_3_1.exe
.PHONY : CMakeFiles/assignment_3_1.dir/build

CMakeFiles/assignment_3_1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\assignment_3_1.dir\cmake_clean.cmake
.PHONY : CMakeFiles/assignment_3_1.dir/clean

CMakeFiles/assignment_3_1.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1 C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1 C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\cmake-build-debug C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\cmake-build-debug C:\Users\obada\ikt101g22h\assignments\solutions\assignment_3_1\cmake-build-debug\CMakeFiles\assignment_3_1.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/assignment_3_1.dir/depend
