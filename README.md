# 📖⚙💻 Estudos sobre sistemas distribuídos

## 🧪 Configurando o ambiente de estudos

- **1º**: Instale o `python` (caso não tenha instalado).
- **2º**: Configure um ambiente virtual do Python pelo `powershell`:

```
cd C:\
mkdir projetoSD
cd projetoSD
python -m venv projetoSD
```
- **3º**: Para iniciar o ambiente virtual, rode o comando:

```
.\Scripts\Activate  
```

- **4º**: Se quiser calcular o tempo de execução de um programa, use a sintaxe do `powrshell`:

```
Measure-Command { language .\program }
```

> *Exemplo com linguagem de programação*:

```
Measure-Command { python .\prog1.py }
```

> *Exemplo sem linguagem de programação*:

```
Measure-Command {.\prog1-thread-4.exe }
```

## 1️⃣ Sistema não distribuído:

- Quando são executados os programas `prog1.py` e `prog1-mod.py`:

> `prog1.py` →  TotalSeconds: 6,3160648

>  `prog1-mod.py` → TotalSeconds: 3,94512

## 🔢 Sistema distribuído:

### Por processos

- Quando são executados os programas `prog1-proc.py` e `prog1-proc-4.py`:

> `prog1-proc.py` →  TotalSeconds: 1,6072725

>  `prog1-proc-4.py` → TotalSeconds: 0,0605766

### Por threads

- Quando são executados os programas `prog1-thread-4.py` e `prog1-thread-4.exe` (binário criado pela linguagem `c`):

> `prog1-thread-4.py` →  TotalSeconds: 2,7360153

> `prog1-thread-4.exe` →  TotalSeconds: 0,0282723

#### 👁️‍🗨️ Observação:

- O `python` não implementa corretamente o *multi-threading*, por isso o programa compilado pelo `c` foi mais eficiente.
- O ***GIL*** (Global Interpreter Lock) é um mecanismo que garante que apenas uma *thread* execute código `python` por vez, mesmo em sistemas com múltiplos núcleos de CPU. Ele é necessário para proteger a memória compartilhada e evitar inconsistências durante a execução de operações em objetos Python. Contudo, isso significa que o verdadeiro paralelismo não é alcançado em *threads* puramente `python`.
- Como apenas uma *thread* pode estar ativa no interpretador `python` a qualquer momento, o uso de várias *threads* em aplicações intensivas de CPU geralmente não resulta em um ganho significativo de desempenho.
- Em `c`, você pode usar bibliotecas como `pthread` (*POSIX threads*) que oferecem controle de baixo nível sobre a criação, gerenciamento e sincronização de threads. Isso permite otimizar recursos de maneira mais granular, o que é perfeito para programas de alto desempenho.
