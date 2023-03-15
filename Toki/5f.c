#include<stdio.h>
#include<math.h>

void main(){
    long int a,b;
    double n;
    scanf("%lf",&n);
    if(n==trunc(n)){
        printf("%.0lf %.0lf",n,n);
    } else if (n<0){
        a = trunc(n);
        b = a - 1;
        printf("%ld %ld",b,a);
    } else {
        a = trunc(n);
        b = a + 1;
        printf("%ld %ld",a,b);
    }
    printf("\n");
}