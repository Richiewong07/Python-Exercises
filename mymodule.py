# mymodule.py
import pdb

def test ():
  name = "Narf"
  print(name[10])
  pdb.set_trace()
# Inserted set_trace
  print("done")
if __name__ == '__main__':
  test()
