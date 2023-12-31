from passlib.context import CryptContext

class Hash:
    __context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def verify_hash(plain_password, hashed_password):
        return Hash.__context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_hash(password):
        return Hash.__context.hash(password)
