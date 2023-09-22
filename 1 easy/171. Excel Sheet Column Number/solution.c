int titleToNumber(char * columnTitle){
    int res = 0;
    char *s = columnTitle;
    while (*s){
        res = res * 26 + (*s - 'A') + 1;
        s++; 
    }
    return (res);
}
