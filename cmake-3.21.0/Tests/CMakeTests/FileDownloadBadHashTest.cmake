if(NOT "/home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeTests" MATCHES "^/")
  set(slash /)
endif()
set(url "file://${slash}/home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeTests/FileDownloadInput.png")
set(dir "/home/uho/vits-finetuning/cmake-3.21.0/Tests/CMakeTests/downloads")

file(DOWNLOAD
  ${url}
  ${dir}/file3.png
  TIMEOUT 2
  STATUS status
  EXPECTED_HASH SHA1=5555555555555555555555555555555555555555
  )
