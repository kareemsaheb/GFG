void function(int value)
{
value = 10000;
}

void function2(int *reference)
{

*reference = 10000;
	
}
/* x address 2000 x value 10 */

int main()
{
	int x = 10;
	function(x); // call by value with 10
	function2(&x); // call by reference with 2000
	return 0;
}