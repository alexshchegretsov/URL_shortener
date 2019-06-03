BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base_62_encode(id, alphabet=BASE62):
    """Encode a positive number in Base X

    Arguments:
    - `id`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    arr = []
    base = len(alphabet)
    while id:
        id, rem = divmod(id, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base_62_decode(link_id, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `link_id`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    link_id_length = len(link_id)
    url_id = 0
    idx = 0

    for char in link_id:
        power = (link_id_length - (idx + 1))
        url_id += alphabet.index(char) * (base ** power)
        idx += 1

    return url_id
