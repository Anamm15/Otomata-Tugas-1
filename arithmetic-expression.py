operator = {'+', '-', '*', '/'}
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def is_arithmetic_expression(expression):
    jumlahBukaKurung = 0
    if (expression[0] in operator and expression[0] != '-') or expression[0] == ')':
        return False
    
    for i in range(len(expression)):
        if expression[i] in operator and expression[i-1] in operator:
            return False
        if expression[i] in operator and expression[i] != '-' and expression[i-1]=='(':
            return False
        if expression[i] == '(':
            jumlahBukaKurung+=1
        if expression[i] == ')':
            if jumlahBukaKurung == 0 or expression[i-1] in operator or expression[i-1]=='(':
                return False
            jumlahBukaKurung-=1    
    if jumlahBukaKurung or expression[len(expression)-1] in operator:
        return False
    return True
        
if __name__ == "__main__":
    expression = input('Masukkan kalimat aritmatika: ')
    if is_arithmetic_expression(expression):
        print('Kalimat aritmatika')
    else:
        print('Bukan kalimat aritmatika')
