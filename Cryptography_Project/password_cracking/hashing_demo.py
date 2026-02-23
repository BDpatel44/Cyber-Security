import hashlib, os

password = "mypassword"
salt = os.urandom(16)
hashed = hashlib.sha256(salt + password.encode()).hexdigest()
print("Salt:", salt.hex())
print("Hashed:", hashed)