#include <stdio.h>
#include <locale.h>

#define MAX_ROWS 100
#define MAX_COLS 100

int main()
{
    setlocale(LC_ALL, "Portuguese");

    FILE* arq_venda = fopen("vendas.txt", "r");
    FILE* arq_produto = fopen("produtos.txt", "r");
    FILE* arq_vendedor = fopen("vendedores.txt", "r");
    FILE* arq_saida = fopen("totais.txt", "w");



    char linha_venda[1024]; // Buffer para armazenar a linha lida
    char linha_produto[1024];
    char linha_vendedor[1024];

    int matriz1[MAX_ROWS][MAX_COLS];
    int matriz2[MAX_ROWS][MAX_COLS];
    int matrizResultado[MAX_ROWS][MAX_COLS];
    int numRows1, numCols1, numRows2, numCols2;

    printf("Log de vendas:\n");

    // Ignora a primeira linha do arquivo de vendas
    fgets(linha_venda, sizeof(linha_venda), arq_venda);
 
    // Imprime a contagem e o conteúdo do arquivo de vendas, começando em 0
    for (int contador_linhas = 0; fgets(linha_venda, sizeof(linha_venda), arq_venda) != NULL; contador_linhas++) {
        printf("[%d] %s", contador_linhas, linha_venda);  
    }
    
    printf("\n\n");
    printf("Catalogo de produtos:\n");

    fgets(linha_produto, sizeof(linha_produto), arq_produto);

    for (int contador_linhas = 0; fgets(linha_produto, sizeof(linha_produto), arq_produto) != NULL; contador_linhas++) {
        printf("[%d] %s", contador_linhas, linha_produto);
    }

    printf("\n\n");
    printf("Lista de vendedores:\n");

    fgets(linha_vendedor, sizeof(linha_vendedor), arq_vendedor);

    for (int contador_linhas = 0; fgets(linha_vendedor, sizeof(linha_vendedor), arq_vendedor) != NULL; contador_linhas++) {
        printf("[%d] %s", contador_linhas, linha_vendedor);
    }



    // arrumar
    
    // Ler a primeira matriz (vendas)
    fscanf(arq_venda, "%d %d", &numRows1, &numCols1);

    for (int i = 0; i < numRows1; i++) {
        for (int j = 0; j < numCols1; j++) {
            fscanf(arq_venda, "%d", &matriz1[i][j]);
        }
    }

    // Ler a segunda matriz (produtos)
    fscanf(arq_produto, "%d %d", &numRows2, &numCols2);

    for (int i = 0; i < numRows2; i++) {
        for (int j = 0; j < numCols2; j++) {
            fscanf(arq_produto, "%d", &matriz2[i][j]);
        }
    }

    // Realizar a soma das matrizes
    if (numRows1 != numRows2 || numCols1 != numCols2) {
        printf("As dimensões das matrizes não são compatíveis para a soma.\n");
        return 1;
    }

    for (int i = 0; i < numRows1; i++) {
        for (int j = 0; j < numCols1; j++) {
            matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }

    // Escrever a matriz de resultado no arquivo de saída
    fprintf(arq_saida, "%d %d\n", numRows1, numCols1);

    for (int i = 0; i < numRows1; i++) {
        for (int j = 0; j < numCols1; j++) {
            fprintf(arq_saida, "%d ", matrizResultado[i][j]);
        }
        fprintf(arq_saida, "\n");
    }

    //printf("Total geral vendido: ")

    fclose(arq_venda);
    fclose(arq_produto);
    fclose(arq_vendedor);
    fclose(arq_saida);
    putchar('\n');

    return 0;
}