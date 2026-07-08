class WeakDiffieHellmanAttack:
    def __init__(self, primeModulus, generatorBase):
        self.primeModulus = primeModulus
        self.generatorBase = generatorBase

    def crackPrivateKey(self, interceptedPublicKey):
        for possibleExponent in range(1, self.primeModulus):
            if (self.generatorBase ** possibleExponent) % self.primeModulus == interceptedPublicKey:
                return possibleExponent
        return None

simulatedPrime = 227
simulatedGenerator = 14

alicePrivate = 189
alicePublic = (simulatedGenerator ** alicePrivate) % simulatedPrime

bobPrivate = 192
bobPublic = (simulatedGenerator ** bobPrivate) % simulatedPrime

attackEngine = WeakDiffieHellmanAttack(simulatedPrime, simulatedGenerator)
recoveredAlicePrivate = attackEngine.crackPrivateKey(alicePublic)

if recoveredAlicePrivate is not None:
    interceptedSharedSecret = (bobPublic ** recoveredAlicePrivate) % simulatedPrime
    print(f"Intercepted Alice Public: {alicePublic}")
    print(f"Cracked Alice Private Key: {recoveredAlicePrivate}")
    print(f"Successfully Intercepted Shared Secret: {interceptedSharedSecret}")