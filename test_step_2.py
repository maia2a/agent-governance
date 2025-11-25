from src.core.models import Product
from src.orchestrator.graph import build_graph

def run_graph_test():
  print("🚀 Iniciando Orquestrador de Agentes...")

  # 1. Definir dados iniciais
  initial_products = [
    Product(name="iPhone 15", target_price=5000, vendor="Amazon MOCK"),
    Product(name="MacBook Pro", target_price=10000, vendor="Apple Store MOCK"),
    Product(name="AirPods Pro", target_price=2000, vendor="Apple Store MOCK"),
  ]

  initial_state = {
    "products": initial_products,
    "proposals": [],
    "logs": [],
  }

  # 2. Construir o grafo
  app = build_graph()

  # O .invoke executa o grafo do início ao fim
  result = app.invoke(initial_state)
  
  # 3. Exibir resultados do Estado Final
  print("\n--- Resultado Final da Execução ---")

  for log in result["logs"]:
    print(log)

  print("\n📦 Propostas Geradas:")
  if result["proposals"]:
    for p in result["proposals"]:
      print(f"💰 COMPRAR: {p.product.name} | Motivo: {p.reasoning}")
  else:
    print("Nenhuma oportunidade encontrada nesta rodada.")

if __name__ == "__main__":
  run_graph_test()