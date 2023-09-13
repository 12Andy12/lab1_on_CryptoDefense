from random import randint
import Fast_pow

P = 10001779
G = 10000763


class CryptoUser(object):
    def __init__(self):
        self.private_key = randint(10 ** 4, P)
        self.my_public_key = Fast_pow.mega_pow(G, self.private_key, P)
        self.common_key = None

    def get_my_private_key(self):
        return self.private_key

    def get_my_public_key(self):
        return self.my_public_key

    def get_my_common_key(self):
        return self.common_key

    def generate_common_key(self, other_public_key):
        self.common_key = Fast_pow.mega_pow(other_public_key, self.private_key, P)

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.common_key
        for c in message:
            encrypted_message += chr(ord(c) + key % 10 + 1)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.common_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key % 10 - 1)
        return decrypted_message
