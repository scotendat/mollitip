def inch_swap_sell(privatekey, amount_to_swap, fromTokenAddress, to_symbol):
    """Swap tokens on 1inch using a private key.

    Args:
        privatekey (str): The private key of the account to use for the swap.
        amount_to_swap (int): The amount of tokens to swap.
        fromTokenAddress (str): The address of the token to swap from.
        to_symbol (str): The symbol of the token to swap to.

    Returns:
        dict: The transaction receipt.
    """

    # Get the 1inch API key.
    api_key = get_api_key()

    # Get the 1inch client.
    client = get_client(api_key)

    # Get the token addresses.
    fromTokenAddress = get_token_address(fromTokenAddress)
    toTokenAddress = get_token_address(to_symbol)

    # Get the amount of tokens to swap.
    amount_to_swap = int(amount_to_swap * 10 ** 18)

    # Get the current gas price.
    gas_price = get_gas_price()

    # Get the current nonce.
    nonce = get_nonce(privatekey)

    # Create the swap transaction.
    transaction = client.create_swap_transaction(
        privatekey,
        amount_to_swap,
        fromTokenAddress,
        toTokenAddress,
        gas_price,
        nonce,
    )

    # Send the swap transaction.
    transaction_receipt = client.send_transaction(transaction)

    # Return the transaction receipt.
    return transaction_receipt
