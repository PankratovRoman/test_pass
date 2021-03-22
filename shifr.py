secure = {'!Qв': 'a', '_>и': 'b', ':3н': 'c', 'кN9': 'd', 'у0.': 'e', 'х=}': 'f', 'б@#': 'g', 'ы](': 'h', 'эay': 'i',
          'Vи*': 'j', '$я%': 'k', '&чj': 'l', '+с-': 'm', 'kм#': 'n', '3и,': 'o', '[т<': 'p', '.,ь': 'q', 'aфP': 'r',
          'Bыf': 's', 'Iв;': 't', 'Sа6': 'u', 'п_9': 'v', 'рC;': 'w', 'оns': 'x', 'лR|': 'y', ')дo': 'z', 'ж&z': 'A',
          'э%h': 'B', 'й$)': 'C', 'цB;': 'D', 'уlK': 'E', 'lгJ': 'F', '|к|': 'G', 'lеd': 'H', '(н)': 'I', '}ш{': 'J',
          '+=_': 'K', '__0': 'L', '&^%': 'M', '><?': 'N', 'hsj': 'O', '|][': 'P', 'm<ы': 'Q', 'klH': 'R', '(!*': 'S',
          'mH*': 'T', 'aвd': 'U', 'kаj': 'V', ')as': 'W', '/.L': 'X', 'zdf': 'Y', ']|p': 'Z', 'zja': '1', 'okk': '2',
          '@34': '3', 'l}|': '4', 'xпn': '5', 'zsf': '6', '89L': '7', '#4м': '8', 'lиL': '9', 'Opk': '0'}


def le_shifr(encrypted):
    """Функция для шифровки введенного значения"""
    reversed_dict = {x: y for y, x in secure.items()}
    result = [(a, reversed_dict[a]) for a in encrypted]
    return result


def decrypting(decrypted):
    """Функция для де-шифровки введенного значения"""
    predecr_pass = [(decr_pass[i:i + 3]) for i in range(0, len(decrypted), 3)]
    result = [(a, secure[a]) for a in predecr_pass]
    return result


def output(pwd):
    for item, item1 in pwd:
        print(str(item1), end='')


choose = input("Type 1 for encrypt your pass, and 2 for decryption: ")

if choose == "1":
    open_pass = list(input('Enter your password here: '))
    print('Your encrypted password: ')
    output(le_shifr(open_pass))
elif choose == "2":
    decr_pass = input('Enter your encrypted value here: ')
    print('Your decrypted password: ')
    output(decrypting(decr_pass))
else:
    print("Choose 1 or 2")
