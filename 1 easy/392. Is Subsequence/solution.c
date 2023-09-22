bool isSubsequence(char * s, char * t){
    while (*s && *t)
    {
        if (*s == *t)
            s++;
        t++;
    }
    if (*s == '\0')
        return (1);
    return (0);
}
