from os import listdir

__all__ = [x.replace('.py', '') for x in listdir() if x != '__init__.py' and '.py' in x]
