#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void split_args(char *line, char *args[]) {
  int i=0;
  char *piece = strtok(line, " \n");
  while (piece) {
    args[i++] = piece;
    piece = strtok(NULL, " \n");
  }
  args[i] = piece;
}

void execute(char *cmd[]) {
  pid_t pid;

  if ((pid=fork()) == 0) {
    execvp(*cmd, cmd);
    perror("execve");
  } else {
    while (wait(0) != pid);
  }
}

int main() {
  char *user = getenv("USER");

  while (1) {
    //char *args[] = {"date", NULL};
    char *args[1024];
    printf("$%s => ", user);
    
    char *line = NULL;
    size_t linecapp = 0;
    getline(&line, &linecapp, stdin);
    
    split_args(line, args);

    execute(args);
  }
  return 0;
}