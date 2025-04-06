import threading

global r
r = 0
lock = threading.Lock()  # Cria um lock para sincronização

def fun(ri):
    global r
    x = 0
    for i in range(ri):
        for j in range(10000):
            x += 1
    # Usar lock para proteger a modificação da variável global
    with lock:
        r += x

# Criar as threads
t1 = threading.Thread(target=fun, args=(2500,))
t2 = threading.Thread(target=fun, args=(2500,))
t3 = threading.Thread(target=fun, args=(2500,))
t4 = threading.Thread(target=fun, args=(2500,))

# Iniciar as threads
t1.start()
t2.start()
t3.start()
t4.start()

# Aguardar as threads terminarem
t1.join()
t2.join()
t3.join()
t4.join()

# Exibir o resultado final
print(r)