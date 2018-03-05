# one.py

def func():
    print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

def function():
    pass
def function2():
    pass

if __name__ == '__main__':  # RUN THE SCRIPT!
    function2()
    function()

#     print('ONE.PY is being run directly!')
# else:
#     print('ONE.PY has been imported!')
