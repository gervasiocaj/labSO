# Laboratório 1

## QT1 - Quais os estados possíveis de um processo no kernel linux 4.8? Quais as razões para mudança entre os estados?

```
TASK_RUNNING
TASK_INTERRUPTIBLE
TASK_UNINTERRUPTIBLE
TASK_DEAD
TASK_WAKEKILL
TASK_WAKING
TASK_PARKED
TASK_NOLOAD
TASK_NEW
TASK_STATE_MAX
```

Basicamente, quando um processo é iniciado (ou forked), seu status é RUNNING. Quando precisa de algum recurso, o processo dorme, entrando em INTERRUPTIBLE quando aguarda um timeslot ou evento, ou UNINTERRUPTIBLE, quando está aguardando um sinal de resposta do recurso sendo acessado. Ao fim da execução, o status é ZOMBIE, e o sistema operacional se encarrega de limpar e reutilizar o espaço.

## QP1 - Explique os argumentos e retornos das system calls open e write (sobre os arquivos inputA e inputB)

No diff a seguir, são enfatizadas as diferentes regiões de memória que são alocadas, lidas e escritas.

```
@@ -1,35 +1,36 @@
-execve("./L1_qp1", ["./L1_qp1", "/tmp/a", "-o", "/tmp/rastro2.txt"], [/* 16 vars */]) = 0
-brk(0)                                  = 0x1d8f000
+execve("./L1_qp1", ["./L1_qp1", "/tmp/a", "-o", "/tmp/rastro1.txt"], [/* 16 vars */]) = 0
+brk(0)                                  = 0x1260000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
-mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f19fe6d0000
+mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f268bc80000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=34176, ...}) = 0
-mmap(NULL, 34176, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f19fe6c7000
+mmap(NULL, 34176, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f268bc88000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P \2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=1840928, ...}) = 0
-mmap(NULL, 3949248, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f19fe030000
-mprotect(0x7f19fe1ea000, 2097152, PROT_NONE) = 0
-mmap(0x7f19fe3ea000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1ba000) = 0x7f19fe3ea000
-mmap(0x7f19fe3f0000, 17088, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f19fe3f0000
+mmap(NULL, 3949248, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f268b630000
+mprotect(0x7f268b7ea000, 2097152, PROT_NONE) = 0
+mmap(0x7f268b9ea000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1ba000) = 0x7f268b
+9ea000
+mmap(0x7f268b9f0000, 17088, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f268b9f0000
close(3)                                = 0
-mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f19fe6c0000
-mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f19fe6b0000
-arch_prctl(ARCH_SET_FS, 0x7f19fe6b0740) = 0
-mprotect(0x7f19fe3ea000, 16384, PROT_READ) = 0
+mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f268bc70000
+mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f268bc60000
+arch_prctl(ARCH_SET_FS, 0x7f268bc60740) = 0
+mprotect(0x7f268b9ea000, 16384, PROT_READ) = 0
mprotect(0x600000, 4096, PROT_READ)     = 0
-mprotect(0x7f19fe622000, 4096, PROT_READ) = 0
-munmap(0x7f19fe6c7000, 34176)           = 0
+mprotect(0x7f268bc22000, 4096, PROT_READ) = 0
+munmap(0x7f268bc88000, 34176)           = 0
open("/tmp/a", O_RDWR)                  = 3
-brk(0)                                  = 0x1d8f000
-brk(0x1db0000)                          = 0x1db0000
+brk(0)                                  = 0x1260000
+brk(0x1281000)                          = 0x1281000
write(3, "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 42) = 42
rt_sigprocmask(SIG_BLOCK, [CHLD], [], 8) = 0
-rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [CHLD], SA_RESTORER|SA_RESTART, 0x7f8694266cb0}, 8) = 0
+rt_sigaction(SIGCHLD, NULL, {SIG_DFL, [CHLD], SA_RESTORER|SA_RESTART, 0x7f535bc66cb0}, 8) = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
-nanosleep({15, 0}, 0x7fffc5302ac0)      = 0
+nanosleep({15, 0}, 0x7fffe0986090)      = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

## QT3 - Que estrutura de dados no kernel linux 4.8 armazena os file descriptors de um processo? Explique cada um dos campos dessa estrutura

Uma linked list circular (`list_head`). Cada campo (`task_struct`) contém um `children` que é um processo forked e um `sibling`, que é o próximo processo que seu pai criou.