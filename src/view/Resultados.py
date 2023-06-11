from pulp import LpStatus

def mostrarResultados(modelo):
    print("Status: ", LpStatus[modelo.status])
    print("Valor otimizado da Função Objetivo: ", modelo.objective.value())
    for variaveis in modelo.variables():
        print(variaveis.name, "=", variaveis.varValue)