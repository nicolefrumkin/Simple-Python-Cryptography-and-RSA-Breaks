Simple Python Cryptography and RSA Breaks

This repository contains solutions for a cryptography assignment focused on implementing and breaking simple encryption methods in Python. It covers repeated-key XOR ciphers and simplified attacks on RSA.

## 📁 Folder Structure

- `q1.py` - Handles Repeated Key Cipher (encryption, decryption, brute-force, and smarter breaking).
- `q2.py` - Breaks simplified RSA schemes (PIN recovery, credit card decryption, signature forgery).
- `q1d.cipher`, `q1e.cipher`, `q2a-pin.txt`, `q2b-card.txt` - Sample encrypted inputs used for testing.
- `q1c.txt`, `q1d.txt`, `q1e.txt`, `q2a.txt`, `q2b.txt`, `q2c.txt` - Short explanations of each method and how it works.

## 🔐 Question Breakdown

### Question 1 – Repeated Key Cipher

- **Part A & B**: Encrypt and decrypt text using XOR and a repeating byte key.
- **Part C**: Score plaintext by how "English-like" it is.
- **Part D**: Brute-force attack to find the key for short encrypted texts.
- **Part E**: Smarter key breaking for longer ciphertexts using frequency-based analysis.

### Question 2 – RSA Attacks

- **Part A**: Crack a 4-digit PIN by comparing encrypted values.
- **Part B**: Recover a credit card number using cube root and a few checks.
- **Part C**: Forge a fake server signature that still passes validation.

## ▶️ How to Run

Make sure you’re using Python 3. Run any of the decryption tasks like this:

```bash
python3 decrypt.py 1d
python3 decrypt.py 1e
python3 decrypt.py 2a
