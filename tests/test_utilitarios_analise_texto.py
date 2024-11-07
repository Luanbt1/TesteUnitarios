import unittest
from src.utilitarios_analise_texto import UtilitariosAnaliseTexto


class TestUtilitariosAnaliseTexto(unittest.TestCase):
    def setUp(self):
        self.util = UtilitariosAnaliseTexto("A arara viu a arara. O ovo caiu!")

    def test_frequencia_palavras(self):
        esperado = {'a': 2, 'arara': 2, 'viu': 1, 'o': 1, 'ovo': 1, 'caiu': 1}
        self.assertEqual(self.util.frequencia_palavras(), esperado)

    def test_encontrar_frases_palindromas(self):
        util = UtilitariosAnaliseTexto("A arara arara. A asa da asa.")
        frases_palindromas = util.encontrar_frases_palindromas()

    def test_grupos_anagramas(self):
        palavras = ["amor", "roma", "carro", "arco", "mora"]
        esperado = [['amor', 'roma', 'mora'], ['carro'], ['arco']]
        self.assertEqual(self.util.grupos_anagramas(palavras), esperado)

    def test_prefixo_comum(self):
        palavras = ["flor", "floresta", "florida"]
        self.assertEqual(self.util.prefixo_comum(palavras), "flor")
        self.assertEqual(self.util.prefixo_comum(["casa", "casarão"]), "casa")
        self.assertEqual(self.util.prefixo_comum(["carro", "bicicleta"]), "")

    def test_detectar_palavras_chave(self):
        util = UtilitariosAnaliseTexto("O carro da Maria e o carro do João.")
        esperado = {'carro': 2, 'maria': 1, 'joão': 1}
        self.assertEqual(util.detectar_palavras_chave(), esperado)

    def test_fatores_primos(self):
        self.assertEqual(self.util.fatores_primos(28), [2, 2, 7])
        self.assertEqual(self.util.fatores_primos(13), [13])
        self.assertEqual(self.util.fatores_primos(1), [])

    def test_contar_frases(self):
        util = UtilitariosAnaliseTexto("Olá! Como vai? Estou bem.")
        self.assertEqual(util.contar_frases(), 3)
        util_vazio = UtilitariosAnaliseTexto("")
        self.assertEqual(util_vazio.contar_frases(), 0)

    def test_palavras_unicas_ordenadas(self):
        util = UtilitariosAnaliseTexto("Banana maçã banana pera maçã.")
        esperado = ['banana', 'maçã', 'pera']
        self.assertEqual(util.palavras_unicas_ordenadas(), esperado)


if __name__ == '__main__':
    unittest.main()
