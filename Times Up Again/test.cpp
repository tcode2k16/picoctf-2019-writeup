// CPP program to evaluate a given 
// expression where tokens are  
// separated by space. 
#include <bits/stdc++.h> 
#include<unistd.h>
#include<sys/wait.h>
#include<sys/prctl.h>
#include<signal.h>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>

using namespace std; 

// https://www.geeksforgeeks.org/expression-evaluation/
// Function to find precedence of  
// operators. 
int precedence(char op){ 
    if(op == '+'||op == '-') 
    return 1; 
    if(op == '*'||op == '/') 
    return 2; 
    return 0; 
} 
  
// Function to perform arithmetic operations. 
long long applyOp(long long a, long long b, char op){ 
    switch(op){ 
        case '+': return (a + b); 
        case '-': return (a - b); 
        case '*': return (a * b); 
        case '/': return (a / b); 
    } 
} 
  
// Function that returns value of 
// expression after evaluation. 
long long evaluate(string tokens){ 
    int i; 
    // stack to store integer values. 
    stack <long long> values; 
      
    // stack to store operators. 
    stack <char> ops; 
      
    for(i = 0; i < tokens.length(); i++){ 
        // printf("char: %c\n", tokens[i]);
        // fflush(stdout);
        if (!ops.empty()) {
            // printf("top: %c\n", ops.top());
            // fflush(stdout);
        }
        // Current token is a whitespace, 
        // skip it. 
        if(tokens[i] == ' ') 
            continue; 
          
        // Current token is an opening  
        // brace, push it to 'ops' 
        else if(tokens[i] == '('){ 
            // printf("got here\n");
            // fflush(stdout);
            ops.push(tokens[i]); 
        } 
          
        // Current token is a number, push  
        // it to stack for numbers. 
        else if(tokens[i] == '-' and isdigit(tokens[i+1])) {
            i++;
            long long val = 0; 
            // printf("done this\n");
            // fflush(stdout);
            // There may be more than one 
            // digits in number. 
            while(i < tokens.length() &&  
                        isdigit(tokens[i])) 
            { 
                val = (val*10) + (tokens[i]-'0'); 
                i++; 
            } 
            i--;
            // printf("int: %d\n", -val);
            // fflush(stdout);
              
            values.push(-val); 
        } else if(isdigit(tokens[i])){ 
            long long val = 0; 
            // printf("done this\n");
            // fflush(stdout);
            // There may be more than one 
            // digits in number. 
            while(i < tokens.length() &&  
                        isdigit(tokens[i])) 
            { 
                val = (val*10) + (tokens[i]-'0'); 
                i++; 
            } 
            i--;
            // printf("int: %d\n", val);
            // fflush(stdout);
              
            values.push(val); 
        } 
          
        // Closing brace encountered, solve  
        // entire brace. 
        else if(tokens[i] == ')') 
        { 
            
            // printf("sym here\n");
            // fflush(stdout);
            // if (!ops.empty()) {
            //     printf("%c\n", ops.top());
            //     fflush(stdout);
            // }
            // printf("sym here\n");
            // fflush(stdout);
            while(!ops.empty() && ops.top() != '(') 
            { 
                long long val2 = values.top(); 
                values.pop(); 
                  
                long long val1 = values.top(); 
                values.pop(); 
                  
                char op = ops.top(); 
                ops.pop(); 
                  
                values.push(applyOp(val1, val2, op)); 
            } 
              
            // pop opening brace. 
            if(!ops.empty()) 
               ops.pop(); 
        } 
          
        // Current token is an operator. 
        else
        { 
            // While top of 'ops' has same or greater  
            // precedence to current token, which 
            // is an operator. Apply operator on top  
            // of 'ops' to top two elements in values stack. 
            while(!ops.empty() && precedence(ops.top()) 
                                >= precedence(tokens[i])){ 
                long long val2 = values.top(); 
                values.pop(); 
                  
                long long val1 = values.top(); 
                values.pop(); 
                  
                char op = ops.top(); 
                ops.pop(); 
                  
                values.push(applyOp(val1, val2, op)); 
            } 
              
            // Push current token to 'ops'. 
            ops.push(tokens[i]); 
        } 
    }

    // printf("done with parsing!\n");
    // fflush(stdout); 
      
    // Entire expression has been parsed at this 
    // point, apply remaining ops to remaining 
    // values. 
    // printf("%d\n",values.top());
    // fflush(stdout); 
    // printf("%d\n",ops.empty());
    // fflush(stdout); 
    while(!ops.empty()){ 
        long long val2 = values.top(); 
        values.pop(); 
                  
        long long val1 = values.top(); 
        values.pop(); 
                  
        char op = ops.top(); 
        ops.pop(); 
                  
        values.push(applyOp(val1, val2, op)); 
    } 
      
    // Top of 'values' contains result, return it. 
    return values.top(); 
} 

