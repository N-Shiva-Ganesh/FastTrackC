/*1. Copy contents of one string to another.*/

#include<stdio.h>
#include<string.h>
int string_copy(char*,char*,int);
int main()
{
	char str1[30];
	char str2[30];
	int len;
	printf("Enter the first string\n");
	scanf("%s",str1);
	len = strlen(str1);
	printf("length=%d\n",len);
	string_copy(str1,str2,len);	
	return 0;
}

int string_copy(char *str1, char *str2, int len)
{
	int i;
	printf("String 1 = %s\n",str1);
	for(i=0;i<len;i++)

	{
		
		*(str2+i)=*(str1+i);
	}
	printf("The copied string in string 2 is %s\n",str2);	
	return 0;
}
		
