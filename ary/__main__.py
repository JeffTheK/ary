from .project import Project

def main():
    name = input("name: ")
    language = input("language: ")
    project = Project(name, language)
    print(f"creating {name} project written in {language}")

    language = language.lower()
    if language == "python":
        setup_python_project()
    else:
        print(f"{language} not found")