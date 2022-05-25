###Creates blank Untitled file
import pykernel
program=pykernel.Editor()
try:
    program.loop()
except KeyboardInterrupt:
    program.quit()
###Open Text.txt File
program=pykernel.Editor("Text.txt")
try:
    program.loop()
except KeyboardInterrupt:
    program.quit()
###Try To Open Nonexistent_File.txt
program=pykernel.Editor("Nonexistent_File.txt")
try:
    program.loop()
except KeyboardInterrupt:
    program.quit()
###Create/open Nonexistent_File.txt
program=pykernel.Editor("Nonexistent_File.txt","n+")
try:
    program.loop()
except KeyboardInterrupt:
    program.quit()