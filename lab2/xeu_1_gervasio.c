#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char *user = getenv("USER");

  while (1) {
    char *line = NULL;
    size_t linecapp = 0;
    printf("$%s => ", user);
    getline(&line, &linecapp, stdin);
  }
  return 0;
}