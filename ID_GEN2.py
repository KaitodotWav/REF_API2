from PIL import Image, ImageDraw, ImageFont, ImageOps
from threading import Thread
from datetime import datetime
import os, openpyxl, json, errno, re

class Container:
    class FormatTemplate:
        def __init__(self):
            self.settings = {
                "template" : None,
                "data" : None,
                "sheet" : None,
                "border" : None,
                "border_color":None,
                "output" : None,
                "output_name" : None
            }
            self.commands = []
            self.raw = {"settings" : self.settings, "commands": self.commands}

    class XL_Data:
        def __init__(self, XL, sheet:str):
            self.root = openpyxl.load_workbook(XL)
            self.sheet = self.root[sheet]
            self.nav = {}
            for index, header in enumerate(self.sheet.iter_cols()):
                fetched = header[0].value
                if fetched is None or isinstance(fetched, str) and len(fetched.strip(" ")) <= 0: continue
                self.nav[fetched] = index

        def __repr__(self): return str(self.nav)


class FileHandler():    #File Handling
    def __init__(self, format:str=None):
        self.json = Container.FormatTemplate().raw
        self.json = self.loadJson(format)
        self.xl =  Container.XL_Data(self.json["settings"]["database"], self.json["settings"]["sheet"])

    def loadJson(self, file):
        with open(file, 'r', encoding="utf8") as f:
            j = json.load(f)
            j["read_path"] = file
            return j
    
class NameHandler():
    def __init__(self, raw):
        self.firstname = None
        self.surname = None
        self.suffix = None
        self.middle_initial = None
        self.middle_name = None
        self.analize(raw)

    def __repr__(self):
        return f"{self.surname}, {self.firstname} {self.middle_initial} {self.suffix}."
        
    def analize(self, name):
        pizza = name.split(" ")
        if "," in name:
            dev = name.split(",")
            self.surname = dev[0]
        else:
            dot = name.count(".")
            if not isinstance(dot, re.Match):
                pass
        self.suffix = self.suffix_finder(name)

    def suffix_finder(self, name):
        name = name.lower()
        pattern = r"(?:\s+)?(?:jr\.|sr\.|[ivx]{1,3})$"
        match = re.search(pattern, name)
        return match.group(0).strip().title() if match else None


class Generator():  #Image Generation
    def __init__(self, template = None, log=None):
        self.root = Image.open(template) if template != None else None

    def run(self, commands:list):
        for c in commands:
            pass

class GenApp(): #MAIN program
    def __init__(self, format_data:str):
        self.data = FileHandler(format_data)
        self.var = self.varManger()

    def execute(self, **kwargs):
        pass

    def dirManger(self, path):
        pass

    def varManger(self):
        file, ext = os.path.splitext(self.data.json["read_path"])
        xfile, xext = os.path.splitext(self.data.json["settings"]["database"])
        self.var = {
            "@FORMAT" : file,
            "@XLFILE" : xfile,
            "@XLSHEET" : self.data.json["settings"]["sheet"]
        }

    def run(self, mode=0):
        XL = self.data.xl.sheet
        for index, row in enumerate(XL.iter_rows()):
            self.execute(XL=XL, index=index, row=row)
            #xl analyzer
            #name analyzer

    def _check_xl_data(self, source, reference):
        found = 0
        for var in reference: 
            fetched = source[reference[var]].value
            if fetched is None or isinstance(fetched, str) and len(fetched.strip(" ")) <= 0: continue
            else: found += 1
        return False if found == 0 else True

if __name__ == "__main__":
    #y = GenApp(r"data\formats\sample.json")
    #print(y.data.json)

    n = NameHandler("Molinos, John Naoise L.")
    print()
    print(n)