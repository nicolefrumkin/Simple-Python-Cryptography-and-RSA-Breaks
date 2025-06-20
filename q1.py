class RepeatedKeyCipher:

    def __init__(self, key: bytes = bytes([0, 0, 0, 0, 0])):
        """Initializes the object with a list of integers between 0 and 255."""
        # WARNING: DON'T EDIT THIS FUNCTION!
        self.key = list(key)

    def encrypt(self, plaintext: str) -> bytes:
        """Encrypts a given plaintext string and returns the ciphertext."""
        if isinstance(plaintext, str):
            text_bytes = bytearray(plaintext.encode('latin-1'))
        else:
            text_bytes = bytearray(plaintext)
        for i in range(len(text_bytes)):
            text_bytes[i] = text_bytes[i]^self.key[i%len(self.key)]
        return bytes(text_bytes)

    def decrypt(self, ciphertext: bytes) -> str:
        """Decrypts a given ciphertext string and returns the plaintext."""
        decrypted = self.encrypt(ciphertext)
        return decrypted.decode('latin-1')


class BreakerAssistant:

    def plaintext_score(self, plaintext: str) -> float:
        """Scores a candidate plaintext string, higher means more likely."""
        score = 0
        valid = [' ', '?', '!', '"', '.', ',', ':', "'", '-','0','1', '2', '3', '4', '5', '6', '7', '8', '9', '\n']
        common_letters = ['e','t','a','o','i','n','s','h','r','d']
        for char in plaintext:
            if 'a' <= char.lower() <= 'z' or char in valid:
                score += 1
            if char.lower() in common_letters:
                score +=1

        return score

    def brute_force(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher by brute-forcing all keys."""
        max_score = 0
        correct_plaintext = ""
        curr_key = [0]*key_length
        while True:
            key = bytes(curr_key)
            temp = RepeatedKeyCipher(key)
            plain_text = temp.decrypt(cipher_text)
            score = self.plaintext_score(plain_text)
            if score > max_score:
                max_score = score
                correct_plaintext = plain_text
            pos = key_length - 1
            while pos >= 0:
                curr_key[pos] += 1
                if curr_key[pos] < 256:
                    break
                curr_key[pos] = 0
                pos -= 1
            if pos < 0:
                break
        return correct_plaintext
        
    def smarter_break(self, cipher_text: bytes, key_length: int) -> str:
        """Breaks a Repeated Key Cipher any way you like."""
        key = [0]*key_length
        for i in range(key_length):
            if i >= len(cipher_text):
                break
            max_score = 0
            correct_key_byte = 0
            temp_cipher_text = bytes([cipher_text[k] for k in range(i, len(cipher_text), key_length)])
            for key_int in range(256):
                key_byte = bytes([key_int])
                temp = RepeatedKeyCipher(key_byte)
                plain_text = temp.decrypt(temp_cipher_text)
                score = self.plaintext_score(plain_text)
                if score > max_score:
                    max_score = score
                    correct_key_byte = key_int
            key[i] = correct_key_byte
        full_key = bytes(key)
        temp = RepeatedKeyCipher(full_key)
        return temp.decrypt(cipher_text)
        
        
