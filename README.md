# Agência Prado

## Dashboard de saúde do Pixel Meta

`dashboard/index.html` é um painel estático que lê as exportações de **Eventos recebidos** do Events Manager
(uma planilha por evento, agregada por hora) e aponta os gargalos de rastreamento e conversão.

- Abrir: basta abrir `dashboard/index.html` no navegador. O botão **Carregar exportações** aceita novos `.xlsx`
  do Events Manager (vários de uma vez; linhas repetidas são ignoradas).
- Atualizar os dados embutidos: coloque as exportações em `data/raw/` e rode `python3 dashboard/build.py`
  (requer `pandas` e `openpyxl`). O HTML é gerado a partir de `dashboard/pixel-template.html`.
