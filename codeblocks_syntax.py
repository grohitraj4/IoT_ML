Programming is done within Code Blocks
Example: C/C++
#include<iostream.h>

void main(){
    cout<<"Im inside code block 1";
    for(int i=0;i<=10;i++){
        cout<<"Im inside code block 2";
        for(int j=0;j<=10;j++){
            cout<<"Im inside code block 3";
        }
        cout<<"Im inside code block 2";
    }
    cout<<"Im inside code block 1";
}

In python
print("This is block 1")
print("This is also block 1")
for i in range(10):
    print("This is code block 2")
    for j in range(10):
        print("This is code block 3")
    print("This is code block 2")
print("This is block 1")