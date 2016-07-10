#include<stdio.h>
#define lower 'a' - 'A'

typedef union tmptype{
	char str[100];
}string;

int strlen(char *str){
	int len = 0;
	while(*str++)len++;
	return len;
}

int mystrcmp(char *str1,char *str2){
	while(*str1){
		if(*str1 - *str2)return 0;
		str1++,str2++;
	}
	return 1;
}

char *strcp(char *src,char *dest){
	char *tmp = dest;
	while(*src)*tmp++ = *src++;
	*tmp = 0;
	return dest;
}

int contains(char *S,char *str,int flag){
	int lenS = strlen(S),lenstr = strlen(str);
	char *tmp_p = str;
	char *stmp_p = S;
	if(flag){//开关 
		char tmp[lenstr + 1];
		char stmp[lenS + 1];
	 	tmp_p = strcp(str,tmp);
		stmp_p = strcp(S,stmp);
		while(*tmp_p){
			if(*tmp_p > 'a' - 1){
				*tmp_p -= lower;
			}
			tmp_p++;
		}
		while(*stmp_p){
			if(*stmp_p > 'a' - 1){
				*stmp_p -= lower;
			}
			stmp_p++;
		}
		tmp_p = str;
	}
	while(*tmp_p && lenstr > lenS){
		if(lenS <= lenstr--){
			if(mystrcmp(stmp_p,tmp_p++))return 1;
		}
	}
	return 0;
}

int main(){
	int flag,i,n;
	char S[100]; 
	scanf("%s",S);
	scanf("%d",&flag);
	scanf("%d",&n);
	string strings[n];
	for(i = 0;i < n;i++){
		scanf("%s",strings[i].str);
	}
	if(flag){
		printf("Ignore case\n");
	}
	for(i = 0;i < n;i++){
		if(contains(S,strings[i].str,flag)){
			printf("%s contains %s\n",strings[i].str,S);
		}
	}
}

