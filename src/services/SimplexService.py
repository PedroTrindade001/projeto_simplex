from pulp import *

def executarSimplex():
    # Criar o modelo / alterar entre LpMaximize e LpMinimize
    modelo = LpProblem("problema", LpMaximize)

    # Inicializar as variáveis de decisão
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)

    # Adicionar restrições para o modelo
    modelo += (x + 3 * y <= 10, "Restrição1")
    modelo += (x + 4 * y <= 50, "Restrição2")

    # Adicionar função objetivo para o modelo
    modelo += lpSum([3 * x, 10 * y])

    # Solucionar problema
    modelo.solve()

    return modelo