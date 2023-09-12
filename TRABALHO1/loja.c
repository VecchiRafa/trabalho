#include <stdio.h>
#include <locale.h>

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

    float somaTotal = 0;
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
    
    while (fgets(linha_produto, sizeof(linha_produto), arq_produto) && fgets(linha_venda, sizeof(linha_venda), arq_venda)) {
        int meio, inicio, fim, meioProduto;
        int elementosLidos1 = sscanf(linha_produto, "%d %*d %*d", &inicio); // Lê o elemento do meio da linha do arq_produto
        int elementosLidos4 = sscanf(linha_produto, "%*d %f %*d", &meioProduto);
        int elementosLidos2 = sscanf(linha_venda, "%*d %d %*d", &meio); // Lê o elemento do meio da linha do arq_venda
        int elementosLidos3 = sscanf(linha_venda, "%*d %*d %d", &fim);
        if (meio == 108) {
            int multiplicacao = fim * 25.00;
            printf("Resultado da multiplicação: %d\n", multiplicacao);
        } else {
            printf("Deu algum erro\n");
        }
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