import csv

def read_csv(path):
    with open(path,"r",encoding="utf-8") as f:
        return csv.reader(f)

def write_csv(path,mode="w"):
    with open(path,mode,newline="",encoding="utf-8") as f:
        return csv.writer(f)