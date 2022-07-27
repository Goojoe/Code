#include<iostream>
using namespace std;
class zhengfangti {
	public:
		int bianchang;
		int midu;
		int tiji;
		int zhiliang;
		void get_val(int x,int y){
			bianchang=x;
			midu=y;
			tiji=x*x*x;
			zhiliang=tiji*midu;
		} 
		void print_val(){
			cout<<"边长是："<<bianchang<<endl;
			cout<<"体积是："<<tiji<<endl; 
			cout<<"密度是："<<midu<<endl;
			cout<<"质量是："<<zhiliang<<endl;
		}
}; 
int main(){
	zhengfangti test;
	test.get_val(1,2);
	test.print_val();
	return 0;
}