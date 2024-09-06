# Função para descobrir o próximo número de cada sequência

def proximo_a():
    # Sequência: 1, 3, 5, 7, ___ (números ímpares consecutivos)
    seq = [1, 3, 5, 7]
    seq.append(seq[-1] + 2)  # Próximo número ímpar
    return seq

def proximo_b():
    # Sequência: 2, 4, 8, 16, 32, 64, ____ (multiplicação por 2)
    seq = [2, 4, 8, 16, 32, 64]
    seq.append(seq[-1] * 2)  # Próximo número é o dobro do anterior
    return seq

def proximo_c():
    # Sequência: 0, 1, 4, 9, 16, 25, 36, ____ (quadrados perfeitos)
    seq = [0, 1, 4, 9, 16, 25, 36]
    seq.append((len(seq))**2)  # Próximo quadrado perfeito
    return seq

def proximo_d():
    # Sequência: 4, 16, 36, 64, ____ (quadrados de números pares)
    seq = [4, 16, 36, 64]
    prox_num_par = 2 * (len(seq) + 1)  # Próximo número par
    seq.append(prox_num_par ** 2)  # Próximo quadrado perfeito de número par
    return seq

def proximo_e():
    # Sequência: 1, 1, 2, 3, 5, 8, ____ (Fibonacci)
    seq = [1, 1, 2, 3, 5, 8]
    seq.append(seq[-1] + seq[-2])  # Próximo número na sequência Fibonacci
    return seq

def proximo_f():
    # Sequência: 2, 10, 12, 16, 17, 18, 19, ____ (alterna entre salto e sequência)
    seq = [2, 10, 12, 16, 17, 18, 19]
    if seq[-1] == 19:
        seq.append(20)  # Próximo número consecutivo
    return seq

# Imprimir as sequências com o próximo número
print("a) Sequência:", proximo_a())
print("b) Sequência:", proximo_b())
print("c) Sequência:", proximo_c())
print("d) Sequência:", proximo_d())
print("e) Sequência:", proximo_e())
print("f) Sequência:", proximo_f())
