from os import path
import nose

here = path.abspath(path.dirname(__file__))
nose.main(defaultTest=here)
