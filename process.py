with open('cleveland.csv', 'w') as write_file:
    write_file.write(''.join([str(i) + ' ' for i in range(74)]))
    write_file.write('74\n')
    with open('cleveland.data', 'r') as f:
        while True:
            buffer = ''
            for i in range(10):
                buffer += f.readline()[:-1] + ' '
            if buffer == 10*' ' :
                break
            buffer = buffer[:-1] + '\n'
            write_file.write(buffer)

