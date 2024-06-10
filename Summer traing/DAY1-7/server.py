import socket
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate AES key
aes_key = get_random_bytes(16)
aes_cipher = AES.new(aes_key, AES.MODE_ECB)

# Generate RSA key pair
rsa_key = RSA.generate(2048)

# Server configuration
server_host = '127.0.0.1'
server_port = 12345

# Function to sign data using RSA private key
def sign_data(data):
    hash_value = SHA256.new(data)
    signature = pkcs1_15.new(rsa_key).sign(hash_value)
    return signature

# Function to verify signature using RSA public key
def verify_signature(data, signature, public_key):
    hash_value = SHA256.new(data)
    try:
        pkcs1_15.new(public_key).verify(hash_value, signature)
        return True
    except (ValueError, TypeError):
        return False

# Server
def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_host, server_port))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:", data.decode())

                # Decrypt received data using AES
                decrypted_data = aes_cipher.decrypt(data).decode()
                print("Decrypted:", decrypted_data)

                # Verify signature
                signature = conn.recv(256)
                if verify_signature(data, signature, rsa_key.public_key()):
                    print("Signature verified.")
                else:
                    print("Signature verification failed.")

                # Echo back to client
                conn.sendall(data)

# Client
def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        message = "Hello, Server!"

        # Encrypt message using AES
        encrypted_message = aes_cipher.encrypt(message.encode())
        print("Encrypted:", encrypted_message)

        # Send encrypted message
        s.sendall(encrypted_message)

        # Sign message
        signature = sign_data(encrypted_message)
        s.sendall(signature)

        # Receive echo from server
        data = s.recv(1024)
        print('Received:', data.decode())

if __name__ == "__main__":
    server()
f