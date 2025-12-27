from solution_optimized import ChecksumVerifier

verifier = ChecksumVerifier()
checksum = verifier.calculate(__file__)
assert isinstance(checksum, str)
print("Checksum verifier tests passed")
