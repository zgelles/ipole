#include <stdlib.h>
#include <stdio.h>

void changer(double *rm, int ind){
    rm[ind]+=1;
}

int main(){
    printf("hi\n");
    int nx = 2;
    int ny = 2;
    int ringmax = 2;
    double (*image)[nx*ny] = calloc(nx*ny*(ringmax), sizeof(*image));
    for (int i=0;i<nx*ny;i++){
        image[0][i]=1;
        image[1][i]=2;
        //        image[1][i]=1;
    }

    changer(image[1], 2);
    //    printf("%f\n", image[1][3]);
    for (int i=0;i<nx*ny;i++){
        printf("%f\n", image[1][i]);
    }

    /* for (int i=0;i<10;i++) */
    /*     printf("%f\n", image[0][i]); */
    

    //    changer(image[1],2);
    /* for (int i=0;i<2;i++){ */
    /*     for (int j=0;j<nx*ny;j++){ */
    /*         printf("%f\n",image[i][j]); */
    /*         if (image[i][j]>1.5){ */
    /*             printf("%i %i\n", i,j); */
    /*         } */
    /*     } */
    /* } */
    //    printf("%f\n",image[0][5]);

    return 0;
}

