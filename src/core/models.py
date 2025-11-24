from dataclasses import dataclass
from os import name
from typing import Optional


from datetime import datetime


@dataclass
class Product:
  """Representa o produto que estamos monitorando."""
  name: str
  target_price: float
  current_price: Optional[float] = None
  url: str = ""
  vendor: str = ""

@dataclass
class PurchaseProposals:
  """
    O artefato gerado pelo agente quando encontra uma oportunidade.
    Isso é o que o humano vai aprovar ou rejeitar.
  """
  product: Product
  reasoning: str 
  generated_at: datetime = datetime.now()
  status: str = "PENDING"
  
  def approve(self):
    self.status = "APPROVED"
  
  def reject(self):
    self.status = "REJECTED"