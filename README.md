# Simple CI/CD Pipeline (FastAPI + Docker + GitHub Actions)

![CI/CD Status](https://github.com/JoeMachiato/First-CI-CD-Pipeline/actions/workflows/cicd.yml/badge.svg)

## O projekcie
Ten projekt to kompletny, zautomatyzowany potok CI/CD (Continuous Integration / Continuous Delivery) zbudowany od zera. Służy jako demonstracja nowoczesnych praktyk DevOps.

Został zaprojektowany tak, aby przy każdym wypchnięciu kodu (push) do gałęzi `main`:
1. Sprawdzić jakość kodu (Linting - `flake8`).
2. Uruchomić testy jednostkowe (`pytest`).
3. Zbudować nowy obraz konteneryzacyjny (`Docker`).
4. Bezpiecznie wysłać gotowy obraz do rejestru publicznego (Docker Hub).

## Technologie
* **Aplikacja:** Python, FastAPI
* **Testy & Jakość:** Pytest, Flake8
* **Konteneryzacja:** Docker, Docker Hub
* **Automatyzacja (CI/CD):** GitHub Actions

## Jak uruchomić to lokalnie?

Zbudowany obraz jest dostępny publicznie na Docker Hub. Aby uruchomić aplikację na dowolnym komputerze z zainstalowanym Dockerem, wystarczy wpisać:

```bash
docker run -p 8000:8000 joemachiato97/moje-api:latest
```
Po uruchomieniu, API będzie dostępne w przeglądarce pod adresem: http://localhost:8000