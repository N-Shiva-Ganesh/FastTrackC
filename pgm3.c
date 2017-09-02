/*3. Reverse the content of string.*/

#include<stdio.h>
#include<string.h>
int string_reverse(char*,char*,int);
int main()
{
	char str1[30];
	char str2[30];
	int len;
	printf("Enter the first string\n");
	scanf("%s",str1);
	len = strlen(str1);
	printf("length=%d\n",len);
	string_reverse(str1,str2,len);	
	return 0;
}

int string_reverse(char *str1, char *str2, int len)
{
	int i,j=0;;
	printf("String 1 = %s\n",str1);
	for(i=len-1;i>=0;i--)
	{
		
		*(str2+j)=*(str1+i);
		j++;
	}
	*(str2+j) = '\0';

	printf("The Reversed string is %s\n",str2);	
	return 0;
}
		
