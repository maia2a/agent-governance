from typing import List, Dict, Optional
import operator
from src.core.models import Product, PurchaseProposals

class AgentState:
  """
    Define a memória compartilhada do nosso fluxo de agentes.
  """
  products: List[Product]
  proposals: Annotated[List[PurchaseProposals], operator.add]
  logs: Annotated[List[str], operator.add]
