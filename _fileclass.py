from cryptography.fernet import Fernet

class MyFile:
    
    filename: str
    filekey: str
    
    def __init__(self, filename, filekey):
        
        self.filename = str(filename)
        self.filekey = str(filekey)
    
    def generate_key(cls):
        with open(cls.filekey,"wb") as filekeygen:
            key_ciph = Fernet.generate_key()
            filekeygen.write(key_ciph)
        
    def encrypt(cls):
        with open(cls.filename, "rb") as filere:
            content = filere.read()        
        with open(cls.filekey,"rb") as keyfile:
            key = keyfile.read()
        fernet = Fernet(key)    
        encrypter = fernet.encrypt(content)
        with open(cls.filename, "wb") as encr:
            encr.write(encrypter)
            
    def decrypt(cls):
        with open(cls.filename, "rb") as filere:
            content = filere.read()
        with open(cls.filekey,"rb") as keyfile:
            key = keyfile.read()
        fernet = Fernet(key)    
        decrypted = fernet.decrypt(content)
        with open(cls.filename, "wb") as encr:
            encr.write(decrypted)
        


    
    