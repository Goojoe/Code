#include<iostream>
using namespace std;
int main(){
	int a[6]={0,2,3,1,4,5};
	for(int i=5;i>=1;i--){
		for(int j=1;j<=i;j++){
			//TODO
			if(a[i]<a[i-1]){
				int temp=a[i];
				a[i]=a[i-1];
				a[i-1]=temp;
			}
		}
	}
	for(int i=1;i<=5;i++){
		cout<<a[i]<<endl;
	}
	return 0;
}