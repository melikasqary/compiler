import os
import sys
os.add_dll_directory("C:\\Program Files\\SciTools\\bin\\pc-win64")
sys.path.append("C:\\Program Files\\SciTools\\bin\\pc-win64\\Python")
import understand as und

db = und.open("C:\\Users\\melika\\OpenUnderstand\\benchmark\\JSON\\src\\src.udb")

print ("\n")

res = len(db.ents("class"))
print (f"Number of classes = {res}")