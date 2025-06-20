# Simple Python Cryptography and RSA Breaks

In this project, I implemented and broke basic cryptographic schemes using Python. I worked on repeated-key XOR ciphers and explored simplified RSA vulnerabilities, including PIN cracking, credit card recovery, and signature forgery. This was a great hands-on experience in thinking like both a cryptographer and an attacker.

## 📁 Folder Structure

```
q1.py       # Implements and breaks repeated-key XOR cipher (encryption, decryption, scoring, brute-force, smart attack)
q2.py       # Performs RSA attacks: PIN cracking, credit card recovery, and forging digital signatures
q1*.cipher  # Sample encrypted files for XOR tests
q2*-*.txt   # Sample encrypted files and supporting inputs for RSA attacks
q1c.txt-q2c.txt  # Short explanations of methods, attack logic, and implementation notes
```

## 🔐 What I Did

### 🔁 Repeated Key Cipher (q1.py)

* **Encryption/Decryption**: I wrote the core logic for encrypting and decrypting messages using a repeated-key XOR scheme.
* **Plaintext Scoring**: Implemented a scoring system that guesses if a decrypted string is "English-like" (based on characters and frequency).
* **Brute-force Attack**: Tried every possible short key to find the one that gives the best scoring plaintext.
* **Smarter Break**: Improved the attack to scale for longer keys using a frequency-based approach, guessing each byte independently.

### 🔓 RSA Vulnerability Exploits (q2.py)

* **PIN Recovery**: Brute-forced a 4-digit RSA-encrypted PIN by matching encrypted outputs.
* **Credit Card Recovery**: Used cube root approximation and validation to recover short credit card numbers from RSA ciphertexts.
* **Signature Forgery**: Crafted a fake server response with a valid-looking signature that passed signature verification logic.

## ▶️ How to Run

Make sure you're using Python 3. Example usage:

```bash
python3 decrypt.py 1d   # Decrypt short XOR cipher with brute-force
python3 decrypt.py 1e   # Decrypt long XOR cipher using smarter break
python3 decrypt.py 2a   # Recover a PIN using RSA decryption attack
```

---

This project helped me get comfortable with cryptographic thinking, understand how subtle flaws lead to major breaks, and practice writing efficient attack code from scratch.
