def determine_season(m:int) -> str:
    if 1  <= m < 7: return f'WINTER'
    elif 7 <= m <=12: return f'SUMMER'
    else: return f' неправильный формат данных. Введите целое число m от 1  до 12'


if __name__ == '__main__':
    determine_season(5)