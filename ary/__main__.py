class Project:
    def __init__(self, name, language, author="JeffTheK"):
        self.name = name
        self.language = language
        self.author = author

def main():
    name = input("name: ")
    language = input("language: ")
    project = Project(name, language)
    print(f"creating {name} project written in {language}")