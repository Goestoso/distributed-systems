from multiprocessing import Process, Value, Lock

def fun(ri, r, lock):
    x = 0
    for i in range(ri):
        for j in range(10000):
            x += 1
    with lock:  # Garantir acesso exclusivo à variável compartilhada
        r.value += x

if __name__ == '__main__':
    r = Value('i', 0)  # Variável compartilhada
    lock = Lock()      # Lock para sincronização

    # Dividir o trabalho em 4 processos
    p1 = Process(target=fun, args=(2500, r, lock))
    p2 = Process(target=fun, args=(2500, r, lock))
    p3 = Process(target=fun, args=(2500, r, lock))
    p4 = Process(target=fun, args=(2500, r, lock))

    # Iniciar os processos
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Aguardar os processos terminarem
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    # Exibir o resultado
    print(r.value)