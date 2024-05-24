
install.packages("tidyverse")
install.packages("tokenizers")

library(tidyverse)

library(tokenizers)

texto <- paste("Também entendo que, pelo fato de estarmos em temporada eleitoral, as expectativas quanto ao que vamos realizar este ano são baixas. Mesmo assim, senhor presidente da Câmara, aprecio a atitude construtiva que o senhor e os outros líderes assumiram no final do ano passado para aprovar o orçamento e perpetuar a redução dos impostos sobre as famílias trabalhadoras. Desse modo, espero que possamos colaborar este ano sobre questões que são prioritárias para ambos os partidos, como a reforma da justiça criminal e a assistência às pessoas dependentes de drogas vendidas com receita médica. Quem sabe possamos surpreender os cínicos novamente.")
palavras <- tokenize_words(texto)
palavras
frases <- tokenize_sentences(texto)
frases

frases_palavras <- tokenize_words(frases[[1]])

frases_palavras
length(frases_palavras)
length(frases_palavras[[1]])

length(frases_palavras[[2]])

length(frases_palavras[[3]])

length(frases_palavras[[4]])
sapply(frases_palavras, length)

#https://programminghistorian.org/pt/licoes/processamento-basico-texto-r
#https://www.tidyverse.org/blog/2019/04/r-version-support/
