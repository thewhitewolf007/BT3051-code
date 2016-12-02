#include <stdio.h>
#include <time.h>
int main()
{

int a[800][800] = {0};
int b[800][800] = {0};
int c[800][800] = {0};
for (int i=0;i<800;i++){
	a[i][i]=1;
}
for (int i=0;i<800;i++){
	b[i][i]=1;
}
for (int k=0;k<800;k++){
	for(int j=0;j<800;j++){
		for(int i=0;i<800;i++){
			c[i][j]+=a[i][k]*b[k][j];
		}
	}
}
return 0;
}