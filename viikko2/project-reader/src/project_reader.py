from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        parsed_toml = toml.loads(content)
        #print(parsed_toml)

        name = parsed_toml["tool"]["poetry"]["name"]
        desc = parsed_toml["tool"]["poetry"]["description"]
        l = parsed_toml["tool"]["poetry"]["license"]
        authors = parsed_toml["tool"]["poetry"]["authors"]
        dep = parsed_toml["tool"]["poetry"]["dependencies"]
        dev_dep = parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, l, authors, dep, dev_dep)
