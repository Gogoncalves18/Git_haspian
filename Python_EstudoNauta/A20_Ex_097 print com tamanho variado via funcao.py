def escreva(msg):
    tam=int((len(msg))+4)
    print('='*tam)
    print(f'{msg:^{tam}}')
    print('='*tam)


escreva('Bom dia python')
escreva('Oi!')
escreva('Nossa como vc é simpatico pela manha')
