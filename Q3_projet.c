#include <stdio.h>

int main(){
    int n,k;
    int nb_possibilite=0;
    int tab1[10];
    int tab2[10];
    int tab3[10];
    int tab4[10];
    int tab5[10];
    int tab6[10];
    int tab7[10];
    int tab8[10];
    int tab9[10];
    int tab10[10];

    n=1;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                if(a+b == k){
                    nb_possibilite++;
                }
            }
        }
        tab1[k]=nb_possibilite;
        nb_possibilite=0;
    }
    printf("Pour n = 1 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab1[i]);
    }
    printf("\n");
    printf("\n");

    n=2;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    if(a+b+c == k){
                        nb_possibilite++;
                    }
                }
            }
        }
        tab2[k]=nb_possibilite;
        nb_possibilite=0;
    }
    printf("Pour n = 2 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab2[i]);
    }
    printf("\n");
    printf("\n");

    n=3;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    for(int d=0 ; d <= 10 ; d++){
                        if(a+b+c+d == k){
                            nb_possibilite++;
                        }
                    }
                }
            }
        }
        tab3[k]=nb_possibilite;
        nb_possibilite=0;
    }

    printf("Pour n = 3 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab3[i]);
    }
    printf("\n");
    printf("\n");

    n=4;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    for(int d=0 ; d <= 10 ; d++){
                        for(int e=0 ; e <= 10 ; e++){
                            if(a+b+c+d+e == k){
                                nb_possibilite++;
                            }
                        }
                    }
                }
            }
        }
        tab4[k]=nb_possibilite;
        nb_possibilite=0;
    }

    printf("Pour n = 4 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab4[i]);
    }
    printf("\n");
    printf("\n");

    n=5;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    for(int d=0 ; d <= 10 ; d++){
                        for(int e=0 ; e <= 10 ; e++){
                            for(int f=0 ; f<=10 ; f++){
                                if(a+b+c+d+e+f == k){
                                    //printf("%d ; %d ; %d ; %d ; %d ; %d\n", a, b, c, d, e, f);
                                    nb_possibilite++;
                                }
                            }
                        }
                    }
                }
            }
        }
        //printf("%d possibilites pour n = %d et k = %d\n",nb_possibilite, n, k);
        tab5[k]=nb_possibilite;
        nb_possibilite=0;
    }

    printf("Pour n = 5 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab5[i]);
    }
    printf("\n");
    printf("\n");

    n=6;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    for(int d=0 ; d <= 10 ; d++){
                        for(int e=0 ; e <= 10 ; e++){
                            for(int f=0 ; f<=10 ; f++){
                                for(int g=0 ; g<=10 ; g++){
                                    if(a+b+c+d+e+f+g == k){
                                        //printf("%d ; %d ; %d ; %d ; %d ; %d ; %d\n", a, b, c, d, e, f, g);
                                        nb_possibilite++;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        //printf("%d possibilites pour n = %d et k = %d\n",nb_possibilite, n, k);
        tab6[k]=nb_possibilite;
        nb_possibilite=0;
    }

    printf("Pour n = 6 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab6[i]);
    }
    printf("\n");
    printf("\n");

    n=7;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    for(int d=0 ; d <= 10 ; d++){
                        for(int e=0 ; e <= 10 ; e++){
                            for(int f=0 ; f<=10 ; f++){
                                for(int g=0 ; g<=10 ; g++){
                                    for(int h=0 ; h<=10 ; h++){
                                        if(a+b+c+d+e+f+g+h == k){
                                        //printf("%d ; %d ; %d ; %d ; %d ; %d ; %d ; %d\n", a, b, c, d, e, f, g, h);
                                        nb_possibilite++;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        //printf("%d possibilites pour n = %d et k = %d\n",nb_possibilite, n, k);
        tab7[k]=nb_possibilite;
        nb_possibilite=0;
    }

    printf("Pour n = 7 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab7[i]);
    }
    printf("\n");
    printf("\n");

    n=8;
    for(int k=1 ; k <= 10; k++){
        for(int a=0 ; a <= 10 ; a++){
            for(int b=0 ; b <= 10 ; b++){
                for(int c=0 ; c <= 10 ; c++){
                    for(int d=0 ; d <= 10 ; d++){
                        for(int e=0 ; e <= 10 ; e++){
                            for(int f=0 ; f<=10 ; f++){
                                for(int g=0 ; g<=10 ; g++){
                                    for(int h=0 ; h<=10 ; h++){
                                        for(int i=0 ; i<=10 ; i++){
                                            if(a+b+c+d+e+f+g+h+i == k){
                                                //printf("%d ; %d ; %d ; %d ; %d ; %d ; %d ; %d\n", a, b, c, d, e, f, g, h);
                                                nb_possibilite++;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        //printf("%d possibilites pour n = %d et k = %d\n",nb_possibilite, n, k);
        tab8[k]=nb_possibilite;
        nb_possibilite=0;
    }

    printf("Pour n = 8 et   ");
    for(int i=1 ; i<= 10 ; i++){
        printf("k=%d\t", i);
    }
    printf("\npossibilites :\t");
    for(int i=1 ; i<= 10 ; i++){
        printf("%d\t", tab8[i]);
    }
    printf("\n");
    printf("\n");

    return 0;
}