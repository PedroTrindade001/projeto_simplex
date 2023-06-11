from src.services.SimplexService import executarSimplex
from src.view.Grafico import mostrarGrafico, mostrarGraficoResultado
from src.view.Resultados import mostrarResultados

mostrarGrafico()
modelo = executarSimplex()
mostrarResultados(modelo)
mostrarGraficoResultado()




