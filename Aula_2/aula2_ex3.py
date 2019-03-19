valor_livro = 24.95
desconto = 0.4
custo_envio_1 = 3.00
custo_envio_demais = 0.75
quantidade_livros = 60

custo_total = ((quantidade_livros*valor_livro)-desconto*(quantidade_livros*valor_livro))+custo_envio_1+((quantidade_livros-1)*custo_envio_demais)
print('Custo total na compra dos livros: R${:.2f}'.format(custo_total))

