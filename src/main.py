

def sum(fst: int, snd: int) -> int:
    return fst + snd


def main():
    while True:
        print('Provide two number')

        values = list(map(int, input().split()))
        if len(values) < 2:
            continue
        if len(values) < 2:
            continue
        a, b = values
        print(f"Sum of your numbers: {sum(fst=a, snd=b)}")
        break


if __name__ == '__main__':
    main()
