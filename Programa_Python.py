language: python
python:
  - "2.6"
  - "2.7"
  - "3.2"
  - "3.3"
# command to install dependencies
script: python tests/test_all_of_the_units.py
branches:
  only:
    - master

import unittest  
  
def cuadrado(num):  
    """Calcula el cuadrado de un numero."""  
  
    return num ** 2  
  
  
class EjemploPruebas(unittest.TestCase):  
    def test(self):  
        l = [0, 1, 2, 3]  
        r = [cuadrado(n) for n in l]  
        self.assertEqual(r, [0, 1, 4, 9])  
  
if __name__ == "__main__":  
    unittest.main()  
