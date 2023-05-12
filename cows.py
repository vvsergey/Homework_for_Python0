def pharse_ends(cow:int) -> str:
    s = f'На лугу пасется {cow} коров'
    cow = cow % 100
    if 11 <= cow <= 19: return s
    cow = cow % 10
    if cow == 1: return s + 'а'
    elif  2 <= cow <= 4: return s +'ы'
    else: return s




if __name__ == '__main__':
    [ print(pharse_ends(cow)) for cow in range(1000)[1:]]
    