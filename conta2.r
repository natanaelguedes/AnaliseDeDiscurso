
install.packages("tidyverse")
install.packages("tokenizers")
install.packages("readr")
library(readr)
library(tidyverse)

library(tokenizers)
dad
texto=data.frame(aldeiavitoria)
texto
data.frame(aldeiavitoria)
texto <- tokenize_words(aldeiavitoria)
texto
frases <- tokenize_sentences(Arquivo)
frases
typeof(dados)

table(testess)

frases_palavras <- tokenize_words(data.frame(Arquivo))
aldeiavitoria$Texto
aldeiavitoria[duplicated(aldeiavitoria)]
exdf <- as.data.frame(Arquivo)

saida=inner_join(Ald_aVitPerguntas$Column1.1,Ald_aVitPerguntas$Column1.2)

# Retornando como vetor:
exdf[duplicated(Arquivo), ]

# Mantendo a estrutura de data.frame
exdf[duplicated(Arquivo), , drop = FALSE]
frases_palavras
length(frases_palavras)
length(frases_palavras[[1]])

length(frases_palavras[[2]])

length(frases_palavras[[3]])

length(frases_palavras[[4]])
sapply(frases_palavras, length)

tabela <- table(aldeiavitoria)

tabela <- data_frame(palavra = names(aldeiavitoria), contagem = as.numeric(aldeiavitoria))
Arquivo
count_words("Arquivo")
table(aldeiavitoria)
tabela
arq = transpose(tabela)
arq
arrange(tabela, desc(aldeiavitoria))
frases <- tokenize_sentences()

frases

frases_palavras <- tokenize_words(frases[[1]])

frases_palavras

length(frases_palavras)

select.list(contagem2)

length(frases_palavras[[1]])

length(frases_palavras[[2]])

length(frases_palavras[[3]])

length(frases_palavras[[4]])
sapply(frases_palavras, length)
Arquivo
table.prop("V1")
contagem2$V1
apply(table(contagem2$V1)  , 0, sum )
#https://programminghistorian.org/pt/licoes/processamento-basico-texto-r
#https://www.tidyverse.org/blog/2019/04/r-version-support/
getRversion() #versão do r para rodar este script é a 4.2.1

getwd()
ex01 <- read.table("C:\\Users\\natan\\OneDrive\\Documentos\\19-de-mai.-11.03_-dados-da-pesquisa-2-_transição-feita-no-word_.txt", sep = ",")
ex01$V1[611]= ""
remove.col
ex01
library(readxl)
testess <- read_excel("C:\\Users\\natan\\OneDrive\\Área de Trabalho\\texto.xls")
View(testess)
?read.csv()
ler = read.csv("C:\\Users\\natan\\OneDrive\\Documentos\\dados_audio_tabela.csv", sep=",")
texto <- scan(contagem2)
texto <- tolower(texto)
vetor = c(contagem2)
table(data.frame(aldeiavitoria))

prop.table(contagem2)
lista_palavras <- strsplit(texto, "\\W+")
vetor_palavras <- unlist(lista_palavras)

frequencia_palavras <- table(vetor_palavras)
frequencia_ordenada_palavras <- sort(frequencia_palavras, decreasing=TRUE)

palavras <- paste(names(frequencia_ordenada_palavras), frequencia_ordenada_palavras, sep=";")

cat(palavras, palavras, file="frequencias.csv", sep="\n")

write.csv(Arquivo, "Arquivo.csv", )
contaPalavras <- function(linhas) {
  palavras <- strsplit(linhas, "\\W+")
  todas <- unlist(palavras)
  contagem <- table(todas)
  contagem[order(-contagem)]
}
linhas <- c(aldeiavitoria)
contaPalavras(linhas)

getwd()
data.frame(table(aldeiavitoria))
aldeiavitoria = table(Arquivo, getOption("max.print"))
aldeiavitoria
Arquivo
library(tidyr) # lendo tidyr

palavras <- untidy %>% 
  separate("palavras", # coluna a ser separada
           sep = " ", # o que separa uma observa??o de outra
           into = Arquivo$palavras, # novas colunas
           convert = TRUE) # converter o nome da coluna para 'character'

palavras

ta

s=na.exclude(aldeiavitoria3)
table(data.frame(aldeiavitoria3))

Arquivo$a
duplicated(aldeiavitoria$Texto)

as.data.frame(table(aldeiavitoria$Texto))
as.data.frame(aldeiavitoria)
table(exdf)

