#include <stdio.h>
#include <locale.h>

const float Chocolate = 108; 
const float Marshmallow = 10.50;
const float Brownie = 30.00;
const float Ice_cream = 15.00;
const float Cake = 17.50;
const float Donut = 12.90;
const float Cookie = 20.70;
const float Candy = 31.44;
const float Cupcake = 46.02;
const float Pudding = 55.80;

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

    //float somaTotal = 0;
    //float totalProdutos = 0;
    //float totalVendedor = 0;

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


    printf("\n\n");
    printf("Dados das vendas:\n");

    // Fechar e reabrir o arquivo de vendas para ler novamente
    fclose(arq_venda);
    arq_venda = fopen("vendas.txt", "r");
    
    int contador_linhas = 0;

     while (fgets(linha_venda, sizeof(linha_venda), arq_venda) != NULL) {
        int elementosLidos, multiplicador;
        sscanf(linha_venda, "%*d %d %d", &elementosLidos, &multiplicador);

        if (elementosLidos == 108) {
            float resultado = Chocolate * multiplicador;
            printf("Chocolate = %.2f\n", resultado);
        }
        if (elementosLidos == 209) {
            float resultado = Marshmallow * multiplicador;
            printf("Marshmallow = %.2f\n", resultado);
        }
        if (elementosLidos == 308) {
            float resultado = Brownie * multiplicador;
            printf("Brownie = %.2f\n", resultado);
        }
        if (elementosLidos == 407) {
            float resultado = Ice_cream * multiplicador;
            printf("Ice cream = %.2f\n", resultado);
        }
        if (elementosLidos == 506) {
            float resultado = Cake * multiplicador;
            printf("Cake = %.2f\n", resultado);
        }
        if (elementosLidos == 605) {
            float resultado = Donut * multiplicador;
            printf("Donut = %.2f\n", resultado);
        }
        if (elementosLidos == 704) {
            float resultado = Cookie * multiplicador;
            printf("Cookie = %.2f\n", resultado);
        }
        if (elementosLidos == 803) {
            float resultado = Candy * multiplicador;
            printf("Candy = %.2f\n", resultado);
        }
        if (elementosLidos == 902) {
            float resultado = Cupcake * multiplicador;
            printf("Cupcake = %.2f\n", resultado);
        }
        if (elementosLidos == 101) {
            float resultado = Pudding * multiplicador;
            printf("Pudding = %.2f\n",resultado);
        }
        contador_linhas++;
       
    }

    //printf("\n\n");
    //printf("Total geral vendido: %d", somaTotal);

    fclose(arq_venda);
    fclose(arq_produto);
    fclose(arq_vendedor);
    fclose(arq_saida);
    putchar('\n');

    return 0;
}