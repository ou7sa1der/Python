word_to_remove = input()
sequence = input().split(f'{word_to_remove}')



while True:
    sequence = ''.join(sequence)
    if word_to_remove in sequence:
        sequence = sequence.split(f'{word_to_remove}')
        sequence = ''.join(sequence)
    else:
        print(sequence)
        break