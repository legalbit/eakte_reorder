# if necessary
# pip install pypdf, zipfile

from pypdf import PdfReader, PdfWriter
import zipfile
import os

#
# dir structure:
# ..
#   working_dir\
#       zipped.zip
#       pdf_reorder.py
#
cwd = os.getcwd()
files_dir = os.path.join(cwd, "files_dir")
files = []

with zipfile.ZipFile("zipped.zip", "r") as zip:
    zip.extractall(files_dir)

for f in os.listdir(files_dir):
    
    file = os.path.join(files_dir, f)
    if file.endswith(".pdf"):
        reader = PdfReader(file)
        meta = reader.metadata
        data = {
            "file": file,
            "cdate": meta.creation_date,
            "mdate": meta.modification_date
        }
        files.append(data)

files = sorted(files, key=lambda x: x["mdate"])

writer = PdfWriter()
for file in files:
    reader = PdfReader(file["file"])
    writer.append(reader)

output_file = os.path.join(cwd, "output.pdf")
with open(output_file, "wb"):
    writer.write(output_file)