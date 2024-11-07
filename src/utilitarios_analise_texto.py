import re
from collections import Counter, defaultdict

class UtilitariosAnaliseTexto:
    def __init__(self, texto):
        self.texto = texto

    def frequencia_palavras(self):
        """Retorna a frequência de cada palavra em um dicionário, ignorando maiúsculas/minúsculas."""
        palavras = re.findall(r'\b\w+\b', self.texto.lower())
        return dict(Counter(palavras))

    def encontrar_frases_palindromas(self):
        """Encontra frases palíndromas no texto, ignorando espaços e pontuações."""
        frases = re.split(r'[.!?]', self.texto)  # Divide o texto em frases com base nos pontos finais, exclamações e interrogações
        palindromas = []
        for frase in frases:
            frase_limpa = ''.join(filter(str.isalnum, frase.lower()))  # Remove pontuação e converte para minúsculas
            if frase_limpa == frase_limpa[::-1] and frase.strip():  # Verifica se é palíndroma
                palindromas.append(frase.strip())  # Adiciona a frase à lista de palíndromas
        return palindromas


    def grupos_anagramas(self, lista_palavras):
        """Agrupa palavras que são anagramas entre si em uma lista de listas."""
        dicionario_anagramas = defaultdict(list)
        for palavra in lista_palavras:
            palavra_ordenada = ''.join(sorted(palavra.lower()))
            dicionario_anagramas[palavra_ordenada].append(palavra)
        return list(dicionario_anagramas.values())

    def prefixo_comum(self, lista_palavras):
        """Encontra o prefixo comum mais longo em uma lista de palavras."""
        if not lista_palavras:
            return ""
        prefixo = lista_palavras[0]
        for palavra in lista_palavras[1:]:
            while not palavra.startswith(prefixo):
                prefixo = prefixo[:-1]
                if not prefixo:
                    return ""
        return prefixo

    def detectar_palavras_chave(self, palavras_comuns=None):
        """Detecta palavras-chave no texto, ignorando palavras comuns fornecidas na lista palavras_comuns."""
        if palavras_comuns is None:
            palavras_comuns = {"de", "a", "o", "e", "do", "da"}
        palavras = [palavra.lower() for palavra in re.findall(r'\b\w+\b', self.texto) if
                    palavra.lower() not in palavras_comuns]
        return dict(Counter(palavras))

    def fatores_primos(self, numero):
        """Retorna os fatores primos de um número."""
        if numero <= 1:
            return []
        fatores = []
        divisor = 2
        while numero > 1:
            while numero % divisor == 0:
                fatores.append(divisor)
                numero //= divisor
            divisor += 1
        return fatores

    def contar_frases(self):
        """Conta o número de frases no texto, considerando pontos, exclamações e interrogações."""
        frases = re.split(r'[.!?]', self.texto)
        return len([frase for frase in frases if frase.strip()])

    def palavras_unicas_ordenadas(self):
        """Retorna uma lista de palavras únicas em ordem alfabética, ignorando maiúsculas/minúsculas."""
        palavras = set(re.findall(r'\b\w+\b', self.texto.lower()))
        return sorted(palavras)
