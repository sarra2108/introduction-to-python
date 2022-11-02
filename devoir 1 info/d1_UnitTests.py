# test automatique pour D1
# metez-le dans le meme repertoire que votre fichier solution et excutez le fichier test avec Run
# put it in the same directory as your solution file and press Run to excute the test file

import unittest
from d1 import *

class d1_Tests(unittest.TestCase):

    def test_q1(self):
        print("Test de la  question 1")
        print("Q1_1")
        n=tempsVoyage(400,100)
        self.assertEqual(n,240.0)
        print("Q1_2")
        n=tempsVoyage(20.6,60)
        self.assertEqual(n, 20.6)
      

    def test_q2(self):
        print("\nTest de la  question 2")
        print("Q2_1")
        n=noteFinale(100,100,100,100,100)
        self.assertEqual(n,100.0)
        print("Q2_2")
        n=noteFinale(50,90.5,60,80,70)
        self.assertEqual(n, 74.625)
      

    def test_q3(self):
        print("\nTest de la  question 3")
        print("Q3_1")
        n = bibformat("Antoine de Saint Exupery", "Le petit prince", "Paris", "Jeunesse", 1943)
        self.assertEqual(n, 'Antoine de Saint Exupery (1943). Le petit prince. Paris: Jeunesse')
       
        

   # pas de unit test pour Q4 parce qu'elle ne retourne rien
   

if __name__ == '__main__':
    unittest.main()

