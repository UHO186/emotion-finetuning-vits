# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.21

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

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/uho/vits-finetuning/cmake-3.21.0/Bootstrap.cmk/cmake

# The command to remove a file.
RM = /home/uho/vits-finetuning/cmake-3.21.0/Bootstrap.cmk/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/uho/vits-finetuning/cmake-3.21.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/uho/vits-finetuning/cmake-3.21.0

# Include any dependencies generated for this target.
include Tests/CMakeLib/CMakeFiles/testAffinity.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include Tests/CMakeLib/CMakeFiles/testAffinity.dir/compiler_depend.make

# Include the progress variables for this target.
include Tests/CMakeLib/CMakeFiles/testAffinity.dir/progress.make

# Include the compile flags for this target's objects.
include Tests/CMakeLib/CMakeFiles/testAffinity.dir/flags.make

Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o: Tests/CMakeLib/CMakeFiles/testAffinity.dir/flags.make
Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o: Tests/CMakeLib/testAffinity.cxx
Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o: Tests/CMakeLib/CMakeFiles/testAffinity.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/uho/vits-finetuning/cmake-3.21.0/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o"
	cd /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o -MF CMakeFiles/testAffinity.dir/testAffinity.cxx.o.d -o CMakeFiles/testAffinity.dir/testAffinity.cxx.o -c /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib/testAffinity.cxx

Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/testAffinity.dir/testAffinity.cxx.i"
	cd /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib/testAffinity.cxx > CMakeFiles/testAffinity.dir/testAffinity.cxx.i

Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/testAffinity.dir/testAffinity.cxx.s"
	cd /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib/testAffinity.cxx -o CMakeFiles/testAffinity.dir/testAffinity.cxx.s

# Object files for target testAffinity
testAffinity_OBJECTS = \
"CMakeFiles/testAffinity.dir/testAffinity.cxx.o"

# External object files for target testAffinity
testAffinity_EXTERNAL_OBJECTS =

Tests/CMakeLib/testAffinity: Tests/CMakeLib/CMakeFiles/testAffinity.dir/testAffinity.cxx.o
Tests/CMakeLib/testAffinity: Tests/CMakeLib/CMakeFiles/testAffinity.dir/build.make
Tests/CMakeLib/testAffinity: Source/libCMakeLib.a
Tests/CMakeLib/testAffinity: Source/kwsys/libcmsys.a
Tests/CMakeLib/testAffinity: Utilities/std/libcmstd.a
Tests/CMakeLib/testAffinity: Utilities/cmexpat/libcmexpat.a
Tests/CMakeLib/testAffinity: Utilities/cmlibarchive/libarchive/libcmlibarchive.a
Tests/CMakeLib/testAffinity: Utilities/cmliblzma/libcmliblzma.a
Tests/CMakeLib/testAffinity: Utilities/cmzstd/libcmzstd.a
Tests/CMakeLib/testAffinity: Utilities/cmbzip2/libcmbzip2.a
Tests/CMakeLib/testAffinity: Utilities/cmcurl/lib/libcmcurl.a
Tests/CMakeLib/testAffinity: Utilities/cmzlib/libcmzlib.a
Tests/CMakeLib/testAffinity: /usr/lib/x86_64-linux-gnu/libssl.so
Tests/CMakeLib/testAffinity: /usr/lib/x86_64-linux-gnu/libcrypto.so
Tests/CMakeLib/testAffinity: Utilities/cmnghttp2/libcmnghttp2.a
Tests/CMakeLib/testAffinity: Utilities/cmjsoncpp/libcmjsoncpp.a
Tests/CMakeLib/testAffinity: Utilities/cmlibuv/libcmlibuv.a
Tests/CMakeLib/testAffinity: Utilities/cmlibrhash/libcmlibrhash.a
Tests/CMakeLib/testAffinity: Tests/CMakeLib/CMakeFiles/testAffinity.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/uho/vits-finetuning/cmake-3.21.0/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable testAffinity"
	cd /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/testAffinity.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Tests/CMakeLib/CMakeFiles/testAffinity.dir/build: Tests/CMakeLib/testAffinity
.PHONY : Tests/CMakeLib/CMakeFiles/testAffinity.dir/build

Tests/CMakeLib/CMakeFiles/testAffinity.dir/clean:
	cd /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib && $(CMAKE_COMMAND) -P CMakeFiles/testAffinity.dir/cmake_clean.cmake
.PHONY : Tests/CMakeLib/CMakeFiles/testAffinity.dir/clean

Tests/CMakeLib/CMakeFiles/testAffinity.dir/depend:
	cd /home/uho/vits-finetuning/cmake-3.21.0 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/uho/vits-finetuning/cmake-3.21.0 /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib /home/uho/vits-finetuning/cmake-3.21.0 /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib /home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeLib/CMakeFiles/testAffinity.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Tests/CMakeLib/CMakeFiles/testAffinity.dir/depend

