from src.core.models import Product
from src.orchestrator.graph import build_graph

config = {"configurable":{"thread_id": "sessao_de_compras_1"}}

def run_human_in_the_loop():
  print("🤖 Agente Iniciado...")

  initial_state ={
    "products": [Product("PS5 Pro", 4000.00, vendor="Amazon")],
    "proposals": [],
    "logs": [],
  }

  app = build_graph()

  print("\n--- 1ª Execução: Monitoramento ---")
  for event in app.stream(initial_state, config=config):
    for key, value in event.items():
      print(f"✅ Passo concluído: {key}")
    
  
  snapshot = app.get_state(config)

  print("\n🛑 O Agente PAUSOU antes de executar.")
  print("--- Estado Atual (Snapshot) ---")

  current_proposals = snapshot.values.get("proposals", [])

  if not current_proposals:
    print("Nenhuma proposta encontrada. O Agente terminou normalmente.")
    return
  
  for p in current_proposals:
    print(f"📝 Proposta Pendente: {p.product.name} por R$ {p.product.current_price}")

  user_input = input("\n👤 Humano: Você autoriza a compra? (s/n): ")

  if user_input.lower() == "s":
    print("\n🚀 Autorizado! Retomando execução...")

    for event in app.stream(None, config=config):
      for key, value in event.items():
        if key == "execute":
          print("💰 Dinheiro gasto com sucesso!")
          print(value["logs"][-1])
  else:
    print("\n🛑 Compra REJEITADA. O Agente terminou normalmente.")

if __name__ == "__main__":
  run_human_in_the_loop()