#include <stdio.h>
#include <locale.h>

const float Chocolate = 25.00;
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
    FILE* arq_saida = freopen("totais.txt", "w", stdout);

    char linha_venda[1024]; // Buffer para armazenar a linha lida
    char linha_produto[1024];
    char linha_vendedor[1024];

    printf("\n\nLog de vendas:\n");

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

    // TOTAL DOS PRODUTOS ==================================================
    fclose(arq_venda);
    arq_venda = fopen("vendas.txt", "r");

    float productTotals[11] = {0.0};
    float totalGeralVendido = 0.0; // Inicializa o total geral com zero

    while (fgets(linha_venda, sizeof(linha_venda), arq_venda) != NULL) {
        int elementosLidos, multiplicador;
        sscanf(linha_venda, "%*d %d %d", &elementosLidos, &multiplicador);

        switch (elementosLidos) {
            case 108:
                productTotals[0] += Chocolate * multiplicador;
                break;
            case 209:
                productTotals[1] += Marshmallow * multiplicador;
                break;
            case 308:
                productTotals[2] += Brownie * multiplicador;
                break;
            case 407:
                productTotals[3] += Ice_cream * multiplicador;
                break;
            case 506:
                productTotals[4] += Cake * multiplicador;
                break;
            case 605:
                productTotals[5] += Donut * multiplicador;
                break;
            case 704:
                productTotals[6] += Cookie * multiplicador;
                break;
            case 803:
                productTotals[7] += Candy * multiplicador;
                break;
            case 902:
                productTotals[8] += Cupcake * multiplicador;
                break;
            case 101:
                productTotals[9] += Pudding * multiplicador;
                break;
            default:
                break;
        }

        // Acumula o valor da venda ao total geral
        totalGeralVendido += (float)elementosLidos * multiplicador;  
    }
    
    printf("\n\nTotal geral vendido: %.2f", totalGeralVendido);

    // Imprimir o total de vendas de cada produto
    printf("\n\nTotal de vendas de cada produto:\n");

    if (productTotals[0] > 0.0) {
        printf("Produto 108 (Chocolate): %.2f\n", productTotals[0]);
    }
    if (productTotals[1] > 0.0) {
        printf("Produto 209 (Marshmallow): %.2f\n", productTotals[1]);
    }
    if (productTotals[2] > 0.0) {
        printf("Produto 308 (Brownie): %.2f\n", productTotals[2]);
    }
    if (productTotals[3] > 0.0) {
        printf("Produto 407 (Ice cream): %.2f\n", productTotals[3]);
    }
    if (productTotals[4] > 0.0) {
        printf("Produto 506 (Cake): %.2f\n", productTotals[4]);
    }
    if (productTotals[5] > 0.0) {
        printf("Produto 605 (Donut): %.2f\n", productTotals[5]);
    }
    if (productTotals[6] > 0.0) {
        printf("Produto 704 (Cookie): %.2f\n", productTotals[6]);
    }
    if (productTotals[7] > 0.0) {
        printf("Produto 803 (Candy): %.2f\n", productTotals[7]);
    }
    if (productTotals[8] > 0.0) {
        printf("Produto 902 (Cupcake): %.2f\n", productTotals[8]);
    }
    if (productTotals[9] > 0.0) {
        printf("Produto 101 (Pudding): %.2f\n", productTotals[9]);
    }
    // TOTAL DOS VENDEDORES  ==================================================

    fclose(arq_venda);
    arq_venda = fopen("vendas.txt", "r");
    fclose(arq_vendedor);
    arq_vendedor = fopen("vendedores.txt", "r");

    fgets(linha_venda, sizeof(linha_venda), arq_venda);

    // Mapa para rastrear as vendas de cada vendedor
    float vendasPorVendedor[100] = {0.0}; // Suponha que haja 100 vendedores no máximo

    // Mapa para mapear códigos de vendedor para nomes
    char nomesVendedores[100][50]; // Suponha que os nomes dos vendedores tenham no máximo 50 caracteres

    // Lê o arquivo de vendedores e mapeia códigos para nomes
    while (fgets(linha_vendedor, sizeof(linha_vendedor), arq_vendedor) != NULL) {
        int codigoVendedor;
        char nome[50];
        sscanf(linha_vendedor, "%d %s", &codigoVendedor, nome);
        strcpy(nomesVendedores[codigoVendedor], nome);
    }

    while (fgets(linha_venda, sizeof(linha_venda), arq_venda) != NULL) {
        int codigoVendedor, codigoProduto, quantidade;
        sscanf(linha_venda, "%d %d %d", &codigoVendedor, &codigoProduto, &quantidade);

        // Calcula o valor total da venda
        float valorVenda = 0.0;
        switch (codigoProduto) {
            case 108:
                valorVenda = Chocolate * quantidade;
                break;
            case 209:
                valorVenda = Marshmallow * quantidade;
                break;
            case 308:
                valorVenda = Brownie * quantidade;
                break;
            case 407:
                valorVenda = Ice_cream * quantidade;
                break;
            case 506:
                valorVenda = Cake * quantidade;
                break;
            case 605:
                valorVenda = Donut * quantidade;
                break;
            case 704:
                valorVenda = Cookie * quantidade;
                break;
            case 803:
                valorVenda = Candy * quantidade;
                break;
            case 902:
                valorVenda = Cupcake * quantidade;
                break;
            case 101:
                valorVenda = Pudding * quantidade;
                break;
            default:
                break;
        }

        // Acumula o valor da venda para o vendedor correspondente
        vendasPorVendedor[codigoVendedor] += valorVenda;
    }

    // Imprime o total de vendas de cada vendedor com seus nomes
    printf("\n\nTotal de vendas de cada vendedor:\n");
    for (int i = 1; i < 100; i++) {
        if (vendasPorVendedor[i] > 0.0) {
            printf("Vendedor %d (%s): %.2f\n", i, nomesVendedores[i], vendasPorVendedor[i]);
        }
    }

    fclose(arq_venda);
    fclose(arq_produto);
    fclose(arq_vendedor);
    fclose(arq_saida);
    putchar('\n');

    return 0;
}