BLACKLIST = set([
    "DeployerPubKey1111111111111111111111111111111",
    "DeployerPubKey2222222222222222222222222222222",
])

def is_blacklisted(deployer):
    return deployer in BLACKLIST