Arquivo$palavras[2]="ra?zes"
Arquivo$palavras[2]
Arquivo$palavras[3]="a?"
Arquivo$palavras[3]
Arquivo$palavras[15]="?rvore"
Arquivo$palavras[15]
Arquivo$palavras[16]="t?"
Arquivo$palavras[16]
Arquivo$palavras[27]="?rvore"
Arquivo$palavras[39]="n?o"
Arquivo$palavras[41]="ibirap?"
Arquivo$palavras[42]="?"
Arquivo$palavras[46]="pa?ses"
Arquivo$palavras[49]="ent?o"
Arquivo$palavras[53]="n?o"
Arquivo$palavras[55]="n?o"
Arquivo$palavras[62]="ent?o"
Arquivo$palavras[63]="?"
Arquivo$palavras[65]="n?s"
Arquivo$palavras[70]="t?"
Arquivo$palavras[71]="?"
Arquivo$palavras[76]="cren?a"
Arquivo$palavras[83]="n?s"
Arquivo$palavras[91]="est?"
Arquivo$palavras[99]="esp?cie"
Arquivo$palavras[101]="transcri??o"
Arquivo$palavras[108]= "categoriza??o"
Arquivo$palavras[115]= "gr?ficos"
Arquivo$palavras[120]= "?"
Arquivo$palavras[122]= "?"
Arquivo$palavras[123]= "n?"
Arquivo$palavras[131]= "interven??o"
Arquivo$palavras[133]= "n?o"
Arquivo$palavras[136]= "gr?fico"
Arquivo$palavras[139]="n?o"
Arquivo(Arquivo[which(Arquivo$palavras[149]="?" && Arquivo$palavras[151]="document?rio"])]
Arquivo <- Arquivo[ which( Arquivo$palavras[149]="?" | Arquivo$palavras[151]="document?rio"]) , ]
Arquivo[Arquivo$palavras[149]='?']

 Arquivo$palavras[151]="document?rio"
 Arquivo$palavras[149]="?"
 solution<-as.data.frame(table(unlist(aldeiavitoria3)))
 table(solution)
 teste=read.csv("C:\\Users\\natan\\OneDrive\\?rea de Trabalho\\aldeia vit?ria - apresenta??o.csv", sep = ";", header = T)
?read.csv

df1= data.frame(table(aldeiavitoria3$Column1.1))
df2= data.frame(table(aldeiavitoria3$Column1.2))
df3=data.frame(table(aldeiavitoria3$Column1.3))
df4=data.frame(table(aldeiavitoria3$Column1.4))
df5=data.frame(table(aldeiavitoria3$Column1.5))
df6=data.frame(table(aldeiavitoria3$Column1.6))
df7= data.frame(table(aldeiavitoria3$Column1.7))
df8= data.frame(table(aldeiavitoria3$Column1.8))
df9=data.frame(table(aldeiavitoria3$Column1.9))

