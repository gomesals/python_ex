def media(x1, x2):
    """
        Retorna a média de dois números
        >> > media(10, 8)
        9.0
        >> > media(10, 5)
        7.5
    """
    return (x1 + x2) / 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
