# CMake generated Testfile for 
# Source directory: /home/uho/vits-finetuning/cmake-3.21.0
# Build directory: /home/uho/vits-finetuning/cmake-3.21.0
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
include("/home/uho/vits-finetuning/cmake-3.21.0/Tests/EnforceConfig.cmake")
add_test([=[SystemInformationNew]=] "/home/uho/vits-finetuning/cmake-3.21.0/bin/cmake" "--system-information" "-G" "Unix Makefiles")
set_tests_properties([=[SystemInformationNew]=] PROPERTIES  _BACKTRACE_TRIPLES "/home/uho/vits-finetuning/cmake-3.21.0/CMakeLists.txt;858;add_test;/home/uho/vits-finetuning/cmake-3.21.0/CMakeLists.txt;0;")
subdirs("Source/kwsys")
subdirs("Utilities/std")
subdirs("Utilities/KWIML")
subdirs("Utilities/cmlibrhash")
subdirs("Utilities/cmzlib")
subdirs("Utilities/cmcurl")
subdirs("Utilities/cmnghttp2")
subdirs("Utilities/cmexpat")
subdirs("Utilities/cmbzip2")
subdirs("Utilities/cmzstd")
subdirs("Utilities/cmliblzma")
subdirs("Utilities/cmlibarchive")
subdirs("Utilities/cmjsoncpp")
subdirs("Utilities/cmlibuv")
subdirs("Source")
subdirs("Utilities")
subdirs("Tests")
subdirs("Auxiliary")