df10= data.frame(table(aldeiavitoria3$Column1.10))
df11= data.frame(table(aldeiavitoria3$Column1.11))
df12= data.frame(table(aldeiavitoria3$Column1.12))
df13= data.frame(table(aldeiavitoria3$Column1.13))
df14= data.frame(table(aldeiavitoria3$Column1.14))
df15= data.frame(table(aldeiavitoria3$Column1.15))
df16= data.frame(table(aldeiavitoria3$Column1.16))
df17= data.frame(table(aldeiavitoria3$Column1.17))
df18= data.frame(table(aldeiavitoria3$Column1.18))
df19= data.frame(table(aldeiavitoria3$Column1.19))
df20= data.frame(table(aldeiavitoria3$Column1.20))
df21= data.frame(table(aldeiavitoria3$Column1.21))
df22= data.frame(table(aldeiavitoria3$Column1.22))
df23= data.frame(table(aldeiavitoria3$Column1.23))
df24= data.frame(table(aldeiavitoria3$Column1.24))
df25= data.frame(table(aldeiavitoria3$Column1.25))
df26= data.frame(table(aldeiavitoria3$Column1.26))
df26= data.frame(table(aldeiavitoria3$Column1.27))
df27= data.frame(table(aldeiavitoria3$Column1.28))
df28= data.frame(table(aldeiavitoria3$Column1.29))
df29= data.frame(table(aldeiavitoria3$Column1.30))
df30= data.frame(table(aldeiavitoria3$Column1.31))
df31= data.frame(table(aldeiavitoria3$Column1.32))
df32= data.frame(table(aldeiavitoria3$Column1.33))
df33= data.frame(table(aldeiavitoria3$Column1.34))
df34= data.frame(table(aldeiavitoria3$Column1.35))
df35= data.frame(table(aldeiavitoria3$Column1.36))
df36= data.frame(table(aldeiavitoria3$Column1.37))
df37= data.frame(table(aldeiavitoria3$Column1.38))
df38= data.frame(table(aldeiavitoria3$Column1.39))
df39= data.frame(table(aldeiavitoria3$Column1.40))
df40= data.frame(table(aldeiavitoria3$Column1.41))
df41= data.frame(table(aldeiavitoria3$Column1.42))
df42= data.frame(table(aldeiavitoria3$Column1.43))
df43= data.frame(table(aldeiavitoria3$Column1.44))
df44= data.frame(table(aldeiavitoria3$Column1.45))
df45= data.frame(table(aldeiavitoria3$Column1.46))
df46= data.frame(table(aldeiavitoria3$Column1.47))
df47= data.frame(table(aldeiavitoria3$Column1.48))
df48= data.frame(table(aldeiavitoria3$Column1.49))
df49= data.frame(table(aldeiavitoria3$Column1.50))
df50= data.frame(table(aldeiavitoria3$Column1.51))
df51= data.frame(table(aldeiavitoria3$Column1.52))
df52= data.frame(table(aldeiavitoria3$Column1.53))
df53= data.frame(table(aldeiavitoria3$Column1.54))
df54= data.frame(table(aldeiavitoria3$Column1.55))
df55= data.frame(table(aldeiavitoria3$Column1.56))
df56= data.frame(table(aldeiavitoria3$Column1.57))
write.csv(df1,"testes1.csv")
write.csv(df2,"testes2.csv")
write.csv(df3,"testes3.csv")
write.csv(df4,"testes4.csv")
write.csv(df5,"testes5.csv")
write.csv(df6,"testes6.csv")
write.csv(df7,"testes7.csv")
write.csv(df8,"testes8.csv")
write.csv(df9,"testes9.csv")
write.csv(df10,"testes10.csv")
write.csv(df11,"testes11.csv")
write.csv(df12,"testes12.csv")
write.csv(df13,"testes13.csv")
write.csv(df14,"testes14.csv")
write.csv(df15,"testes15.csv")
write.csv(df16,"testes16.csv")
write.csv(df17,"testes17.csv")
write.csv(df18,"testes18.csv")
write.csv(df19,"testes19.csv")
write.csv(df20,"testes20.csv")
write.csv(df21,"testes21.csv")
write.csv(df22,"testes22.csv")
write.csv(df23,"testes23.csv")
write.csv(df24,"testes24.csv")
write.csv(df25,"testes25.csv")
write.csv(df26,"testes26.csv")
write.csv(df27,"testes27.csv")
write.csv(df28,"testes28.csv")
write.csv(df29,"testes29.csv")
write.csv(df30,"testes30.csv")
write.csv(df31,"testes31.csv")
write.csv(df32,"testes32.csv")
write.csv(df33,"testes33.csv")
write.csv(df34,"testes34.csv")
write.csv(df35,"testes35.csv")
write.csv(df36,"testes36.csv")
write.csv(df37,"testes37.csv")
write.csv(df38,"testes38.csv")
write.csv(df39,"testes39.csv")
write.csv(df40,"testes40.csv")
write.csv(df41,"testes41.csv")
write.csv(df42,"testes42.csv")
write.csv(df43,"testes43.csv")
write.csv(df44,"testes44.csv")
write.csv(df45,"testes45.csv")
write.csv(df46,"testes46.csv")
write.csv(df47,"testes47.csv")
write.csv(df48,"testes48.csv")
write.csv(df49,"testes49.csv")
write.csv(df50,"testes50.csv")
write.csv(df51,"testes51.csv")
write.csv(df52,"testes52.csv")
write.csv(df53,"testes53.csv")
write.csv(df54,"testes54.csv")
write.csv(df55,"testes55.csv")
write.csv(df56,"testes56.csv")
write.csv(df57,"testes57.csv")

 rows
install.packages("reshape2")
data.frame(df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25,df26,df27,df28,df29,df30,df31,df32,df33,df34,df35,df36,df37,df38,df39,df40,df41,df42,df43,df44,df45,df46,df47,df48,df49,df50,df51,df52,df53,df54,df55,df56) 
mer
require(reshape2)
mat <- rownames(data) 
melt(mat)
install.packages("dplyr") 
library(dplyr)
data=merge(df1,df2)
data
SAIDA=merge(data.frame(data))
