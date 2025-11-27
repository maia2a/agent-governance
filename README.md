# 🛡️ Sentinela: AI Agent Governance Orchestrator

> **"Em 2026, o desafio não será criar um agente, mas sim controlá-lo."**

## 📋 Sobre o Projeto

O **Sentinela** é uma prova de conceito de uma arquitetura de governança para Agentes Autônomos. Diferente de scripts de automação tradicionais ou "caixas pretas" de IA, este sistema implementa um padrão rigoroso de **Human-in-the-Loop (HITL)**.

O sistema monitora preços de mercado, utiliza LLMs (GPT-4o) para analisar oportunidades de compra com raciocínio complexo, mas **interrompe a execução** antes da transação crítica, exigindo aprovação humana explícita para prosseguir. Isso garante segurança, auditabilidade e confiança em operações automatizadas financeiras.

## 🏗️ Arquitetura (Clean Architecture)

O projeto foi construído seguindo princípios estritos de **Clean Architecture** e **SOLID**, garantindo desacoplamento entre a lógica de negócios, a orquestração do agente e as ferramentas externas.

```text
src/
├── core/           # Entidades e Regras de Negócio (Puro Python)
├── orchestrator/   # Grafo de Estado e Lógica do Agente (LangGraph)
├── adapters/       # Integrações (OpenAI, Scrapers, DB)
└── main.py         # Entrypoint
```

### O Fluxo do Agente (State Machine)

O sistema é modelado como um Grafo de Estados Cíclico:

1.  **Monitor Node:** Varre fontes de dados (Simulação de Scraper).
2.  **Analyst Node (AI):** O GPT-4o analisa o contexto (preço vs alvo) e gera um argumento de venda.
3.  **⏸️ Human Checkpoint:** O grafo **congela** seu estado na memória.
4.  **Decision:**
    - _Aprovado:_ O fluxo segue para o nó de Execução.
    - _Rejeitado:_ O fluxo encerra ou retorna ao monitoramento.
5.  **Execution Node:** Realiza a chamada de API final (Mock de Pagamento).

## 🚀 Tech Stack

- **Linguagem:** Python 3.10+
- **Orquestração de Agentes:** [LangGraph](https://langchain-ai.github.io/langgraph/) (Pela capacidade de persistência e ciclos).
- **Inteligência:** OpenAI GPT-4o (Reasoning).
- **Persistência de Estado:** MemorySaver (Dev) / PostgreSQL (Prod ready).
- **Design Pattern:** Dependency Injection, Repository Pattern.

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python 3.9 ou superior.
- Chave de API da OpenAI (opcional para modo mock).

### Passos

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/agent-governance.git
    cd agent-governance
    ```

2.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure as Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz:

    ```env
    OPENAI_API_KEY=sk-sua-chave-aqui
    ```

4.  **Execute a Simulação:**

    ```bash
    python3 test_step_3.py
    ```

## 🎮 Exemplo de Uso

Ao executar o agente, você verá o seguinte fluxo no terminal:

```text
🤖 AI Analyst (GPT-4o) Conectado.
--- [Monitor] Verificando preços ---
[Monitor] iPhone 15: R$ 4200.00
--- [Analista AI] Analisando oportunidades ---
[Analista AI] 🧠 Análise GPT: O preço está 16% abaixo do alvo, recomendando compra imediata pela oportunidade rara.

🛑 O Agente PAUSOU antes de executar.
👤 Humano: Você autoriza a compra? (s/n):
```

Se o usuário digitar `s`, o estado é recuperado e a compra é efetuada.

## 💡 Por que LangGraph?

Optamos pelo LangGraph ao invés de LangChain tradicional (Chains) porque processos de governança exigem **controle de estado**. Precisamos saber exatamente onde o agente parou, quais variáveis ele tinha na memória e poder "viajar no tempo" ou editar o estado antes de autorizar a ação.

## 🔜 Próximos Passos (Roadmap)

- [ ] Implementar Interface Gráfica (Streamlit ou Slack Block Kit).
- [ ] Substituir `MemorySaver` por `PostgresSaver` para persistência em disco.
- [ ] Adicionar múltiplos agentes (ex: um Agente "Crítico" que tenta achar defeitos no produto antes da compra).

---

**Desenvolvido por [Gabriell Maia do Amaral Duarte]**
_Engenharia de Software & IA Agentic_

---
