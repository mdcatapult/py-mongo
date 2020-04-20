import os, sys

parent_dir = os.path.dirname(__file__)
print("###############")
print( os.path.join(parent_dir, '../src'))
print(sys.path)
print("#########################")
sys.path.insert(0, os.path.join(parent_dir, '../src'))
print(sys.path)
print("#####################################")
sys.path.insert(0, '/home/daniel.james@medcat.local/workspace/py-mongo/src')
