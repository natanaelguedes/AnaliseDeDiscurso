def contar_palavras(texto):
    # Remover pontuações que não sejam letras ou números
    texto = ''.join(caracter if caracter.isalnum() else ' ' for caracter in texto)

    # Dividir o texto em palavras e converter tudo para minúsculas
    palavras = texto.lower().split()

    # Criar um dicionário para contar as ocorrências de cada palavra
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem


def exibir_em_colunas(contagem):
    # Ordenar as palavras alfabeticamente
    palavras_ordenadas = sorted(contagem.keys())

    # Determinar o comprimento máximo das palavras para alinhar colunas
    max_comprimento_palavra = max(len(palavra) for palavra in palavras_ordenadas)

    # Exibir as palavras e suas contagens em colunas
    print("Palavra".ljust(max_comprimento_palavra + 5), "Contagem")
    print("-" * (max_comprimento_palavra + 5), "-------")
    for palavra in palavras_ordenadas:
        print(f"{palavra.ljust(max_comprimento_palavra + 5)} {contagem[palavra]}")


# Exemplo de uso
texto = """

Nossas raízes aí assim mostrando que a gente vai falar dessa parte de baixo da árvore, tá nosso estudo. Vai tratar agora da parte de baixo da árvore tem tudo a ver não tem e já foi caindo da terra e se tivéssemos conversado nem isso, pois então é mentira, pô, nós estamos na fase, Ibirapuã tá? É dentro desse sistema de crença, a gente tem três categorias que nós vamos conversar hoje nessa conversa. A gente tá gravando depois a gente vai fazer uma espécie de transcrição e a gente vai fazer uma categorização das falas das narrativas para gerar gráficos para gerar dados isso é pesquisa, né? Diferentemente do projeto de outros projetos de intervenção que não precisa gerar gráfico para assim, não precisa mas a pesquisa a gente termina gerando que esse documentário.


Na pesquisa esse relatório ou os artigos que irão para o mundo vai trazer visibilidade de vocês da história de vocês, mas vai trazer dados né concretos na vamos dizer assim que podem ficar arquivados uma futura biblioteca de vocês, né? O caminho é para isso então a gente as três dimensões são diversidades de expressões culturais. Que aí a gente vai deixar vocês muito livre para falar sobre as diversas formas de expressão de cultura que vocês têm essa diversidade, ela pode vir casando-se também com os saberes locais que a outra dimensão é outra dimensão não é outra categoria. E por último a espiritualidade tá porque a gente entende que os valores são determinantes para a conservação dos saberes locais para a cultura.

Local e para a espiritualidade. Tá certo então vamos eu vou ficar meio que coordenando tem a equipe que vai estar registrando seja em fotografia seja em documentário em gravação e vocês vão ficar muito à vontade, só vamos ter cuidado e aí oh.


Segurança vai faz bem esse papel para tentar ajudar que outras pessoas também possam estar participando a professora que tal Fulano tava não falou nada, né? Aí aí a gente já vai se vendo assim, né? Não sei também obrigada então gente, vamos falar sobre sobre a diversidade de expressões culturais a gente pede mas não necessariamente seguir só esse roteiro vocês poderão trazer outros elementos que a gente vai estar. Considerando o estudo, mas a gente pede que você Espalhe um pouco sobre danças possíveis, literatura existente sobre vocês cantos os artesanatos e o grafismo indígena são os pontos que nós gostaríamos que vocês falassem, então a palavra tá facultada aberta para quem queira falar.


Pode ser isso, viu danças, por exemplo isso vou pegar o CPF enquanto a tua anotando o CPF, vocês já podem começar falando sobre as danças essa essa parte das danças foi é muito interessante, porque quando a senhora falou já já estimulou a memória, né de dona Cilene dizendo que quando ia abrir o Maceió daquela parte para cá, a gente só tá falando de que dona Cilene que era muito Canto, né? A dança ela sempre fez muito parte do processo de trabalho então aqui elas mesmo nossas mais velhas, elas podem falar melhor do que eu né, danças que faziam parte desse contexto natural da vida que elas era da Lapinha pastoril, coco de roda Ciranda isso daqui foi tudo fez parte da vivência da comunidade aqui, mas atualmente o que a gente tem é?


O Toré é o que a gente tá agora Lapinha Ciranda coco de roda são expressões que a gente vai resgatar e fortalecer é verdade, né? A gente vai resgatar e fortalecer é compromisso nosso nesse processo que nós estamos aqui de resiliência de só de só estarmos quatro anos aqui nessa Aldeia, né em construção, mas assim todo esses esses essas expressões que fazem parte aqui construir o nosso identidade e que foi muito fragilizada por muitas situações, a gente tem o corpo também selado de estar resgatando e fortalecendo. E aproveitando enquanto elas estão aqui para nos contar. Como é como faz como era naquela época, vocês falaram aqui um pouquinho, né? Ela era mestra e do pastoril dança.


Tinha eu era mestra a minha irmã que já se foi era contra mestra, eu era o cordão encarnado e ela era o cordão azul não era Diana Senhora, eu era o cordão encarnado e era era o cordão azul e nos fale sobre esse cordão encarnado cordão Azul, como é isso era o homem tabulado essa bolada era justo de uma da de uma barraca aqui a minha mãe tinha então a gente informou um pastoril com 12 pessoas 6 é do lado é do lado vermelho e saiu do lado azul, né? Aí quando o aí tinha a bandeira azul e tinha a bandeira vermelha aí quando as pessoas queriam ser eu quero ver a bandeira vermelha cantar eu dou tudo para cantar aí botava o dinheiro na bandeira vermelha. Aí a gente começava com o macaco, mas agora o Maracanã será esse não era daqueles que as mina baús hoje faz assim a gente botava, mas não pode começar a


Tá entendendo, mas e agora desce a bandeira vermelha só para bandeira azul, dou tudo para o azul cantar a bandeira vermelha ficava assim em pé e a bandeira azul aqui cantava enquanto era para dançar Ciranda pegava na mão da outra bota o Zé buba para tocar É aí ó, tem um detalhe que ela não falaram que tinha aí essa era uma competição para quem é retardava mais fundos para o movimento era o movimento. Então elas faziam os escravo que era perfumado esse cravo ela ia vender ofereceu já rapazes conheci o nome dela ela ia mas no


Este lindo cravo, ela não viu o nome dela que tal Fulano a Deus aí eu recebi aquele cravo fazia aquilo ali, ele comprou muito dava o que pudesse, mas a minha saiu então no final de tudo é que era feito não era assim aí cada um tinha sua arrematação, né? Ela fez já veio era carne, às vezes era um peixe preto era para rematar pai também e ganhar dinheiro, né? Aí ficava aquele peixe bem fritado os bico que também que leva outro preparar um pratinho de carne aí era assim que nem um leilão aí disse assim, olha eu dou tudo. Eu dizia assim, eu dou tanto. Aí eu disse assim. Quem dá mais eu disse assim. Quem dá Mais eu dou mais aí eu disse quem ganhava era quem dava mais beleza assim eu do


E assim não eu bato mais aí quem ganhava era quem dava mais é a dança do Xangô não agora perseguição de dizer assim, eu dou tanto tanto de um rapaz viado para namorar comigo, mas eu não queria namorar com ele, mas ele sempre queria rematar me arrematar seu pé é pra mulher logo. Eu tô dizendo eu dou tudo. Ele não pediu ele em mim é que fala que atualmente foi o meu marido que eu tive nove filhos com ele, fiquei viúva em 1980, tudo começou lá, eu mato ele pagou e ela quando eu fui para cá daqueles que tem aquele tema é e fazer os Cravos para vim eu botava o perfume cheiroso. Esse aqui tá mais o do cordão Azul tá mais?


Ela tá malha ela sim e ainda tinha um oferecimento que alguém terminou de cantar comigo a senhora lembra da música. Como era que a gente cantava ela não agora a música Chiquitita porque faz 50 anos que eu do jeito que ela tava mas ele terminou de cantar agora não foi aí pô, dependia da moça que ela queria fazer, né? E no caso assim como eu sempre ia fazer assim era meio traquino as meninas cantava porque assim pelo nome o jovem Paulo por sua bondade receba este cabo com amor e caridade meu jovem falou foi quem mereceu este lindo cravo, ela falava o nome dela. Às vezes era cigana foi quem lhe deu aí a gente ia lá entregar o carro sozinha e daí já saía valendo agora. Vamos ouvir a música Cilene. Eu não vi Selene o pastor e dizer faz sempre.


Foi afamado porque tem Cleonice que está ao seu lado Cilene. É quem dança ou bera ou Marlene é quem dança que era quanta mestre coisa linda igual você vive, viu? Olha Cadê Carvalho dessa bandeira do Guarujá encarnado só o azulão é tanto para dar a bandeira azul descer aqui, só que é a vermelha isso era num palanque, viu? Isso era não falando cai de cima não, fala 12 pessoas cantando umas 6:10 é junto as roupas tudo enfeitar ela, como é que não tem agora era muito bonita já tem sentimento vai voltar é uma coisa muito linda é bem organizada, viu? Então vocês têm todo uma intenção de tomar isso de volta e tem médico aqui, né?


Vai esperar Nossa agora a semente e agora é nós tem tem tem tem aí gente, que coisa bacana, a gente não vê mais o cordão Ciranda a gente não vê mais o a Lapinha de roda tem muito difícil poderiam falar sobre o coco o coco de roda tem mas é no quilombo, né? Mas nasceu aqui era mas eu não sou daqui e se expandiu pra lá é muito do jeito que dançava coco de roda deve ser muito pouco de roda já ia dizer tem gente que dançou. Ah que coisa bonita. Então nós temos vocês, aliás, eu não posso esquecer meu papel, vocês acham que isso tudo.


Steve retomar é você o passado no presente é muito perdido, minha filha, ela ainda ativa as filhas estão aqui vai subir aqui, né? Jovem. Então os cantos estavam atrelados as damas, né É do Toré naquela época já existia também hoje, eu tô orando aqui a época. Ainda hoje chega o silêncio porque foi no momento do Silêncio do Povo Tabajara, a gente não podia se identificar como indígena, né? Tinha os caboclos, mas Ficava muito retraído do que nem pra cidade podia dizer que era era os Caboclo, então isso daí foi nesse silêncio de cento e poucos anos que nós silenciavam elas tinha isso daí tudo como pescador como moradores na cultura que existia mas não representava assim com o indígena embora que fosse e sabia que era que os nossos pais dizia que a gente era que todos eram mas por causa da perseguição que foi feita em cima do Povo Tabajara.


Comente nós aqui do litoral sul, né? Vindo ali de Arataca guia até aqui a a a Jacó. Isso foi uma perseguição ferrenha, muitos desse povo saíram como eles também perderam a sua casa sua residência que era tudo na beira da praia e perderam sua residência para ir morar na vida dos pescadores onde era o cemitério dos animais que morria de tudo que não prestava ali então tinha toda essa riqueza, mas não podia apresentar enquanto originário que era.


Com certeza então Eh sobre artesanatos, como é que vocês veem essa questão antes e agora também né? Nessa mesma linha de discussão que vocês estão falando, mas os artesanatos porque nós estamos indo aqui eh diversas Artes, né, belíssimas seja no brinco seja nos adornos, né nos cocares é colares tiaras e mais tantas outras coisas que com certeza está presente só aqui, né? Imagina nas residências de vocês em tudo, né? Como é que vocês falariam sobre essa questão dos artesanatos? Essa é uma prática que eu mesma Particularmente eu achava que não não desenvolvia eu não fazia isso no meu dia a dia. Mas de repente eu me vejo com meu pai sabe da sei quantos tipos de nó e eu gosto muito dessa arte texto.


Né e painho é tecelão artesão. E aí eu tanto que o que eu mais me identifico é do macramê e de habilidades texto mesmo, só que aí conversando e observando, né? Os outros parentes no dia a dia a gente faz muita artesanato desde dona Cilene me contando que quando ia pegava a palha do côco e transformava em um em um objeto que servia de apoio na pesca, né? Não fazia a cinta do do da da cintura, né? Como é a história que fazia. Então são são o artesanato são o foi e é o que a gente tira de recurso natural e usa Como suporte para nossa prática cotidiana e também para decorar porque a gente vê eu pensava o artesanato muito como algo externa nós assim para decorar seja nós decorar, né? Como acessórios para para nossas vestimentas ou para a decoração do ambiente. Mas ele também está presente como elemento do dia a dia a do tema que você acabou.


Fazer isso tudo se considera o artesanato todo aquele que a gente faz em recursos naturais usam potes aqui pote e E assim a gente já vem nesse sentido de estar fortalecendo de querer voltar a fazer as panelas de barras cerâmica as outras comunidades já iniciaram esse processo. Mas se a senhora parar para falar que essas meninas tudinho já fizeram pote de cerâmica de casa com barro preparado suas cuia da quenga do coco reutiliza para fazer suas unhas fazer. Olha tem três falando cada uma vai falar de uma vez a senhora aqui. E aqui pode ser pode pode falar a gente fazia a concha para tirar o feijão que hoje não se usa mais a gente ainda vê ainda no no no no negócio do povo que vende, né? Aquele tempo antigo então agora não sei ver mais já concha agora a concha de alumínio nunca.


Hambúrguer do que a outra mas a minha coxa era uma queixa de coco eu vou rapar partiu pouco eu raspava o coco vai tirar um pelo dele bem tiradinho. Pegava o ferro botava no fogo aí furava do lado pro alto para o outro pegava uma uma uma uma uma o o o cabo para caçava um pau bem forte que o pau que eu gostava de botar era aquele pau como é beijado que eu vou agora me esqueci que ele é forte que só botava e enfiava aquele que era o que ele tirar o feijão e a gente fazia a pá do coqueiro fazer a pá do do do do lá aqueles pedaços de coqueiro do lado de outro fazia assim tirava e fazia a papa mexer com comer aí entendendo e aqui ainda era aquele dentro do coco que a gente pisava o tempero da quenga que hoje o povo vende tempero é relado já geladinho naquele tempo a a O Gominho e a pimenta.


Correio ela vinha ela vinha não vinha pro não vinha pronta vinha pra gente bater, né? E a gente usava o pilãozinho fazia um Pilão pegava um pedaço de madeira bem forte aquela coisa lá no meio fazia o grosso em cima o grossinho bate e pá pá machucar aí tinha a ver se a gente fosse bater muito muito forte, aquele se lascavam no chão, a gente tinha que botar assim no canto para poder pisar é se não assim, olha para botar ela dentro da comida para comer e o que com a coxa era o a a queda de coco para tirar o feijão a a o o qualquer coisa de comida. Que fosse comida líquida mole é tirava fogueira fosse para mexer a sua mulher de camarão. Achou uma moqueca de peixe tinha paciência vai para cá.


Botar o au au o quego o peixe de esgoto olhava Toddynho, eles utilizava-se do que tinha para fazer seus filhos o artesanato era o próprio utensílio era o próprio artesanato. Era esse que a gente fazia também tá entendendo? É aqui dentro do côco, era o o a pata a gente fazia parte é tá entendendo? Tudo a gente fala assim, a gente cantava bem fui muita rede rede de mangote de pescar rede, meu pai, ele é pescador, ele comprava os filhos e me ensinou eu fazer rede e me ensinou eu fazer o jereré, aí eu pescada o Maciel quando ela falou pra gente pescava do Maceió, a gente abriu Maceió e a gente pescava tanto no Maceió, como monte de rede tá entendendo? Tanto na rede pequeno que era uma gote como na rede grande que cabe com as quatro cinco dessas pessoas aquela rede grande que vai botar lá, ó, faz que faz o arrastão tá entendendo?


Aí a gente pescava também e pescava dentro do manga camarão pescava dentro do Monte Siri. Aratu tá entendendo? Pescava tudo tudo. Se tivesse no meio, mas já não usava a rede não aí não era na realidade ela numa pindaúva a pindaúva e o jereré a gente botava a isca botava o nalho ou o cordão na ponta de uma vara aí botava onde a gente sabia que tinha Siri aí a gente sakuya, botava a pedra era para mudar os bota o chumbo, né? A gente deram chuva a gente dava uma pedrinha aí botava um pedacinho de de de peixe ou carne o que fosse pra fazer um engodo para a água descer no carro, eu desci ia levava aquele gostinho quando a gente vinha ela vinha quatro cinco seis feridas de uma vez aí quando a gente levanta rapidamente o bicho tava agarrado comeu ela disse que a gente ia puxar ela por baixo, ó, aí pegava e botava o dedo da lata.


Ah agora vamos ouvi-la e depois ela pode ser porque nessa sequência, ela já falou tudo que eu ia falar. Hahaha é minha mãe é mesmo agora vocês que ela falou aí eu fiz também a mesma coisa e sobre a palha do coqueiro que meu pai ensinava a gente fazer aquelas paredes que teve três palha fazia aquela trança para ir para dentro do Mangue ali mesmo ali já Coma mesmo ali naquele mãe que vocês vê ali para botar nas camboas. Ó, o peixe não passar quando a água fosse secando o peixe não passar sair daqui de dentro para fora ficava tudo ali dentro e ele passava uma o o mangote a rede na boca, quando tava cheio quando era no outro dia que a Maria ia secar os peixes, já tava tudo ali e você só pegando aqueles peixe e ela tá falando.


E eu também eu já fiz do mesmo jeito a quenga do Coco o pilãozinho o pilãozinho e também eu já trabalhei também fazer sabe o quê para revender? Eu ia para as pedras passa para Tambaba para aquelas Barreiras pegar aquelas areia em cada em cada barreira, tinha uma tinha uma qualidade de areia sereia diferente diferente, a gente botava eu botava nas garrafas isso aí enfeitando as garrafas de vidro para eu vender. Olha que coisa isso era vários desenhos que fazia na garrafa era vários desenhos que eu fazia nas garrafas para eu vender naquele tempo e também meu pai me ensinou também o que eu remendar fazer um mangote um pano de mangote.


E a rede também rede de pescar sardinha, eu fazia também por mim pagava para eu fazer aqueles novinhos sabia fazer então se nós tivéssemos que ofertaram um curso nós já temos as mestras, né? Já temos as mechas professoras estão aqui, né? Os homens viviam mais alguma coisa sobre essa questão de danças literaturas tantos artesanatos era porque ela falou não fazia pulmão e tirar aquelas vara para fazer esse trem da Uva para ir pescar nas pedras provava o anzol com Mário fazia arapuca para pegar cargas d'água no Mangue também tá bem fazia para pegar os caranguejo também aprender a fazer também.


Ratoeira para pegar caranguejo Ah, mas era essa raposa normal, mas como é que é fazer de cana e fazer daquelas lata de óleo antiga, vocês viram que coisa bacana, né? A história da Camboa aproveitava quando acabou e a secando deixava os peixinho ali tá? Pegava tudinho, olha ninguém inteligência e só complementando também que tem uns parentes da gente tio da Milena e faz muita arte em Cipó e ele faz tudo essa imaginar desde não tem cílios assim cadeira e tal diversos objetos decorativos também. Cipó isso aqui eh eh nossa aí.


Esse negócio de que que lindo não tinha nada é você se pó de fogo, você faz muita coisa, ele sempre usa, você pode e fogo menino sim para fazer os artesanatos, tudo ele faz mesa cadeira faz peixe de Decoração. Faça luminária várias coisas assim. Ai que ai que bacana e ele mora por aqui aqui no girador, ele tem um pouquinho que ele sempre Espanha todos os artesanatos dele, quando você sair daqui quiser ver ali na entrada da da do computador de DC. Você vai ver logo, eles estão lá dele, eles têm muita coisa, muita muita muita muita coisa.

É bom para tirar foto e sobre o grafismo indígena. Ah é aqui faz parte da vida da gente do cotidiano que é igual das outras das outras aldeias é o jenipapo. A extração é toda manual agora o grafismo a gente se inspira muito na natureza para fazer né? Tem cada povo tem o seu grafismo e aquilo que significa a gente tá fortalecendo agora a identidade da nossa aldeia fazendo os grafismos que seja também que identifica a gente enquanto Taquara, né, Tabajara. Taquara aqui a última foi a da estrela do mar a gente pode depois passar a foto professora para senhora para ajudar a exemplificar essas fotos dos graves, mas a gente trouxe com o nosso grupo de mulheres e piraporã eu não tenho vocês uma tardezinha no nosso Card, já tá as fotos a gente pode mandar posso mandar o card do das mulheres. Esse é lindo Jaciara se vocês permitirem porque assim tem a gente foi convidada aí.

Eu fui convidada eu a minha pessoa eu convidei a Viviane para dar uma um suporte uma uma Assessoria Técnica simples inicialmente para a construção de uma minuta porque tem Paulo eh Cássia de Naldo, né? Vocês Juscelino tem um outro ou se é são vocês três não tenho quatro tem um jogo o quarto, Josivaldo é o Josualdo isso então assim eu eh eu disse claro como com prazer a gente constrói essa menuda pensa sabendo até disse para ele sabendo que é assim, que que é uma minuta, depois vocês passam a assembleia com o grupo todo para poder aprovar esse plano para para tudo e orientar. Então assim ele até sugeriu o que a gente botasse um grafismo e nós não queríamos pegar embora, a gente tem um grafismo no livro. O Povo Tabajara já ali, mas se vocês pudessem colocar a gente pode mesclando um pouco grafismo.


Para já colocar algo daqui, hum de vocês entendem no plano para ir luxando o plano. Então se vocês puderem e não se eu puderem passar para nós para mim. Eu tô com uma uma Assessoria Técnica e olhe nossos traços a gente consegue identificar mesmo que seja um parente nosso de outra Aldeia a gente já vê aquela aquela pintura ali ia estar abaixada ali foi uma Tabajara que fez, né? Porque a gente sabe identificar pelo nosso modo mesmo jeito que a gente usa não é mesmo com pincel a gente faz traços finos e diferencia muito dos potiguaras. Se você ver os potiguares, elas são figuras muito carimbadas e a gente sempre se atenta muito a fazer traços finas e detalhes mais delicados, né? Pois pronto É bom porque o cacete Paulo faz parte dessa coordenação dessa gerência aí e eu eu dei o meu sim. Aí convidei Vivian que deu sim também dela e a gente tá meio que construindo essa pra


Até terça-feira viu? É até terça-feira para vocês apresentarem essa minuta lá, né? Então assim é uma minuta. Quando eu disse o Paulo é uma minuta, eu disse que eu casei com uma minuta é algo mais simples, né para mas a gente já quer nessa minuta colocar traços de grafismo de vocês aí já você puder me disponibilizar. Tá certo? Já agradecemos acho que em todas as letras tem uns meninos muito habilidosos e as meninas também que essa daqui também pinta ela a irmã dela eu professora já passei dessa fase e agora minha mão minha concentração. Macramê não do grafismo. Ah do grafismo é no começo, era só nós tá tá tá tá tá na pintura hoje já tá jovens. A Geração Jovem, já assumiu o posto dos grafismo. Agora já é essa nova geração de jovens, meu Deus nunca mais tá aí chegou a minha vez de dizer a geração dos jovens eu


Ah pois é não mas jovens ó jovens pelo pelo estatuto é até 29 para nós até 34. Então já passou a minha já passou. Ainda temos vários jovens por aqui, né? Todos os jovens por aqui. Se for até 34 já era é até 100 tá vendo ou seja, somos todos jovens bem gente então dentro dos saberes locais muitos saber. Eles já foram expressados aqui, mas a gente coloca medicina indígena as rezadeiras benzedeiras parteiras, né? Como era que isso era visto se tem antigamente tinha hoje não tem mais mas se tinha citar exemplos símbolos de proteção se vocês utilizam se nos grafismos tem alguma relação com a proteção que vocês pedem a Deus para que proteja.


Valorização da oralidade dos saberes ancestrais e se vocês eh se a gente consegue trazer né várias informações mais antigas e e a gente consegue por exemplo tem um depoimento da Jaciara, né falando do registro audiovisual onde ela tá pegando vários depoimentos a ali nós temos a companheira que estava já sem perder espaço já registrando também, né daquela do lucro de produção é óbvio que não perde nenhuma oportunidade são valorizações de saber eles é na prática que eu tô dizendo aqui, mas eu gostaria que eu ouvi de vocês tá e eu também a valorização dos sinais da natureza. Tem povos que se movimentam tem pessoas que se movimentam conforme o sinal da natureza. Então isso ainda exigem de vocês. Então a gente pode ir para o parque por exemplo medicina.


Indígena ainda predomina muitos saberes antigos dos os chás das rezas das curas assim nesse nível.


Se existia ou se dá medo sim, principalmente já já tá falando eu vou dar a ideia porque eu sei que eu vou falar e vai vir as outras falas aqui, espera aí vou estimular vou estimular, por exemplo. Eh, claro que tem os chás que a gente conhece os chás mais comuns, né? Aí tem os bodos o Capim Santo e tal tem esses chás, mas também tem a a história que diz comida carregada que é as comidas que a gente pode que não pode comer em certa situação, mulher de resguarda, a gente tem as comidas do resguardo, né? Eh dependência se a gente tiver com alguma inflamação no corpo tem certas comidas que a gente não come e tem comida que a gente come porque vai curaca comida também cura né numa fraqueza a gente faz uma cabeça de galo, né? Então só trazendo assim que por meio da nossa gastronomia também é uma forma de Medicina, né? Então trazendo esse exemplo de medicina indígena pelo que também que a gente prepara para comer tanto a Cleonice vai falar para a senhora.


Foi que ela até hoje tem os dentes dela bebendo caldinho de ostra que é um caldo forte. Ela tem todos os dentes perfeitamente dos 50 nossas comidas. Elas também é medicinais. A gente tem a comida que vai fortalecer para tratar doença, né para recuperar no resguardo para recuperar de uma fraqueza para levantar o corpo dá para não pegar outras doenças, né a comida forte para deixar a gente mais resistente além das ervas e da Medicina, né? E aí também tem a questão de de de a gente utilizar. Vamos lá como medicina painho tem um problema de câmara que eu já aprendi com painho que quando eu tô na minha época de crise das câmeras, eu tenho que andar com a castanha de caju, senão eu não consigo fazer nada na minha vida de dores e dores e dores. Porque eu já tenho uma fibromialgia, né? A caju tá as câimbras então no período que eu toco de candra é a


Caju agora é comigo o tempo todo isso aí, eu já aprendi hoje eu já aprendi com meus mais velhos meus meninos bebê que eu sou mãe de dois, né? Se toma um susto bate a aliança ou então pega ali uma Seixas esquenta joga na água banho aquela criança para evitar que ele tenha outros problemas depois criança que assustou a gente bate a aliança no copo d'água, né para crianças então suado suado quando tá com soluço viram na roupa passar na boca e coloca na pele, entendeu? É esse esse essa situação aqui de painho, eu espero experienciei com o meu com o meu filho Yuri Yuri vinha muito com muitos problemas não sabia qual era a questão do menino. Qual dia ser um mau olhado um mal vento uma situação assim, né painho? Então o cara que painho painho disse que fez com a gente quando era criança e agora ele fez com o neto dele que é o meu filho que é de chegar com outro pai, o senhor aí é com o senhor isso aí é para trabalhar quando


Nosso lado tirava aquela roupa e vestia na criança e ele na porta botava a gente gusava e tirava também esse essa coisa é uma medicina também, imagina e hoje eu tô duro todinho por causa que para mim botar a camisa dele todinho hoje a gente ela falou aquele comida da cabeça de galo que a gente fala aqui a cabeça de gato a gente usava para quem tá fraco. Começava com caldinho da caridade minhas irmãs, que relações conhece mais do que porque às vezes não comia nada não descia, mas o caldinho da caridade é feito o que a pimenta do Rei um pouquinho de farinha a peneirada para não com caroço, né e fazer botava um pouquinho de coentro e aquele caldinho levantava até de fome e tinha a bebida do


Da gente né? Se recuperar do resguardo, né? Como é essa bebida se é cooperado desgraçado a bebida para recuperar do resguardo que tomava mãe depois do parto depois do parto. Valeu eu tive muitos meus filhos em casa e tinha Parteira. Eles tinham carteira assim, mas muitas parteiras já morreram sim, mas tinha as parteiras e as parteiras o marido dela era um dos partidos meu marido ele era enfermeiro e ele era parceiro, a gente tomava água inglesa que é muito bom para limpar, né? A gente fazia assim muito chato também fazia chá de de eucalipto para febre hoje em dia o povo usa da farmácia, mas naquela época, eu dava meus filhos assim era achar dia eucalipto a folha do eucalipto era.


Vou abaixar o que mais a gente usava é a febre é é baixar a febre, mas era essa para a a a a a a a inflamação era a raiz da urtiga Branca Aroeira que é muito bom que é um anti-inflamatório Aroeira com babatenon. Porque eu tive um problema de varizes tem uma cirurgia de varizes e a minhas veias ela custou muito a sarar e eu botava tudo o que se dizia e não sarava mas ajuda a minha casa tinha um pé de Aroeira e tinha um pé de uma batedor eu peguei rapei a rapada da Aroeira que isso aí é muito gordinho de junta também pai, peguei cozinhei. Botei no vidrinho daquele vidinho de dipirona. Aí botei no buraco. Aonde era feia e de botei lá todo dia eu botava e sarou e ele é um anti-inflamatório, né? Agora mesmo. Eu peguei o problema da minha pele e aí eu tava dizendo que eu e


Não sei o que eu faço pomada já passei e estou tomando anti-inflamatório. Eu agora vou fazer aí pro meu lá, vou lavar com aroeira e para bater de novo, porque ele é um anti-inflamatório e tem aí da urtiga branca é muito bom também e é fácil encontrar é fácil encontrar Aroeira é fácil encontrar eu vou bater de novo é e a urtiga branca é um pouco difícil, mas caçando se acha outra coisa que eu fazia pode dormir de colete, estavam do leite tossindo. Eu fazia chá eu fazia a raiz da vassourinha, mas de dentro com aquele com o mato que ele é tinha uns espinhos cortava a raiz lavado com a colônia quando tava gripado eu botava a colônia pra cozinhar e dava banho no meu menino de colônia e lá quando eu tava de resguardo minhas pernas inchou e meu marido foi buscar uma uma uma um homem do do do do do do do do Duma planta o nome despertou porque ele é um anti-inflamatório que desincha as minhas pernas.


Ele trazia cozinhava coava e Eu lavava as minhas pernas porque era o nome daquela eu sou mãe de nove filhos, só uma que eu tive na maternidade assim que fui a cirurgia, mas o resto tudo e foi carne e tudo e outro parava remédio é inspetor da planta. Se chama é inspetor também tinha salsa da praia que é muito boa também. É só essa da praia e tinha isso aí a gente fazia uma misturada de irmão Paulo. Sabe que às vezes aquele tempo a gente usava não tinha farmácia o remédio era remédio do mato. Pera aí e essa menina daqui pegou um cansaço cuidar da pequena, minha mãe fez para ela o lambedor da do coisa do Jatobá da Lapa do Jatobá da casca da casca do Jatobá e ela melhorou mais que ela era cansada era minha filha mais velha, minha mãe fez esse chapéu.


Você é muito chato e ainda me fazia o ó comeu o melão, meu pai gostava muito de fazer o melão também lá o Arqueiro o melão São Caetano, né? É aquele outro também me esqueci agora que tem alguma lá em casa aqui sempre arrasa com ele é que é bom pra pra pra pra verme pra gente bota ele passa no estômago Mastruz com Leite é muito bom também tá entendendo? É uma vitamina e também é muito boa também para problema de verme, entendeu? Aí naquele tempo não seguia mas essa imunidade também, né? Aí realmente era animado. Eu queria dormir tudinho fazendo chá de mato. A gente vê assim não coisa tão difícil da gente fazer quando você estoura uma veia, a gente tem uma senhora diz que se estoura que tem não para. Então a gente tem um o quê mesmo comigo já aconteceu umas três vezes que a gente tá e não tem já me acordei com o vaso e até chegar no médico.


Então o que é que a gente pega um caroço de feijão que sempre e com aquele caroço de feijão, ele fica ali em cima um pouco, então pronto já para


destaca o sangue canto não precisa ir para hospital caroço cozido o grupo cru, feijão, bota em cima montar se ele não for grande que ele não passa, mas tá ali já tranca ele já para isso já é meu avô minha avó, minha mãe já fazia isso pensou com outras sementes, só feijão.

Bacana e as mais antigas no caso aqui tem né? Esse grupo aqui é tinha rezadeiras, minha mãe era uma das Rezadeira. Que coisa linda e ainda existe rezadeiras. Hoje existe aqui em Jacumã, eu não conheço mais, mas é pouquíssimos as rezadeiras fazem parte de um grupo de pessoas, né? Por exemplo eu vou dar um exemplo lá no São João do Cariri que é o estudo que nós estamos fazendo é muito interessante os depoimentos de mulheres sobre toda mulheres que dão que curam vacas que é chamada as almas almas vaqueiras. Então já tinha isso era Piaba.


Fazia muito ele salvava, elas salvam. Hoje os animais que estão Entrelaçados que estão com problemas com as rezas voltadas para os animais, né? Rezavam eles retornavam era tudo pelo poder da da oração da reza que era destinada para aquele fim de cura, né? Aquele tempo estava já tinha tudo isso você vê que você conheceu o ouviu falar de Maria do Caio. Ela é uma Tabajara, ela é quem trouxe Henrique que trabalhava com a Jurema e trazia essas regras dor de dente, ela morava dor de dente, rezava. O dente aí da teve época e quem deriva tá com 80 ou 90 anos uma vez ela chegou lá na minha casa com o dente correndo doido uma dor e dei aí minha mãe chamava assim José aí minha mãe era criou bola. O Gi sabia de tudo.


Debate botar Fazia tudo beber tudo tá entendendo? Aí ela ela ela ela ela acho que é a fé, né? É a Bíblia diz que a fé é quem cura, né? Isso é a fé é que cura ela tinha aquela fé de Zé foi essa que o meu dente estou com uma dor insuportável. Tô com muita correr. A mamãe tirou os Ramos não saber não sei qual era o homem que ela tirou isso me resolveu ela é rezando rezando rezando rezando rezando era pequena ela me lembro essa razão depois o dente da mulher passou aí eu pergunto na na no entendimento de vocês também é uma medicina. Com certeza é uma medicina bem então assim diz e disse o nosso senhor Jesus quando teve aqui na terra, né que ele disse nós tivéssemos perto do tamanho do do do veríamos montanhas então aí esse processo de cura a fé é o alimento a gente eu estava já a gente somos movido pela


A gente tem nosso saberes e temos nosso conhecimento também espiritual. Pronto já estamos entrando na espiritualidade, né? Só para fechar essa parte de valorização dos sinais de saber dos sinais da natureza vocês vocês só para fechar antes de entrar mais por atualidade. Vocês costumam sempre olhar os sinais era a parte que eu ia perguntar seu zé, depois ele chega aí ele foi logo meu cavalo dele ali tem que saber como é que como sai, porque tem esse que é preciso saber a gente tem a gente mora a gente morava muito assim, geralmente a gente ficava sempre à mercê quando a gente ia construir um friozinho sempre baixar a gente sempre na beira do rio era as partes mais que tudo.


Então quando a gente ia pescar o que eu fazia alguma coisa a gente se observa muito a válvula do Lolô a ova do Lolô, quando o tempo vai ser de inverno que vai chover muito ele sobe e faz o o o o a obra dele lá embaixo. Mas quando vai descer vai chover muito a gente vai conhecer que vai chover muito vai dar cheia no Rio a obra dele tá lá em cima. A gente já sabe já tem esse conhecimento de que olha o inverno esse ano vai ser forte, não vamos puxar até onde a gente vai até a gente pode botar roçado, porque era essa experiência que a gente tinha e hoje as pessoas ainda estão muito ligadas, é quem mais se se baseiam, né na na lua nas Maré, acho que hoje os pescadores são muito guiados também do pé do vento da natureza e também a gente sabe do tempo certo de plantar cada.


Coisa né? A gente segue que a natureza tem o calendário dela o tempo que vai ser de chuva que vai dar certo de plantar o milho o feijão de fazer os roçado. Então tudo isso a gente se baseia nos sinais e no tempo da natureza, né? Não é não é a gente que vai no nosso ritmo, a gente tem que acompanhar o ritmo da natureza gostaríamos de ouvir seu Zé também que já que é o caçador é eu sou mais plantar e é ficar sem muito mas eu


Parei de matar os bichinhos que os bichos precisa de viver então Antigamente eu precisava de matar para alimentar né das coisas mas hoje ele não precisa mais. Então eu vejo os bichinho besteira para lá agora Padre cultura os sinais que o senhor fez na natureza respeito e considera. Parabéns de plantar as coisas cansada. Eu tava em casa, eu olhava um tempo a lua cheia. Aí eu achei de outro 9 horas aí quando a lua sair de 9 horas já ia para o Mato porque eu sabia que o trator já tinha saído para para comer para ser alimentado as coisas leituras do tempo aí quando eu me importar. Olha que ele já tô no mato. Aí eu sei que o meu cachorro bota só dava ele na cabeça, né? Aí eu matava um covar trazer para casa aí.


A esposa para parar e eu já passava para dentro, né que ia subir vivia disso nela e ela é das casas era peixe. Eu nunca sou muito a peixe. Felizmente eu não gosto de peixe a minha a moto é carne mesmo. Sim. E aí o tempo de plantar cada coisa como jerimum a melancia o feijão e aí vai ter cultura agora, né? Agricultura eu boto esse tempo agora tá tá molhado. Você tem que se preparar para maniv é boa. Você não é boa para o feijão para melancia pro pro jerimum não, é porque é negócio de rama e hoje e o Martins esse não milho é dependente é esse tipo de coisa, ele não bota com chuva. Faça uma marcação ele não bota tem que segura ali não gosta muito de água o jerimum não manda assim ó é tudinho não mas não bota agora isso é a batata gosta de de chuva a macaxeira.


Ah o inhame isso aí eu vou simbora logo, mas na chuva é só esse negócio agora quando começou a o verão começava o tempo enxugar é para o planejar uma para melancia eu vi muito até para estar muito aqui que a gente gosta de plantar e bota aquele maxixe é isso é que eles gostam de sono, não gostei. Nunca chuva. Então essas coisas que a gente nós temos. E aí a gente fica preparando. Quando começa Janeiro aqui no meu tempo era moleque quando as primeiras pessoas de Janeiro nós já plantava nós já ia colher mas hoje a obra de Deus mudou tudo por tudo aí vê aí vem Janeiro, vem fevereiro vem vem vem Março a gente no meio do nosso água no meio de Maio aí é sempre uma produção sempre acaba nada de Cultura sempre fala nada de vantagem que não tem uma ligação a desgraçado de Deus mesmo, né? Que é a chuva que nem a gente tá?


Mas a gente agradece a Deus por tudo que hoje tem aí o tempo molhado nós planta agora já tô preparando os terrenos, já tomei para começar a plantar já proteger rabo de batata nesse dia aqui o meio Gmail que nós temos Batata para comer inhame e é um pé de de fruta que é a minha Granja é o pote mais tem é fruta que eu gosto de plantar quando garrafa com pé de pau é para mim tanto de fruta para mim tá arrancando um pedaço do meu dedo que não é para arrancar então é essas coisas que a gente acabar em cima disso, quem é da agricultura e quem é da pescaria e sempre consegue fazer a diferença, né? O que que eu posso plantar agora ou ou E qual é o tempo certo que é isso? Você a gente planta, nós vamos dizer pros outros agora aqui. O jerimum é 3,5 você planta hoje aqui é três meses, se Deus quiser, você já tá colhendo essa melancia que tá aí como é que o senhor ver?


Vai dar certo ela ficar aí dá dá deu aqui deu que nem pedra por aqui, ó, daqui a pouco quanto tempo ela vai começar a florar para ter flores meia tá madura três meses é e é gay e a lagarto não comeu a do tempo. Já estamos esperando por que e ela tá madura para você saber a coisa mais simples do mundo chegou em cima dela, só porque eu tô ela aqui um pouquinho que a cisterna com si própria, ele tá madura tem um anelzinho nela que sempre pensando nela, eu não vou muito pela não, mas quero meio covardia, eu vou sempre nela. Você quer comer ela assim, ela é pronto. A primeira é de primeira então é dessas coisas que a gente convive dia aqui na terra e ele disse que a gente precisa sobreviver, né e Naldo na construção você consegue.

Fazer leituras de tempo da natureza poderia falar pra gente porque cada cada etapa da construção, né? Tem sei lá um sim um tempo. Você é quadrado, né? Exemplo aqui eu chego no terreno aí logicamente eu pesquiso o tempo se vai ser chuvoso ou sol a gente ali daquele início começa as medições de a gente começa assim a topografia passa.


Faz as ruas aí dá do meu fio para um muro é dois metros do Muro para dentro são 5 metros aí de 5 m por diante começa a falar com a construção aí tudo dá um tempo, né? Exemplo tempo da cavação, leva aí 8 dias 10 dias construção em si. Aí a gente pega uma casa de


De dois quartos quatro quatro quartos, aí ele leva um processo de três meses, tu dá um tempo, né? Há um tempo de cavar leva uns 15 dias aí a construção mais uma um mês para subir para botar laje a mais 15 dias cobrir aí com mais um mês, estamos já finalizando aí tu dá um tempo quer dizer a chuva a gente corre muito que ela quer é isso que ela quer perguntar isso porque aqui atrapalha ela tá parecendo. Porque quanto você não cobre a pintura você não tem direito de reclamar você não quer ela tira a chuva tira mas depois que você cobriu aqui você pode acabar dentro pode chover, mas não empata o seu trabalho aí de jeito nenhum. Esse é o tempo que se preocupe com mais corrupto mais prioridade é cavação rapidamente fez a sapato chamou baldrame fez alvenaria rapidamente.


Vamos cobrir porque eu não sei o queixo antes da água chegar da chuva porque cobriu a gente tem como ele sempre falou, né? Cobriu pronto. A gente tem trabalho ali com um um formigueiro tá? Sempre aqui trabalha ali interno aí vem instalação de água luz, eh internet e várias há vários etapas. O cara não tem seu tempo, né? Enquanto não chove a gente cobriu cobriu a prioridade minha cobrir cobriu você tá na parte de Deus lá de fora, aí você já vai trabalhar pela lava parte de fora, mas vai chover já não faz aquilo ali vai fazer essa parte aqui tem um exemplo que foi pintado pelo Cacique Paulo eh o pessoal quando vai o comportamento do animal é um peixe, né chamado, né? Quando os ovos vão para cima da água aí.


A repetir por favor na etapa o o o Lulú larga a arma ele sempre ele bota as suas aulas é ele só bota fora d'água é dentro da água que ele tem mas ele escolhe aquelas plantas tendão para ele colocar suas obras, então a gente observa ela quando a gente quer saber se o o inverno vai ser forte ou se não vai ter muita chuva no inverno. Então ele já disse para a gente pela natureza. Se ele botar mais alto então vai vir cheia vai chover muito vai ser bem velha, mas se ele voltar em baixo não vai ter então a gente que planta a gente que caça a gente que pesca já vai saber que ela o tempo vai ser assim os pescadores um sinal como esse como é que faz a lista.


Vamos ver eu tenho esse animal porque tá ali me levou. Eu tenho um animal que quando eu ia passar mesmo é verdade assobiava, eu já senti que não ia me negocia ser bom, mas é verdade. Isso aí é verdade que eu vejo aí o que eu fazia eu me sentava eu tava ali com o meu cachorro ia me não fazia não fazia barulho nenhum centavo, depois o cachorro saía e ela pode voltar as mulheres dizia. Então vamos embora para casa do cachorro, porque você ver o que é que ela faz no meu cavalo, ela tem criança bem grande todo dia eu vou lá ela e ela mexeu.

Sabe e eu não quero nem de mexer que eu mexia nós ajudar a ler no mesmo. Sim ele não mexo porque eu sei que ela mexe a minha esposa começou a mangar muito dela. Eu digo não brinca com um lado de Fulozinha. Isso é um negócio é sério, ela começou a brincar ela pegou ela fez um Totó no cabelo dela uma trança que foi obrigado a Ele parava aí pra pra contar pra contar o cabelo que ninguém teve não teve mais não ter Cidinha. Não tem importância não. Tem mãe não quer subir não sei não teve ninguém no mundo que desatar esse povo não deve botar isso. Quero botar em banheiro. Eu digo que ele foi prova viva a história não sabe o que ela é brava mesmo. É mas você talvez se perder dentro da Mata, né? Se ela se tiver de acordo com a energia da Mata tudo acontece normal agora se for entrar e não for pegar da permissão vai pro mato.


Chega o meu pai faz o seguinte, meu pai é é caçadora tem que nem eu perdido gostava de caçar meu pai aí pai tava em casa. Daqui a pouco escutava fica subindo dela aí e meu pai e já teve mais antiga ainda, né? Botar um chapéu tem um torrinho botar o chapéu dele lá aí quando ela ele escutava o vídeo dela, ela disse olha lá no chapéu pegar o chapéu, porque na cabeça dele aí me dá meu fumo aí começou a dizer tá querendo fogo Ela Quer fumar quer fumar e ele se toca dentro da Mata botar o fumo lá o dia no outro dia que tesão lá naquela tapa tu levava e ele tinha coisa que nunca ia matar não matar um tatu nunca e ela nunca perdeu ele e ela pede você assim, ó assim, ó pertinho pertinho é você ficou arriado. Fica quietinho ali não chame ele não fica ali quando você pensava que você tá no caminho. Você viu o caminho bem pertinho assim, mas que que ajeitar a gente sabe que


Isso outras coisas né? Mas para o nosso flocos ela é Ela existe, ela é geral existe e ela faz mesmo ela ajuda com animal, ela pega da minha mulher que pega ela não sobe diretamente ela transou e deu uma Pisadinha neta você ver como é que tá o cabelo do cavalo, ela fez não tem que desmancha ele desmancha não isso quer dizer que a mãe natureza tem seus Guardiões com moto Fulozinha no manga que a gente tem o pai do manga e no mar a gente tem jogo que ela foi João agora foi esse quem é pescador do mar conhece e ele o que ele faz, por favor, fale é o momento escalda Graças.


Ela tá aí gulosinho pra gente caçar na mata é Comadre Fulozinha no Mangue é o pai do Mangue, mas tem a hora de sair do mãe, entendeu? Caranguejo com com espirrar daqui que a gente lá no Mangue criou o os ah, eh, vovó achava que eu tava na casa da mãe dos meus primos, só que na verdade por perto da casa dele tem o rio do gancho e lá a gente foi o que a gente inventou de fazer pegar pedaços de digital, garrafa PET que é uma jangadinha a gente saiu do Rio do gancho até a praia do amor da jangadinha e a gente se preocupando porque a gente tinha que voltar antes do pai e do manga aparecer o que é isso, vocês são os guardiões que tem pessoa que tem dentro da Mata só para fazer para ver se dá demais É verdade tem pessoas que vai pescar vai com Mangue só para fazer maldade ele não


Utilizando não vai tirar sua subsistência, mas vai atrapalhar só aleijar a quebrar matar os bichinhos maltratar então quando o pai de manga pega pega o cabra entra aqui, ele sabe que o caminho dele 100 anos ali, mas ele se perde e nunca mais volta, ele canta ele ali ele se perde na porta de casa, não tem. Tem um amigo meu que ele ele um amigo meu ele foi ele Deus culpado são muito amiga, isso é um vizinho.


Ah tá aqui não tem aquela aquelas coisas aqui embaixo pronto, ele entrou no forno Neves vai ser aqui em São Paulo e ele pensando que o amigo dele tava na frente e chamando ele ele me tira o cara amiga ele atrás chamando ele eu tô aqui. Fala aí e então tô indo tô indo o medo passou quase de manhã de duas horas dentro do manga perdido para sair deu trabalho e ele disse não sai daí não. Fica aí que eu vou lhe encontrar eu falei como ele saiu dentro do ônibus o pai de mãe, como é que a mulher fez no cabelo da minha mulher. Cadê ele é real? Porque você tá escutando aqui não é história de cara não tinha nada. Agora eu gostei tanto mas não falou não fala que a a o não sei se é o mesmo porque eu já vejo falar minha avó falava Lampião, né? Que ele tinha uma luz aqui na na na na cabeça dentro do mar, você consegue ver ele por essa luz na cabeça dele o nome dele, ele tem o Lampião mesmo.


É a gente se sempre seguia quando a gente olha de ver dentro do mar que a gente olha a gente na vida da beira da praia, a gente já veio porque não é pescador não é navio e nem Tá pescando a gente conhece o lugar onde se pesca aonde pode ter um barco então sempre quem tem o direito de ver ver ver sempre aquela luzinha acesa que eu moro na frente do sofrimento pode estar chamando quando tá maluco tá aceso e ele tá lá, então não vai entrar no mar não vai fazer coisas que não deve brincadeira é como se fosse um farão oposto ele vai se posicionando oposto dele, porque a Luz está lá mas não chega perto dele. É porque é algum perigo é alguma coisa ali sim, ele gosta de distanciar e você nunca vai chegar junto dele não ele vai se distanciar porém cada vez mais que você vai querer você vai entrar no abismo e que ele insistir com ele.


Ele vai vai perder e ele vai se perder assim em qualquer monta é motivo, ela se perder Ali na beira da praia, ele não tem saída para ele ver ele tá então o caminho tá fechado. Tem um paredão tapando a visão dele não tem é que nem é que nem a o pai de manga e aqui na pracinha. Mas falou assim quando a subiu o dela tá longe, é porque ela tá perto e quando o assovio dela tá perto do ouvido, ela joga toda subindo meus ouvidos, porque eu acho que eu escuto mais que pensamento porque chega aí eu vou ficar suspenso do chão diferente que você sabe que não é ninguém é sabe que não é uma coisa interessante, né aqui o relato dos Guardiões da natureza do nada Floresta vai acabar o que brincar com ela, ela pega ela não porque a gente vive isso não é que viveu a gente vive isso muitas pessoas hoje não acreditam não tem não, mas a gente não tem tem nada só o cabelo dela porque ela trouxe aqui até que ele desmanchar.


No lenha a gente ainda vive num contexto de natureza embora a cidade queira invadir isso aqui tudo mas o território ainda tá ainda aqui a senhora vem muito aqui por roçado. Vem muito só nós estamos com as onça. Solta aí 11 onça pintada.


Hum então plantando. Ah não vou plantar hoje não na próxima semana vai plantar de vacilo porque ela tá andando aí não é jaguatirica não é a onça pintada é a onça pintada, elas estão mais o camarão camarão, porque o território dela é tudo é a boca dela. Ela foi mostrada aqui. Agora já perdeu na divisa com Santa Rita, né? Porque aqui faz tudo quando vai viver tanto aí ela não tem mais mato, ela não tá mais fechada agora pegada lá na lá na minha rua lá da casa de Juliete que era de Jussara as pegadas dela e dos filhotinhos tava lá ao redor da casa porque Jussara guardou uns cachorros e um filhote dentro de casa e ela escutando né arrudiando arrudiando por causa dos filhotinhos que tava lá.


Ele viu ele não viu ela porque ele adormeceu, mas depois ele viu quando ela pegou uma uma uma uma um lobo-guará e comeu a metade do Lobo, né? Então tem que ter cuidado a gente que estamos por ali que vai sair se afastando com a gente aqui ela não vem, mas sempre quando vai ficando mais só menos gente ela e ela é Traiçoeira. Né o filho dela planta sozinho lá não é dizer prestar atento, né? Porque ele tá pegando agora tem que ficar sempre digo assim, não abandonou aqui embaixo, né? Porque o outro menino foi tava de dirigir. Ele atirou nela com arte de preto e ela ela se assustou foi embora da casa que tu bota a carne. Quando ela tá comendo a casa, só tá correndo.


Hum gostei gente. Ah com os ovos aqui que ela tava dizendo assim. Ah, pois se eu me encontrar com ela só tem uma maneira de eu de eu me escapar dela eu vou ficar quieto era jogar merda nela, porque numa hora dessa esse cara todinho tá grávida a liderança jovem nenhuma. Vem aqui nesse grupo, né? É subiu, né? Vocês consideram por exemplo tudo que tá sempre relatado aqui, vocês consideram isso o importante Com certeza a gente tá aprendendo, né? Que que tá importante mesmo, né?


Não vê né que passa assim nunca viu não tá vendo? Hoje é é tipo assim, ela fez essa pergunta, botei a presença dela e muitos locais os jovens não presta atenção aqui os mais velhos falam entenderam tipo pela minha idade. O pessoal diz assim, por que você sabe tanta coisa porque o meu tio avô ele vinha passar o final de semana na casa de Tia Josi e ele dizia a minha filha tem uma coisa que ninguém rouba de vocês. É o que você aprende é o estudo e você saber ele andava comigo até o caminho da casa tia dela dizendo nem sabia que tudo é uma família só aí ele dizia assim para mim é os coelhos são todos os meus parentes e não levantamento da árvore genealógica, foi que a gente veio ver que a minha bisavó é tia bisavó de maior não entendeu? Aí assim tipo a juventude.


Para esse ensinamento e adiante a juventude, tem que ir saber e passar para os seus filhos dos seus filhos e passando à frente para porque as os mais velhos vão morrendo né? É isso aí, não é reunião dessa portanto é isso que ia aí tem que passar isso mesmo que você dá certo, tem que passar por cima e hoje o jovem não quer entrar numa palhaçada dessa não agora procura onde é que ele queria estar muito aqui, né? Aquele reunião esse daqui só são 10 pessoas mesmo qualquer grupo para os jovens não quer nada com uma coisa ele não quer nem com os pais dela, imagina o negócio dela nessa época o jovem. Não quero nada com a vida, então me parece que a liderança jovem que eu trabalho muito bonito, aí eu não quero aprender eu vi um dia certo ela.


outras coisas que levam eu até amor tem é e agora gente o satanás, né para ir finalizando a nossa conversa de hoje a gente e mesmo antes de finalizar tudo bem uma coisa a questão da onça que foi citada é deixa eu falar quero levar a carne para ela, você joga 5 Kg de carne é essa fica e ela faz carreira, mas não mas falando sério é pelo meu conhecimento agora já não tem nada a ver assim é Mais especificamente a Ah, isso é um bom indicativo eh dentro da biodiversidade a presença de onça que é uma espécie ameaçada de extinção, isso é um bom indicativo por outro lado na representação para muitos povos a presença de


Ali no uma onça, por exemplo significa poder significa força da Lei. Então tome os cuidados físicos, mas perceba é percebam isso tá? Porque ela também né? Sim é é um sinal físico de uma energia voltada para lei para poder ler ler lei, tá? Então que ela esteja representando essa força cura vamos dizer assim, né para vocês tomam Cuidado os físicos porque é um animal como qualquer outro, né? Mas que animal que eu como ele ataca é qualquer animal que come só o ser humano, quando eu tô com fome. Eu quero um bolo. Tem biscoito, viu? Agora é verdade, é verdade esses bichos eu tenho uma eu quero.


A gente só saber que é gostoso, a gente quer atacar às vezes sem forma o ser humano e ele não comia outra comida só bebia leite e nada do do mato. Eu não queria ver das novinho. Pois é eu pegava a mamadeira de leite preparava dava ele deitava botava no pé mais na boca e bebia, ele não queria outra coisa só leite. Depois ele fez uma coisa errada. Eu fui embora até hoje falo da cobra que você andava com ela no pescoço a cobra é mas aí foi a qual foi o perigo, mas quando eu disse é assim desse corpo aqui assim eu tenho um botão Neo eu botava para o meu jato para ela comer ela comia quando era meu filho eu ia trabalhar ela levava ela bem ela veio aqui enrolava aí amarrada, né? Como amarrei ela pelo pescoço. Quando eu chegar em casa tirava é levei para o serviço.


Aí fiquei lá trabalhando e o cara mudando meu fogo no mato lá e daqui a pouco o irmão uma vez e ela tá amarrada no que ela tá lá no meio assim lá e eu devia Abrir como é que eu vou tirar essa cobra daí o Ibama veio com o Ibama, mas não quer que judeu, né com os bichos os bichos e eu digo agora e eu caçava a gente tinha ido lá e cadê seu patrão disseste ali, eu vi que Ele saísse, mas daqui a pouco ele foi para o lado da cobra porque tá toda fora Vixe Maria. Isso é uma jiboia. Poxa, depois nós desce, ela tá amarrado. Ele foi aquela Marreta, porque essa bicha tava aí para o fogo, eu amarrei para não requeimado, eu vou levar para soltar ela diz muito bem muito bem. Isso é Tabajara gostosa, aí eu peguei a bomba, botei aqui no pescoço e ela tava.


Chamado do fogo e o povo já tinha visto ela começou a me atacar aqui homem ela deu três voltas aqui que daqui a pouco eu não podia fazer nada assim é e me deu deu certo, vocês falava assim se ela estava estressada e eu agarrado com a cabeça dela. Digo que eu soltar ela vai me matar de morder agora e eu seguro a rocha eu lhe arrocha aí e aí foi que ela deu uma gota sério aí que eu me atacar, viu? Sabe Briguei, eu briguei com essa mão direita aqui não tem muita Rocha a boca dela, mas ela tem um pescoço o pescoço não é mas eu não tinha força com essa mão para tirar a cobra que eu sei como ver uma meia hora eu não ter suei, mas tirei eu digo aí agora não tem vamos manter amizade não tem nada vai para o cacete aí mentira o cacete de bagacei a cabeça dela todinha depois de tanta amizade. Oi batata essa bichinha aí mesmo. Aí eu disse tá morto safado. Eu vou ali vou buscar outro negócio ali com ela dá conta que é cavalo lá, quando eu cheguei não tava mais lá não.


Foi-se embora homem foste embora com a cabeça todos buguerame.


Espiritualidades vocês seguem.


Geralmente, a gente tem o nosso rituais porque é o Toré a gente trabalha com ele na nossa festividade na nossa luta no nossos plantios e reuniões que a gente tem porque é a nossa Cultura, né para manter. Nossa cultura viva e o que a gente tem hoje aqui outros povos como eu conheço que ando eles têm o Toré. E tem também a sua parte que faz o seu culto afro brasileiro. E também eles incluem contou né? Porém nós aqui hoje Tabajara aqui desta Aldeia, a gente tem o Toré como cultura e cantamos os nossos cânticos sem Celebrando é em memória dos nossos passar nossos antepassados e acreditamos sim na força do Encantado que para outras pessoas que não entendem acha quem é quem é o Encantado a gente sabe que ele existe está em nosso meio e a gente não vê.


Espírito santo de Deus. Esse sim é o encantado que nós pedimos a proteção que estamos sempre com ele e buscando a ele em cada momento e de acordo com Tupan quem é Tupan Tupan nosso Deus o criador de todas as coisas e está no domínio de todas as coisas e sem ele nada são-nos. Essa é o que nós professamos aqui e a nossa cultura, ela é viva. Ela é dinâmica não é uma coisa já sabe então em cada momento a gente estamos mudando para manter a nossa cultura viva.


Agora que as pessoas indígenas eles podem ter diversas religiões. Então vai ter indígena que é católico o indígena que é evangélico, mas aí são questões individuais de religião, porque a gente não mistura a nossa religião com a nossa cultura e nossa tradição independente. Por exemplo aqui a gente tem as pessoas que são evangélicas, mas a gente dança o Toré a gente faz o fortalecimento da nossa cultura e digo ao modo. Esse é o momento que a gente se encontra os católicos com os evangélicos com os parentes que são de qualquer outra religião para fortalecer a identidade e a cultura Tabajara que a gente tá fortalecendo aqui na aldeia nós Conquista Taquara, porque esse é um assunto muito delicado que muitas vezes as pessoas perguntam assim, qual é a religião do indígena acha que não é a religião é a nossa cultura e a nossa tradição que para nós é Sagrada também é de igual modo Sagrada, né? Mas que a gente respeita as individualidades.


Dos parentes porque a gente sabe do processo que a gente passou aqui, né? Desde a época da colonização de como eh essas nossas práticas culturais, inclusive foram muito demonizadas, né? E hoje a gente traz isso, não é nem um sincretismo não. A gente tá fui pra frente não é nem questão de de ser um sincretismo não é é uma questão da gente eh trazer uma explicação tá dentro da gente enquanto a gente entende do que é sagrado, né? E dentro do nosso contexto a gente respeita tudo isso é diversidade é muito importante que mais alguém mais gostaria de falar.


Ela tá falando alguém mais por exemplo o Maraca, né? Esse Maracá balançou aí quando se usa o Maracá né É um tipo, né? Então o que significa usar o Maracá ele nos dá força é uma ferramenta Sagrada muita das vezes a gente outras pessoas que não conhecem, mas quando a gente balança o Maraca eu quero contar para vocês, nós estávamos ali na Elizabeth. Tava eu Edinaldo e um outro uma outra pessoa que estava conosco entre nós se lembra nós Recebemos um ataque de policiais juntamente com Os capangas da Elizabeth e só tava nós três cercaram a gente e nós falamos o Maracaçumé naquilo dali do jeito que eles vieram vocês vieram ligeiro para não secar, eles saíram mais ligeiro ainda então ao balançado Maracá a gente recebe força para nossa natureza da nossa mãe terra e a gente eu sinto diferente.


Não é cor. Eles pensou que tinha muita gente, eu acredito que eles giram muitos outros que estavam ali, então não é somente o Maracanã, não é somente o campo tem todo aceitação e o respeito da cultura da dança dos índios, então é um objeto que é que nem um sanfoneiro usava um deles lá e tem um estrangeiro tudo tem a sua parede. Então é isso. Que é isso é instrumento. Esse instrumento de de trabalho de trabalho dançando e tá ali balançando ele aquilo ali é uma ele vai além disso o maracay de trás toda, né? A gente sabe quando é para fazer silêncio quando tá chamando para a gente se juntar e isso isso então é um instrumento de comunicação é um instrumento de força é um instrumento de proteção é um


Instrumento de trabalho como ela disse né de dança porque na dança também se utiliza o ritmo e o som né? Então cheio de significado, né na vida de vocês tem uma representação é uma importância.


O Cocaia. Nossa veste a nossa identidade é o nosso CPF ao nosso registro é o que nós estamos a gente é tanto que você me ver sem cocar. Sou natural, quando eu coloco o carro quando eu chegar a uma diversidade mesmo diante dos nossos parentes porque não se mede o cocar pelo tamanho dele, nem quem eu sou mas eu estou com o cocar eu estou representando assim os nossos ancestrais a nossa força a nossa nós poder a gente se puder não é simplesmente. O Paulo é uma representação representa agora e traz a força da natureza, né? Inclusive é são temas né, traz a força da natureza dos pássaros, né? Seja?


Lá de qual pena, a gente tá usando a gente traz a força da natureza que a gente está representando junto com a gente não tocar.


Acho que é um símbolo de proteção como a pintura que já vou mas é um é um símbolo de proteção para a gente quando a gente vai eh reivindicar os nossos direitos. A gente sempre está se vestindo de proteção. Então é o cocar é o Maracá é uma bordona é a nossa pintura. Então a gente tá se preparando os colares. A gente tá se preparando para ir para a guerra. A gente tá se preparando para ir lutar para reivindicar nossos direitos, então é como a gente se sente ponto não é não é a mesma coisa se eu saio da minha casa e simplesmente chego naquele local, não é a mesma coisa quando eu passo por esse todo esse processo de me pintar junto com meus parentes, porque um vai me pintando a gente tá trocando energias eh eh o cocar. Eu não costumo emprestar o meu koka para outra pessoa a não ser que seja minha irmã uma coisa muito próxima para já as próprias é diferente. Eu não consumo não, não costumo emprestar.


Para ninguém porque a gente tem energias cada um de nós tem energia dentro de nós positiva negativa a gente tem energia. Então a partir do momento que eu passo um objeto meu para você, eu tô passando minha energia para você, eu tô dividindo isso com você, então não costumo emprestar para outra pessoa que eu não conheço porque eu não sei que tipo de energia eu vou trazer para mim. Eu sei qual é a energia que eu vou passar para aquela pessoa, mas eu não sei qual é a energia aqui é aquela pessoa vai me trazer então é uma forma que eu também não costumo fazer né? Que é um é são objetos nossos e que a gente tem que ter muito cuidado. Nesse contexto não se presta porque o cocar ele é ele é próprio da pessoa. A gente não empresta nem para tirar uma foto não se pode tirar o cocada da cabeça e bota na cabeça de ninguém e um outro e nem um outro é a nossa identidade é a nossa vida que nós estamos a ver é como o nosso cordão, você vê aqui um cordão desse daqui ele com muita das vezes a pessoa olha simplesmente para você um cordão, não é?


sempre um portal, ele tem todas as peças e ele é um elo ele é fechado, ele não tá aberto então isso mostra que nós estamos fechado, ele traz esse símbolo de que o nosso corpo está protegido se a gente bota para eu ter um monte de onça quando eu saí porque quem é onça ela até o seu poder diante do todo o outro animal que está inferior, ela vai ele vai tem medo de me atacar porque eu estou


Acima dela eu tenho os dentes. As presas de crocodilo de jacaré também que a gente anda muito na mata os nossos parentes que estão dentro da ponta da Amazonas todo ele tem o seu cordão com os dentes de jacaré, jacaré então aqui dali representa. Nós não somos atacado nem por cobra e nem por outra jacaré é muito difícil você saber ver que um jacaré atacou ou um índio foi atacado por uma cobra você sempre ele tem a sua proteção. Isso daí é ancestrais.


Tiaras com as penas na cabeça dessas mulheres tão lindas tem algum significado também é um tipo de Coca na verdade, né? Eu eu me acho especial quando estou com ela eu chego num determinado local sem ela as pessoas vão me receber vou falar comigo de qualquer forma, mas se eu estiver com ela aí chegou uma indígena o tratamento é diferencial, então isso aqui para mim ela tem muito poder.


A respeito né? Ele respondeu e Respeito, tipo assim, quando você tá normalmente é uma forma e quando você começa a se vestir tipo com a roupa da Aldeia com a tiara, tipo eu mesmo né? Fico toda arrepiada quando eu já tô me preparando para ir para algum lugar é como se tivesse força e energia e você se sentir se protegida e as pessoas que olham de uma certa forma e passa uma pergunta tipo e você é indígena. Aí eu respondo sempre fui desde que nasci percebendo cada narrativa, por exemplo o símbolo de proteção tem uma ligação muito grande quando a diversidade e com a espiritualidade.


pintura Doutora também e elas hoje tem muito geralmente quando eu saio se eu tivesse meu Cocais eu mesmo se não tiver pintado quando eu colar eu estou no


Para mim eu não estou me vendo ali, eu não estou no contexto e sim que envergonhado. Quando não estou com meu como ministro evangélico, quando eu saio quando eu teto em gravata na mão, estou lá no pouco representando aquilo dali então quando eu saio da Aldeia que eu vou fazer apresentação indígena, se eu não tiver a caráter com minhas trazem eu estou incapaz, eu sou


Alguma coisa mas para gente encerrar.


Então no momento como esse que nós já estamos aqui para a gente temos assim um sentimento de pertencer.


Né, a gente não é simplesmente uma reunião com essa daqui a gente escolheu aquelas pessoas que somam que pertence porque a gente tem uns muitos outros que até tem mas não tem o contexto não tá no contexto e para nós esse momento aqui é sagrado, mas aqui estamos no momento que eu cheguei a gente não fizemos o nosso ritual que eu postei no Cantar, prefiro fazer mas a gente vai encerrar cantando pelo menos uma música, vamos balançar o Maraca e Vamos agradecer sempre a gente agradece ao nosso Deus desta forma porque é dele que nós por ele que nós estamos aqui não é que nós estamos aqui para aí, mas é que ele nós somos dele todo respeito a nossa mãe Terra nós pertencemos a ela.


Então o pertencimento não é o território que é nosso é nós que somos do território.

Esse bebê emocionante, né território, não é nosso nós que pertencemos ao Território que visam muito bom. A gente eu quero dizer que eu cheguei feliz agora tô saindo plena no sentido de que a gente conseguiu trabalhar a temática, vamos ter o desafio enquanto a equipe de apoio e de suporte aqui para a gente catalogar isso no formato de resultados de pesquisa, né? A gente tem um relatório que deve ir para secretaria de educação e cultura do Estado da Paraíba, mas deve vir também para cada Aldeia cada uma tiragem relatório e na nossa próxima vinda que eu ainda não tenho ideia eu volto a convidar os dois fiquem atendo que eu fico falando tá? É mas a gente volta a conversar a gente.


Ali templo também porque tem duas dois próximos Domingos serão as duas próximas à aldeias que faltam eh, depois disso a gente vai trabalhar essa parte de de registro de de de trabalhar a cada Aldeia para depois começar a marcar a volta para a gente bater martelo, como se diz, né? No norte os indígenas chamam a bater gordura pra gente validar dentro do campo da acadêmico que a gente chama validação da pesquisa pra gente validar cada Aldeia e a cada Aldeia validando os resultados o resultado final que será nosso, esse é o nosso segundo vai ter o terceiro será o quarto encontro que a gente vai procurar um lugar eh. Possivelmente eu não sei se lá odeia de Vitória, porque tudo começou lá, eu acho que por consideração essa questão ética. Talvez lá ou em um outro espaço onde a gente possa botar um data show para presidencial para a secretaria.


A a gerência de vocês consigam esse espaço só para a gente apresentar o resultado final todo da pesquisa, que aí bota uma data show, né? Que que vocês acham sim, não é? Uma boa é de uma uma um auditório que a gente consiga acompanhar, né? Isso é bom porque fecha mesmo sendo independente da Aldeia, eu acho que num lugar que não vai ser a noite, né? Fica muito claro. A gente já teve experiência de querer fazer essas coisas de dia. E aí você viu? É na logística fica ruim então uma estrutura né? E não tata show é todo mundo acompanha é bom porque todo mundo acompanha, viu? Cacique, já fica aqui uma provocação para o senhor e para colocar assim que é Dinaldo também lá da gerência, né pra gente um final quer dizer o quarto encontro já ser uma área assim que a gente não pode e passa muito né? Não sei como vocês verem melhor, desde que tenha um espaço projetar e todo mundo ver o resultado.


Projetar durante o dia que fica em aberto a gente não tem como existe uma gerência que trata da acho que lá existe esse espaço então muito obrigada pela presença de todos e todas obrigada de nada demais. Olha e até dá agora. Se der manda uma logística maior de vocês isolar muito para a gente poder assistir sem estourar muita claridade, né? Até dar uma voltando que existe essa panela essa coordenação e a gente poderia tentar usar o poder político dessa coisa assim para conseguir o espaço mais tipo um pequeno auditório que possa projetar e os Tabajara vem por principalmente. Principalmente não pode faltar os que participaram do grupo focal. Esses são as pessoas que no final caramba, esse é o nosso resultado. É onde a gente tá bem onde a gente não está bem É aqui e vai relatório para todo mundo.


É pessoal nesse momento assim, a gente vai ver que isso aqui é para todo o povo mas com diferencial para vocês porque vocês têm o poder de presenciar que nem todo mundo vai ser presente, mas o poder de fala é com cada um de vocês que começaram que são dando isso daí certo de opinar, você pode se manifestar concorda não concorda. Como já foi dito pela nossa professora ou na sua visão que podia melhorar e pode ser trazido porque às vezes a gente estamos aqui eu tô com minha visão. Tô com meu esquema. Tá tudo ali no esquema. Mas eu posso ter uma visão que possa melhorar dentro do contexto e a gente na criação eu vejo assim que tem esse espaço. Tem sim, desde que a gente


O Gabriel né, Gabriel? Às vezes ele vem só coisa aí.


É não moça é não é lá na barra do na barra do grau é lá em Tambaba é um pessoal da barra de gramame, né? Pode chamar o carro não deixa aí não tá muito longe. Liga para ele liga, se você tiver contato aí porque não dá para ir a pé, não é muito longe é longe demais. É muito longe viu? Ele viu.


Aí você pega aqui pega bem danado, porque senão dentro da máquina quando você arca de Bilu do teu lado demais viva a nossa mãe natureza no nosso dia viva nossas matas, Maravilhas Muitas Águas Doces livros nossos participantes viu as mulheres indígenas no Brasil.


Eu sou peneirada, Taquara, o meu nome é Ibirapuã medir Afonso raiz dessa terra. Taquara não anda só eu vou aí nessa terra da guarda no anta fora, eu vou chamar o meu bebê para poder me mudar aqui a nossa fé e atacar é meu lugar aqui é nossa fé e atacar meu.


Vou vender a data para o meu nome é Girassol chover será da Taquara. O meu nome é gira como eu sou aí nessa terra para caralho, eu sou a licença venha passar a noite com você. Ô, meu Deus para poder me lutar contra amar o teu medo para poder me mudar, porque aqui é nossa querida para melhorar meu Deus na Terra.


Então vamos ver se pode mais Deus vamos ver quem pode dar beijinho no chão é Deus não saio de cruz na terra hoje, não dá certo. Vamos ver quem pode demais é Deus no céu Mãe Natureza o nosso dia a nossas matas Viva o povo indígena do Brasil.
"""

resultado = contar_palavras(texto,encoding="utf-8")
exibir_em_colunas(resultado)