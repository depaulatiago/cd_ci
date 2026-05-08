# Exemplo simples de CI com GitHub Actions

Demo mínimo mostrando um pipeline de CI em Python.

## Estrutura

- [app.py](app.py) — função `soma(a, b)`
- [test_app.py](test_app.py) — teste com `pytest`
- [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml) — pipeline

## Como funciona o pipeline

O arquivo [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml) tem
um job `test` que roda em todo `push` e `pull_request` para `main`:

- Faz checkout do código
- Instala Python 3.12
- Instala `pytest`
- Roda os testes

Se algum teste falhar, o pipeline fica vermelho.

## Rodar localmente

```bash
pip install pytest
pytest
```
