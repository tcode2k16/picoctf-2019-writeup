// #include <stdio.h> 
// #include <stdlib.h> 

// // int gen_expr(int a1) {
// //   if (a1) {
// //     v3 = maybe_decrease(a1);
// //     v4 = maybe_decrease(a1);
// //     v5 = get_random_op();
// //     putchar(40);
// //     v6 = gen_expr(v3);
// //     printf(" %c ", (unsigned int)v5);
// //     v7 = gen_expr(v4);
// //     putchar(41);
// //     result = do_op(v5, v6, v7);
// //   } else {
// //     v1 = (signed int)get_random();
// //     printf("(%lld)", v1);
// //     result = v1;
// //   }
// //   return result;
// // }

// int main() {
//   // srand(time(0));
//   char buf[512];
//   FILE* file = popen("./times-up-again", "r");
//   if (!file) {
//     puts("error\n");
//     return -1;
//   }
//   fgets(buf, sizeof(buf), file);
//   printf("%s", buf);

// }


#include<unistd.h>
#include<sys/wait.h>
#include<sys/prctl.h>
#include<signal.h>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include "expr.h"


int main(int argc, char** argv) {
  pid_t pid = 0;
  int inpipefd[2];
  int outpipefd[2];
  char buf[512];
  char msg[256];
  int status;

  pipe(inpipefd);
  pipe(outpipefd);
  pid = fork();
  if (pid == 0)
  {
    // Child
    dup2(outpipefd[0], STDIN_FILENO);
    dup2(inpipefd[1], STDOUT_FILENO);
    dup2(inpipefd[1], STDERR_FILENO);

    //ask kernel to deliver SIGTERM in case the parent dies
    prctl(PR_SET_PDEATHSIG, SIGTERM);

    //replace tee with your process
    execl("./times-up-again", "times-up-again" ,(char*) NULL);
    // Nothing below this line should be executed by child process. If so, 
    // it means that the execl function wasn't successfull, so lets exit:
    exit(1);
  }
  // The code below will be executed only by parent. You can write and read
  // from the child using pipefd descriptors, and you can send signals to 
  // the process using its pid by kill() function. If the child process will
  // exit unexpectedly, the parent process will obtain SIGCHLD signal that
  // can be handled (e.g. you can respawn the child process).

  //close unused pipe ends
  close(outpipefd[0]);
  close(inpipefd[1]);

  // Now, you can write to outpipefd[1] and read from inpipefd[0] :  
  // while(1)
  // {
  //   printf("Enter message to send\n");
  //   scanf("%s", msg);
  //   if(strcmp(msg, "exit") == 0) break;

  //   write(outpipefd[1], msg, strlen(msg));
  //   read(inpipefd[0], buf, 256);

  //   printf("Received answer: %s\n", buf);
  // }

  read(inpipefd[0], buf, 512);

  printf("Received answer: %s\n", buf);
  *(strchr(buf, '\n')) = 0;
  char *temp = strchr(buf, ' ')+1;

  struct expr_var_list vars = {0};
  struct expr *e = expr_create(temp, strlen(temp), &vars, NULL);
  if (e == NULL) {
    printf("Syntax error");
    return 1;
  }

  float result = expr_eval(e);
  printf("result: %f\n", result);


  kill(pid, SIGKILL); //send SIGKILL signal to the child process
  waitpid(pid, &status, 0);
}