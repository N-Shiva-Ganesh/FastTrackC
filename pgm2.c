/*2. Find the length of string.*/

#include<stdio.h>
#include<string.h>

int main()
{
	char str1[30];
	int len;
	printf("Enter the string\n");
	scanf("%s",str1);
	len = string_length(str1);
	printf("The length of the given string is %d\n",len);
	return 0;
}

int string_length(char *p)
{
	int count = 0;
	while(*p!='\0')
	
	{
		count++;
		p++;
	}
	return count;
}
		
