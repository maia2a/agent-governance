from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from src.core.models import PurchaseProposal
from src.adapters.price_checker import MockPriceChecker
from src.orchestrator.state import AgentState

price_checker = MockPriceChecker()

def monitor_price_node(state: AgentState):
  """
    Nó responsável por verificar os preços de todos os produtos na lista.
  """
  products = state["products"]
  logs = ["--- [Monitor] Iniciando verificação de preços ---"]

  updated_products = []
  for product in products:
    checked_product = price_checker.check_price(product)
    updated_products.append(checked_product)
    logs.append(f"[Monitor] {product.name} - Preço atual: R$ {checked_product.current_price}")

  return {"products": updated_products, "logs": logs}

def analyst_node(state: AgentState):
  """
    Nó que analisa se vale a pena comprar.
    (Futuramente, aqui entrará o GPT-4 analisando o contexto).
  """
  products = state["products"]
  new_proposals = []
  logs = ["--- [Analyst] Iniciando análise de preços ---"]

  for product in products:
    if product.current_price and product.current_price <= product.target_price:
      proposal = PurchaseProposal(product=product, reasoning="Preço alvo atingido (Lógica Determinística)")
      new_proposals.append(proposal)
      logs.append(f"[Analista] Oportunidade identificada: {product.name}")
  return {"proposals": new_proposals, "logs": logs}

def execution_node(state: AgentState):
  """
    Passo 3: Executar a compra (SÓ RODA APÓS APROVAÇÃO).
  """
  proposals = state["proposals"]
  logs = ["--- [Executor] Iniciando fase de compra ---"]

  if not proposals:
    logs.append("[Executor] Nenhuma proposta pendente.")
  for proposal in proposals:
    logs.append(f"[Executor] 🛒 COMPRA EFETUADA via API: {proposal.product.name} por R$ {proposal.product.current_price}")
  
  return {"logs": logs}  


def build_graph():
  workflow = StateGraph(AgentState)

  workflow.add_node("monitor_price", monitor_price_node)
  workflow.add_node("analyst", analyst_node)
  workflow.add_node("execute", execution_node)

  workflow.set_entry_point("monitor_price")
  workflow.add_edge("monitor_price", "analyst")
  workflow.add_edge("analyst", "execute")
  workflow.add_edge("execute", END)

  checkpointer = MemorySaver()

  return workflow.compile(checkpointer=checkpointer, interrupt_before["execute"])