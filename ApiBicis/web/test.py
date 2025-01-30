import unittest

import nuestrasFunciones

class TestBicis(unittest.TestCase):
    
    def testIva(self):
        
        self.assertEqual(21,nuestrasFunciones.CalcularIva(100))
        
                       
if __name__ == "__main__":
    unittest.main()