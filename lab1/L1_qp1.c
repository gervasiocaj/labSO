#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (int argc, char* argv[]) {
 int fd;
 char pathbuf[256];
 char* path = argv[1];
 snprintf (pathbuf, sizeof pathbuf, "%s", path);
 fd = open (pathbuf, O_RDWR);
 char* buf = (char*) malloc (sizeof (char) * 42);
 write (fd, buf, 42);
 sleep (15);
 return 0;
}
