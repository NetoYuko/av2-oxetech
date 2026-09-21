# Gilded Rose - Refatoração e Boas Práticas

Este projeto é a entrega final da avaliação (Av2), focado em refatorar o sistema legado "Gilded Rose". O objetivo foi transformar um código complexo e acoplado em uma arquitetura limpa, testável e escalável, aplicando princípios SOLID e Clean Code.

## Decisões de Arquitetura

O código original sofria de "code smells", como números mágicos, funções gigantes e o anti-pattern *arrowhead*. Para resolver isso, tomamos as seguintes decisões:

*   **Princípio de Responsabilidade Única (SRP):** Removemos toda a lógica misturada da função principal. Cada tipo de item agora possui sua própria classe dedicada, sendo responsável apenas por gerenciar suas regras específicas de degradação e valorização.
*   **Princípio Aberto/Fechado (OCP):** A classe principal `GildedRose` foi transformada em um roteador simples. Agora, o sistema está aberto para extensão sem precisar de alteração no código existente.
*   **Clean Code:** Extraímos valores fixos e limites para um arquivo de constantes, melhorando a legibilidade. Aplicamos *guard clauses* para eliminar o aninhamento profundo.

##  Estrutura de Arquivos e Funções

O projeto foi reestruturado isolando o código de produção dos testes, utilizando o diretório `src/`:

*   `src/constants.py`: Centraliza todas as strings mágicas (nomes dos itens) e limites numéricos (qualidade máxima, mínima e limites de dias).
*   `src/item.py`: Classe base original fornecida pelo sistema legado
*   `src/gilded_rose.py`: Contém a classe `GildedRose`. Sua função `update_quality` agora apenas identifica o tipo do item e delega a atualização para a classe responsável.
*   `src/normal_item.py`: Regras de negócio para itens comuns (perdem 1 de qualidade por dia, ou 2 após o vencimento).
*   `src/aged_brie_item.py`: Regras do queijo (aumenta de qualidade com o tempo).
*   `src/sulfuras_item.py`: Regras do item lendário (valores imutáveis).
*   `src/backstage_pass_item.py`: Regras do ingresso (acelera o ganho de qualidade e zera após o show).
*   `src/conjured_item.py`: (Feature Nova) Regras do item conjurado, que degrada duas vezes mais rápido que o normal.
*   `tests/test_gilded_rose.py`: Suíte completa de testes de caracterização para garantir a preservação do comportamento.

##  Sobre os Testes

Adotamos a estratégia de escrever **Testes de Caracterização** antes de modificar qualquer linha do código legado. Isso criou uma rede de segurança que garantiu que as regras de negócio fossem 100% preservadas durante a refatoração. 

A suíte cobre os "caminhos felizes" e todos os casos de borda críticos.

##  Como Rodar o Projeto

**Pré-requisitos:** Python 3.x instalado.

1. Clone este repositório.
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

##  Como Testar

Os testes foram desenvolvidos utilizando o `pytest`. Para rodar a suíte completa de testes e verificar se todas as regras de negócio estão sendo respeitadas, execute o comando abaixo na raiz do projeto:

```bash
pytest
```

Para ver o nível de detalhamento de cada teste, você pode usar:

```bash
pytest -v
```