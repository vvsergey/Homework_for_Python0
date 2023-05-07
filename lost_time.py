def find_time(hour:int, minutes:int) -> bool:
    if hour <=23 and minutes < 60:
        return True
    return False

if __name__ == '__main__':
    hour = int(input())
    minutes = int (input())
    print(find_time(hour, minutes))
    
