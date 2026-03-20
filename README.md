# 🔢 Binary & Number Converter

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)

A collection of Python scripts designed to perform manual base conversions between Binary and Decimal systems without relying on built-in shortcut functions, focusing on algorithmic logic.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## 🛠 Technologies
- **Python 3.x**: Core logic and base conversion algorithms.

## ✨ Features
- **Bi-directional Conversion:** Includes independent scripts for converting Binary to Number and Number to Binary.
- **Input Validation:** Both scripts feature `while True` loops and `try-except` blocks to ensure only valid data is processed.
- **Manual Algorithms:** 
  - Uses the positional power method ($2^i$) for binary decoding.
  - Uses successive division and modulo operations for decimal encoding.
- **Error Handling:** Custom `ValueError` triggers to prevent invalid characters (non-binary) or negative integers.

## 📂 Project Architecture
The repository contains two main scripts:
* `binary_to_decimal.py`: Takes a binary representation and returns its positive integer.
* `decimal_to_binary.py`: Takes a positive integer and returns its binary representation.

## 📚 What I Learned
* **Mathematical Logic:** Implementing the manual process of base conversion using floor division (`//`) and modulo (`%`).
* **String and List Manipulation:** Reversing lists and joining elements to format output correctly.

## 🔮 Future Improvements
- [ ] Integration into a single interactive CLI menu.
- [ ] Ability to handle floating-point (fractional) binary numbers.
- [ ] Graphical User Interface (GUI).
