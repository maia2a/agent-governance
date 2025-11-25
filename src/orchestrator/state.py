from typing import List, Dict, Optional, TypedDict, Annotated
import operator
from src.core.models import Product, PurchaseProposal

class AgentState(TypedDict):
  """
    Define a memória compartilhada do nosso fluxo de agentes.
  """
  products: List[Product]
  proposals: Annotated[List[PurchaseProposal], operator.add]
  logs: Annotated[List[str], operator.add]
