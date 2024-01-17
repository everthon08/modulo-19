
grafico= sns.lineplot(data= df_preco_gasolina_2021, x= 'dia', y= 'venda', color= 'red')
grafico.set_title('Preço da gasolina em julho de 2021 em SP ')
plt.xlabel('Dia')
plt.ylabel('Preço de venda no dia')
plt.savefig('gasolina.png')
plt.show(grafico)
