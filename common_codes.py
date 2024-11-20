import os
import random
import math

# Função que cria um diretório caso ele não exista
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Função que retorna um valor aleatório com base em um valor máximo e mínimo
def generate_random_values(intervalo):
    min_val, max_val = intervalo
    return round(random.uniform(min_val, max_val), 2)

# Função que retorna o valor da potência gerada (W) pela turbina e velocidade da água com base em um cálculo simples. Retorna o valor com no máximo 3 casas decimais
def get_power(speed):
    return math.ceil((2000 * speed ** 3) * 1000) / 1000