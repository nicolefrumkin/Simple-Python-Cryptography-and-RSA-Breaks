from q2_atm import ATM, ServerResponse


def extract_PIN(encrypted_PIN) -> int:
    """Extracts the original PIN string from an encrypted PIN."""
    for pin in range(10000):
        encrypted_attempt = ATM().encrypt_PIN(pin)
        if encrypted_attempt == encrypted_PIN:
            return pin
    return -1

def extract_credit_card(encrypted_credit_card) -> int:
    """Extracts a credit card number string from its ciphertext."""
    cube_root = int(round(encrypted_credit_card ** (1/3)))
    for guess in range(cube_root - 2, cube_root + 3):
        if ATM().encrypt_credit_card(guess) == encrypted_credit_card:
            return guess
    return -1


def forge_signature():
    """Forge a server response that passes verification."""
    approval_status = ATM.CODE_APPROVAL
    signature = 1
    return ServerResponse(status=ATM.CODE_APPROVAL, signature=signature)