// int main() { 
//     // cout << evaluate("(10+1)") << "\n"; 
//     cout << evaluate("(((((-826701676) - (-1438557138)) - ((533548175) - (2007560516))) + (((-2114031573) - (1772790520)) * (((-1574207334) + (696304266)) + ((1245841263) * (2040484312))))) * ((((938950606) * (-859778227)) + ((-1392684737) - (-803056447))) * (((1690394102) - ((-85463468) * (-1119664953))) + ((-1644399076) - (587921107)))))") << "\n"; 


//     // cout << evaluate("100 * 2 + 12") << "\n"; 
//     // cout << evaluate("100 * ( 2 + 12 )") << "\n"; 
//     // cout << evaluate("100 * ( 2 + 12 ) / 14"); 
//     // cout << evaluate("(((100) * ( 2 + 12 ))) / 14"); 
//     return 0; 
// } 


int main(int argc, char** argv) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  char buf[1000];
  fgets(buf, 1000, stdin);
  
  *(strchr(buf, '\n')) = 0;
  char* temp = strchr(buf, ' ')+1;
  // printf("%s", temp);
  long long out = evaluate(temp);
  // long long out = 10;

  // fprintf(stderr, "%s\n", temp);
  // fflush(stderr);


  // memset(buf, 0, sizeof(buf));
  // fgets(buf, 1000, stdin);

  // printf("%lld", out);
  fprintf(stdout, "%lld\n", out);
  // fflush(stdout);

  // fprintf(stderr, "%lld\n", out);
  // fflush(stderr);

  // while(true) {
  //   memset(buf, 0, sizeof(buf));
  //   fgets(buf, 1000, stdin);
  //   // printf("%s", buf);
  //   // fflush(stdout);
  //   fprintf(stderr, "%s", buf);
  //   fflush(stderr);
  // }
}

// int main(int argc, char** argv) {
//   pid_t pid = 0;
//   int inpipefd[2];
//   int outpipefd[2];
//   char buf[1000];
//   char msg[256];
//   int status;

//   pipe(inpipefd);
//   pipe(outpipefd);
//   pid = fork();
//   if (pid == 0)
//   {
//     // Child
//     dup2(outpipefd[0], STDIN_FILENO);
//     dup2(inpipefd[1], STDOUT_FILENO);
//     dup2(inpipefd[1], STDERR_FILENO);

//     //ask kernel to deliver SIGTERM in case the parent dies
//     prctl(PR_SET_PDEATHSIG, SIGTERM);

//     //replace tee with your process
//     execl("./times-up-again", "times-up-again" ,(char*) NULL);
//     // Nothing below this line should be executed by child process. If so, 
//     // it means that the execl function wasn't successfull, so lets exit:
//     exit(1);
//   }
//   // The code below will be executed only by parent. You can write and read
//   // from the child using pipefd descriptors, and you can send signals to 
//   // the process using its pid by kill() function. If the child process will
//   // exit unexpectedly, the parent process will obtain SIGCHLD signal that
//   // can be handled (e.g. you can respawn the child process).

//   //close unused pipe ends
//   close(outpipefd[0]);
//   close(inpipefd[1]);

//   // Now, you can write to outpipefd[1] and read from inpipefd[0] :  
//   // while(1)
//   // {
//   //   printf("Enter message to send\n");
//   //   scanf("%s", msg);
//   //   if(strcmp(msg, "exit") == 0) break;

//   //   write(outpipefd[1], msg, strlen(msg));
//   //   read(inpipefd[0], buf, 256);

//   //   printf("Received answer: %s\n", buf);
//   // }

//   // read(inpipefd[0], buf, 1000);
//   // *(strchr(buf, '\n')) = 0;
//   // char *temp = strchr(buf, ' ')+1;

//   // // printf("%s\n", temp);
//   // // fflush(stdout);
//   // printf("%d",evaluate(temp));
//   // fflush(stdout);

//   // sprintf(msg, "%d\n", evaluate(temp));
//   // write(outpipefd[1], msg, strlen(msg));
  
//   while(true) {
//     memset(buf, 0, sizeof(buf));
//     read(inpipefd[0], buf, 1000);
//     printf("%s", buf);
//     fflush(stdout);
//   }
  
//   kill(pid, SIGKILL); //send SIGKILL signal to the child process
//   waitpid(pid, &status, 0);
// }