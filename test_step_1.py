from src.core.models import Product, PurchaseProposals
from src.adapters.price_checker import MockPriceChecker

def run_test():
  print("--- Iniciando Teste da Fase 1 ---")
  
  # 1. Criar um produto alvo (Ex: iPhone 15, meta R$ 5000)
  iphone = Product(name="iPhone 15", target_price=5000, vendor="Amazon MOCK")
  
  # 2. Inicializar o Checker Mock
  checker = MockPriceChecker()
  
  # 3. Executar checagem
  updated_product = checker.check_price(iphone)
  
  # 4. Validar lógica simples
  if updated_product.current_price and updated_product.current_price <= updated_product.target_price:
    print("✅ Preço alvo atingido!")
    proposal = PurchaseProposal(product=updated_product, reasoning="Preço abaixo do alvo!")
    print(proposal)
  else:
    print(f"❌ Preço ainda alto: R$ {updated_product.current_price}")
    
  print ("--- Fim do Teste da Fase 1 ---")

if __name__ == "__main__":
  run_test()