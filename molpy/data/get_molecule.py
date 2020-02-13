import os
# from util import read_xyz

dirname = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(dirname) if f.endswith(".xyz")]
name = [os.path.splitext(f)[0] for f in files]

d = dict(zip(name, files))

print(name, files)

# xyz = read_xyz(files[0])
# print(xyz)

# filename = os.path.join(dirname, 'look_and_say.dat')

# with open(filename, 'r') as handle:
#     look_and_say = handle.read()
