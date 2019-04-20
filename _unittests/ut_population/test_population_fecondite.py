# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version


class TestPopulationFecondite(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "pyrsslocal"],
                                        __file__, hide=True)

    def test_population_fecondite(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from actuariat_python.data import fecondite_france
        df = fecondite_france()
        self.assertTrue(len(df) >= 35)
        self.assertEqual(df.shape[1], 3)
        self.assertEqual(df.columns[0], "age")
        self.assertEqual(df.columns[-1], "2015")


if __name__ == "__main__":
    unittest.main()
