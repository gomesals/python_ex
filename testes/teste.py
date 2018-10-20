import funcoes

import unittest


class TestaMedia(unittest.TestCase):

    def testa_valor(self):
        self.assertEqual(funcoes.media(10, 8), 9.0)
        self.assertEqual(funcoes.media(10, 5), 7.5)

    def testa_tipo(self):
        self.assertEqual(type(funcoes.media(10, 10)), float)

unittest.main()
