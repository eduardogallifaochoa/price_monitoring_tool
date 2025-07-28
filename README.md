# 🐍 Price Monitoring Tool

![Build Status](https://github.com/eduardogallifaochoa/price_monitoring_tool/actions/workflows/ci_cd.yaml/badge.svg)
[![codecov](https://codecov.io/gh/eduardogallifaochoa/price-monitoring-tool/branch/main/graph/badge.svg)](https://codecov.io/gh/eduardogallifaochoa/price-monitoring-tool)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A **real-time cryptocurrency price monitoring system** built with **Python**, **Binance API**, **SQLite**, and **PyInstaller**, fully tested and integrated with **GitHub Actions CI/CD**.

---

## **What It Does**
- Fetches **real-time BTC & ETH prices** via Binance API.
- **Stores historical data** in CSV and SQLite.
- **Alerts** when price change exceeds a configurable threshold (e.g., ±2%).
- Includes **unit tests (pytest + coverage)**.
- **CI/CD pipeline** automatically tests and builds an `.exe` artifact.

---

## **Key Tech**
- **Python 3.11+**
- **APIs:** Binance Spot
- **DB:** SQLite
- **Testing:** Pytest + Coverage
- **CI/CD:** GitHub Actions + PyInstaller

---

## **Quick Start**
```bash
git clone https://github.com/eduardogallifaochoa/price-monitoring-tool.git
cd price-monitoring-tool
pip install -r requirements.txt
python main.py
```

## **Run Tests**
```bash
python run_tests.py
```

## **Highlights**
This project showcases:

- API integration and data persistence (CSV + SQLite).

- AI-assisted coding for architecture and testing.

- Automated test coverage with Pytest.

- CI/CD pipeline creating ready-to-use executables.

## **Contact**
- **GitHub:** [eduardogallifaochoa](https://github.com/eduardogallifaochoa)
- **LinkedIn:** [Eduardo Gallifa Ochoa](https://www.linkedin.com/in/eduardogallifaochoa/)
- **Email:** eduardogallifaochoa@gmail.com
