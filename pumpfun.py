def is_token_on_pumpfun(token_address: str) -> bool:
    """
    Fast local check to see if a token is likely from Pump.fun based on address suffix.
    """
    return token_address.lower().endswith("pump")
