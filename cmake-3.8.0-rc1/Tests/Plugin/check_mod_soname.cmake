execute_process(COMMAND ${readelf} -d ${mod} OUTPUT_FILE ${mod}.readelf.txt)
file(STRINGS ${mod}.readelf.txt soname REGEX "SONAME")
if(soname)
  message(FATAL_ERROR "${mod} has soname but should not:\n  ${soname}")
else()
  message(STATUS "${mod} has no soname as expected")
endif()
