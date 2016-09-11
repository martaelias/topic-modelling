__author__ = 'marta'

import re
import sys
from os import listdir
from os.path import isfile, join

def process_intervinent(text):
    m = re.search("D3__Intervinent>(.+?)</D3", text)
    if m:
        found = m.group(1)
        #print found
        return found

def process_speech(text):
    m = re.search("D3__Text_normal>(.+?)</D3", text)
    if m:
        found = m.group(1)
        #print found
        return found

def scrape_xml_file(filename):
    with open(filename, "r") as f:
        interventions = []
        new_intervention = []
        for line in f.readlines():
            m = re.search("D3__(.+?)</D3", line)
            if m:
                found = m.group(1)
                if found.startswith("Text_normal"):
                    token = process_speech(line)
                    new_intervention.append(token)
                elif found.startswith("Intervinent"):
                    token = process_intervinent(line)
                    if new_intervention:
                        interventions.append(new_intervention)
                    new_intervention = [token]
                else:
                    None
        #Despues de este loop interventions es una lista de listas. Cada sublista contiene
        # el nombre del locutor en el primer elemento, y el resto de elementos son cada una
        # de los parrafos de sus intervenciones.

def main(in_dir, out_dir):
    for f in listdir(in_dir):
        filename = join(in_dir, f)
        if isfile(filename):
            scrape_xml_file(filename)

if __name__ == "__main__":
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    main(in_dir, out_dir)
