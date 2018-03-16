from os import listdir, path

__all__ = [x.replace('.py', '')
           for x in listdir(path=path.dirname(__file__))
           if x != '__init__.py' and '.py' in x]
