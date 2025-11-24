import random
from abc import ABC, abstractmethod
from src.core.models import Product

class PriceCheckerInterface(ABC):
  """
    Interface abstrata. O Agente só conhece isso, não a implementação real.
    Princípio de Inversão de Dependência (D do SOLID).
  """
  @abstractmethod
  def check_price(self, product: Product) -> Product:
    pass

class MockPriceChecker(PriceCheckerInterface):
  """
    Simula a checagem de preços para testes controlados.
  """
  def check_price(self, product: Product) -> Product:
    #Simula uma flutuação de preço entre -20% e +20% do alvo
    variation = random.uniform(0.8, 1.2)
    simulated_price = round(product.target_price * variation, 2)
    
    product.current_price = simulated_price
    print(f"[MOCK] Verificando {product.name} na {product.vendor}: R$ {simulated_price}")
    return product