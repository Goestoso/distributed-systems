#include <stdio.h>
#include <pthread.h>

int r;

struct arg {
  int ri;
};


void *fun(void *a) {
  struct arg *args = a;
  int i,j,x;

  x=0;
  for(i=0; i < args->ri; i++)
    for(j=0; j < 10000; j++)
      x=x+1;
  r=r+x;
}


void main() {
  pthread_t threads1;
  pthread_t threads2;
  pthread_t threads3;
  pthread_t threads4;
  struct arg a;
  a.ri=2500;
  pthread_create(&(threads1), NULL, fun, &a);
  pthread_create(&(threads2), NULL, fun, &a);
  pthread_create(&(threads3), NULL, fun, &a);
  pthread_create(&(threads4), NULL, fun, &a);
  pthread_join(threads1, NULL);
  pthread_join(threads2, NULL);
  pthread_join(threads3, NULL);
  pthread_join(threads4, NULL);
  
  printf("\n%d\n",r);
}

