# Exemplo simples de CI/CD com GitHub Actions

Demo mínimo mostrando um pipeline de CI/CD em Python.

## Estrutura

- [app.py](app.py) — função `soma(a, b)`
- [test_app.py](test_app.py) — teste com `pytest`
- [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml) — pipeline

## Como funciona o pipeline

O arquivo [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml) tem dois jobs:

1. **CI (`test`)** — roda em todo `push` e `pull_request` para `main`:
   - Faz checkout do código
   - Instala Python 3.12
   - Instala `pytest`
   - Roda os testes

2. **CD (`deploy`)** — só roda se:
   - O job `test` passou (`needs: test`)
   - O push foi para a branch `main` (`if: github.ref == 'refs/heads/main'`)

   Aqui o deploy é simulado com um `echo`. Em um caso real, esse passo
   poderia publicar em um servidor, fazer push para o GitHub Pages,
   subir um container, etc.

## Rodar localmente

```bash
pip install pytest
pytest
```
