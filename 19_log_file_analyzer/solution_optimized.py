import hashlib

class ChecksumVerifier:
    def calculate(self, path, algo="sha256"):
        hash_func = hashlib.new(algo)
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
