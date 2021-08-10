litro_leite = 100                                             #temos 100 litros de leite
litro_por_kg_queijo = 10                                       #cada kg de queijo possui 3 litros de leite
kg_por_pacote = 3                                             # cada pacote de queijo possui 3 kg
gramas_por_pacote = 0.5
litro_por_pacote = kg_por_pacote*litro_por_kg_queijo          #então multiplicando 3 litros de queijo por 3 pacotes
quantidade_de_pacotes_3kg = litro_leite//litro_por_pacote         #dividindo 100 litros de leite por 9 litros por pacote
litro_sobrando = litro_leite%litro_por_pacote                 #pegar o que sobrou dos 100 litros após utilizá-lo para fazer caixas de 3kg
litro_sobrando_em_kg = litro_sobrando                         #1 litro = 1 kg, então fica numericamente igual
pacotes_de_100g = litro_sobrando_em_kg/gramas_por_pacote      #dividindo 1 kg por 100 gramas para obter a quantidade de pacotes de 100g
total_pacotes = pacotes_de_100g+quantidade_de_pacotes_3kg     #somando todos os pacotes

print("hoje temos ", litro_leite, " litros de leite.")        
print("logo serão produzidos ", quantidade_de_pacotes_3kg, " pacotes de 3 Kg.")
print("e também serão produzidos ",pacotes_de_100g, " pacotes de 100g.")
print("então temos no total ", total_pacotes, " pacotes de queijo.")
