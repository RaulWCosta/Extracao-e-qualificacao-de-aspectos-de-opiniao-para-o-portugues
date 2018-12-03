import pickle



textos = {
    "10.001": {
        "opinions": [
            [
                "Bom de espaço de memoria.",
                "ARMAZENAMENTO",
                "memoria",
                "+"
            ],
            [
                "A camera tambem e muito boa.",
                "CAMERA",
                "camera",
                "+"
            ],
            [
                "Boa velocidade na reproducao de videos.",
                "DESEMPENHO",
                "velocidade",
                "+"
            ],
            [
                "Bom custo/beneficio.",
                "PREÇO",
                "custo/beneficio",
                "+"
            ],
            [
                "Muito bom custo/beneficio.",
                "PRECO",
                "custo/beneficio",
                "+"
            ],
            [
                "Recomendo.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Bom custo/beneficio. Muito bom custo/beneficio. Boa velocidade na reproducao de videos e bom de espaco de memoria. A camera tambem e muito boa. Recomendo."
    },
    "10.002": {
        "opinions": [
            [
                "A camera nao e das melhores.",
                "CAMERA",
                "camera",
                "-"
            ],
            [
                "O sistema e rapido.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "O design nao e dos melhores.",
                "DESIGN",
                "design",
                "-"
            ],
            [
                "Bom custo beneficio.",
                "PRECO",
                "custo beneficio",
                "+"
            ],
            [
                "Display e bastante resistente.",
                "TELA",
                "Display",
                "+"
            ]
        ],
        "review": "Bom custo beneficio. A camera nao e das melhores, nem o design. Mas o sistema e rapido e display e bastante resistente."
    },
    "10.003": {
        "opinions": [
            [
                "Incluindo slot pra 2 chips mais cartao de memoria.",
                "ARMAZENAMENTO",
                "cartao de memoria",
                "+"
            ],
            [
                "Bateria q dura de 1 a 3 dias.",
                "BATERIA",
                "Bateria",
                "+"
            ],
            [
                "Camera q grava em 4k com abertura 1.7 igual a muitos top de linha.",
                "CaMERA",
                "Camera",
                "+"
            ],
            [
                "Processador octa core 2.0 igual a alguns tops de linha.",
                "DESEMPENHO",
                "Processador",
                "+"
            ],
            [
                "TV digital em alta qualidade.",
                "OUTRO",
                "TV digital",
                "+"
            ],
            [
                "NFC.",
                "OUTRO",
                "NFC.",
                "+."
            ],
            [
                "Leitor de digital multifuncoes.",
                "OUTRO",
                "Leitor de digital",
                "+."
            ],
            [
                "Aparelho intermediario com cara e funcoes de um top de linha.",
                "PRODUTO",
                "Aparelho",
                "+"
            ],
            [
                "Funcionalidades e melhores ou iguais a maioria dos intermediarios.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "As pessoas esquecem q esse aparelho e intermediario, nao top de linha e como intermediario ele da SHOW, pois ele vai alem da sua faixa intermediaria.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Aparelho intermediario com cara e funcoes de um top de linha. As pessoas esquecem q esse aparelho e intermediario, nao top de linha e como intermediario ele da SHOW, pois ele vai alem da sua faixa intermediara, incluindo slot pra 2 chips mais cartao de memoria, bateria q dura de 1 a 3 dias, leitor de digital multifuncoes, NFC, processador octa core 2.0 igual a alguns tops de linha, camera q grava em 4k com abertura 1.7 igual a muitos top de linha e TV digital em alta qualidade.O restante das funcionalidades e melhor ou igual a maioria dos intermediarios."
    },
    "10.004": {
        "opinions": [
            [
                "Bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Quase nao utilizei ainda.",
                "PRODUTO",
                "produto",
                "x"
            ]
        ],
        "review": "Bom. Quase nao utilizei ainda."
    },
    "10.005": {
        "opinions": [
            [
                "Bom aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Ainda descobrindo suas funcionalidades.",
                "PRODUTO",
                "produto",
                "x"
            ]
        ],
        "review": "Bom aparelho. Ainda descobrindo suas funcionalidades."
    },
    "10.006": {
        "opinions": [
            [
                "Eficiente e agil.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "Adorei.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Produto de muita boa qualidade.",
                "PRODUTO",
                "Produto",
                "+"
            ],
            [
                "Ate o momento nao tive problemas com o aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Adorei. Produto de muita boa qualidade, eficiente e agil. Ate o momento nao tive problemas com o aparelho."
    },
    "10.007": {
        "opinions": [
            [
                "otimo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "otimo. Excelente."
    },
    "10.008": {
        "opinions": [
            [
                "Satisfeito.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Meu 1° aparelho Foi o Motog-1 dai em tao Nao quis outra marca ... Por isso dei credibilidade Ao fabricante Motorola..Agora adiquiri o ( Motog-5 plus ) Aparelho sensacional Motorola esta de parabens TKS ....",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Satisfeito. Meu 1° aparelho Foi o Motog-1 dai em tao Nao quis outra marca ... Por isso dei credibilidade Ao fabricante Motorola..Agora adiquiri o ( Motog-5 plus Aparelho sensacional Motorola esta de parabens TKS ...."
    },
    "10.010": {
        "opinions": [
            [
                "Camera muito boa.",
                "CaMERA",
                "Camera",
                "+"
            ],
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Excelente. Camera muito boa."
    },
    "10.011": {
        "opinions": [
            [
                "Show de bola, era o que eu procurava.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Melhor da categoria.",
                "PRODUTO",
                "produto",
                "++"
            ]
        ],
        "review": "Melhor da categoria. Show de bola, era o que eu procurava."
    },
    "10.013": {
        "opinions": [
            [
                "Satisfeita.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Como foi comprado recentemente esta em avaliacao.",
                "PRODUTO",
                "produto",
                "x"
            ]
        ],
        "review": "Satisfeita. Como foi comprado recentemente esta em avaliacao."
    },
    "10.014": {
        "opinions": [
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Excelente. Excelente."
    },
    "10.015": {
        "opinions": [
            [
                "Elogio.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Gostei do produto, recomendo.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Elogio. Gostei do produto, recomendo."
    },
    "10.016": {
        "opinions": [
            [
                "Com destaques para sua camera, e o moto gestos!!!!",
                "CaMERA",
                "camera",
                "+"
            ],
            [
                "otimo custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Excelente. otimo custo-beneficio com destaque para sua camera, e o moto gestos!!!!"
    },
    "10.017": {
        "opinions": [
            [
                "util.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Satisfeita.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Satisfeita. util."
    },
    "10.018": {
        "opinions": [
            [
                "Muito bom!",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Moto g plus. Muito bom!"
    },
    "10.019": {
        "opinions": [
            [
                "Eu tava com Windows phone, entao percebi que Android e menos fluido, em alguns animacoes se percebe atraso, mas e bom.",
                "DESEMPENHO",
                "desempenho",
                "-."
            ],
            [
                "Uma coisa que falta e a funcao nativa da transmitir arquivos via Wi-Fi direct.",
                "OUTRO",
                "outro", #NAO SEI O QUE COLOCAR
                "-"
            ],
            [
                "Gostei.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Produto muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Produto muito bom. Gostei, eu tava com Windows phone, entao percebi que Android e menos fluido, em alguns animacoes se percebe atraso, mas e bom, uma coisa que falta e a funcao nativa da transmitir arquivos via Wi-Fi direct."
    },
    "10.020": {
        "opinions": [
            [
                "Boa durabilidade da bateria.",
                "BATERIA",
                "bateria",
                "+"
            ],
            [
                "Cameras perfeitas.",
                "CaMERA",
                "Cameras",
                "++"
            ],
            [
                "Celular top, muitos recursos.",
                "PRODUTO",
                "Celular",
                "+"
            ],
            [
                "Celular perfeito.",
                "PRODUTO",
                "Celular",
                "++"
            ]
        ],
        "review": "Celular perfeito. Celular top, muitos recursos. Boa durabilidade da bateria e cameras perfeitas."
    },
    "10.021": {
        "opinions": [
            [
                "A camera e alta qualidade.",
                "CaMERA",
                "camera",
                "+"
            ],
            [
                "Compensa!",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "O produto e muito bom e atende ao requerido.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "De facil manuseio.",
                "USABILIDADE",
                "manuseio",
                "+"
            ]
        ],
        "review": "Moto G. O produto e muito bom e atende ao requerido, de facil manuseio e a camera e alta qualidade. Compensa!"
    },
    "10.022": {
        "opinions": [
            [
                "Bateria com otima duracao.",
                "BATERIA",
                "Bateria",
                "+"
            ],
            [
                "Processador bom.",
                "DESEMPENHO",
                "Processador",
                "+"
            ],
            [
                "Design bonito.",
                "DESIGN",
                "Design",
                "+"
            ],
            [
                "Muito bom!!!",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Recomendo o produto.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Linha Moto G sempre bacana!",
                "PRODUTO",
                "Moto G",
                "+"
            ],
            [
                "Funcoes faceis de usar.",
                "USABILIDADE",
                "Funcoes",
                "+"
            ]
        ],
        "review": "Muito bom!!! Recomendo o produto. Design bonito, processador bom, bateria com otima duracao, funcoes faceis de usar. Linha Moto G sempre bacana!"
    },
    "10.023": {
        "opinions": [
            [
                "So acho que devem melhorar a qualidade da camera tanto traseira quanto frontal.",
                "CaMERA",
                "camera",
                "-"
            ],
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. So acho que devem melhorar a qualidade da camera tanto traseira quanto frontal."
    },
    "10.024": {
        "opinions": [
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Muito util.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito util. Muito bom."
    },
    "10.025": {
        "opinions": [
            [
                "Maravilhoso.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Vale a pena, nao nos deixa apontar um item negativo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Todos aqui em casa temos algum modelo da Motorola,mas o G5 plus e um passo à frente de todos os outros.",
                "PRODUTO",
                "G5 plus",
                "+"
            ]
        ],
        "review": "Maravilhoso. Todos aqui em casa temos algum modelo da Motorola,mas o G5 plus e um passo à frente de todos os outros. Vale a pena, nao nos deixa apontar um item negativo."
    },
    "10.026": {
        "opinions": [
            [
                "Destaque para a camera.",
                "CaMERA",
                "camera",
                "+"
            ],
            [
                "Destaque para o desempenho em jogos.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "Otimo custo beneficio.",
                "PRECO",
                "custo beneficio",
                "+"
            ]
        ],
        "review": "Otimo custo beneficio. Destaque para o desempenho em jogos e camera."
    },
    "10.027": {
        "opinions": [
            [
                "Fotos maravilhosas,.",
                "CAMERA",
                "camera",
                "+"
            ],
            [
                "Leve.",
                "PESO",
                "peso",
                "+"
            ],
            [
                "Custo-beneficio excelente.",
                "PRECO",
                "Custo-beneficio",
                "+"
            ],
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Otimo aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Facil de usar.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "Muito bom. otimo aparelho.Custo-beneficio excelente.Leve e facil de usar.Fotos maravilhosas,."
    },
    "10.028": {
        "opinions": [
            [
                "otimo custo-beneficio.",
                "PRECO",
                "custo-beneficio",
                "+"
            ],
            [
                "Smartphone com custo-beneficio muito bom.",
                "PRECO",
                "custo-beneficio",
                "+"
            ],
            [
                "Moderno.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Aparelhjo simples.",
                "PRODUTO",
                "Aparelhjo", #DUVIDA
                "."
            ]
        ],
        "review": "Smartphone com custo-beneficio muito bom. Aparelhjo simples, moderno e com otimo custo-beneficio."
    },
    "10.029": {
        "opinions": [
            [
                "Bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Produto muito facil de se utilizar.",
                "USABILIDADE",
                "Produto",
                "+"
            ]
        ],
        "review": "Bom. Produto muito facil de se utilizar."
    },
    "10.030": {
        "opinions": [
            [
                "Bateria que dura bastante.",
                "BATERIA",
                "Bateria",
                "+"
            ],
            [
                "Celular com um lindo design.",
                "DESIGN",
                "design",
                "+"
            ],
            [
                "Chegou bem rapido.",
                "EMPRESA",
                "empresa",
                "+"
            ],
            [
                "O preCo estava bom.",
                "PRECO",
                "preco",
                "+"
            ],
            [
                "Muitas funcoes.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Fiz uma otima compra.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente aparelho e tecnologia.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Excelente aparelho e tecnologia. Fiz uma otima compra, celular com um lindo design, muitas funcoes e bateria que dura bastante.O preco estava bom e chegou bem rapido."
    },
    "10.031": {
        "opinions": [
            [
                "Camera boa.",
                "CAMERA",
                "Camera",
                "+"
            ],
            [
                "Rapido.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "Se você fizer root (usuarios avancados) consegue usar o miracast, sem precisar comprar o chromecast qe custa uns 300 reais.",
                "OUTRO",
                "outro", # NAO FACO IDEIA
                "!"
            ],
            [
                "O unico ponto negativo por enquanto e que o android stock NaO PERMITE USAR MIRACAST (na TV smart), mesmo o telefone tendo essa opcao.",
                "OUTRO",
                "android stock",
                "-"
            ],
            [
                "Excelente custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "Funcionalidade boa.",
                "PRODUTO",
                "Funcionalidade",
                "+"
            ],
            [
                "Um celular excelente.",
                "PRODUTO",
                "celular",
                "+"
            ],
            [
                "Tirando alguns detalhes, o celular e excelente!",
                "PRODUTO",
                "celular",
                "+"
            ],
            [
                "A nitidez e imbativel (para ler textos por exemplo)",
                "TELA",
                "nitidez",
                "+"
            ],
            [
                "A tela nao tem o melhor contraste de cores (eu descobri que prefiro tela super AMOLED)",
                "TELA",
                "tela",
                "-"
            ],
            [
                "Tambem percebi um bug que quando se carrega o celular, dependendo da capa de protecao nao da pra usar a tela touch (a voltagem interfere na deteccao dos toques)",
                "TELA",
                "tela",
                "-"
            ]
        ],
        "review": "Excelente custo-beneficio. Um celular excelente, rapido, camera boa e funcionalidade boa. A tela nao tem o melhor contraste de cores (eu descobri que prefiro tela super AMOLED), mas a nitidez e imbativel (para ler textos por exemplo O unico ponto negativo por enquanto e que o android stock NaO PERMITE USAR MIRACAST (na TV smart, mesmo o telefone tendo essa opcao. Se você fizer root (usuarios avancados consegue usar o miracast, sem precisar comprar o chromecast qe custa uns 300 reais. Tambem percebi um bug que quando se carrega o celular, dependendo da capa de protecao nao da pra usar a tela touch (a voltagem interfere na deteccao dos toques Tirando esses detalhes, o celular e excelente!"
    },
    "10.032": {
        "opinions": [
            [
                "Tudo bem, mas uma das maiores vantagens do aparelho que e vir com o Android sem muitas modificacoes, acaba se tornando uma fraqueza, pq ele nao tem a funcao compartilhar via Wi-Fi direct nativa, e preciso baixar apps que facam isso, e ate agora nao achei um com sem anuncios.",
                "OUTRO",
                "Android",
                "-"
            ],
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. Tudo bem, mas uma das maiores vantagens do aparelho que e vir com o Android sem muitas modificacoes, acaba se tornando uma fraqueza, pq ele nao tem a funcao compartilhar via Wi-Fi direct nativa, e preciso baixar apps que facam isso, e ate agora nao achei um com sem anuncios."
    },
    "10.033": {
        "opinions": [
            [
                "otimo!",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Moto G5plus. otimo!"
    },
    "10.034": {
        "opinions": [
            [
                "Excelente aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "otimo smartphone, reune os melhores atributos de um aparelho premium.",
                "PRODUTO",
                "smartphone",
                "+"
            ]
        ],
        "review": "Excelente aparelho. otimo smartphone, reune os melhores atributos de um aparelho premium."
    },
    "10.035": {
        "opinions": [
            [
                "otimo aparelho, esta entre os melhores smartphones da linha mediana da atualidad.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Facil de usar e com varios recurso que sao encontrados na linha premium.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "otimo aparelho, esta entre os melhores smartphones da linha mediana da atualidad. Facil de usar e com varios recurso que sao encontrados na linha premium."
    },
    "10.036": {
        "opinions": [
            [
                "Bonito.",
                "DESIGN",
                "design",
                "+"
            ],
            [
                "Preco honesto.",
                "PREcO",
                "Preco",
                "+"
            ],
            [
                "otimo custo/beneficio.",
                "PREcO",
                "custo/beneficio",
                "+"
            ],
            [
                "Bom hardware.",
                "PRODUTO",
                "hardware",
                "+"
            ],
            [
                "Enfim, cumpre o que promete.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "otimo aparelho intermediario.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "otimo aparelho intermediario. Bonito, bom hardware, preco honesto, enfim, cumpre o que promete, otimo custo/beneficio."
    },
    "10.037": {
        "opinions": [
            [
                "Nao tive nenhum a queixa da entrega, obrigada Kabum pela entrega no prazo.",
                "EMPRESA",
                "Kabum", #nota
                "+"
            ],
            [
                "Produto bom.",
                "PRODUTO",
                "Produto",
                "+"
            ],
            [
                "Produto excelente.",
                "PRODUTO",
                "Produto",
                "+"
            ],
            [
                "Facil mexer, ate o momento nao tenho queixas.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "Produto excelente. Produto bom, facil mexer, ate o momento nao tenho queixas. Nao tive nenhum a queixa da entrega, obrigada Kabum pela entrega no prazo."
    },
    "10.038": {
        "opinions": [
            [
                "Muito superior ao esperado pelo preco.",
                "PREcO",
                "preco",
                "+"
            ],
            [
                "otimo produto.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "otima recepcao e imagens Recomendo!!!!",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "otimo produto. Muito superior ao esperado pelo preco. otima recepcao e imagens Recomendo!!!!"
    },
    "10.039": {
        "opinions": [
            [
                "Para que pagar mais se pode ter quase o mesmo por menos.",
                "PREcO",
                "preco",
                "+"
            ],
            [
                "otimo Celular.",
                "PRODUTO",
                "Celular",
                "+"
            ],
            [
                "Aparelho muito bom, me atende no que preciso no dia a dia.",
                "PRODUTO",
                "Aparelho",
                "+"
            ]
        ],
        "review": "otimo Celular. Aparelho muito bom, me atende no que preciso no dia a dia, para que pagar mais se pode ter quase o mesmo por menos."
    },
    "10.040": {
        "opinions": [
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente produto.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Excelente produto. Muito bom."
    },
    "10.041": {
        "opinions": [
            [
                "Mto barato e de qualidade.",
                "PREcO",
                "preco",
                "+"
            ],
            [
                "Impecavel.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Impecavel. Mto barato e de qualidade."
    },
    "10.042": {
        "opinions": [
            [
                "Aparelho e bem rapido.",
                "DESEMPENHO",
                "Aparelho",
                "+"
            ],
            [
                "Os gestos ajudam bastante no dia a dia.",
                "OUTRO",
                "gestos",
                "+"
            ],
            [
                "E o leitor de digitais da uma seguranca a mais.",
                "OUTRO",
                "leitor de digitais",
                "+"
            ],
            [
                "Bom, mas poderia ter versao de 3gb.",
                "PRODUTO",
                "produto",
                "+."
            ]
        ],
        "review": "Bom, mas poderia ter versao de 3gb. Os gestos ajudam bastante no dia a dia, e o aparelho e bem rapido, e o leitor de digitais da uma seguranca a mais."
    },
    "10.043": {
        "opinions": [
            [
                "A memoria ram poderia ser 3gb.",
                "ARMAZENAMENTO",
                "memoria ram",
                "-"
            ],
            [
                "Estou muito satisfeito com o desempenho.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "otimo atendeu minhas expectativas.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "otimo atendeu minhas expectativas. Estou muito satisfeito com o desempenho, contudo a memoria ram poderia ser 3g."
    },
    "10.044": {
        "opinions": [
            [
                "Gostei muito a bateria dura bastante,!!",
                "BATERIA",
                "bateria",
                "+"
            ],
            [
                "As funcoes da camera podia ser melhor, nao tem embeleze , como assim? e nao tem, triste!!",
                "CaMERA",
                "camera",
                "-"
            ],
            [
                "E o sinal da tv, e enfeite ja rodei , todos os lugares que vou nao pega, tenho outro aparelho da concorrência e pega normalmente!!",
                "OUTRO",
                "sinal da tv",
                "-"
            ],
            [
                "MAravilhoso.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "MAravilhoso. Gostei muito a bateria dura bastante,!! as funcoes da camera podia ser melhor, nao tem embeleze , como assim? e nao tem, triste!! e o sinal da tv, e enfeite ja rodei , todos os lugares que vou nao pega, tenho outro aparelho da concorrência e pega normalmente!!"
    },
    "10.045": {
        "opinions": [ # COMO LIDA COM REPETICAO?
            [
                "otimo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Muito bom, tamanho ideal.",
                "TAMANHO",
                "tamanho",
                "+"
            ]
        ],
        "review": "otimo. Muito bom, tamanho ideal."
    },
    "10.047": {
        "opinions": [
            [
                "otima relacao custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ]
        ],
        "review": "otima relacao custo-beneficio. otima relacao custo-beneficio."
    },
    "10.048": {
        "opinions": [
            [
                "Celular barato!",
                "PREcO",
                "Celular",
                "+"
            ],
            [
                "Comparado com outras marcas, atualmente achei que este celular tem o melhor custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "++"
            ],
            [
                "Celular bom.",
                "PRODUTO",
                "Celular",
                "+"
            ],
            [
                "Eu possuia um Samsung S5 mas ele parou de funcionar de repente, este motorola G5 e melhor que o S5 em diversas areas.",
                "PRODUTO",
                "motorola G5",
                "+"
            ]
        ],
        "review": "Celular bom e barato! Comparado com outras marcas, atualmente achei que este celular tem o melhor custo-beneficio. Eu possuia um Samsung S5 mas ele parou de funcionar de repente, este motorola G5 e melhor que o S5 em diversas areas."
    },
    "10.049": {
        "opinions": [
            [
                "unico detalhe contra e que nao aceita cartao de memoria.",
                "ARMAZENAMENTO",
                "cartao de memoria",
                "-"
            ],
            [
                "otimo aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Entao e tudo de bom, cinco estrelas.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Na realiza eu comprei para o meu filho, segundo ele, o aparelho e otimo, atende quase todas às necessidades.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "otimo aparelho. Na realiza eu comprei para o meu filho, segundo ele, o aparelho e otimo, atende quase todas às necessidades, unico detalhe contra e que nao acita cartao de memoria entao e tudo de bom, cinco estrelas."
    },
    "10.050": {
        "opinions": [
            [
                "otimo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Estou muito satisfeito com o aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "otimo. Na verdade, por enquanto e pequena, pois tenho o celular ha menos de um mês. Mas estou muito satisfeito com o aparelho."
    },
    "10.051": {
        "opinions": [
            [
                "e um produto com uma otima qualidade.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Recomendo a todos que procuram um produto com alta performance, ampla opcao de caracteres, pratico e otima qualidade, compre esse smartphone.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Praticidade e qualidade.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ],
            [
                "Oferece uma praticidade muito elevada tanto em termos de uso como em caracteres de opcoes.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "Praticidade e qualidade. e um produto com uma otima qualidade, oferece uma praticidade muito elevada tanto em termos de uso como em caracteres de opcoes. Por esses e outros motivos recomendo a todos que procuram um produto com alta performance, ampla opcao de caracteres, pratico e otima qualidade, compre esse smartphofe."
    },
    "10.052": {
        "opinions": [
            [
                "Otima.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. Otima."
    },
    "10.053": {
        "opinions": [
            [
                "Otima camera.",
                "CaMERA",
                "camera",
                "+"
            ],
            [
                "Otimo desempenho.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "Otimo custo beneficio.",
                "PREcO",
                "custo beneficio",
                "+"
            ],
            [
                "Excelente aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "So o software que poderia ter alguns recursos de fabrica a mais, como gravador de voz e ligacoes.",
                "SISTEMA",
                "software",
                "-"
            ]
        ],
        "review": "Otimo custo beneficio. Excelente aparelo. Otimo desempenho e camera. So o software que poderia ter alguns recursos de fabrica a mais, como gravador de voz e ligacoes."
    },
    "10.054": {
        "opinions": [
            [
                "So a camera nao e tudo aquilo que e anunciado me decepcionou.",
                "CaMERA",
                "camera",
                "-"
            ],
            [
                "Gostei.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Aparelho muito bom.",
                "PRODUTO",
                "Aparelho",
                "+"
            ],
            [
                "Android e bom despacha bem rapido.",
                "SISTEMA",
                "Android",
                "+"
            ]
        ],
        "review": "Gostei. Aparelho muito bom androide e bom despacha bem rapido , so a camera nao e tudo aquilo que e anunciado me decepcionou."
    },
    "10.055": {
        "opinions": [
            [
                "Tem bom preco.",
                "PREcO",
                "preco",
                "+"
            ],
            [
                "Cumpre o que promete.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Bom produto, funciona bem.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Cumpre o que promete. Bom produto, funciona bem, tem bom preco e cumpre o que promete."
    },
    "10.056": {
        "opinions": [
            [
                "Celular excelente!",
                "PRODUTO",
                "Celular",
                "+"
            ]
        ],
        "review": "Moto G5 Plus. Celular excelente!"
    },
    "10.057": {
        "opinions": [
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Estou gostando.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. Estou gostando."
    },
    "10.058": {
        "opinions": [
            [
                "Foco, camera nitidas.",
                "CaMERA",
                "camera",
                "+"
            ],
            [
                "Designer moderno.",
                "DESIGN",
                "Designer",
                "+"
            ],
            [
                "Preco bom.",
                "PREcO",
                "Preco",
                "+"
            ],
            [
                "Recomendo!",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente Aparelho! Recomendo!",
                "PRODUTO",
                "Aparelho",
                "+"
            ],
            [
                "Um smartphone com excelentes caracteristicas.",
                "PRODUTO",
                "smartphone",
                "+"
            ],
            [
                "Tenho usado o aparelho desde da 2ª geracao, gosto do produto e da marca Motorola/Lenovo, por isso recomendo a todos e principalmente aos meus amigos e familiares.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "E a durabilidade tambem excelente.",
                "RESISTÊNCIA",
                "durabilidade",
                "+"
            ],
            [
                "Facil de usar.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "Excelente Aparelho! Recomendo! Tenho usado o aparelho desde da 2ª geracao, gosto do produto e da marca Motorola/Lenovo, por isso recomendo a todos e principalmente aos meus amigos e familiares. Um smartphone com excelentes caracteristicas, designer moderno, preco bom, facil de usar, foco, camera nitidas e a durabilidade tambem excelente.Recomendo!"
    },
    "10.059": {
        "opinions": [
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Excelente."
    },
    "10.060": {
        "opinions": [
            [
                "Muito bom aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Foi presente, mas o presenteado elogiou bastante.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom aparelho. Foi presente, mas o presenteado elogiou bastante."
    },
    "10.061": {
        "opinions": [
            [
                "otimo custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "Um dos melhores intermediarios.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "otimo custo-beneficio. Um dos melhores intermediarios."
    },
    "10.062": {
        "opinions": [
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Atende todas as minha necessidades .",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. Atende todas as minha necessidades ."
    },
    "10.063": {
        "opinions": [
            [
                "Camera e bem rapida e de boa qualidade.",
                "CaMERA",
                "Camera",
                "+"
            ],
            [
                "Estava usando o Chrome que veio instalado e nao sei porque estava travando muito o Celular, instalei o Firefox acabou o problema.",
                "DESEMPENHO",
                "Chrome", #DUVIDA
                "-."
            ],
            [
                "O sensor digital e muito bem vindo, pois facilita o acesso ao Celular e ate alguns aplicativo de bancos.",
                "OUTRO",
                "sensor digital",
                "+"
            ],
            [
                "Recomendo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Satisfeito.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Foi meu primeiro Moto que tenho, ate o momento estou satisfeito.",
                "PRODUTO",
                "Moto", #DUVIDA
                "+"
            ]
        ],
        "review": "Satisfeito. Foi meu primeiro Moto que tenho, ate o momento estou satisfeito.O sensor digital e muito bem vindo,pois facilita o acesso ao Celular e ate alguns aplicativo de bancos.Estava usando o Crome que veio instalado e nao sei porque estava travando muito o Celular,instalei o Firefox acabou o problema.Camera e bem rapida e de boa qualidade.Recomendo."
    },
    "10.064": {
        "opinions": [
            [
                "Excelente custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "Produto bom.",
                "PRODUTO",
                "Produto",
                "+"
            ]
        ],
        "review": "Produto bom. Excelente custo-beneficio."
    },
    "10.065": {
        "opinions": [
            [
                "Bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Memoria. Bom."
    },
    "10.066": {
        "opinions": [
            [
                "Satisfeito com a compra.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Era o eu esperava com a compra.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Satisfeito com a compra. Era o eu esperava com a compra."
    },
    "10.067": {
        "opinions": [
            [
                "Ponto fraco para design.",
                "DESIGN",
                "design",
                "-"
            ],
            [
                "otimo custo-benificio.",
                "PREcO",
                "custo-benificio",
                "+"
            ],
            [
                "As partes em plastico o tornam fragil.",
                "RESISTÊNCIA",
                "plastico", #DUVIDA
                "-"
            ],
            [
                "Vale a pena principalmente pelo Android puro.",
                "SISTEMA",
                "Android",
                "+"
            ],
            [
                "Ponto fraco por possuir apenas um alto-falante.",
                "SOM",
                "alto-falante",
                "-"
            ],
            [
                "Vale a pena principalmente pelas Moto Acoes que facilitam a usabilidade.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "otimo custo-benificio. Vale a pena principalmente pelo Android puro e pelas Moto Acoes que facilitam a usabilidade.Ponto fraco por possuir apenas um alto-falante e para design, as partes em plastico o tornam fragil."
    },
    "10.068": {
        "opinions": [
            [
                "Muito bommmm.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Facilita a vida de quem vive na tecnologia.",
                "PRODUTO",
                "produto",
                "+."
            ]
        ],
        "review": "Muito bommmm. Facilita a vida de quem vive na tecnologia."
    },
    "10.069": {
        "opinions": [
            [
                "Com preco bom.",
                "PREcO",
                "preco",
                "+"
            ],
            [
                "otimo produto.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "otimo aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "E qualidade melhor ainda.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "otimo produto. otimo aparelho, com preco bom e qualidade melhora ainda."
    },
    "10.070": {
        "opinions": [
            [
                "Elogio.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Faz pouco tempo de uso mas parece um bom aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Elogio. Faz pouco tempo de uso mas parece um bom aparelho."
    },
    "10.071": {
        "opinions": [
            [
                "Otimo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Otimo. Excelente."
    },
    "10.073": {
        "opinions": [
            [
                "Barato.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Barato. Excelente."
    },
    "10.074": {
        "opinions": [
            [
                "Entrega rapida.",
                "EMPRESA",
                "empresa", #DUVIDA
                "+"
            ],
            [
                "E ate entao estou gostando muito do aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Bom aparelho, atende na maioria dos requisitos!",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Bom aparelho, atende na maioria dos requisitos! Entrega rapida e ate entao estou gostando muito do aparelho."
    },
    "10.075": {
        "opinions": [
            [
                "Muito rapido.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "O melhor aparelho que tive ate hoje.",
                "PRODUTO",
                "aparelho",
                "++"
            ]
        ],
        "review": "Muito rapido. O melhor aparelho que tive ate hoje."
    },
    "10.076": {
        "opinions": [
            [
                "Camera muito boa.",
                "CaMERA",
                "Camera",
                "+"
            ],
            [
                "Excelente!",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Excelente aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Celular top de linha.",
                "PRODUTO",
                "Celular",
                "+"
            ]
        ],
        "review": "Excelente! Celular top de linha, camera muito boa, excelente aparelho."
    },
    "10.077": {
        "opinions": [
            [
                "Show.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Show. Muito bom."
    },
    "10.078": {
        "opinions": [
            [
                "Bateria que dura bastante.",
                "BATERIA",
                "Bateria",
                "+"
            ],
            [
                "Processamento muito rapido.",
                "DESEMPENHO",
                "Processamento",
                "+"
            ],
            [
                "Bonito.",
                "DESIGN",
                "design",
                "+"
            ],
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Recomendo compra.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "O celular atendeu plenamente minhas expectativas.",
                "PRODUTO",
                "celular",
                "+"
            ],
            [
                "Pesquisei muito antes de comprar e nao me arrependi.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Facil de usar.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "Excelente. O celular atendeu plenamente minhas expectativas. Pesquisei muito antes de comprar e nao me arrependi. Facil de usar, bonito, processamento muito rapido e bateria que dura bastante. Recomendo compra."
    },
    "10.079": {
        "opinions": [
            [
                "Bom aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Atendeu as expectativas.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Bom aparelho. Atendeu as expectativas."
    },
    "10.080": {
        "opinions": [
            [
                "Apenas nao gostei muito da camera, mas quando ao restante estou satisfeita!",
                "CaMERA",
                "camera",
                "-"
            ],
            [
                "Tendo em vista seu custo, vale muito a pena...",
                "PREcO",
                "custo",
                "+"
            ],
            [
                "Satisfeita.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Satisfeita. Tendo em vista seu custo, vale muito a pena...apenas nao gostei muito da camera, mas quando ao restante estou satisfeita!"
    },
    "10.081": {
        "opinions": [
            [
                "Tudo certo em relacao à loja, que foi rapida e me atendeu prontamente quando tive duvidas.",
                "EMPRESA",
                "loja",
                "+"
            ],
            [
                "Celular com otimo custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "Produto muito bom, atendendo as expectativas da marca Moto.",
                "PRODUTO",
                "Produto",
                "+"
            ]
        ],
        "review": "Celular com otimo custo-beneficio. Tudo certo em relacao à loja, que foi rapida e me atendeu prontamente quando tive duvidas, produto muito bom, atendendo as expectativas da marca Moto."
    },
    "10.082": {
        "opinions": [
            [
                "Bom custo beneficio.",
                "PREcO",
                "custo beneficio",
                "+"
            ],
            [
                "e um bom custo beneficio.",
                "PREcO",
                "custo beneficio",
                "+"
            ],
            [
                "Vale a pena a compra no segmento de intermediarios.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Bom custo beneficio. e um bom custo beneficio. Vale a pena a compra no segmento de intermediarios."
    },
    "10.083": {
        "opinions": [
            [
                "Um bom produto.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "e um produto bom mas nao contemplou as minhas expectativas.",
                "PRODUTO",
                "produto",
                "+."
            ]
        ],
        "review": "Um bom produto. e um produto bom mas nao contemplou as minhas expectativas."
    },
    "10.084": {
        "opinions": [
            [
                "Alem do desing maravilhoso e otimo acabamento.",
                "DESIGN",
                "design",
                "+"
            ],
            [
                "Cumpre o que promete com um otimo custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "Cumpre o que promete.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Cumpre o que promete. Cumpre o que promete com um otimo custo-beneficio, alem do desing maravilhoso e otimo acabamento."
    },
    "10.085": {
        "opinions": [
            [
                "otima memoria.",
                "ARMAZENAMENTO",
                "memoria",
                "+"
            ],
            [
                "Muito bom desempenho.",
                "DESEMPENHO",
                "desempenho",
                "+"
            ],
            [
                "otimo custo-beneficio.",
                "PREcO",
                "custo-beneficio",
                "+"
            ],
            [
                "otimo Smartphone.",
                "PRODUTO",
                "Smartphone",
                "+"
            ],
            [
                "Este Smartphone superou a minha expectativa. Nao e tao caro quanto os tops de linha, mas atende muito bem a minha necessidade.",
                "PRODUTO",
                "Smartphone",
                "+"
            ]
        ],
        "review": "otimo Smartphone. Este Smartphone superou a minha expectativa. Nao e tao caro quanto os tops de linha, mas atende muito bem a minha necessidade. otima memoria, muito bom desempenho. otimo custo-beneficio."
    },
    "10.086": {
        "opinions": [
            [
                "Sua camera e ok para os demais do mercado.",
                "CaMERA",
                "camera",
                "+."
            ],
            [
                "Seu processador consegue rodar todos os aplicativos-jogos que eu utilizava antes e ate os atuais.",
                "DESEMPENHO",
                "processador",
                "+"
            ],
            [
                "A ENTREGA FOI RaPIDA E MUITO BOA.",
                "EMPRESA",
                "entrega",
                "+"
            ],
            [
                "Produto de um ALTO custo beneficio.",
                "PREcO",
                "custo beneficio",
                "+"
            ],
            [
                "Tem um preco otimo portanto nao me arrependi.",
                "PREcO",
                "preco",
                "+"
            ],
            [
                "O celular embora seja lancamento e barato consegue bater de frente com a maioria dos celulares atuais e mais utilizados (2016-2017)",
                "PRODUTO",
                "celular",
                "+"
            ],
            [
                "Nao tive nenhum problema por enquanto.",
                "PRODUTO",
                "produto",
                "+."
            ]
        ],
        "review": "Produto de um ALTO custo beneficio. O celular embora seja lancamento e barato consegue bater de frente com a maioria dos celulares atuais e mais utilizados (2016-2017 Sua camera e ok para os demais do mercado e seu processador consegue rodar todos os aplicativos-jogos que eu utilizava antes e ate os atuais portanto tem um preco otimo portanto nao me arrependi e nao tive nenhum problema por enquanto. A ENTREGA FOI RaPIDA E MUITO BOA."
    },
    "10.087": {
        "opinions": [
            [
                "Intermediario de ponta.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Ate que e facil de manusear e encontrar as customizacoes.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "Intermediario de ponta. Ate que e facil de manusear e encontrar as customizacoes."
    },
    "10.088": {
        "opinions": [
            [
                "O produto atende as expectativas que eu esperava encontrar.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Facil manuseio.",
                "USABILIDADE",
                "usabilidade",
                "+"
            ]
        ],
        "review": "O produto atende as expectativas que eu esperava encontrar. Facil manuseio."
    },
    "10.089": {
        "opinions": [
            [
                "Muito bom o produto, otimo custo beneficio.",
                "PREcO",
                "custo beneficio",
                "+"
            ],
            [
                "Estou usando ainda, mas e muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom o produto, otimo custo beneficio. Estou usando ainda, mas e muito bom."
    },
    "10.090": {
        "opinions": [
            [
                "Bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Ainda pouco tempo de uso.",
                "PRODUTO",
                "produto",
                "x"
            ]
        ],
        "review": "Bom. Ainda pouco tempo de uso."
    },
    "10.091": {
        "opinions": [
            [
                "otimo custo beneficio.",
                "PREcO",
                "custo beneficio",
                "+"
            ],
            [
                "Boas configuracoes por um preco razoavel.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "otimo custo beneficio. Boas configuracoes por um preco razoavel."
    },
    "10.092": {
        "opinions": [
            [
                "Produto muito bom.",
                "PRODUTO",
                "Produto",
                "+"
            ],
            [
                "Produto excelente para qualquer ambiente.",
                "PRODUTO",
                "Produto",
                "+"
            ]
        ],
        "review": "Produto muito bom. Produto excelente para qualquer ambiente."
    },
    "10.093": {
        "opinions": [
            [
                "Boa velocidade.",
                "DESEMPENHO",
                "velocidade",
                "+"
            ],
            [
                "Bonito.",
                "DESIGN",
                "design",
                "+"
            ],
            [
                "Leve.",
                "PESO",
                "peso",
                "+"
            ],
            [
                "Muito bom!",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "otimo produto!",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom! Boa velocidad.e. Bonito e leve. otimo produto!"
    },
    "10.094": {
        "opinions": [
            [
                "Com 32GB de armazenamento que e o suficiente para usar sem problemas futuros.",
                "ARMAZENAMENTO",
                "armazenamento",
                "+"
            ],
            [
                "A memoria RAM de 2GB da conta de realizar varias tarefas ao mesmo tempo sem travar.",
                "ARMAZENAMENTO",
                "memoria RAM",
                "+"
            ],
            [
                "A duracao da bateria que poderia ser melhor.",
                "BATERIA",
                "bateria",
                "-"
            ],
            [
                "A camera melhorou bastante em relacao as versoes anteriores do Moto G.",
                "CaMERA",
                "camera",
                "+"
            ],
            [
                "O design que poderia ser melhor.",
                "DESIGN",
                "design",
                "-"
            ],
            [
                "e um excelente aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ],
            [
                "Atende o basico em um smartphone.",
                "PRODUTO",
                "smartphone",
                "+."
            ],
            [
                "Em resumo: perfeito para uso intermediario no dia a dia.",
                "PRODUTO",
                "produto",
                "+."
            ],
            [
                "Ja vem com Android 7.",
                "SISTEMA",
                "Android 7",
                "+"
            ]
        ],
        "review": "Atende o basico em um smartphone. e um excelente aparelho, ja vem com Android 7 e com 32GB de armazenamento que e o suficiente para usar sem problemas futuros. A memoria RAM de 2GB da conta de realizar varias tarefas ao mesmo tempo sem travar e a camera melhorou bastante em relacao as versoes anteriores do Moto G. Em resumo: perfeito para uso intermediario no dia a dia. So a duracao da bateria e o design que poderiam ser melhores."
    },
    "10.095": {
        "opinions": [
            [
                "Positiva.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Extremamente satisfeito.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Positiva. Extremamente satisfeito."
    },
    "10.096": {
        "opinions": [
            [
                "Apenas comecou a esquentar do nada, Resetei e nunca mais esquentou.",
                "DESEMPENHO",
                "desempenho",
                ".."
            ],
            [
                "Muito bom aparelho.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "Moto g 5 Plus. Muito bom aparelho, apenas comecou a esquentar do nada, Resetei e nunca mais esquentou."
    },
    "10.097": {
        "opinions": [
            [
                "Satisfeitissimo.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Sou fa da marca.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Sempre inovando e como sempre, Android puro.",
                "SISTEMA",
                "Android",
                "+"
            ]
        ],
        "review": "Satisfeitissimo. Sou fa da marca. Sempre inovando e como sempre, Androide puro."
    },
    "10.098": {
        "opinions": [
            [
                "Ja disponho de aparelhos semelhantes da Motorola (Moto Xplay). Achei o Moto G5 um pouco mais lento e ocasionalmente trava e reinicia sozinho.",
                "DESEMPENHO",
                "desempenho",
                "-"
            ],
            [
                "Bom celular pelo custo.",
                "PREcO",
                "celular",
                "+"
            ]
        ],
        "review": "Bom celular pelo custo. Ja disponho de aparelhos semelhantes da Motorola (Moto Xplay Achei o Moto G5 um pouco mais lento e ocasionalmente trava e reinicia sozinho."
    },
    "10.099": {
        "opinions": [
            [
                "Quando no wi fi a navegacao e bem rapida, no 4G nem tanto.",
                "OUTRO",
                "navegacao",
                "+"
            ],
            [
                "Nao tem a opcao de excluir uma unica ligacao feita ou recebida.",
                "OUTRO",
                "ligacao",
                "-"
            ],
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. Quando no wi fi a navegacao e bem rapida, no 4G nem tanto. Nao tem a opcao de excluir uma unica ligacao feita ou recebida."
    },
    "10.100": {
        "opinions": [
            [
                "Produto de boa qualidade.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Como e um produto que adquiri a pouco tempo, ate o momento nao me deu problermas.",
                "RESISTÊNCIA",
                "resistência",
                "+."
            ]
        ],
        "review": "Produto de boa qualidade. Como e um produto que adquiri a pouco tempo, ate o momento nao me deu problermas."
    },
    "10.101": {
        "opinions": [
            [
                "Muito bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Ate o momento atende as minhas expectativas.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito bom. Ate o momento atende as minhas expectativas."
    },
    "10.102": {
        "opinions": [
            [
                "QUALIDADE.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "APARELHO DE oTIMA QUALIDADE.",
                "PRODUTO",
                "aparelho",
                "+"
            ]
        ],
        "review": "QUALIDADE. APARELHO DE oTIMA QUALIDADE."
    },
    "10.103": {
        "opinions": [
            [
                "Muito Bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Gostei bastante do produto.",
                "PRODUTO",
                "produto",
                "+"
            ]
        ],
        "review": "Muito Bom. Gostei bastante do produto."
    },
    "10.104": {
        "opinions": [
            [
                "Excelente.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "Produto otimo.",
                "PRODUTO",
                "Produto",
                "+"
            ]
        ],
        "review": "Excelente. Produto otimo."
    },
    "10.105": {
        "opinions": [
            [
                "Bateria dura pouco.",
                "BATERIA",
                "Bateria",
                "-"
            ],
            [
                "E a camera deixa bastante a desejar.",
                "CaMERA",
                "camera",
                "-"
            ],
            [
                "Ate que e bom.",
                "PRODUTO",
                "produto",
                "+"
            ],
            [
                "O celular e bom.",
                "PRODUTO",
                "celular",
                "+"
            ]
        ],
        "review": "Ate que e bom. O celular e bom, mas bateria dura pouco e a camera deixa bastante a desejar."
    },
    "10.106": {
        "opinions": [
            [
                "COMO VOU SABER, SE NaO RECEBI.",
                "EMPRESA",
                "empresa",
                "-"
            ],
            [
                "NaO RECEBI O PRODUTO A MAIS DE 30 DIAS.",
                "EMPRESA",
                "empresa",
                "-"
            ],
            [
                "COM A LOJA ESTa ALeM DA PIOR POSSiVEL.",
                "EMPRESA",
                "loja",
                "--"
            ]
        ],
        "review": "NaO RECEBI O PRODUTO A MAIS DE 30 DIAS. COMO VOU SABER, SE NaO RECEBI. COM A LOJA ESTa ALeM DA PIOR POSSiVEL."
    },
    "10.107": {
        "opinions": [
            [
                "Bom custo/beneficio.",
                "PREcO",
                "custo/beneficio",
                "+"
            ],
            [
                "Gostei do celular.",
                "PRODUTO",
                "celular",
                "+"
            ]
        ],
        "review": "Bom custo/beneficio. Gostei do celular."
    },
    "10.109": {
        "opinions": [
            [
                "A bateria nao esta durando muito.",
                "BATERIA",
                "bateria",
                "-"
            ],
            [
                "Algumas vezes o aparelho esquenta muito, mesmo estando com o Display apagado.",
                "DESEMPENHO",
                "desempenho",
                "-"
            ],
            [
                "Duas semanas de uso e tudo bem.",
                "RESISTÊNCIA",
                "resistência",
                "+."
            ]
        ],
        "review": "Moto G5 Plus. Duas semanas de uso e tudo bem, a bateria nao esta durando muito e algumas vezes o aparelho esquenta muito,, mesmo estando com o Display apagado."
    },
    "10.110": {
        "opinions": [
            [
                "Diferente.",
                "PRODUTO",
                "produto",
                "."
            ],
            [
                "Ainda estou avaliando.",
                "PRODUTO",
                "produto",
                "x"
            ]
        ],
        "review": "Diferente. Ainda estou avaliando."
    }
    # "10.111": {
    #     "opinions": [
    #         [
    #             "Seu desempenho e excelente, principalmente pelo seu valor.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Seu valor poderia ser um pouco menor.",
    #             "PREcO",
    #             "-"
    #         ],
    #         [
    #             "Bom telefone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O aparelho e show.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom telefone. O aparelho é show.se desempenho é excelente, principalmente pelo seu valor, porém ele poderia ser um pouco menor."
    # },
    # "10.112": {
    #     "opinions": [
    #         [
    #             "Creio que para usuarios mais exigentes nao compensaria.",
    #             "PRODUTO",
    #             "-."
    #         ],
    #         [
    #             "Razoavel.",
    #             "PRODUTO",
    #             "."
    #         ],
    #         [
    #             "É um aparelho regular.",
    #             "PRODUTO",
    #             "."
    #         ],
    #         [
    #             "A camera com uma saliência grande requer cuidados para nao danificar.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Razoavel. É um aparelho regular. Creio que para usuarios mais exigentes nao compensaria. A camera com uma saliência grande requer cuidados para nao danificar."
    # },
    # "10.113": {
    #     "opinions": [
    #         [
    #             "Adorei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom o manuseio, configuracao otima.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Adorei. Muito bom o manuseio, configuracao otima."
    # },
    # "10.114": {
    #     "opinions": [
    #         [
    #             "Satisfeito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Cumpre o que promete.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Satisfeito. Cumpre o que promete."
    # },
    # "10.115": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gosto muito dos moto g e este supera minhas expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Exelente. Gosto muito dos moto g e este supera minhas expectativas."
    # },
    # "10.116": {
    #     "opinions": [
    #         [
    #             "Deixa a desejar na bateria.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Deixa a desejar no designer.",
    #             "DESIGN",
    #             "-"
    #         ],
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Muito bom deixa a desejar so a bateria e designer."
    # },
    # "10.117": {
    #     "opinions": [
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "COMPRARIA COM CERTEZA.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. COMPRARIA COM CERTEZA."
    # },
    # "10.118": {
    #     "opinions": [
    #         [
    #             "oTIMO.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adorei, atendeu minhas necessidades.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "oTIMO. Adorei, atendeu minhas necessidades."
    # },
    # "10.119": {
    #     "opinions": [
    #         [
    #             "SATISFAcaO.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O PRODUTO É MUITO BOM E FUNCIONA PERFEITAMENTE.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "SATISFAcaO. O PRODUTO É MUITO BOM E FUNCIONA PERFEITAMENTE."
    # },
    # "10.120": {
    #     "opinions": [
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Perfeito.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Perfeito. Bom produto."
    # },
    # "10.121": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Satisfeito com a aquisicao.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Satisfeito com a aquisicao."
    # },
    # "10.122": {
    #     "opinions": [
    #         [
    #             "A bateria dura mais de 1 dia, isso usando com frequência!",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Super rapido, nao trava, processador muito bom!",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Ele é lindo!",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Maravilhoso!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tô apaixonada por ele, melhor celular!",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Maravilhoso! Ele é lindo! Super rapido, não trava, processador muito bom! A bateria dura mais de 1 dia, isso usando com frequência! Tô apaixonada por ele, melhor celular!"
    # },
    # "10.123": {
    #     "opinions": [
    #         [
    #             "A memoria é muito boa.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "A bateria chega a durar 48 horas.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "A resolucão da camera é perfeita.",
    #             "CaMERA",
    #             "++"
    #         ],
    #         [
    #             "O audio é muito bom.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "otimo celular.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "otimo celular. A resolucão da camera é perfeita, o audio é muito bom. A memoria é muito boa e a bateria chega a durar 48 horas."
    # },
    # "10.124": {
    #     "opinions": [
    #         [
    #             "Dura bastante tempo.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Gostei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Gostei. Bateria. Dura bastane tempo."
    # },
    # "10.125": {
    #     "opinions": [
    #         [
    #             "Ele tem mais precisão e o reconhecimento digital e bem superior ao G4plus.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Produto custo beneficio bom.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Poderia ter um preço melhor.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "O meu Smartphone so tem um mês, então minha avaliação ainda é superficial, por enquanto me surpreendeu eu tinha o Smartphone Motorola G4 Plus que eu gostava muito também, mas fui assaltada, e na hora de comprar um novo optei em comprar a nova versão e me surpreendi, estou gostando muito.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto custo beneficio bom, poderia ter um preço melhor. O meu Smartphone so tem um mês, então minha avaliação ainda é superficial, por enquanto me surpreendeu eu tinha o Smartphone Motorola G4 Plus que eu gostava muito também, mas fui assaltada, e na hora de comprar um novo optei em comprar a nova versão e me surpreendi, estou gostando muito ele tem mais precisão e o reconhecimento digital e bem superior ao G4plus."
    # },
    # "10.126": {
    #     "opinions": [
    #         [
    #             "O fone que vem com o aparelho não tem boa qualidade.",
    #             "ACESSoRIO",
    #             "-"
    #         ],
    #         [
    #             "Ele tem boa memoria.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "A camera tem menos estabilidade, sinto de alguns app's exclusivos da série Galaxy.",
    #             "CaMERA",
    #             "-"
    #         ],
    #         [
    #             "Ele é rapido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O aparelho é bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Faltou um pouco de capricho pelo fabricante.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "A tv não tem boa recepção.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Os sub icones como sinal do wi fi poderia ser mais destacados e amigaveis.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Bem...é bem legal.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bom mas pode melhorar. Na verdade faço comparação com a Samsung pois era o que eu tinha.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "A tela é bem brilhante.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom mas pode melhorar. Na verdade faço comparação com a Samsung pois era o que eu tinha. A camera tem menos estabilidade, sinto de alguns app's exclusivos da série Galaxy. A tv não tem boa recepção. O fone que vem com o aparelho não tem boa qualidade. O aparelho é bonito. A tela é bem brilhante. Os sub icones como sinal do wi fi poderia ser mais destacados e amigaveis. Ele é rapido e tem boa memoria. Bem...é bem legal mas faltou um pouco de capricho pelo fabricante."
    # },
    # "10.128": {
    #     "opinions": [
    #         [
    #             "Com muita memoria.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho muito bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Recomendo por ter algo a mais que é através da digital a sua segurança, foi o que me chamou a minha atenção.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto. Um bom produto,com muita memoria,aparelho muito bonito e recomendo por ter algo a mais que é através da digital a sua segurança,foi o que me chamou a minha atenção."
    # },
    # "10.129": {
    #     "opinions": [
    #         [
    #             "Gostei do assistente de configuração que importou totalmente os aplicativos existentes no celular Moto E antigo.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Plenamente satisfatorio.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Plenamente satisfatorio. Gostei do assistente de configuração que importou totalmente os aplicativos existentes no celular Moto E antigo."
    # },
    # "10.130": {
    #     "opinions": [
    #         [
    #             "Camera muito boa.",
    #             "CaMERA",
    #             "+"
    #         ],
    #         [
    #             "Bom desempenho.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "otimo custo beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Melhor celular na sua faixa de preço.",
    #             "PREÇO",
    #             "++"
    #         ]
    #     ],
    #     "review": "otimo custo beneficio. Melhor celular na sua faixa de preço. Bom desempenho. Camera muito boa."
    # },
    # "10.131": {
    #     "opinions": [
    #         [
    #             "Olha realmente tenho esse produto que comprei mas lojas americanas.",
    #             "PRODUTO",
    #             "X"
    #         ],
    #         [
    #             "Ele esta com uma mancha na tela do lado direito na parte inferior do aparelho, o que vocês podem fazer a respeito.",
    #             "TELA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Olha realmente tenho esse produto que comprei mas lojas americanas, porém ele es. Olha realmente tenho esse produto que comprei mas lojas americanas, porém ele está com uma mancha na tela do lado direito na parte inferior do aparelho, o que vocês podem fazer a respeito."
    # },
    # "10.132": {
    #     "opinions": [
    #         [
    #             "Elogio.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "otimo Celular! adorei!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Elogio. otimo Celular! adorei!"
    # },
    # "10.133": {
    #     "opinions": [
    #         [
    #             "Apenas a bateria a bateria podia ser melhor.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Bom Produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei do produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom Produto. Gostei do produto, apenas a bateria a bateria podia ser melhor."
    # },
    # "10.135": {
    #     "opinions": [
    #         [
    #             "Nota 10.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito satisfeito.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Nota 10. Muito satisfeito."
    # },
    # "10.136": {
    #     "opinions": [
    #         [
    #             "Ótimo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Moto G Plus. Ótimo!"
    # },
    # "10.137": {
    #     "opinions": [
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom e fácil.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Recomendo. Muito bom e fácil."
    # },
    # "10.138": {
    #     "opinions": [
    #         [
    #             "Entregue antes do prazo.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Celular de ótimo custo-beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Celular de ótimo custo-beneficio e entregue antes do prazo. Recomendo."
    # },
    # "10.139": {
    #     "opinions": [
    #         [
    #             "Celular com boa bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Celular com boa camera.",
    #             "CaMERA",
    #             "+"
    #         ],
    #         [
    #             "Celular com bom custo beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Gostei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Celular com bons recursos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Celular com Android 7.0.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Gostei. Celular com Android 7.0, com bons recursos, boa bateria, boa camera e bom custo beneficio."
    # },
    # "10.140": {
    #     "opinions": [
    #         [
    #             "Aprovado!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O produto atingiu as minhas expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Aprovado! O produto atingiu as minhas expectativas."
    # },
    # "10.141": {
    #     "opinions": [
    #         [
    #             "Câmera muito boa.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto..",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Recomendo. Ótimo produto.. Camara muito boa."
    # },
    # "10.142": {
    #     "opinions": [
    #         [
    #             "Produto excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Foi presente.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Produto excelente. Foi presente."
    # },
    # "10.143": {
    #     "opinions": [
    #         [
    #             "Rápido ...",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Facil de usar ...",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Rápido, facil de usar, ..."
    # },
    # "10.144": {
    #     "opinions": [
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Até o momento estou adorando o aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Até o momento estou adorando o aparelho."
    # },
    # "10.145": {
    #     "opinions": [
    #         [
    #             "Aparelho design excelente.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom respondeu todas expectativas,.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Facilidade de uso.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Aparelho design excelente, facilidade de uso, muito bom respondeu todas expectativas,."
    # },
    # "10.146": {
    #     "opinions": [
    #         [
    #             "APARELHO MUITO BONITO.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "APARELHO NA COR OURO MUITO LEGAL.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "APARELHO FUNCIONAL ACERTEI NA COMPRA POIS SÓ GOSTO DA MARCA MOTOROLA (MOTO G 5).",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "APARELHO NA COR OURO MUITO LEGAL. APARELHO MUITO BONITO, FUNCIONAL ACERTEI NA COMPRA POIS SÓ GOSTO DEA MARCA MOTOROLA (MOTO G 5"
    # },
    # "10.147": {
    #     "opinions": [
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda é cedo.",
    #             "PRODUTO",
    #             "x"
    #         ]
    #     ],
    #     "review": "Bom produto. Ainda é cedo."
    # },
    # "10.148": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PREÇO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Cxb. Bom."
    # },
    # "10.149": {
    #     "opinions": [
    #         [
    #             "Otimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo produto. Otimo produto."
    # },
    # "10.150": {
    #     "opinions": [
    #         [
    #             "Pouca memória para os recursos que possui.",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "A duração da bateria deixa a desejar, pois um dia que se tenha uma maior conversação ou se decida usar os recursos de TV que o aparelho fornece ela se esgota rapidamente.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "A câmera está abaixo da categoria.",
    #             "CÂMERA",
    #             "-"
    #         ],
    #         [
    #             "Para um uso simples, apenas internet, redes sociais, email e uma ou outro ligação o aparelho atende, mas um uso um pouco mais intenso dos recursos o aparelho não suporta.",
    #             "DESEMPENHO",
    #             "-."
    #         ],
    #         [
    #             "Razoável.",
    #             "PRODUTO",
    #             "."
    #         ],
    #         [
    #             "Aparelho Razoável.",
    #             "PRODUTO",
    #             "."
    #         ],
    #         [
    #             "Recomendo que seja comprada uma capa de proteção.",
    #             "RESISTÊNCIA",
    #             "!"
    #         ],
    #         [
    #             "O aparelho é muito liso e facilmente escapa da mão.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "A tela está abaixo da categoria.",
    #             "TELA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Rasoável. Aparelho Razoável, porém pouca memória para os recursos que possui, a câmera e a tela estão abaixo da categoria e a duração da bateria deixa a desejar, pois um dia que se tenha uma maior conversação ou se decida usar os recursos de TV que o aparelho fornece ela se esgota rapidamente. Para um uso simples, apenas internet, redes sociais, email e uma ou outro ligação o aparelho atende, mas um uso um pouco mais intenso dos recursos o aparelho não suporta. Recomendo que seja compara uma capa de proteção, pois o aparelho e muito liso e facilmente escapa da mão, e com certeza uma pelicula de proteção."
    # },
    # "10.151": {
    #     "opinions": [
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "otimo. Ótimo."
    # },
    # "10.152": {
    #     "opinions": [
    #         [
    #             "Bateria muito boa que aguenta até mais de um dia sem recarregar com minha experiência de uso.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Um processador muito bom que otimiza demais o uso no dia-a-dia.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Produto de excelente custo-beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou com o smartphone há mais ou menos 1 mês e só tenho elogios.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Display excelente e com cores vívidas.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto de excelente custo-benefício. Estou com o smartphone há mais ou menos 1 mês e só tenho elogios. Bateria muito boa que aguenta até mais de um dia sem recarregar com minha experiência de uso, display excelente e com cores vívidas, além de um processador muito bom que otimiza demais o uso no dia-a-dia. Recomendo!"
    # },
    # "10.153": {
    #     "opinions": [
    #         [
    #             "Duração da bateria excelente!",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Processador rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ]
    #     ],
    #     "review": "MOTOG 5 PLUS. Processador rápido, duração da bateria excelente!"
    # },
    # "10.154": {
    #     "opinions": [
    #         [
    #             "A função de dividir a tela e usar dois aplicativos simultaneamente é ótima.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O Android 7.0 é muito bom.",
    #             "SISTEMA",
    #             "+"
    #         ],
    #         [
    #             "Gosto do Android quase puro e a Motorola atualiza o sistema operacional mais rápido que os demais fabricantes.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto. Gosto do Android quase puro e a Motorola atualiza o sistema operacional mais rápido que os demais fabricantes. O Android 7.0 é muito bom. A função de dividir a tela e usar dois aplicativos simultaneamente é ótima."
    # },
    # "10.155": {
    #     "opinions": [
    #         [
    #             "Ótimo produto!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótima surpresa!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótima surpresa! Ótimo produto!"
    # },
    # "10.156": {
    #     "opinions": [
    #         [
    #             "Boa duração de bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Design muito bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Ótimo aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo aparelho. Design muito bonito, rápido e com uma boa duração de bateria."
    # },
    # "10.157": {
    #     "opinions": [
    #         [
    #             "A durabilidade da bateria que não dura 12 horas vc usando as redes sociais mas tirando isto estou satisfeita com o produto.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Custo beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Custo beneficio. Aparelho excelente, exceto a durabilidade da bateria que não dura 12 horas vc usando as redes sociais mas tirando isto estou satisfeita com o produto."
    # },
    # "10.158": {
    #     "opinions": [
    #         [
    #             "Bacana.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto. Bacana."
    # },
    # "10.159": {
    #     "opinions": [
    #         [
    #             "Boa câmera qualidade de imagem.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Uso as redes sociais numa boa sem problemas ou travamentos.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Adoro ver TV em HD nele.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Moto G5 plus ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adorei esse é o meu primeiro Motorola e estou muito satisfeita.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Moto G5 plus ótimo. Adorei esse é o meu primeiro Motorola e estou muito satisfeita boa câmera qualidade de imagem adoro ver TV em HD nele uso as redes sociais numa boa sem problemas ou travamentos. Recomendo."
    # },
    # "10.160": {
    #     "opinions": [
    #         [
    #             "Com espaço interno de bom tamanho.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Câmeras frontal e traseira com qualidade muito boa.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Para jogos não se discute roda qualquer jogo.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Para mim melhor custo benefício do mercado.",
    #             "PREÇO",
    #             "++"
    #         ],
    #         [
    #             "Exelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto de alta qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Com uma tela de ótimo tamanho.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Exelente produto. Produto de alta qualidade, com espaço interno de bom tamanho, câmeras frontal e traseira com qualidade muito boa. Para jogos não se discute roda qualquer jogo e com uma tela de ótimo tamanho, para mim melhor custo benefício do mercado."
    # },
    # "10.161": {
    #     "opinions": [
    #         [
    #             "Produto excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Atende as expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto excelente. Atende as expectativas."
    # },
    # "10.162": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Smartphone muito bom perfeito.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Excelente. Smartphone muito bom perfeito. Recomendo."
    # },
    # "10.163": {
    #     "opinions": [
    #         [
    #             "Moderno.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda estou conhecendo pois não faz 1 mês que adquiri.",
    #             "PRODUTO",
    #             "x"
    #         ]
    #     ],
    #     "review": "Moderno. Ainda estou conhecendo pois não faz 1 mês que adquiri."
    # },
    # "10.164": {
    #     "opinions": [
    #         [
    #             "Produto bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou experimentando....",
    #             "PRODUTO",
    #             "x"
    #         ]
    #     ],
    #     "review": "Produto bom. Estou experimentando...."
    # },
    # "10.165": {
    #     "opinions": [
    #         [
    #             "Pouco tempo de uso. Estou experimentando....",
    #             "PRODUTO",
    #             "x"
    #         ]
    #     ],
    #     "review": "Pouco tempo de uso. Estou experimentando...."
    # },
    # "10.166": {
    #     "opinions": [
    #         [
    #             "Gostei da câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Gostei da rapidez no processamento.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Lindo.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Gostei em especial do toque digital.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Inovador.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei do celular em todos aspectos.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Lindo e inovador. Gostei do celular em todos aspectos, em especial do toque digital, da rapidez no processamento e câmera."
    # },
    # "10.167": {
    #     "opinions": [
    #         [
    #             "Celular com ponto forte na qualidade das fotos.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Bom custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Vale a pena pelo custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Celular bem completo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom custo benefício. Celular bem completo, com ponto forte na qualidade das fotos. Vale a pena pelo custo benefício."
    # },
    # "10.169": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uso para falar e web,.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Bom. Uso para falar e web,."
    # },
    # "10.170": {
    #     "opinions": [
    #         [
    #             "Para mim, a memória interna deveria ser aumentada, pois o Android quase ocupa toda ela.",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "A bateria está no razoável, pois um dia de conversação mais intensa ira acabar com a mesma.",
    #             "BATERIA",
    #             "."
    #         ],
    #         [
    #             "Gostei do fato de ter o rádio, pois as vezes é util.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Gostei do fato de ter a televisão, pois as vezes é util.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "No tocante ao preço quando comparado aos outros da mesma categoria possui um relação custo beneficio melhor.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "O Aparelho é bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho Bom, porém com algumas limitaçoes.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Aparelho Bom, porém com algumas limitaçoes. O Aparelho é bom, e no tocante ao preço quando comparado aos outros da mesma categoria possui um relação custo beneficio melhor. Para mim, a memória interna deveria ser aumentada, pois o Android quase ocupa toda ela. A bateria está no razoável, pois um dia de conversação mais intensa ira acabar com a mesma. Gostei do fato de ter a televisão e o rádio, pois as vezes em elas são uteis."
    # },
    # "10.171": {
    #     "opinions": [
    #         [
    #             "NORMAL.",
    #             "PRODUTO",
    #             "."
    #         ]
    #     ],
    #     "review": "MOTO G5. NORMAL."
    # },
    # "10.172": {
    #     "opinions": [
    #         [
    #             "Muito bem sua câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto. Muito bem sua câmera."
    # },
    # "10.173": {
    #     "opinions": [
    #         [
    #             "Design elegante.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Excelente custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Não há smartphone perfeito, mas pela sua faixa de preço atende muito bem.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Mas não me arrependi.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Eu sempre comprei Samsung e fiquei apreensivo quanto a um Motorola.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Funciona com desenvoltura, tem bons recursos, não trava (diferente de alguns comentários que li, não sei o que possa ter acontecido), enfim, estou contentíssimo com o produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente custo benefício. Eu sempre comprei Samsung e fiquei apreensivo quanto a um Motorola. Mas não me arrependi. Funciona com desenvoltura, tem bons recursos, não trava (diferente de alguns comentários que li, não sei o que possa ter acontecido, design elegante, enfim, estou contentíssimo com o produto. Não há smartphone perfeito, mas pela sua faixa de preço atende muito bem."
    # },
    # "10.174": {
    #     "opinions": [
    #         [
    #             "Pena não vender no Brasil a versão americana com 4GB de RAM e 64GB de memória interna (o meu é esse)",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "Esse aqui não trava e a bateria dura, DE FATO, 1 dia inteiro.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Para ter mais do que ele oferece, você vai ter que gastar o dobro em aparelhos como Galaxy S8 ou Iphone 9999s, que custam 3k.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Já caí na armadilha dos Iphone (itunes.. Grrrr), e já me encantei com alguns Galaxy. Depois do preço absurdamente abusivo desses aparelhos, no entanto, já era. Agora, só Moto G.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Sem comparação, o melhor custo benefício da história.",
    #             "PREÇO",
    #             "++"
    #         ],
    #         [
    #             "Meu primeiro Moto G foi o Moto G3 Turbo. Agora eu comprei o Moto G5 Plus, e não fica a dever a 99% dos aparelhos do mercado.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Sem comparação, o melhor custo benefício da história. Meu primeiro Moto G foi o Moto G3 Turbo. Agora eu comprei o Moto G5 Plus, e não fica a dever a 99% dos aparelhos do mercado. Para ter mais do que ele oferece, você vai ter que gastar o dobro em aparelhos como Galaxy S8 ou Iphone 9999s, que custam 3k. A diferença é que esse aqui não trava e a bateria dura, DE FATO, 1 dia inteiro. Pena não vender no Brasil a versão americana com 4GB de RAM e 64GB de memória interna (o meu é esse Já caí na armadilha dos Iphone (itunes.. Grrrr, e já me encantei com alguns Galaxy. Depois do preço absurdamente abusivo desses aparelhos, no entanto, já era. Agora, só Moto G."
    # },
    # "10.175": {
    #     "opinions": [
    #         [
    #             "Carrega mais rápido ainda e a bateria dura muito (uso muito celular, jogos, aplicativos, redes sociais).",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Câmera incrível.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Super rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O processador deixou o aparelho voando.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho mais bonito pessoalmente (dourado).",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Designer perfeito.",
    #             "DESIGN",
    #             "++"
    #         ],
    #         [
    #             "Pega vários canais em imagem hd.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "O diferencial dele é a TV, foi por isso que adquiri esse modelo.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Consegui uma promoção incrível pelo extra que de 1499 saiu por 879,00 a vista e por esse preço tenho certeza que não encontraria um celular desse nível.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Amando meu Moto G plus.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito feliz e satisfeita. Super indico.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Alguns comentam que o Moto g retrocedeu, tenho que discordar.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adquiri há 1 mês.",
    #             "PRODUTO",
    #             "X"
    #         ],
    #         [
    #             "Diminuiu o seu tamanho.",
    #             "TAMANHO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Amando meu Moto G plus. Adquiri há 1 mês.Aparelho mais bonito pessoalmente (dourado).Câmera incrível, designer perfeito, super rápido, carrega mais rápido ainda e a bateria dura muito (uso muito celular, jogos, aplicativos, redes sociais.O diferencial dele é a TV, foi por isso que adquiri esse modelo. Pega vários canais em imagem hd.Consegui uma promoção incrível pelo extra que de 1499 saiu por 879,00 a vista e por esse preço tenho certeza que não encontraria um celular desse nível.Alguns comentam que o Moto g retrocedeu, tenho que discordar. Diminuiu o seu tamanho porém o processador deixou o aparelho voando.Muito feliz e satisfeita.Super indico."
    # },
    # "10.176": {
    #     "opinions": [
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente produto, atende todas as minhas necessidades.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente produto. Excelente produto, atende todas as minhas necessidades."
    # },
    # "10.177": {
    #     "opinions": [
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Amo motorola.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Amo motorola."
    # },
    # "10.178": {
    #     "opinions": [
    #         [
    #             "Boa relação custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Boa relação custo benefício."
    # },
    # "10.179": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto nota 10 em tudo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Produto nota 10 em tudo."
    # },
    # "10.180": {
    #     "opinions": [
    #         [
    #             "Boa duração da bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Fino.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Leve.",
    #             "PESO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tela com bom tamanho.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo smartphone. Boa duração da bateria, tela com bom tamanho, fino, leve."
    # },
    # "10.181": {
    #     "opinions": [
    #         [
    #             "Celular com uma bateria super durável.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Celular lindo.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Comprei pelo custo benefício, e levei muito mais que um bom preço.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Satisfeita e feliz !",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Celular de qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda estou aprendendo a mexer nele, mas até o momento posso afirmar que é o melhor celular que tive.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Satisfeita e feliz ! Comprei pelo custo benefício, e levei muito mais que um bom preço. Celular de qualidade, lindo e com uma bateria super durável. Ainda estou aprendendo a mexer nele, mas até o momento posso afirmar que é o melhor celular que tive."
    # },
    # "10.182": {
    #     "opinions": [
    #         [
    #             "Deveria ter acabamento mais refinado.",
    #             "DESIGN",
    #             "-"
    #         ],
    #         [
    #             "Um dos melhores aparelhos pelo preço.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Um dos melhores aparelhos pelo preço mas deveria ter acabamento mais refinado."
    # },
    # "10.183": {
    #     "opinions": [
    #         [
    #             "Excelente Custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Celular muito bom, não precisa mais q isso.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente Custo benefício. Excelente Custo benefício, celular muito bom, não precisa mais q isso."
    # },
    # "10.184": {
    #     "opinions": [
    #         [
    #             "Só fica a desejar por ele travar e ser meio lento em alguns aplicativos no mais é um ótimo aparelho.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Entrega rápida.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Moto G5. Ótimo produto entrega rápida só fica a desejar por ele travar e ser meio lento em alguns aplicativos no mais é um ótimo aparelho."
    # },
    # "10.185": {
    #     "opinions": [
    #         [
    #             "Bateria de longa duração.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Ótima câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Aprovado!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo smartphone!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Boa tela.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Aprovado! Ótimo smartphone! Bateria de longa duração, boa tela, ótima câmera."
    # },
    # "10.186": {
    #     "opinions": [
    #         [
    #             "Não comprei na empresa efacil, empresa ruim.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Por isso cancelei a compra e adquiri em outra empresa.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Não comprei na empresa efacil, empresa não tem um serviço de entrega que permita o agendamento.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "O produto é muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "O produto é muito bom, porém não comprei na empresa efacil, empresa ruim. O produto é muito bom, porém não comprei na empresa efacil, empresa não tem um serviço de entrega que permita o agendamento. Por isso cancelei a compra e adquiri em outra empresa."
    # },
    # "10.187": {
    #     "opinions": [
    #         [
    #             "Custo beneficio muito bom.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom produto. Custo beneficio muito bom."
    # },
    # "10.188": {
    #     "opinions": [
    #         [
    #             "Creio que a unica coisa negativa são os \"apenas\" 2 GB de memória, se fossem 3 GB o aparelho seria imbativel.",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "Destaque para a camera traseira que tira ótimas fotos.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Na sua faixa de preço ainda está valendo a pena.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Um dos melhores aparelhos intermediarios de 2017.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Sem muitos rodeios, o aparelho tem me agradado bastante em praticamente todos os aspectos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Eu comprei esse aparelho depois de varios reviews de outros smartphone nessa faixa de preço e não me decepcionei.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um dos melhores aparelhos intermediarios de 2017. Sem muitos rodeios, o aparelho tem me agradado bastante em praticamente todos os aspectos. Destaque para a camera traseira que tira ótimas fotos. Eu comprei esse aparelho depois de varios reviews de outros smartphone nessa faixa de preço e não me decepcionei. Creio que a unica coisa negativa são os \"apenas\" 2 GB de memória, se fossem 3 GB o aparelho seria imbativel, mas na sua faixa de preço ainda está valendo a pena."
    # },
    # "10.189": {
    #     "opinions": [
    #         [
    #             "O que falta é um bom manual de uso.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Bom custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom custo benefício. Ótimo aparelho. O que falta é um bom manual de uso."
    # },
    # "10.190": {
    #     "opinions": [
    #         [
    #             "Pratico.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Pratico e simples.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Pratico e simples. Pratico."
    # },
    # "10.191": {
    #     "opinions": [
    #         [
    #             "Melhor Custo Beneficio.",
    #             "PREÇO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Melhor Custo Beneficio."
    # },
    # "10.192": {
    #     "opinions": [
    #         [
    #             "Ótimo celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ele é muito bom nas funcionalidades que já usei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Eu estou aprendendo ainda algumas funcionalidades do produto.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Ótimo celular. Eu estou aprendendo ainda algumas funcionalidades do produto. Mas ele é muito bom nas funcionalidades que já usei."
    # },
    # "10.193": {
    #     "opinions": [
    #         [
    #             "Muito rápido!",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Moto g 5 plus ótimo desempenho.",
    #             "DESEMPENHO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Moto g 5 plus ótimo desempenho. Muito rápido!"
    # },
    # "10.194": {
    #     "opinions": [
    #         [
    #             "O celular realmente é bom mas o fone de ouvido deixa a desejar, machuca o ouvido e incomoda bastante.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. O celular realmente é bom mas o fone de ouvido deixa a desejar, machuca o ouvido e incomoda bastante."
    # },
    # "10.195": {
    #     "opinions": [
    #         [
    #             "Mais um produto de qualidade!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Meu terceiro aparelho da Motorola, não me arrependo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Mais um produto de qualidade! Meu terceiro aparelho da Motorola, não me arrependo!"
    # },
    # "10.197": {
    #     "opinions": [
    #         [
    #             "Eu recomendo, custo beneficio são ótimo.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Eu recomendo, custo beneficio são ótimo."
    # },
    # "10.198": {
    #     "opinions": [
    #         [
    #             "Gosto muito dele e quero muito ganhar o iPad.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Moto G5. Gosto muito dele e quero muito ganhar o iPad."
    # },
    # "10.199": {
    #     "opinions": [
    #         [
    #             "Bateria dura até o fim do dia tranquilo.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Não trava e não engasga.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Maravilhoso.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhoso. Ótimo aparelho, bateria dura até o fim do dia tranquilo. Não trava e não engasga. Recomendo!"
    # },
    # "10.200": {
    #     "opinions": [
    #         [
    #             "Aparelho eficiente, sem frescuras e bem performático.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Custo Benefício Bom.",
    #             "PREÇO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Custo Benefício Bom. Aparelho eficiente, sem frescuras e bem performático."
    # },
    # "10.201": {
    #     "opinions": [
    #         [
    #             "Bastante rápido e tem o desempenho comparável aos top de linha, mesmo sendo um da categoria intermediário.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É um ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. É um ótimo produto. Bastante rápido e tem o desempenho comparável aos top de linha, mesmo sendo um da categoria intermediário."
    # },
    # "10.202": {
    #     "opinions": [
    #         [
    #             "Mais um aparelho de qualidade!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Meu terceiro smartphone da linha e mais um produto de qualidade!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Mais um aparelho de qualidade! Meu terceiro smartphone da linha e mais um produto de qualidade!"
    # },
    # "10.203": {
    #     "opinions": [
    #         [
    #             "Recomendado.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Atendeu as expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Recomendado. Atendeu as expectativas."
    # },
    # "10.204": {
    #     "opinions": [
    #         [
    #             "Mais um Smartphone padrão MOTO!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ja é meu terceiro aparelho da linha MOTO G! Mais uma vez um aparelho ótimo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Mais um Smartphone padrão MOTO! Ja é meu terceiro aparelho da linha MOTO G!Mais uma vez um aparelho ótimo!"
    # },
    # "10.205": {
    #     "opinions": [
    #         [
    #             "Mais um aparelho maravilhoso!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Este é o meu terceiro aparelho da Motorola e não compraria um de outra marca!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Mais um aparelho maravilhoso! Este é o meu terceiro aparelho da Motorola e não compraria um de outra marca!"
    # },
    # "10.206": {
    #     "opinions": [
    #         [
    #             "Como sempre um produto sem igual!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Com sempre um produto sem igual! Este é o meu terceiro aparelho da Motorola e não compraria um de outra marca!"
    # },
    # "10.207": {
    #     "opinions": [
    #         [
    #             "Como sempre um produto que atende as expectativas do comprador!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Este é o meu terceiro aparelho da Motorola e não compraria outro!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Como sempre um produto que atende as expectativas do comprador! Este é o meu terceiro aparelho da Motorola e não compraria outro!"
    # },
    # "10.208": {
    #     "opinions": [
    #         [
    #             "Apesar de ser rápido a memória ram ainda é baixa.",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "Smartphone rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Smartphone com um design que agrada, os detalhes são bem feitos.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Custo benefício baixo.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "O preço é muito alto em relação aos benefícios que o aparelho entrega.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Ótimo smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "E um ótimo smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo porém se o valor estiver na faixa de 1.100.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Ótimo smartphone porém custo benefício baixo. E um ótimo smartphone, com um design? que agrada, os detalhes são bem feitos.Apesar de ser rápido a memória ram ainda é baixa e o preço é muito alto em relação aos benefícios que o aparelho entrega. Recomendo porém se o valor estiver na faixa de 1.100."
    # },
    # "10.209": {
    #     "opinions": [
    #         [
    #             "Compra recente não testei muito, mas a bateria está durando bastante!",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "A câmera com zoom perde bastante qualidade.",
    #             "CÂMERA",
    #             "-"
    #         ],
    #         [
    #             "Ainda não testei muito.",
    #             "PRODUTO",
    #             "x"
    #         ]
    #     ],
    #     "review": "Ainda não testei muito. Compra recente não testei muito, mas a bateria está durando bastante! A câmera com zoom perde bastante qualidade."
    # },
    # "10.210": {
    #     "opinions": [
    #         [
    #             "Achei que a duração da bateria é um excelente ponto.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Achei que a qualidade da câmera é um excelente ponto.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "O principal é que os oito processadores cumprem muito bem sua função!",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Lindo.",
    #             "DESIGN",
    #             "+"
    #         ]
    #     ],
    #     "review": "Lindo. Achei que a duração da bateria e a qualidade da câmera foram excelentes pontos, mas o principal é que os oito processadores cumprem muito bem sua função!"
    # },
    # "10.212": {
    #     "opinions": [
    #         [
    #             "Otimo custo-beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Este smathphone me surpreendeu positivamente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda não conheço todos os recursos tecnológicos, mas estou muito satisfeito!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo custo-beneficio. Este smathphone me surpreendeu positivamente. Ainda não conheço todos os recursos tecnológicos, mas estou muito satisfeito!"
    # },
    # "10.213": {
    #     "opinions": [
    #         [
    #             "Câmera boa.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Produto bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Detalhes fazem dele o melhor custo benefício da categoria.",
    #             "PREÇO",
    #             "++"
    #         ],
    #         [
    #             "Muito bom . Recomendo .",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Android puro.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom . Recomendo . Produto bonito, câmera boa, Android puro, fora detalhes de isso fazem dele o melhor custo benefício da categoria."
    # },
    # "10.215": {
    #     "opinions": [
    #         [
    #             "Sempre visito o site do buscape e sempre tem preços descritos na imagem so que quando vc clica na loja o preço sobe igual magica ..",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Entao nao utilizem o buscape como referencia pois ele nunca acerta os preços e nao consigo falar com a central deles para reclamar ..",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "O produto e intermediario digamos que pobre tem que tomar no *** memo.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "E se vcs quiserem celular bom indico que procurem um iphone da apple mesmo versoes mais antigas pois nunca perdem valor de mercado apple e apple...",
    #             "PRODUTO",
    #             "-"
    #         ]
    #     ],
    #     "review": "O produto e intermediario digamos que pobre tem que tomar no *** memo. Sempre visito o site do buscape e sempre tem preços descritos na imagem so que quando vc clica na loja o preço sobe igual magica .. Entao nao utilizem o buscape como referencia pois ele nunca acerta os preços e nao consigo falar com a central deles para reclamar .. E se vcs kiserem celular bom indico que procurem um iphone da aplee mesmo versoes mais antigas pois nunca perdem valor de mercado aplee e aplee..."
    # },
    # "10.216": {
    #     "opinions": [
    #         [
    #             "O moto G5 Plus tem um sério problema na bateria.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Motorola nunca mais!",
    #             "EMPRESA",
    #             "--"
    #         ],
    #         [
    #             "NÃO COMPRE.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Foi o pior aparelho que já comprei, não recomendo para ninguem.",
    #             "PRODUTO",
    #             "--"
    #         ],
    #         [
    #             "Comprei o aparelho e depois de três meses ele já apresentou problemas. O telefone desliga sozinho, mesmo a bateria apresentando carga. Há dificuldade para religá-lo.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "NÃO COMPRE. O moto G5 Plus tem um sério problema na bateria. Comprei o aparelho e depois de três meses ele já apresentou problemas. O telefone desliga sozinho, mesmo a bateria apresentando carga. Há dificuldade para religa-lo. Foi o pior aparelho que já comprei, não recomendo para ninguem. Motorola nunca mais!"
    # },
    # "10.217": {
    #     "opinions": [
    #         [
    #             "Desligou sozinho e parau de funcionar.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "O aparelho é muito bom, mas com 2 semanas de uso ele apagou e não funcionou mais, nesse momento esta na assistencia tecnica,, Uma decepção total, espero que consertem e volte sem mais aborrecimentos...",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Desligou sozinho e parau de funcionar. O aparelho é muito bom, mas com 2 semanas de uso ele apagou e não funcionou mais, nesse momento esta na assistencia tecnica,, Uma decepção total, espero que consertem e volte sem mais aborrecimentos..."
    # },
    # "10.218": {
    #     "opinions": [
    #         [
    #             "Porém em algumas situaçoes ele trava. Já resetei o produto mas não resolveu o problema.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto simples e que atende as principais funçoes do dia a dia.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto. Produto simples e que atende as principais funçoes do dia a dia. Porém em algumas situaçoes ele trava. Já resetei o produto mas não resolveu o problema."
    # },
    # "10.219": {
    #     "opinions": [
    #         [
    #             "Minha experiência infelizmente não foi boa já que o aparelho corrompeu 2 cartoes sd um de 64gb e outro de 128gb, na primeira semana de uso tive que enviar ele para a assistência, a motorola não se responsabiliza pelos cartoes sd que o aparelho corrompeu, e até agora não consegui testar o aparelho novamente pois vou ter que arcar com a compra de outro cartão para fazer o teste, já imaginando que posso vir a perder esse também.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Regular pois na primeira semana de uso tive que enviar ele para a assistência.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Regular pois na primeira semana de uso tive que enviar ele para a assistência. Minha experiência infelizmente não foi boa já que o aparelho corrompeu 2 cartoes sd um de 64gb e outro de 128gb, na primeira semana de uso tive que enviar ele para a assistência, a motorola não se responsabiliza pelos cartoes sd que o aparelho corrompeu, e até agora não consegui testar o aparelho novamente pois vou ter que arcar com a compra de outro cartão para fazer o teste, já imaginando que posso vir a perder esse também."
    # },
    # "10.220": {
    #     "opinions": [
    #         [
    #             "Infelizmente os 2Gb de RAM não suprem a necessidade para quem usa bastante o aparelho com mais de um app ligado.",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "A câmera deixa a desejar, pois se você usa o zoom a qualidade de imagem da foto cai muito, mais muito mesmo.",
    #             "CÂMERA",
    #             "-"
    #         ],
    #         [
    #             "Um bom aparelho porém baixo desempenho.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Com tempo de uso começou a reiniciar sozinho, trava de vez em quando, esquentar bastante.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Design bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Leve.",
    #             "PESO",
    #             "+"
    #         ],
    #         [
    #             "Gostei muito do aparelho de início.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Como a Lenovo viu que vacilou no aparelho pretende lançar agora o G5S Plus corrigindo esses detalhes, trazendo melhoria na câmera que vai ter 2 câmeras traseiras e modelos com 3GB de RAM e com 4GB de RAM.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Android puro.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um bom aparelho porém baixo desempenho. Gostei muito do aparelho de início, design bonito, leve, Android puro, porém com tempo de uso começou a reiniciar sozinho, trava de vez em quando, esquentar bastante, infelizmente os 2Gb de RAM não suprem a necessidade para quem usa bastante o aparelho com mais de um app ligado.A câmera deixa a desejar, pois se você usa o zoom a qualidade de imagem da foto cai muito, mais muito mesmo.Como a Lenovo viu que vacilou no aparelho pretende lançar agora o G5S Plus corrigindo esses detalhes, trazendo melhoria na câmera que vai ter 2 câmeras traseiras e modelos com 3GB de RAM e com 4GB de RAM."
    # },
    # "10.221": {
    #     "opinions": [
    #         [
    #             "Verificar a oferta do Shoptime.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Valor de oferta de 250,00 não corresponde ao produto.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Ela não corresponde ao Smartphone da Motorola que está em propaganda, e sim a um bem inferior da Multilaser.",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Valor de oferta de 250,00 não corresponde ao produto. Verificar a oferta do Shoptime. Ela não corresponde ao Smartphone da Motorola que está em propaganda, e sim a um bem inferior da Multilaser."
    # },
    # "10.222": {
    #     "opinions": [
    #         [
    #             "O fone que vem junto é descartável de tão ruim, não vale R$10.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Possui 8 nucleos e não suporta a capacidade, superaquece e desliga quando usa GPS+Bluetooth juntos, faça o teste e verá: ele esquenta até desligar.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Não possui \"área de transferência\", como todo android.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Não tem botão \"Reiniciar\", aparentemente é algo genial demais para os desenvolvedores. Desligue e ligue.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Não possui nem \"meus documentos\" ou \"biblioteca\", é preciso baixar APP pra gerenciar seus arquivos, acessar seus downloads, etc.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Não funciona bem conectado pelo bluetooth nos carros, tenho iPhones e Galaxys na família que funcionam bem nos carros, o Moto G5 não funciona.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Não tem \"Media Player\", tem que ver pelo Google Musica, você acessa antes um tipo de \"Spotify da google\" antes de acessar suas próprias musicas.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "O celular não tem \"Galeria\" para ver fotos, tem que entrar pelo Google Fotos, você acessa até fotos do orkut, do facebook, de todas as redes sociais antes de conseguir acessar as fotos armazenadas no celular.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "FUJA!",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "MOTO G5: Pior opção possível.",
    #             "PRODUTO",
    #             "--"
    #         ]
    #     ],
    #     "review": "MOTO G5: Pior opção possível. O celular não tem \"Galeria\" para ver fotos, tem que entrar pelo Google Fotos, você acessa até fotos do orkut, do facebook, de todas as redes sociais antes de conseguir acessar as fotos armazenadas no celular;Não tem \"Media Player\", tem que ver pelo Google Musica, você acessa antes um tipo de \"Spotify da google\" antes de acessar suas próprias musicas;Não tem botão \"Reiniciar\", aparentemente é algo genial demais para os desenvolvedores. Desligue e ligue;Não funciona bem conectado pelo bluetooth nos carros, tenho iPhones e Galaxys na família que funcionam bem nos carros, o Moto G5 não funciona;Possui 8 nucleos e não suporta a capacidade, superaquece e desliga quando usa GPS+Bluetooth juntos, faça o teste e verá: ele esquenta até desligar;O fone que vem junto é descartável de tão ruim, não vale R$10;Não possui \"área de transferência\", como todo android. Genial demais para eles também. Não possui nem \"meus documentos\" ou \"biblioteca\", é preciso baixar APP pra gerenciar seus arquivos, acessar seus downloads, etc. FUJA!"
    # },
    # "10.223": {
    #     "opinions": [
    #         [
    #             "Produto Ruim.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Segundo o pessoal a motorola esta trazendo para o terceiro mundo o pior dos piores .",
    #             "PRODUTO",
    #             "--"
    #         ],
    #         [
    #             "Recebi o produto mas o mesmo não carregava. Bateria já estava ruim. Sem conserto, mesmo porque a bateria é lacrada.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Produto Ruim. Recebi o produto mas o mesmo não carregava. Bateria já estava ruim. Sem conserto, mesmo porque a bateria é lacrada. Segundo o pessoal a motorola esta trazendo para o terceiro mundo o pior dos piores ."
    # },
    # "10.224": {
    #     "opinions": [
    #         [
    #             "Tentei entrar em contato com a Onofre e não consegui.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Aparelho com problema. O produto após duas semanas não carrega mais.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Aparelbo com problema. O produto após duas semanas não carrega mais. Tentei entrar en contato com a Onofre e não consegui."
    # },
    # "10.225": {
    #     "opinions": [
    #         [
    #             "Cuidado: não comprem pelo site do Extra, pois esta empresa não entrega no prazo.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Em 02/05/17, comprei este smartphone pelo site do Extra. A promessa foi que o produto seria entregue até 09/05/17. Em 05/05/17, recebi e-mail do Extra no qual afirmava que o produto estava em transporte e seria entregue em breve. Todavia, para minha surpresa, no mesmo dia 05/05/17, recebi outro e-mail do Extra no qual dizia que a entrega não foi concluída, pois supostamente houve três tentativas de entrega e o destinatário estava ausente, sendo o produto devolvido ao Centro de Distribuição da empresa. Evidentemente houve um erro no envio do produto. Primeiramente, moro em um condomínio onde existe portaria 24 horas. Realizo com frequência compras pela Internet e sempre recebo os produtos em minha residência. Em segundo lugar, estranha-me o fato de a empresa afirmar que houve três tentativas de entrega frustradas. O e-mail que recebi afirmando que o produto estava em rota de entrega foi enviado no dia 05/05/17, às 10h36. A informação que obtive na central de atendimento do Extra foi de que a terceira tentativa frustrada de entrega ocorreu no dia 05/05/17, às 14h29. É evidente que, num curto período de menos de 4 horas, de um unico dia, não ocorreram três tentativas frustradas de entrega. Mesmo com esse grave erro, o Extra não demonstrou respeito perante o consumidor. O aparelho era um presente para a minha esposa, em comemoração de uma data especial. Porém, para a minha frustração, o produto não veio no prazo prometido. Decepção! Portanto, fica a dica: não comprem pelo Extra!!",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Cuidado: não comprem pelo site do Extra, pois esta empresa não entrega no prazo. Em 02/05/17, comprei este smartphone pelo site do Extra. A promessa foi que o produto seria entregue até 09/05/17. Em 05/05/17, recebi e-mail do Extra no qual afirmava que o produto estava em transporte e seria entregue em breve. Todavia, para minha surpresa, no mesmo dia 05/05/17, recebi outro e-mail do Extra no qual dizia que a entrega não foi concluída, pois supostamente houve três tentativas de entrega e o destinatário estava ausente, sendo o produto devolvido ao Centro de Distribuição da empresa. Evidentemente houve um erro no envio do produto. Primeiramente, moro em um condomínio onde existe portaria 24 horas. Realizo com frequência compras pela Internet e sempre recebo os produtos em minha residência. Em segundo lugar, estranha-me o fato de a empresa afirmar que houve três tentativas de entrega frustradas. O e-mail que recebi afirmando que o produto estava em rota de entrega foi enviado no dia 05/05/17, às 10h36. A informação que obtive na central de atendimento do Extra foi de que a terceira tentativa frustrada de entrega ocorreu no dia 05/05/17, às 14h29. É evidente que, num curto período de menos de 4 horas, de um unico dia, não ocorreram três tentativas frustradas de entrega. Mesmo com esse grave erro, o Extra não demonstrou respeito perante o consumidor. O aparelho era um presente para a minha esposa, em comemoração de uma data especial. Porém, para a minha frustração, o produto não veio no prazo prometido. Decepção! Portanto, fica a dica: não comprem pelo Extra!!"
    # },
    # "10.226": {
    #     "opinions": [
    #         [
    #             "Peca pela pouca duração da bateria.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "O carregamento rápido só funciona com o aparelho desligado.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "O alarme-despertador não toca se o aparelho estiver desligado.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Infeliz foi o projetista que desenhou aquela maldita bandejinha para a colocação dos 2 chips e do cartão de memória e se você colocou esses 3 itens uma vez com sucesso, não mexa nunca mais com a tal bandejinha porque, senão, jamais conseguirá esse feito novamente!!!",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Boa relação custo-benefício.",
    #             "PREÇO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Boa relação custo-benefício. Peca pela pouca duração da bateria. O carregamento rápido só funciona com o aparelho desligado. O alarme-despertador não toca se o aparelho estiver desligado. Infeliz foi o projetista que desenhou aquela maldita bandejinha para a colocação dos 2 chips e do cartão de memória. Se você colocou esses 3 itens uma vez com sucesso, não mexa nunca mais com a tal bandejinha porque, senão, jamais conseguirá esse feito novamente!!!"
    # },
    # "10.227": {
    #     "opinions": [
    #         [
    #             "A bateria mal da pra um dia completo.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Dou nota zero para a empresa que autorizou uma propaganda mentirosa ir ao ar para seus enganar seus consumidores.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Comprei o produto, através de uma propaganda enganosa da empresa. propaganda enganosa a respeito da durabilidade da bateria.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Moto g 5 , não indico pra ninguém.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Estou muito infeliz com a compra desse produto.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Estou insatisfeita com o produto que eu adquiri.",
    #             "PRODUTO",
    #             "-"
    #         ]
    #     ],
    #     "review": "Estou insatisfeita com o produto que eu adquiri. Comprei o produto, através de uma propaganda enganosa da empresa a respeito da durabilidade da bateria. A bateria mal da pra um dia completo. Estou muito infeliz com a compra desse produto e devido a isso dou nota zero para a empresa que autorizou uma propaganda mentirosa ir ao ar para seus enganar seus consumidores. Moto g 5 , não indico pra ninguém."
    # },
    # "10.228": {
    #     "opinions": [
    #         [
    #             "Quando fui buscar o aparelho, quiseram entregá-lo para mim sem os chips e sem o micro SD que estavam no aparelho - penso que perderam esses chips! Reclamei com a Motorola e estou aguardando solução.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Assistência técnica em Belo Horizonte (WB Celulares) deixa muito a desejar - não tem foco no cliente e pessoal parece ser despreparado: levei meu aparelho para destravar a bandeja de chips, que tinha ficado emperrada no interior do aparelho após inserção do micro SD.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Bandeja de chips é fraca, de plástico, dificulta inserção do cartão micro SD.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Troca de bateria só pode ser feita na assistência técnica, pois não é possível abrir a tampa do aparelho.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Ruim.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Moto G5 Plus decepciona.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "MOTO G ou MOTO Z NUNCA MAIS!",
    #             "PRODUTO",
    #             "--"
    #         ]
    #     ],
    #     "review": "Moto G5 Plus decepciona. Ruim. Bandeja de chips é fraca, de plástico, dificulta inserção do cartão micro SD. Troca de bateria só pode ser feita na assistência técnica, pois não é possível abrir a tampa do aparelho. Assistência técnica em Belo Horizonte (WB Celulares deixa muito a desejar - não tem foco no cliente e pessoal parece ser despreparado: levei meu aparelho para destravar a bandeja de chips, que tinha ficado emperrada no interior do aparelho após inserção do micro SD. Quando fui buscar o aparelho, quiseram entregá-lo para mim sem os chips e sem o micro SD que estavam no aparelho - penso que perderam esses chips! Reclamei com a Motorola e estou aguardando solução. MOTO G ou MOTO Z NUNCA MAIS!"
    # },
    # "10.229": {
    #     "opinions": [
    #         [
    #             "Alto-falante ruim.",
    #             "SOM",
    #             "-"
    #         ]
    #     ],
    #     "review": "Speaker. Review speaker ruim."
    # },
    # "11.001": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Até agora é muito boa.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Até agora é muito boa."
    # },
    # "11.002": {
    #     "opinions": [
    #         [
    #             "Câmera excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Se destaca pela câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Celular muito bom no geral.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo celular. Câmera excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo celular. Câmera excelente. Celular muito bom no geral, se destacando pela câmera."
    # },
    # "11.003": {
    #     "opinions": [
    #         [
    #             "Igual aos outros, a unica coisa que é melhor é que a bateria carrega muito rápido.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Na propaganda diz ter tv digital é mentira.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto. Igual aos outros a unica coisa que é melhor a bateria carrega muito rápido. Na propaganda diz ter tv digital é mentira."
    # },
    # "11.005": {
    #     "opinions": [
    #         [
    #             "Parabéns Shopfacil.com.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "A melhor oferta encontrada e entrega rápida.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente produto. A melhor oferta encontrada e entrega rápida. Parabéns Shopfacil.com."
    # },
    # "11.006": {
    #     "opinions": [
    #         [
    #             "Desempenho fantástico.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Top de linha de verdade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Sempre quis um aparelho da linha S.",
    #             "PRODUTO",
    #             "X"
    #         ],
    #         [
    #             "O S7 tem o tamanho perfeito para não chamar muita atenção.",
    #             "TAMANHO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Top de linha de verdade. Sempre quis um aparelho da linha S e o S7 tem o tamanho perfeito para nao chamar muita atencao e desempenho fantástico."
    # },
    # "11.007": {
    #     "opinions": [
    #         [
    #             "Complicado de encontrar películas compatíveis com a tela toda.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Bordas metalicas riscam com facilidade.",
    #             "DESIGN",
    #             "-"
    #         ],
    #         [
    #             "Botão home ruim.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Produto deixa a desejar.",
    #             "PRODUTO",
    #             "-"
    #         ]
    #     ],
    #     "review": "Qualidade. Produto deixa a desejar, bordas metalicas riscam com facilidade, botão home então nem se fala. Complicado de encontrar películas compatíveis com a tela toda."
    # },
    # "11.008": {
    #     "opinions": [
    #         [
    #             "Bom preço.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Super recomendado.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O Galaxy S7 é um excelente aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Super recomendado. O Galaxy S7 é um excelente aparelho e agora com um bom preço."
    # },
    # "11.009": {
    #     "opinions": [
    #         [
    #             "Otimo!!!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Comprei um S7 ano passado porém perdi, comprei outro igual pois achei maravilhoso!",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Otimo!!! Comprei um S7 ano passado porém perdi, comprei outro igual pois achei maravilhoso!"
    # },
    # "11.010": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Bom."
    # },
    # "11.011": {
    #     "opinions": [
    #         [
    #             "A câmera é espetacular!",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "AMEI!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Por enquanto não tenho do que reclamar, é lindo e cumpre todas as funçoes!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "AMEI! Por enquanto não tenho do que reclamar, é lindo e cumpre todas as funções, e a câmera é espetacular!"
    # },
    # "11.012": {
    #     "opinions": [
    #         [
    #             "Ele é bonito e potente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Nada a reclamar do produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tem sido uma experiência ótima.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Galaxy S7 é um dos tops do mercado.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Galaxy S7 é um dos tops do mercado. Nada a reclamar do produto. Ele é bonito e potente. Tem sido uma experiência ótima."
    # },
    # "11.013": {
    #     "opinions": [
    #         [
    #             "Galaxy S7.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto de otima qualidade, produto feito para durar.",
    #             "RESISTÊNCIA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Galaxy S7. Produto de otima qualidade, produto feito para durar."
    # },
    # "11.014": {
    #     "opinions": [
    #         [
    #             "Muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tinha o s6 e troquei para o s7. Valeu a pena.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom! Tinha o s6 e troquei para o s7. Valeu a pena. Recomendo."
    # },
    # "11.015": {
    #     "opinions": [
    #         [
    #             "Câmera perfeita.",
    #             "CÂMERA",
    #             "++"
    #         ],
    #         [
    #             "Uma otima experiência em jogos.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O melhor celular que tive.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "O melhor celular que tive. Otimo produto uma otima esperiencia em jogos camera perfeita."
    # },
    # "11.016": {
    #     "opinions": [
    #         [
    #             "Vale a pena.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente smartphone, recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Vale a pena. Excelente smartphone, recomendo!"
    # },
    # "11.017": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Bom."
    # },
    # "11.018": {
    #     "opinions": [
    #         [
    #             "Não é o prmeiro produto deste fabricante que compro, so venho me atualizando. Os antigos , que ainda possuo, estao funcionando, limitados pelas novas tecnologias, mas funcionam.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Exelente. Não é o prmeiro produto deste fabricante que compro, so venho me atualizando. Os antigos , que ainda possuo, estao funcionando, limitados pelas novas tecnologias, mas funcionam."
    # },
    # "11.019": {
    #     "opinions": [
    #         [
    #             "Vale o que custa.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo smartphone, recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Vale o que custa. Ótimo smartphone, recomendo!"
    # },
    # "11.020": {
    #     "opinions": [
    #         [
    #             "Muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Mudança do S6 para o S7. Valeu a pena!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom! Mudança do S6 para o S7. Valeu a pena!"
    # },
    # "11.021": {
    #     "opinions": [
    #         [
    #             "Gosto muito da marca Samsung e por isso adquiri este modelo.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Gosto muito da marca Samsung e por isso adquiri este modelo."
    # },
    # "11.022": {
    #     "opinions": [
    #         [
    #             "Excelente bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Bateria dura até 2 dias, muito boa.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Câmera boa.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Processamento rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Só achei um pouco pesado.",
    #             "PESO",
    #             "-"
    #         ],
    #         [
    #             "Bom pra quem gosta de ler, pois a tela é grande.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente bateria. Bateria dura até 2 dias, muito boa. Processamento rápido e câmera boa. Bom pra quem gosta de ler, pois a tela é grande. Só achei um pouco pesado."
    # },
    # "11.023": {
    #     "opinions": [
    #         [
    #             "Sou usuário Samsung a pelo menos 7 anos, recomendo a todos este fabricante, excelente !!!",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Excelente custo beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Top de linha.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Top de linha, excelente custo beneficio. Sou usuário Samsung a pelo menos 7 anos, recomendo a todos este fabricante, excelente !!!"
    # },
    # "11.024": {
    #     "opinions": [
    #         [
    #             "Desempenho imbatível.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Exelente acabamento.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Otimo em tudo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo em tudo! Exelente acabamento, desempenho imbatível."
    # },
    # "11.025": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Ótimo."
    # },
    # "11.026": {
    #     "opinions": [
    #         [
    #             "Estou impressionado com o desempenho do celular!",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo produto. Estou impressionado com o desempenho do celular!"
    # },
    # "11.027": {
    #     "opinions": [
    #         [
    #             "No momento posso dizer q a bateria não dura como especificado no produto.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "O produto no geral é bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou feliz com ele por enquanto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tenho o produto a pouco tempo pra fazer uma avaliação mais detalhada.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "O produto no geral é bom. Tenho o produto a pouco tempo pra fazer uma avaliação mais detalhada. No momento posso dizer q a bateria não dura como especificado no produto. Mas to feliz com ele por enquanto."
    # },
    # "11.028": {
    #     "opinions": [
    #         [
    #             "OTIMA.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "APROVADO.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "APROVADO. OTIMA."
    # },
    # "11.029": {
    #     "opinions": [
    #         [
    #             "Rapido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Excelente acabamento.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Excelente!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Amigável.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente! Amigável, rapido, excelente acabamento."
    # },
    # "11.031": {
    #     "opinions": [
    #         [
    #             "Caro.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Poderia custar mais barato.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não tenho mais.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Bom e caro. Excelente celular, mas não tenho mais. Poderia custar mais barato."
    # },
    # "11.032": {
    #     "opinions": [
    #         [
    #             "Produto otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Imagem top.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto otimo. Imagem top."
    # },
    # "11.033": {
    #     "opinions": [
    #         [
    #             "Otimo aparelho!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Por enquanto estou muito satisfeito!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo aparelho! Por enquanto estou muito satisfeito!"
    # },
    # "11.036": {
    #     "opinions": [
    #         [
    #             "Trava, mesmo que raramente.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Esquenta muito com os dados móveis ligados.",
    #             "DESEMPENHO",
    #             "-"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O celular é bom, no geral.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Exceto pela durabilidade e desempenho, o celular é excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Frágil.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "Na primeira semana de uso já ralou facilmente.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Bom, porem frágil. O celular é bom, no geral. Entretanto, na primeira semana de uso já ralou facilmente, esquenta muito com os dados móveis ligados e trava, mesmo que raramente. O resto o celular é excelente."
    # },
    # "11.037": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Samsung S7. Muito bom."
    # },
    # "11.038": {
    #     "opinions": [
    #         [
    #             "Poderia ser mais barato.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "O aparelho poderia ser um pouco mais barato.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Celular bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Antes eu tinha um S4. Foi um salto de qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou com o aparelho há menos de um mês e até agora estou gostando muito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Poderia ser mais resistente.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "Comprei uma capa reforçada p/ protege-lo contra impactos e evitar danos pois falam da fragilidade do Aparelho.",
    #             "RESISTÊNCIA",
    #             "."
    #         ]
    #     ],
    #     "review": "Celular Bom mas poderia ser mais barato e resistente. Estou com o aparelho a menos de um mes e até agora estou gostando muito. Antes eu tinha um S4. Foi um salto de qualidade. Comprei uma capa reforçada p/ protege-lo contra impactos e evitar danos pois falam da fragilidade do Aparelho. O aparelho poderia ser um pouco mais barato."
    # },
    # "11.039": {
    #     "opinions": [
    #         [
    #             "Adorei!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Adorei!"
    # },
    # "11.040": {
    #     "opinions": [
    #         [
    #             "A bateria, comigo, dura um dia inteiro de uso moderado, ou dez horas de uso intenso, o que satisfaz minhas necessidades.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "A câmera é ótima para fotos em alta velocidade.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "A qualidade da imagem com pouca luz impressiona.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "O sistema é estável, rápido e sem firulas.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O hardware é potente e passa a impressão de que durará vários anos sem se tornar obsoleto.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O preço é alto, mas eu espero que a durabilidade compense o alto investimento.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Um celular de ponta pra durar varios anos.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um celular de ponta pra durar varios anos. O sistema é estável, rápido e sem firulas. O hardware é potente e passa a impressão de que durará vários anos sem se tornar obsoleto. A câmera é ótima para fotos em alta velocidade. A qualidade da imagem com pouca luz também impressiona. A bateria, comigo, dura um dia inteiro de uso moderado, ou dez horas de uso intenso, O que satisfaz minhas necessidades. O preço é alto, Mas eu espero que a durabilidade compense o alto investimento."
    # },
    # "11.041": {
    #     "opinions": [
    #         [
    #             "PRODUTO COM O PROCESSADOR MUITO RAPIDO.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. PRODUTO COM O PROCESSADOR MUITO RAPIDO."
    # },
    # "11.042": {
    #     "opinions": [
    #         [
    #             "Câmera impressionante.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Mostrou-se muito rápido, em meu uso nunca travou.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Design discreto, não chama tanto a atenção quanto o Edge.",
    #             "DESIGN",
    #             "."
    #         ],
    #         [
    #             "Agora com o lançamento do S8 e consequente queda de preço tornou-se um dos melhores custo-benefício do mercado.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho premium.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Aparelho premium, com câmera impressionante. Design discreto, não chama tanto a atenção quanto o Edge. Mostrou-se muito rápido, em meu uso nunca travou. Agora com o lançamento do S8 e consequente queda de preço tornou-se um dos melhores custo-benefício do mercado."
    # },
    # "11.043": {
    #     "opinions": [
    #         [
    #             "Bateria excelente.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Câmera excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Desempenho excelente.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Design excelente.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Sensor de digital excelente.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Curti dmais.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adquiri em menos de um mês, a experiência esta sendo ótima.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Curti dmais. Adquiri em menos de um mês, a experiência esta sendo ótima. Câmera, sensor de digital, desing, desempenho e bateria excelentes."
    # },
    # "11.044": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Cumpre tudo o que se espera do aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Cumpre tudo o que se espera do aparelho."
    # },
    # "11.045": {
    #     "opinions": [
    #         [
    #             "Com a atualizacao a bateria deu uma diminuída na duração.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Com a atualizacao o zoom da camera infelizmente perde a definição.",
    #             "CÂMERA",
    #             "-"
    #         ],
    #         [
    #             "Excelência em smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A melhor experiência com smartphone flagship.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fora a bateria e o zoom, com certeza o melhor até agora.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelência em smartphone. A melhor experiência com smartphone flagship. Com a atualizacao a bateria deu uma diminuída na duração, e o zoom da camera infelizmente perde a definição, Fora isso, com certeza o melhor até agora."
    # },
    # "11.046": {
    #     "opinions": [
    #         [
    #             "A memória é ótima e ainda é expansível.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "A câmera tem muita qualidade.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Troquei um iPhone 5S pelo Galaxy S7 e estou muito satisfeita.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A tela tem muita qualidade.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom! Troquei um iPhone 5S pelo Galaxy S7 e estou muito satisfeita. A tela e a câmera têm muita qualidade. A memória é ótima e ainda é expansível."
    # },
    # "11.047": {
    #     "opinions": [
    #         [
    #             "Ótimo celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gosto bastante! Celular muito rápido!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo celular. Gosto bastante! Celular muito rápido!"
    # },
    # "11.048": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei de tudo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Minha mãe já tinha um e resolvi comprar também.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Excelente. Gostei de tudo, minha mãe já tinha um e resolvi comprar também."
    # },
    # "11.050": {
    #     "opinions": [
    #         [
    #             "Bateria muito boa.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Camera muito boa.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Jogabilidade excelente.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Rápido ótima velocidade de processamento.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "100%.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Rápido ótima velocidade de processamento. Jogabilidade excelente, bateria muito boa, camera muito boa. 100%."
    # },
    # "11.051": {
    #     "opinions": [
    #         [
    #             "O problema pra mim é a bateria.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "A câmera é excepcional.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Smartphone muito bom, o processador até agora não decepcionou.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O problema pra mim é não ser dual chip.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "O problema pra mim é o custo.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Bom produto, apesar do custo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom produto, apesar do custo. Smartphone muito bom, o processador até agora não decepcionou. A câmera é excepcional. O problema pra mim é a bateria, custo e não ser dual chip."
    # },
    # "11.052": {
    #     "opinions": [
    #         [
    #             "Top.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Top."
    # },
    # "11.053": {
    #     "opinions": [
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito boa.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Muito boa."
    # },
    # "11.054": {
    #     "opinions": [
    #         [
    #             "Quase perfeito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O melhor smartphone que já usei.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Quase perfeito. O melhor smartphone que já usei."
    # },
    # "11.055": {
    #     "opinions": [
    #         [
    #             "Excelentes câmeras.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Elegante (em vidro).",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Vale todo o investimento para quem busca um produto premium.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Incrível!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um produto fantástico.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A linha Galaxy S7, é simplesmente poderosa e perfeita em sua montagem Software - Hardware.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Android funcional e leve.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Incrível! Um produto fantástico. A linha Galaxy S7, é simplesmente poderosa e perfeita em sua montagem Software - Hardware. Elegante (em vidro, com um Android funcional e leve, excelentes câmeras, vale todo o investimento para quem busca um produto premium."
    # },
    # "11.056": {
    #     "opinions": [
    #         [
    #             "Ótima câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Potente.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "De outro mundo!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O Galaxy S7 não decepciona.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uma experiência incrível na forma de celular! Simplesmente lindo e incrível, a linha S7 é fantástica.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Android super funcional e leve.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "De outro mundo! Uma experiência incrível na forma de celular! Simplesmente lindo e incrível, a linha S7 é fantástica. Potente e com ótima câmera, e um Android super funcional e leve, o Galaxy S7 não decepciona."
    # },
    # "11.058": {
    #     "opinions": [
    #         [
    #             "Recomendo Samsung S7.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou usando a menos de 1 mês. Mas o produto cumpre tudo que prometeu.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Recomendo Samsung S7. Estou usando a menos de 1 mês. Mas o produto cumpre tudo que prometeu."
    # },
    # "11.059": {
    #     "opinions": [
    #         [
    #             "S7 ÓTIMO.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A PLATAFORMA ANDROIDE DA SAMSUNG É IMBATÍVEL!",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "S7 ÓTIMO. A PLATAFORMA ANDROIDE DA SAMSUNG É IMBARÍVEL!"
    # },
    # "11.060": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Excelente."
    # },
    # "11.061": {
    #     "opinions": [
    #         [
    #             "Processador poderoso.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Qualidade Samsung.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótima tela.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Qualidade Samsung. Aparelho bonito, processador poderoso, ótima tela."
    # },
    # "11.062": {
    #     "opinions": [
    #         [
    #             "Excelente custo beneficio...",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Excelente custo beneficio..."
    # },
    # "11.063": {
    #     "opinions": [
    #         [
    #             "Um ponto negativo é não achar em lugar nenhum película protetora de tela pro modelo flat.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Bateria meia boca.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "A bateria é um lixo e antes das 15hs eu já preciso recarregar.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "O aparelho é fantástico e não trava.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Caríssimo.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "É caro demais.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Paguei R$ 2.000 porque realmente eu precisava de um aparelho TOP, uma vez que meu S5 travava demais. Mas só indico gastar essa pequena fortuna pra quem dependa de um celular de alta performance ou quem esteja nadando no dinheiro.",
    #             "PREÇO",
    #             "-."
    #         ],
    #         [
    #             "Ótimo Aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não me arrependo não.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo Aparelho. Porém Caríssimo, Bateria meia boca. O aparelho é fantástico e não trava. Porém, a bateria é um lixo e antes das 15hs eu já preciso recarregar. Além disso, é caro demais. Paguei R$ 2.000 porque realmente eu precisava de um aparelho TOP, uma vez que meu S5 travava demais. Mas só indico gastar essa pequena fortuna pra quem dependa de um celular de alta performance ou quem esteja nadando no dinheiro.Outro ponto negativo é não achar em lugar nenhum película protetora de tela pro modelo flat.Não me arrependo não."
    # },
    # "11.064": {
    #     "opinions": [
    #         [
    #             "A bateria não aguenta a tela e o processador em uso prolongado.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Ótima câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "É rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Muito bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "A R$2200,00 na promoção da Fast, é o melhor custo-benefício do mercado até o momento.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Em seu preço original de $4200,00, não vale a pena.",
    #             "PREÇO",
    #             "-."
    #         ],
    #         [
    #             "Funcional.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O S7 Edge é um telefone excepcional.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ponto de duvida é durabilidade: Samsung é famosa por ter perda sensível de performance depois de 6 meses. Vamos ver nele como vai.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Na promoção da Fast Shop vale a pena. O S7 Edge é um telefone excepcional que, a R$2200,00 na promoção da Fast, é o melhor custo-benefício do mercado até o momento. Em seu preço original de $4200,00 não mesmo. É rápido, muito bonito, funcional, ótima câmera. A bateria não aguenta a tela e o processador em uso prolongado. Ponto de duvida é durabilidade: Samsung é famosa por ter perda sensível de performance depois de 6 meses. Vamos ver nele como vai."
    # },
    # "11.065": {
    #     "opinions": [
    #         [
    #             "Tem uma bateria que, se utilizada corretamente, pode durar até 24h.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "A camera é sensacional!",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Não decepciona.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O Galaxy S7 é surpreendente",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Não decepciona. O Galaxy S7 é surpreendente com uma bateria que, se utilizada corretamente, pode durar até 24h. A camera é sensacional!"
    # },
    # "11.066": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei do celular conforme minhas expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Gostei do celular conforme minhas expectativas."
    # },
    # "11.067": {
    #     "opinions": [
    #         [
    #             "Econômico na bateria!",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Rápido!",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Interface mais fluida que a versão anterior.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Samsung Galaxy S7. Interface mais fluida que a versão anterior, rápido e econômico na bateria!"
    # },
    # "11.068": {
    #     "opinions": [
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Otimo."
    # },
    # "11.069": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Muito bom."
    # },
    # "11.070": {
    #     "opinions": [
    #         [
    #             "Capacidade de armazenamento muito bom...",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Tem ótima resposta (tempo)",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Comparando com outro Galaxy que tive anteriormente, esse aparelho ainda não travou..",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Ótima aquisição.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótima aquisição. Comparando com outro Galaxy que tive anteriormente, esse aparelho ainda não travou.. Tem ótima resposta (tempo, capacidade de armazenamento muito bom..."
    # },
    # "11.071": {
    #     "opinions": [
    #         [
    #             "As fotos são perfeitas.",
    #             "CÂMERA",
    #             "++"
    #         ],
    #         [
    #             "O aparelho não trava.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O aparelho é bastante rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O aparelho é bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Excelente celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tenho o celular há pouco tempo, mas estou muito satisfeita.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O aparelho é de fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente celular. Tenho o celular há pouco tempo, mas estou muito satisfeita. As fotos são perfeitas. O aparelho é bonito, não trava, é bastante rápido e de fácil manuseio."
    # },
    # "11.072": {
    #     "opinions": [
    #         [
    #             "A cor prata é bem enjoativa.",
    #             "DESIGN",
    #             "-"
    #         ]
    #     ],
    #     "review": "Cor. A cor prata é bem enjoativa."
    # },
    # "11.073": {
    #     "opinions": [
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Produto excelente."
    # },
    # "11.074": {
    #     "opinions": [
    #         [
    #             "Tira fotos surpreendentes.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Tem um acabamento perfeito.",
    #             "DESIGN",
    #             "++"
    #         ],
    #         [
    #             "Sensacional.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Possui uma ótima tela.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Sensacional. Tira fotos surpreendentes, possui uma ótima tela e tem um acabamento perfeito."
    # },
    # "11.075": {
    #     "opinions": [
    #         [
    #             "Bom! A ROM da Samsung me surpreendeu... Minhas experiências anteriores com Samsung se resumiam em hardware muito bom, mas com ROM sofrível de tanto lixo que colocavam. Para o S7, a ROM está limpa, poderia ser um pouco mais, mas está bom!",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom! A ROM da Samsung me surpreendeu... Minhas experiências anteriores com Samsung se resumiam em hardware muito bom, mas com ROM sofrível de tanto lixo que colocavam. Para o S7, a ROM está limpa, poderia ser um pouco mais, mas está bom!"
    # },
    # "11.076": {
    #     "opinions": [
    #         [
    #             "Satisfeito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Interface diferente dos demais androids, porém é agradável.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Satisfeito. Interface diferente dos demais androids, porém é agradável."
    # },
    # "11.077": {
    #     "opinions": [
    #         [
    #             "Câmera espetacular.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Sua câmera é excelente, principalmente em situações com baixa luminosidade.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Celular de acordo com todas as espectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Câmera espetacular. Celular de acordo com todas as espectativas, sua câmera é excelente, principalmente em situações com baixa luminosidade."
    # },
    # "11.078": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom."
    # },
    # "11.079": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Celular como qualquer outro nesta faixa de preço, troquei meu Nexus por ele, demorei um pouco para acostumar, mas é bom...",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Bom. Celular como qualquer outro nesta faixa de preço, troquei meu Nexus por ele, demorei um pouco para acostumar, mas é bom..."
    # },
    # "11.080": {
    #     "opinions": [
    #         [
    #             "Bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Samsung s7. Bom produto."
    # },
    # "11.081": {
    #     "opinions": [
    #         [
    #             "Excelente câmera frontal.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Celular muito rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Celular muito rápido e com excelente câmera frontal. Recomendo."
    # },
    # "11.082": {
    #     "opinions": [
    #         [
    #             "O S7 aceita SD mas não expande a memória interna.",
    #             "ARMAZENAMENTO",
    #             ".."
    #         ],
    #         [
    #             "Algumas pessoas falam da bateria, mas pra mim está durando um dia inteiro.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "As câmeras são boas.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "A velocidade de processamento é boa.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O NFC não é compatível com os cartões Mirafire, ou seja não é compatível com o aplicativo da SPTrans e tantas outras aplicações que utilizam este cartão.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "É tudo de bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A princípio um celular bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um celular quase TOP.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Deixei de comprar o S6 para pegar um mais atual. O celular regrediu. O S6 tinha Infravermelho e podia emular controles remotos, o S7 não tem mais.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "A resolução da tela é ótima.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um celular quase TOP. A princípio um celular bom. Deixei de comprar o S6 para pegar um mais atual. O celular regrediu. O S6 tinha Infravermelho e podia emular controles remotos, o S7 não tem mais. O S7 aceita SD mas não expande a memória interna. O NFC não é compatível com os cartões Mirafire, ou seja não é compatível com o aplicativo da SPTrans e tantas outras aplicações que utilizam este cartão. A resolução da tela é ótima. As câmeras são boas, a velocidade de processamento é boa, enfim o resto é tudo de bom. Algumas pessoas falam da bateria, mas pra mim está durando um dia inteiro."
    # },
    # "11.083": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Até agora ta bem bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Até agora ta bem bom."
    # },
    # "11.084": {
    #     "opinions": [
    #         [
    #             "Ótimo superou minha expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Inigualável.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Ótimo superou minha expectativas. Inigualável."
    # },
    # "11.085": {
    #     "opinions": [
    #         [
    #             "Bateria dura mais que um dia (é só não instalar o Facebook rsss)",
    #             "BATERIA",
    #             "+."
    #         ],
    #         [
    #             "Câmera ótima.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Performance excelente.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Completíssimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não tem nada que falte neste celular.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Não tem modelo melhor no mercado brasileiro que o S7 e seu irmão maior, o Edge.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "À prova d'água.",
    #             "RESISTÊNCIA",
    #             "+."
    #         ],
    #         [
    #             "Tela grande com melhor qualidade do mercado.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Completíssimo. Não tem nada que falte neste celular: câmera ótima, performance excelente, bateria dura mais que um dia (é só não instalar o Facebook rsss, tela grande com melhor qualidade do mercado, à prova d'água. Não tem modelo melhor no mercado brasileiro que o S7 e seu irmão maior, o Edge."
    # },
    # "11.086": {
    #     "opinions": [
    #         [
    #             "Duração da bateria me surpreende. Uso muito o aparelho.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Câmera me surpreende.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Aparelho rápido.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tinha um Iphone 6 e a baixa duração da bateria me fez procurar outra solução. Queria manter num top de linha e peguei o S7.",
    #             "PRODUTO",
    #             "X"
    #         ],
    #         [
    #             "Realmente resistente a água.",
    #             "RESISTÊNCIA",
    #             "+."
    #         ],
    #         [
    #             "Quanto ao software, muito poluído. Poderia ser mais simples. Mas acredito que em breve me adaptarei ao produto, e essa questão será passado.",
    #             "SISTEMA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Aparelho rápido. Tinha um Iphone 6 e a baixa duração da bateria me fez procurar outra solução. Queria manter num top de linha e peguei o S7. Quanto ao software, muito poluído. Poderia ser mais simples. Mas acredito que em breve me adaptarei ao produto, e essa questão será passado. Realmente resistente a água e a câmera e a duração da bateria me surpreende. Uso muito o aparelho."
    # },
    # "11.088": {
    #     "opinions": [
    #         [
    #             "O melhor da Samsung.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "O melhor que a Samsung já conseguiu montar, celular perfeito para todos os usuários.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "O melhor da Samsung. O melhor que a Samsung já conseguiu montar, celular perfeito para todos os usuários."
    # },
    # "11.089": {
    #     "opinions": [
    #         [
    #             "Câmera sensacional.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Processador brutal.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Design invocado.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Vários outros recursos positivos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Mesmo sendo de 2016, ainda vale muito a pena!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Sensacional!",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "O melhor smartphone que tive.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Tela espetacular.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Sensacional! O melhor smartphone que tive. Design invocado, tela espetacular, processador brutal, câmera sensacional e vários outros recursos positivos. Mesmo sendo de 2016, ainda vale muito a pena!"
    # },
    # "11.090": {
    #     "opinions": [
    #         [
    #             "SUPER RECOMENDO, POIS A BATERIA DE TODOS SÃO RUINS, NO MAIS ELE É MARAVILHOSO.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "MEU S7. SUPER RECOMENDO, POIS A BATERIA DE TODOS SÃO RUINS, NO MAIS ELE É MARAVILHOSO."
    # },
    # "11.091": {
    #     "opinions": [
    #         [
    #             "Otima.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otima."
    # },
    # "11.093": {
    #     "opinions": [
    #         [
    #             "Adorei o design.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Leve.",
    #             "PESO",
    #             "+"
    #         ],
    #         [
    #             "Celular ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Só não deixe cair, quebra fácil.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "Fino.",
    #             "TAMANHO",
    #             "+"
    #         ],
    #         [
    #             "Super fácil de mexer.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Celular ótimo. Adorei o design, super fácil de mexer, fino e leve. Só não deixe cair, quebra fácil."
    # },
    # "11.094": {
    #     "opinions": [
    #         [
    #             "O unico defeito é que a películas protetoras disponíveis no mercado não protegem toda a tela por conta do design ligeiramente curvo.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Velocidade de processamento boa.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Design agradável.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Excelente!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Celular muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Celular muito bom. Velocidade de processamento boa e design agradável.O unico defeito é que a películas protetoras disponíveis no mercado não protegem toda a tela por conta do design ligeiramente curvo. De mais, excelente!"
    # },
    # "11.095": {
    #     "opinions": [
    #         [
    #             "Excelente celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito satisfeito com o aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente celular. Muito satisfeito com o aparelho."
    # },
    # "11.096": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou muito satisfeito com o celular.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Estou muito satisfeito com o celular. Recomendo."
    # },
    # "11.097": {
    #     "opinions": [
    #         [
    #             "Boa câmera",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Bom desempenho.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Um bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Boas funcionalidades.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom produto. Um bom produto, com um bom desempenho, câmera e funcionalidades."
    # },
    # "11.100": {
    #     "opinions": [
    #         [
    #             "A câmera é excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei muito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo muito este produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um dos melhores smartphones do mercado.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tela fantástica.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Recomendo muito este produto. Um dos melhores smartphones do mercado. A câmera é excelente e a tela fantástica. Gostei muito."
    # },
    # "11.101": {
    #     "opinions": [
    #         [
    #             "Comparando com S4 e S5 tem mais memória...",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Comparando com S4 e S5, a bateria dura muito mais...",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Comparando com S4 e S5, é muito mais rápido...",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Não tem aquela portinha chata do S5.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Funciona muito bem.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É à prova d'água mesmo.",
    #             "RESISTÊNCIA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Aparelho muito bom! Funciona muito bem. Comparando com S4 e S5, é muito mais rápido, tem mais memória e a bateria dura muito mais. Não tem aquela portinha chata do S5. É à prova d'água mesmo."
    # },
    # "11.102": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Nada a reclamar.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Nada a reclamar."
    # },
    # "11.103": {
    #     "opinions": [
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom!!!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Muito bom!!!"
    # },
    # "11.104": {
    #     "opinions": [
    #         [
    #             "Espaço perfeito!",
    #             "ARMAZENAMENTO",
    #             "++"
    #         ],
    #         [
    #             "A bateria é misteriosa, hora parece que nunca acabará, já em outros momentos, não dura nada..",
    #             "BATERIA",
    #             "-."
    #         ],
    #         [
    #             "Uma ótima câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "RAM perfeita!",
    #             "DESEMPENHO",
    #             "++"
    #         ],
    #         [
    #             "Velocidade do processador perfeito!",
    #             "DESEMPENHO",
    #             "++"
    #         ],
    #         [
    #             "Design perfeito...",
    #             "DESIGN",
    #             "++"
    #         ],
    #         [
    #             "Leitor de digital super rápido.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Liberdade para configurar o aparelho do jeito que quiser...",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Infelizmente a memória interna não permite mudar a maioria dos aplicativos para a memória externa..",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A tela perfeita.",
    #             "TELA",
    #             "++"
    #         ]
    #     ],
    #     "review": "Ótimo produto. Ótimo produto, velocidade do processador e espaço em RAM perfeitos! Infelizmente a memória interna não permite mudar a maioria dos aplicativos para a memória externa.. A bateria é misteriosa, hora parece que nunca acabará, já em outros momentos, não dura nada.. Porém, design perfeito, a tela perfeita, uma ótima câmera, leitor de digital super rápido, e liberdade para configurar o aparelho do jeito que quiser..."
    # },
    # "11.105": {
    #     "opinions": [
    #         [
    #             "Galaxy s7.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Satisfeita.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Galaxy s7. Satisfeita."
    # },
    # "11.106": {
    #     "opinions": [
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Melhor aparelho que ja usei.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Melhor aparelho que ja usei. Excelente produto acessórios um pouco carros para ter todos, mais o óculos foi brinde foi menos um para compra, a capa que protege a lente e um pouco frágil."
    # },
    # "11.107": {
    #     "opinions": [
    #         [
    #             "Um ótimo aparelho!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Reune uma gama imensa de recursos em um unico aparelho, corrigindo problemas que tinham as versões anteriores.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uma versão top dos aparelhos da samsung, que hoje está com um ótimo custo/benefício comparando com os concorrentes.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um ótimo aparelho! Uma versão top dos aparelhos da samsung, que hoje está com um ótimo custo/benefício comparando com os concorrentes. Reune uma gama imensa de recursos em um unico aparelho, corrigindo problemas que tinham as versões anteriores."
    # },
    # "11.108": {
    #     "opinions": [
    #         [
    #             "Ainda não recebi a distribuidora não apareceu com celular ainda. Diz que vieram mas não apareceram não.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Caro.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Celular bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Celular bom. Porem caro. Ainda não recebi a distribuidora não apareceu com celular ainda. Diz que vieram mas não apareceram não."
    # },
    # "11.109": {
    #     "opinions": [
    #         [
    #             "Ótima bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Carrega rápido.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Câmera top.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Ótima performance.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "GS7, fantástico.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Melhor que ele só os da próxima geração que ainda não chegaram aqui (LG G6, Galaxy S8, etc.).",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não falta nada no celular.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "GS7, fantástico. Não falta nada no celular: ótima performance, bateria, carrega rápido, câmera é top. Melhor que ele só os da próxima geração que ainda não chegaram aqui (LG G6, Galaxy S8, etc.."
    # },
    # "11.110": {
    #     "opinions": [
    #         [
    #             "Não trava nunca e isso é essencial.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Satisfeita com a compra.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Satisfeita com a compra. Não trava nunca e isso é essencial."
    # },
    # "11.111": {
    #     "opinions": [
    #         [
    #             "Câmera excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muitas funções.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Compra recomendada.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente aparelho. Muito bom. Rápido, câmera excelente,muitas funções. Compra recomendada."
    # },
    # "11.112": {
    #     "opinions": [
    #         [
    #             "Eu tinha um iphone e pelo alto custo optei pela S7 Samsung.",
    #             "PREÇO",
    #             "+."
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fiquei muito satisfeita!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Eu tinha um iphone e pelo alto custo optei pela S7 Samsung. Fiquei muito satisfeita!"
    # },
    # "11.113": {
    #     "opinions": [
    #         [
    #             "Boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Boa."
    # },
    # "11.114": {
    #     "opinions": [
    #         [
    #             "Rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom, excelente produto. Me surpreendeu.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Troquei um S4 octa core por esse S7. Estava muito satisfeito com o antigo, porém esse aparelho conseguiu me surpreender em todos os aspectos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fácil de usar",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom, excelente produto. Me surpreendeu. Troquei um S4 octa core por esse S7. Estava muito satisfeito com o antigo, porém esse aparelho conseguiu me surpreender em todos os aspectos. Muito bom aparelho. Rápido, fácil de usar etc."
    # },
    # "11.115": {
    #     "opinions": [
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O melhor de todos, sem mais.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Ótimo. O melhor de todos, sem mais."
    # },
    # "11.116": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Particularmente, prefiro do que os IPhone.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Particularmente, prefiro do que os IPhone."
    # },
    # "11.117": {
    #     "opinions": [
    #         [
    #             "Produto de qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Supera as expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto de boa qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto de qualidade. Produto de boa qualidade, supera as expectativas."
    # },
    # "11.118": {
    #     "opinions": [
    #         [
    #             "Muito bom e preciso.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda não possui um só vi o do meu amigo.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Muito bom e preciso. Ainda não possui um só vi o do meu amigo."
    # },
    # "11.119": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Ótimo smartphone."
    # },
    # "11.120": {
    #     "opinions": [
    #         [
    #             "Câmera bacana.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Sem travamentos, câmera bacana.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Satisfeito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto atende às expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Satisfeito. Produto atende às expectativas, sem travamentos, câmera bacana."
    # },
    # "11.121": {
    #     "opinions": [
    #         [
    #             "Boa duração de bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Câmera fantástica.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Rápido",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Compra recomendada.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente aparelho. Aparelho muito bom, câmera fantástica. Rápido e com boa duração de bateria. Compra recomendada."
    # },
    # "11.122": {
    #     "opinions": [
    #         [
    #             "A possibilidade de expansão de memória veio a calhar.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Câmera excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Excelente celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou com o aparelho há cerca de duas semanas e estou muito satisfeito até o momento.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fácil de usar.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente celular. Estou com o aparelho há cerca de duas semanas e estou muito satisfeito até o momento. Fácil de usar, câmera excelente, a possibilidade de expansão de memória veio a calhar."
    # },
    # "11.123": {
    #     "opinions": [
    #         [
    #             "A câmera é incrivelmente sensacional.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Ele informa que tipo de ligação você está recebendo (telemarketing / golpe / propaganda) sem uso de um app especial para isso.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "AMEI.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A cada dia o celular me surpreende com funções que facilita no meu meu dia a dia.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "AMEI. A cada dia o celular me surpreende com funções que facilita no meu meu dia a dia. Um exemplo e ele informar que tipo de ligação você está recebendo (telemarketing / golpe / propaganda sem uso de um app especial para isso. A câmera é incrivelmente sensacional."
    # },
    # "11.124": {
    #     "opinions": [
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "S7 Edge. Ótimo."
    # },
    # "11.125": {
    #     "opinions": [
    #         [
    #             "Optei pelo S7 pela possibilidade de utilizar cartao de memoria, o que ja nao era possivel no S6 e quem trabalha com o aparelho e precisa instalar varios apps, alguns podem ser colocados no cartao de memoria, liberando a memoria interna.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Quanto mais vc usa ela descarrega mesmo porem esse modelo usando o carregador dele faz recarga rapida e carrega rapidão (testei com outro carregador e demora mais) Não aconselho.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Bateria é igual de qq smart .",
    #             "BATERIA",
    #             "."
    #         ],
    #         [
    #             "Vamos ver a bateria daqui um tempo.",
    #             "BATERIA",
    #             "x"
    #         ],
    #         [
    #             "Achei as fotos perfeitas, naao vi deferença entre a superioridade que falam do S6 e vamos combinar que se quer fotos profissionais vc deve comprar uma camera fotografica.",
    #             "CÂMERA",
    #             "++"
    #         ],
    #         [
    #             "A entrega foi a JATO pela fast shop. Comprei no sabado e recebi na terça.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "A transferencia dos dados do meu cel ant pra esse foi hiper tranquila em 10 minutos apenas encostando um ap no outro. Uma coisinha ou outra com app da marca mas isso é o de menos.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Tudo de bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tudo show de bola..",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ate agora me surpreendeu..",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uma dica: Coloquem no seguro porque nao é barato!",
    #             "RESISTÊNCIA",
    #             "!"
    #         ]
    #     ],
    #     "review": "Tudo de bom. Bateria é igual de qq smart . Quanto mais vc usa ela descarrega mesmo porem esse modelo usando o carregador dele faz recarga rapida e carrega rapidão (testei com outro carregador e demora mais Não aconselho.Achei as fotos perfeitas, naao vi deferença entre a superioridade que falam do S6 e vamos combinar que se quer fotos profissionais vc deve comprar uma camera fotografica.Optei pelo S7 pela possibilidade de utilizar cartao de memoria, o que ja nao era possivel no S6 e quem trabalha com o aparelho e precisa instalar varios apps, alguns podem ser colocados no cartao de memoria, liberando a memoria internaA transferencia dos dados do meu cel ant pra esse foi hiper tranquila em 10 minutos apenas encostando um ap no outro.Uma coisinha ou outra com app da marca mas isso é o de menos. Ate agora me surpreendeu.. Vamos ver a bateria daqui um tempo.Tudo show de bola.. A entrega foi a JATO pela fast shop. Comprei no sabado e recebi na terça.Uma dica . Coloquem no seguro porque nao é barato!"
    # },
    # "11.126": {
    #     "opinions": [
    #         [
    #             "Ótima bateria.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Fotos de alta resolução.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Equipamento muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Até agora, não vi pontos negativos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou usando o aparelho a 2 semanas, e ate agora tem sido perfeito.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Display de alta resolução.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Equipamento muito bom. Estou usando o aparelho a 2 semanas, e ate agora tem sido perfeito. Rápido, com fotos de alta resolução, ótima bateria, display de alta resolução.Até agora, não vi pontos negativos."
    # },
    # "11.127": {
    #     "opinions": [
    #         [
    #             "Eu procurava um celular veloz. Encontrei.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O leitor de impressões digitais facilita muito o uso e passa tranquilidade pela segurança.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Veloz e com bons recrusos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Eu procurava um celular com uma tela grande. Encontrei.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Veloz e com bons recrusos. Eu procurava um celular veloz com uma tela grande. Encontrei.Além disso, o leitor de impressões digitais facilita muito o uso e passa tranquilidade pela segurança."
    # },
    # "11.128": {
    #     "opinions": [
    #         [
    #             "Muito bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho muito bom recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom produto. Aparelho muito bom recomendo."
    # },
    # "11.129": {
    #     "opinions": [
    #         [
    #             "Excelente câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Acabamento Premium.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Celular muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um perfeito aparelho!",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Celular muito bom! Excelente câmera, acabamento Premium, um perfeito aparelho!"
    # },
    # "11.130": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Particularmente, eu prefiro do que o IPhone.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Muito bom. Particularmente, eu prefiro do que o IPhone."
    # },
    # "11.131": {
    #     "opinions": [
    #         [
    #             "Boa fluidez.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "É um valor caro a se pagar, mas vale a pena.",
    #             "PREÇO",
    #             "+."
    #         ],
    #         [
    #             "otimo Produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bonito e Rápido.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótima tela.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bonito e Rápido. otimo Produto. Boa fluidez e ótima tela. É um valor caro a se pagar, mas vale a pena."
    # },
    # "11.132": {
    #     "opinions": [
    #         [
    #             "Gosto do processamento extremamente rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Atualmente um dos melhores.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Atualmente um dos melhores. Gosto do processamento extremamente rápido."
    # },
    # "11.133": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Nunca me decepcionou.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Nunca me decepcionou."
    # },
    # "11.134": {
    #     "opinions": [
    #         [
    #             "Já sou cliente dos celulares Galaxy eu não troco.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Bom Aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom Aparelho. Já sou cliente dos celulares Galaxy eu não troco."
    # },
    # "11.135": {
    #     "opinions": [
    #         [
    #             "Melhor custo beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Depois de pesquisar, achei que esse seria o melhor custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Melhor custo beneficio. Depois de pesquisar, achei que esse seria o melhor custo benefício."
    # },
    # "11.136": {
    #     "opinions": [
    #         [
    #             "Recomendo o produto e.mbora eu não tenho mas conheço.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda não pude tê-lo.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Recomendo o produto e.mbora eu não tenho mas conheço. Ainda não pude tê-lo."
    # },
    # "11.137": {
    #     "opinions": [
    #         [
    #             "Ele não vem com película protetora, como o J7, e no mercado NÃO existe uma que ajuste 100%, devido a tela ser um pouco curva.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "RECOMENDO ...",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É um smartphone TOP.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "RECOMENDO ... É um smartphone TOP. Só não dei nota máxima, porque ele não vem com película protetora, como o J7, e no mercado NÃO existe uma que ajuste 100%, devido a tela ser um pouco curva."
    # },
    # "11.138": {
    #     "opinions": [
    #         [
    #             "A bateria dura muito e o carregador carrega muito mais rapido que os normais.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Otimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo produto. Produto muito bom, a bateria dura muito e o carregador carrega muito mais rapido que os normais."
    # },
    # "11.139": {
    #     "opinions": [
    #         [
    #             "Peca um pouco na duração de bateria.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Ótimo desempenho.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Peca um pouco no custo benefício.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Ótimo Produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um ótimo Smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo Produto. Um ótimo Smartphone com ótimo desempenho, peca um pouco na duração de bateria e custo benefício."
    # },
    # "11.140": {
    #     "opinions": [
    #         [
    #             "Só não dei 5 estrelas porque devido o mesmo ser curvo, desnecessário, não é possível encontrar no mercado nenhuma película que fica perfeita nele. Ai você escolhe ficar com o aparelho sem proteção, colocar uma película que fica sobrando pelos lados e soltando ou colocar uma que deixa meio centímetro de cada lado sem proteção.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Vale ressaltar que a Samsung me mandou rapidamente o Gear VR SM-R323NBKAZTO e o ponto frio entregou numa rapidez impressionante.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "RECOMENDO ...",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "RECOMENTO ... Só não dei 5 estrelas porque devido o mesmo ser curvo, desnecessário, não é possível encontrar no mercado nenhuma película que fica perfeita nele. Ai você escolhe ficar com o aparelho sem proteção, colocar uma película que fica sobrando pelos lados e soltando ou colocar uma que deixa meio centímetro de cada lado sem proteção. Vale ressaltar que a Samsung me mandou rapidamente o Gear VR SM-R323NBKAZTO e o ponto frio entregou numa rapidez impressionante."
    # },
    # "11.141": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Muito bom."
    # },
    # "11.142": {
    #     "opinions": [
    #         [
    #             "Prudoto bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente produto para o uso do dia a dia.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Prudoto bom. Excelente produto para o uso do dia a dia."
    # },
    # "11.143": {
    #     "opinions": [
    #         [
    #             "Bateria excelente!",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Camera excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Não há do que reclamar! Só isso!",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Depois do S6, comprei o S7.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Depois do S6, comprei o S7. Não há do que reclamar! Só isso! Camera excelente, bateria excelente!"
    # },
    # "11.144": {
    #     "opinions": [
    #         [
    #             "Maravilhosa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "The Best.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "The Best. Maravilhosa."
    # },
    # "11.146": {
    #     "opinions": [
    #         [
    #             "É um ótimo aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Eu já possuia o S7 Edge e resolvi comprar o S7 como alternativa porque gostei da experiência.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "É um ótimo aparelho. Eu já possuia o S7 Edge e resolvi comprar o S7 como alternativa porque gostei da experiência."
    # },
    # "11.147": {
    #     "opinions": [
    #         [
    #             "Câmara excelente.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Moderno.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Rápido e moderno. Câmara excelente."
    # },
    # "11.148": {
    #     "opinions": [
    #         [
    #             "Excelente!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O aparelho corresponde as expectativas, estou muito feliz em ter comprado este produto!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente! O aparelho corresponde as expectativas, estou muito feliz em ter comprado este produto!"
    # },
    # "11.149": {
    #     "opinions": [
    #         [
    #             "Poderia ter um pouco mais de memória.",
    #             "ARMAZENAMENTO",
    #             "-"
    #         ],
    #         [
    #             "A bateria poderia durar mais.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Câmara ótima.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Aparelho muito rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Leve.",
    #             "PESO",
    #             "+"
    #         ],
    #         [
    #             "Excelente produto!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente produto! Aparelho muito rápido, bonito, leve e com uma câmara ótima. A bateria poderia durar mais e também ter um pouco mais de memória."
    # },
    # "11.150": {
    #     "opinions": [
    #         [
    #             "Otimo celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo celular. Muito bom aparelho."
    # },
    # "11.151": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Muito bom aparelho."
    # },
    # "11.152": {
    #     "opinions": [
    #         [
    #             "Moderno.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O custo é alto, mas ainda é menor do que dia iPhone equivalentes.",
    #             "PREÇO",
    #             "+."
    #         ],
    #         [
    #             "Rápido.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Smartphone muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Smartphone muito bom. Moderno e rápido. O custo é alto, mas ainda é menor do que dia iPhone equivalentes."
    # },
    # "11.153": {
    #     "opinions": [
    #         [
    #             "A duração da bateria não é tão boa quanto deveria. Tem dias que dura apenas 10 horas de uso moderado.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "A câmera traseira é muito boa, porém em condições de baixa luminosidade a perda de qualidade é absurda.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Os apps não travam nem engasgam.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O celular possui design bastante sofisticado, com as bordas metálicas e todo revestido de vidro.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "As bordas metálicas e revestimento de vidro trazem um desconforto relacionado às impressões digitais que marcam todo o aparelho.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Para evitar marcas de digitais comprei uma capa da ClearView da própria Samsung.",
    #             "DESIGN",
    #             "+."
    #         ],
    #         [
    #             "Baixo custo-benefício (como os demais high-ends)",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "O preço ainda é salgado, como tudo que é bom no Brasil. Nada de novidade neste quesito.",
    #             "PREÇO",
    #             "-."
    #         ],
    #         [
    #             "Um ótimo smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "No geral, é um ótimo smartphone, realmente topo de linha.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um ótimo smartphone, porém com baixo custo-benefício (como os demais high-ends O celular possui design bastante sofisticado, com as bordas metálicas e todo revestido de vidro. Isso, porém, traz um desconforto relacionado às impressões digitais que marcam todo o aparelho. Para evitar isso comprei uma capa da ClearView da própria Samsung. A câmera traseira é muito boa, porém em condições de baixa luminosidade a perda de qualidade é absurda. O mesmo para a câmera traseira, guardadas as devidas proporções. Os apps não travam nem engasgam. A duração da bateria não é tão boa quanto deveria. Tem dias que dura apenas 10 horas de uso moderado. O preço ainda é salgado, como tudo que é bom no Brasil. Nada de novidade neste quesito. No mais, é um ótimo smartphone, realmente topo de linha."
    # },
    # "11.154": {
    #     "opinions": [
    #         [
    #             "Show.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adorei o aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Show. Adorei o aparelho."
    # },
    # "11.155": {
    #     "opinions": [
    #         [
    #             "Um pouco mais caro que a maioria porém vale cada centavo.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Excelente smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Perfeito.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Perfeito. Excelente smartphone, um pouco mais caro que a maioria porém vale cada centavo."
    # },
    # "11.156": {
    #     "opinions": [
    #         [
    #             "Vai um conselho: NÃO COMPREM NA SARAIVA !!!! Comprei celular que chegou com defeito de recepção de sinais, enviei imediatamente para troca. SARAIVA informou que não pode proceder a troca, pois eu tinha quebrado a trava do chip. Não quebrei nenhuma trava, e por que não analisar a possibilidade da trava ter sido quebrada na SARAIVA após o retorno. Por que não acreditar na palavra de um cliente idôneo. Instalar um chip no celular não é nada complexo para ninguém, nem pra eu como engenheiro. Se tivesse quebrado trava e utilizasse de má fé como afirmam teria enviado o produto para a troca informando que recebi o produto quebrado !!!! Mas não adianta não querem escutar os argumentos, não consegue falar com supervisor/ gerente que poderia refletir sobre a decisão ( só atendentes te atendem e só respondem o que for determinado ), não recebem e-mails pelo atendimento@saraiva.com ( servidor responde haver problema na entrega ???? ) , reclamações pelo site não são respondidos formalmente. Vou ter que consertar o celular ( perdi a garantia ) por um dano causado no retorno do celular para a SARAIVA. Então Vai um conselho : NÃO COMPREM NA SARAIVA !",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Vai um conselho: NÃO COMPREM NA SARAIVA !!!! Vai um conselho: NÃO COMPREM NA SARAIVA !!!! Comprei celular que chegou com defeito de recepção de sinais, enviei imediatamente para troca. SARAIVA informou que não pode proceder a troca, pois eu tinha quebrado a trava do chip. Não quebrei nenhuma trava, e por que não analisar a possibilidade da trava ter sido quebrada na SARAIVA após o retorno. Por que não acreditar na palavra de um cliente idôneo. Instalar um chip no celular não é nada complexo para ninguém, nem pra eu como engenheiro. Se tivesse quebrado trava e utilizasse de má fé como afirmam teria enviado o produto para a troca informando que recebi o produto quebrado !!!! Mas não adianta não querem escutar os argumentos, não consegue falar com supervisor/ gerente que poderia refletir sobre a decisão ( só atendentes te atendem e só respondem o que for determinado ), não recebem e-mails pelo atendimento@saraiva.com ( servidor responde haver problema na entrega ???? , reclamações pelo site não são respondidos formalmente. Vou ter que consertar o celular ( perdi a garantia por um dano causado no retorno do celular para a SARAIVA. Então Vai um conselho"
    # },
    # "11.157": {
    #     "opinions": [
    #         [
    #             "Melhor que qualquer iPhone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Perfeito, sem qualquer reclamação.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Melhor que qualquer iPhone. Perfeito, sem qualquer reclamação."
    # },
    # "11.158": {
    #     "opinions": [
    #         [
    #             "EXCELENTE.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "MUITO BOM.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "EXCELENTE. MUITO BOM."
    # },
    # "11.159": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Muito bom!"
    # },
    # "11.160": {
    #     "opinions": [
    #         [
    #             "Bateria de duração que chega quase 1 dia.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Ótimo celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo celular. com bateria de duração que chega quase 1 dia.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo celular. Ótimo celular com bateria de duração que chega quase 1 dia."
    # },
    # "11.161": {
    #     "opinions": [
    #         [
    #             "Alta qualidade e performance.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente produto. Alta qualidade e performance."
    # },
    # "11.163": {
    #     "opinions": [
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho excelente, cumpre com o prometido.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não há aparelho melhor no mercado.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Aparelho excelente, cumpre com o prometido. Todos os aspectos marcados acima retratam fielmente o aparelho adquirido. Não há aparelho melhor no mercado. Recomendo."
    # },
    # "11.164": {
    #     "opinions": [
    #         [
    #             "Camera muito boa.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Fluido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Oferece atualizações frequentes.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não deixou nada a desejar.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Sistema muito limpo.",
    #             "SISTEMA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Ótimo produto. Não deixou nada a desejar. Sistema muito limpo, fluido, camera muito boa e oferece atualizações frequentes."
    # },
    # "11.165": {
    #     "opinions": [
    #         [
    #             "O que eu mais busco num celular é a qualidade e possibilidade de edição nas configurações da câmera. E nesse quesito o S7 não deixa a desejar. Já tive o S5 e a Samsung mantem o padrão alto na qualidade da câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "O desempenho me surpreendeu muito.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O prata suja bastante na parte de trás do aparelho.",
    #             "DESIGN",
    #             "-"
    #         ],
    #         [
    #             "O leitor de digital é muito rápido e eficiente.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "O que me frustou foi o fato da empresa ter resolvido retirar a função de infravermelho (eu sempre usava o S5 como controle remoto da TV, ar condicionado, etc. e agora não é mais possível usar essa função na S7)",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "O aparelho é excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "No geral, exceto o preço e a duração da bateria, o celular é fantástico!!",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Migrando do S5 para o S7.",
    #             "PRODUTO",
    #             "X"
    #         ]
    #     ],
    #     "review": "Migrando do S5 para o S7. O aparelho é excelente, o desempenho me surpreendeu muito. O que eu mais busco num celular é a qualidade e possibilidade de edição nas configurações da câmera. E nesse quesito o S7 não deixa a desejar. Já tive o S5 e a Samsung mantem o padrão alto na qualidade da câmera. O que me frustou foi o fato da empresa ter resolvido retirar a função de infravermelho (eu sempre usava o S5 como controle remoto da TV, ar condicionado, etc. E agora não é mais possível usar essa função na S7 O prata suja bastante na parte de trás do aparelho. O leitor de digital é muito rápido e eficiente. No geral, exceto o preço e a duração da bateria, o celular é fantástico!!"
    # },
    # "11.166": {
    #     "opinions": [
    #         [
    #             "Rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Com 4 GB de memória RAM (um exagero, sobra!)",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Bonito.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Fora isso ainda ganhei um Galaxy Gear VR na compra (promoção da Samsung ainda em vigor), show.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "unico ponto negativo é a impossibilidade de trocar a bateria (ou seja, tem vida util contada, de 2-3 anos, fora isso, só alegria.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Funcional.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho top da linha Galaxy, só isso já diz tudo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A prova d´água.",
    #             "RESISTÊNCIA",
    #             "+."
    #         ]
    #     ],
    #     "review": "Excelente smartphone. Aparelho top da linha Galaxy, só isso já diz tudo. Bonito, funcional, rápido, a prova d´água e com 4 GB de memória RAM (um exagero, sobra! unico ponto negativo é a impossibilidade de trocar a bateria (ou seja, tem vida util contada, de 2-3 anos, fora isso, só alegria. Fora isso ainda ganhei um Galaxy Gear VR na compra (promoção da Samsung ainda em vigor, show."
    # },
    # "11.167": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Bom."
    # },
    # "11.168": {
    #     "opinions": [
    #         [
    #             "As fotos são ótimas.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Produto muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adorei o produto, estou curtindo bastante.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto muito bom. Adorei o produto, estou curtindo bastante, as fotos são ótimas."
    # },
    # "11.169": {
    #     "opinions": [
    #         [
    #             "Aparelho bem moderno e rapido com funções de ultima geração.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Perfeito.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Perfeito. Aparelho bem moderno e rapido com funções de ultima geração."
    # },
    # "11.170": {
    #     "opinions": [
    #         [
    #             "Nenhum sinal de travamento.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Produto dispensa comparativos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto excelente e sem arrependimento.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Bastante simplificado.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto excelente e sem arrependimento. Produto dispensa comparativos, sem nenhum sinal de travamento.Bastante simplificado. Não possui a mesma beleza de um iphone mais o processador não se compara com o mesmo."
    # },
    # "11.171": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto bom. Muito bom."
    # },
    # "11.172": {
    #     "opinions": [
    #         [
    #             "Muito BOM!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto TOP.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Vale a pena o investimento.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito BOM! Produto TOP. Vale a pena o investimento."
    # },
    # "11.173": {
    #     "opinions": [
    #         [
    #             "Ótimas fotos.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Aparelho rápido.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Achei que esquenta quando utilizo o gear vr.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Excelente smartphone.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo display",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente smartphone. Aparelho rápido, ótimo display e fotos, achei que esquenta quando utilizo o gear vr."
    # },
    # "11.174": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Otimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo. Bom."
    # },
    # "11.175": {
    #     "opinions": [
    #         [
    #             "Um bom produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um bom aparelho, caro por sinal.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei bastante pela inovação nas características e velocidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Graficos impressionam pela qualidade.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Um bom aparelho, caro por sinal. Gostei bastante pela inovação nas características e velocidade. Graficos impressionam pela qualidade. Um bom produto."
    # },
    # "11.176": {
    #     "opinions": [
    #         [
    #             "Alta capacidade de memória.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "A câmera é um dos diferenciais.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Apesar do android ser basante modificado apresenta boa fluidez.",
    #             "SISTEMA",
    #             "+"
    #         ],
    #         [
    #             "Tela amoled e quad hd dispensa comentários.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Ótimo produto, apesar do android ser basante modificado apresenta boa fluidez. Alta capacidade de memória, tela amoled e quad hd dispensa comentários. A câmera é um dos diferenciais."
    # },
    # "11.177": {
    #     "opinions": [
    #         [
    #             "Não trava.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Rápido.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Totalmente satisfeita.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Perfeito.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Recomendo 100%.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Excelente resolução.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Totalmente satisfeita. Rápido, excelente resolução, não trava, perfeito. Recomendo 100%."
    # },
    # "11.178": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Celular excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Celular excelente. Muito bom."
    # },
    # "11.179": {
    #     "opinions": [
    #         [
    #             "Produto Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Correspondeu as minhas expectativas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto Excelente. Correspondeu as minhas expectativas."
    # },
    # "11.180": {
    #     "opinions": [
    #         [
    #             "Sem comparações!!!",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "O melhore mais completo até agora!",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Sem comparações!!! O melhore mais completo até agora!"
    # },
    # "11.181": {
    #     "opinions": [
    #         [
    #             "Surpresas desagradáveis com a compra do aparelho. O celular é muito bom, pesquisei muito antes de compra-lo, mas não fazia ideia do maior problema deste modelo. A tela do aparelho é levemente curvada na lateral(sim estamos falando do Flat não do Edge), o que impede de haver uma película que cubra toda a tela do celular. O mais estranho é que existe película para o Edge, mas para o flat não. Os modelos de película disponíveis tem uma margem de uns 4mm, o que torna uma luta a experiência de manipular o menu e selecionar um aplicativo e jogar para o canto da tela para ele ir para a página do lado.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Outro problema (o mais grave na minha avaliação) é que a Samsung faz promoções que oferece brindes (no meu caso o óculos VR), mas na hora que você preenche o cadastro fala que o óculos acabou e fica por isso mesmo. O que mais me deixa chateado é que no meu facebook (por ter pesquisado sobre o celular) eu recebo no meu feed a propaganda do S7 e tá lá que quem compra o celular ganha um óculos. Me senti passo para trás pela empresa, e como eles não pararam com a propaganda, me dá a sensação de que a empresa continua a passar outros clientes para trás.",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Duas surpresas desagradáveis com a compra do aparelho. O celular é muito bom, pesquisei muito antes de compra-lo, mas não fazia ideia do maior problema deste modelo. A tela do aparelho é levemente curvada na lateral(sim estamos falando do Flat não do Edge, o que impede de haver uma película que cubra toda a tela do celular. O mais estranho é que existe película para o Edge, mas para o flat não.. Os modelos de película disponíveis tem uma margem de uns 4mm, o que torna uma luta a experiência de manipular o menu e selecionar um aplicativo e jogar para o canto da tela para ele ir para a página do lado. Outro problema (o mais grave na minha avaliação) é que a Samsung faz promoções que oferece brindes (no meu caso o óculos VR, mas na hora que você preenche o cadastro fala que o óculos acabou e fica por isso mesmo. O que mais me deixa chateado é que no meu facebook (por ter pesquisado sobre o celular eu recebo no meu feed a propaganda do S7 e tá lá que quem compra o celular ganha um óculos. Me senti passo para trás pela empresa, e como eles não pararam com a propaganda, me dá a sensação de que a empresa continua a passar outros clientes para trás."
    # },
    # "11.182": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aguardar mais algum tempo para dar uma resposta mais concreta.",
    #             "PRODUTO",
    #             "."
    #         ]
    #     ],
    #     "review": "Bom. Aguardar mais algum tempo para dar uma resposta mais concreta."
    # },
    # "11.183": {
    #     "opinions": [
    #         [
    #             "Facilidade, produtividade, comprei para gravar vídeos, muito satisfeitp.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Segurança, confiança e agilidade.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Segurança, confiança e agilidade. Facilidade, produtividade, comprei para gravar vídeos, muito satisfeitp."
    # },
    # "11.184": {
    #     "opinions": [
    #         [
    #             "Para armazená-las possui ótimo espaço (32gb), além de permitir expandir o espaço utilizando o cartão de memória.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "As fotos e vídeos possuem imagem perfeitas.",
    #             "CÂMERA",
    #             "++"
    #         ],
    #         [
    #             "Satisfeito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito rápido.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aprovei e recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou gostando muito do aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Satisfeito. Estou gostando muito do aparelho. As fotos e vídeos possuem imagem perfeitas. Para armazená-las possui ótimo espaço (32gb, além de permitir expandir o espaço utilizando o cartão de memória. Muito rápido. Aprovei e recomendo."
    # },
    # "11.185": {
    #     "opinions": [
    #         [
    #             "INCRIVEL, NÃO TRAVA DE FORMA ALGUMA.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "APARELHO SENSACIONAL.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "TUDO O QUE EU QUERIA E ESPERAVAPODE PARECER UM POUCO CARO, MAS FAZ TODA DIFERENÇA PARA QUEM PROCURA RAPIDEZ E AGILIDADE ASSIM COMO EU, POIS GARANTO QUE NÃO VAI SE ARREPENDER.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "TINHA O GALAXY S6 E AMAVA DE PAIXÃO, ACABEI VENDENDO E TROQUEI POR UM GALAXY A7, DO QUAL ME ARREPENDO ATÉ HOJE, CELULAR MUITO INFERIOR A LINHA \"S\".FIQUEI APENAS 03 MESES E ENTÃO DECIDI COMPRAR O GALAXY S7 E ESTOU AMANDOOOO! QUANDO EU TROQUEI MEU S6 PELO A7, FIQUEI 03 MESES SOFRENDO!!! CELULAR TRAVAVA DEMAIS, QUALIDADE RUIM E EU FICAVA MUITO ESTRESSADA, COISA QUE NÃO PASSO HOJE EM DIA COM O GALAXS S7AMANDOOOOO",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O FORMATO DO APARELHO CABE CERTINHO E CONFORTAVELMENTE NA PALMA DA MÃO.",
    #             "TAMANHO",
    #             "+"
    #         ],
    #         [
    #             "A QUALIDADE DAS IMAGENS SÃO EXCELENTES.",
    #             "TELA",
    #             "+"
    #         ],
    #         [
    #             "O TOQUE DO DISPLAY É MARAVILHOSO E SUPER DELICADO.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "APARELHO SENSACIONAL. TINHA O GALAXY S6 E AMAVA DE PAIXÃO, ACABEI VENDENDO E TROQUEI POR UM GALAXY A7, DO QUAL ME ARREPENDO ATÉ HOJE, CELULAR MUITO INFERIOR A LINHA \"S\".FIQUEI APENAS 03 MESES E ENTÃO DECIDI COMPRAR O GALAXY S7 E ESTOU AMANDOOOO! INCRIVEL, NÃO TRAVA DE FORMA ALGUMA, A QUALIDADE DAS IMAGENS SÃO EXCELENTES, O TOQUE DO DISPLAY É MARAVILHOSO E SUPER DELICADO, O FORMATO DO APARELHO CABE CERTINHO E CONFORTAVELMENTE NA PALMA DA MÃO, TUDO O QUE EU QUERIA E ESPERAVAPODE PARECER UM POUCO CARO, MAS FAZ TODA DIFERENÇA PARA QUEM PROCURA RAPIDEZ E AGILIDADE ASSIM COMO EU, POIS GARANTO QUE NÃO VAI SE ARREPENDER.QUANDO EU TROQUEI MEU S6 PELO A7, FIQUEI 03 MESES SOFRENDO!!! CELULAR TRAVAVA DEMAIS, QUALIDADE RUIM E EU FICAVA MUITO ESTRESSADA, COISA QUE NÃO PASSO HOJE EM DIA COM O GALAXS S7AMANDOOOOO ???"
    # },
    # "11.186": {
    #     "opinions": [
    #         [
    #             "Tem uma boa memória.",
    #             "ARMAZENAMENTO",
    #             "+"
    #         ],
    #         [
    #             "Bateria poderia ser melhor.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Como utilizo basicamente para redes sociais e agenda, achei que a bateria pudesse durar um pouco mais - dura no máximo um dia e meio.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Uma câmera de ótima qualidade.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Design lindo.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Ótimo design.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Super indico para quem busca design.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Não vem com um monte de aplicativos já instalados - e que você não usa.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Fácil de usar.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Super indico para quem busca praticidade no uso.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Design lindo, mas bateria poderia ser melhor. Fácil de usar, ótimo design, mas como utilizo basicamente para redes sociais e agenda, achei que a bateria pudesse durar um pouco mais - dura no máximo um dia e meio. Fora isso tem uma boa memória, uma câmera de ótima qualidade e não vem com um monte de aplicativos já instalados - e que você não usa. Super indico para quem busca design e praticidade no uso."
    # },
    # "11.187": {
    #     "opinions": [
    #         [
    #             "Apenas achei que a bateria fosse durar um pouco mais.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "O acabamento dele é ótimo.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Por ser todo em vidro suja um pouco, mas nada que uma capinha não resolva.",
    #             "DESIGN",
    #             "-."
    #         ],
    #         [
    #             "O celular é excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Corresponde ao que é informado.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Até agora não tive nenhum problema com o celular.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Corresponde ao que é informado. Até agora não tive nenhum problema com o celular, apenas achei que a bateria fosse durar um pouco mais, mas fora isso o celular é excelente e o acabamento dele é ótimo. Por ser todo em vidro suja um pouco, mas nada que uma capinha não resolva."
    # },
    # "11.188": {
    #     "opinions": [
    #         [
    #             "Podia ter melhor custo-benefício.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Excelente aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente aparelho. Aparelho excelente. Podia ter melhor custo-benefício."
    # },
    # "11.189": {
    #     "opinions": [
    #         [
    #             "Vou tentar entrar em contato com a empresa.???????Só houve uma demora gigantesca na entrega, mas veio.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Paguei sedex pra chegar em 3 dias.. Acabou demorando 15 dias e veio por transportadora. Perdi valor sedex ??",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "O melhor celular do mundo.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Produto maravilhoso! Lindo! Estou amando!",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Comprei 2 s7, o meu veio perfeito, já o do meu marido veio com problema, travamento, não lê a digital, desliga..",
    #             "PRODUTO",
    #             "-."
    #         ]
    #     ],
    #     "review": "O melhor celular do mundo. Produto maravilhoso! Lindo! Estou amando! Comprei 2 s7, o meu veio perfeito, já o do meu marido veio com problema, travamento, não lê a digital, desliga.. Vou tentar entrar em contato com a empresa.???????Só houve uma demora gigantesca na entrega, mas veio. Paguei sedex pra chegar em 3 dias.. Acabou demorando 15 dias e veio por transportadora. Perdi valor sedex ??"
    # },
    # "11.190": {
    #     "opinions": [
    #         [
    #             "A Samsung que enche de APPs que não se utiliza que não tem como apagar.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Só o preço que é alto demais.",
    #             "PREÇO",
    #             "-"
    #         ],
    #         [
    #             "Ótimo aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente aparelho!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É um excelente aparelho.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo aparelho. Excelente aparelho! Só o preço que é alto demais e a Samsung que enche de APPs que não se utiliza que não tem como apagar. Mas é um excelente aparelho."
    # },
    # "11.191": {
    #     "opinions": [
    #         [
    #             "Boa.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Celular samsung. Boa."
    # },
    # "11.192": {
    #     "opinions": [
    #         [
    #             "Um produto com um grande desempenho.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo produto. Um produto com um grande desempenho e de fácil manuseio."
    # },
    # "11.193": {
    #     "opinions": [
    #         [
    #             "Critica por não ter recebido o blinde.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "O blinde que estava previsto em sem entregue junto com o produto não veio, mesmo estando dentro da período promocional.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "As bordas arredondadas ativa, dificulta o manuseio, pois faz com que ações não conceitual se realize.",
    #             "OUTRO",
    #             "-"
    #         ]
    #     ],
    #     "review": "Critica por não ter recebido o blinde. As bordas arredondadas ativa, dificulta o manuseio, pois faz com que ações não conceitual se realize.O blinde que estava previsto em sem entregue junto com o produto não veio, mesmo estando dentro da período promocional."
    # },
    # "11.194": {
    #     "opinions": [
    #         [
    #             "Bateria ruim.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Desempenho excelente.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "O atendimento do Girafa que deixou a desejar, fizeram propaganda enganosa que o produto acompanha um óculos de realidade virtual e quando chegou não acompanhou e disseram que eu teria que cadastrar na Samsung, porém na Samsung não havia mais disponível e pediram pra ver com o Girafa e nenhum resolveu.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Gostei muito do s7.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto muito bom. Gostei muito do s7, desempenho excelente, apenas a bateria ruim. O atendimento do Girafa que deixou a desejar, fizeram propaganda enganosa que o produto acompanha um óculos de realidade virtual e quando chegou não acompanhou e disseram que eu teria que cadastrar na Samsung, porém na Samsung não havia mais disponível e pediram pra ver com o Girafa e nenhum resolveu."
    # },
    # "11.195": {
    #     "opinions": [
    #         [
    #             "Adorei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "E muito show esse celular S7.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Adorei. E muito show esse celular S7."
    # },
    # "11.196": {
    #     "opinions": [
    #         [
    #             "Ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adorei o celular, além de lindo é toop.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo. Adorei o celular, além de lindo é toop."
    # },
    # "11.197": {
    #     "opinions": [
    #         [
    #             "Toooop.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adorei esse celular.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo produto. Adorei esse celular. Toooop."
    # },
    # "11.198": {
    #     "opinions": [
    #         [
    #             "Quanto à bateria, não vi melhoria.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "A câmera esta me surpreendendo a cada dia.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "As fotos noturnas ficam boas e as funcionalidades e opções de personalização são muito uteis para o dia a dia.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "É um ímã para impressão digital.",
    #             "DESIGN",
    #             "-"
    #         ],
    #         [
    #             "O always on é uma inovação no aparelho.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "O leitor de digital é outro fator positivo, pois ele é rápido e prático.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "O always on poderia exibir os ícones de outros apps como facebook, whatsapp, instagram...",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "A certificação de resistência à agua eu não testei, pois no S5 essa resistência, seguindo todas as recomendações e verificações, não funcionou.",
    #             "OUTRO",
    #             "X"
    #         ],
    #         [
    #             "É um pouco pesado.",
    #             "PESO",
    #             "-"
    #         ],
    #         [
    #             "Galaxy S7.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Por hora estou gostando muito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Realizei a troca do galaxy 5 para o galaxy s7.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excluindo o valor e a bateria, estou satisfeita com o aparelho.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "O material parece de qualidade.",
    #             "RESISTÊNCIA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Galaxy S7. Realizei a troca do galaxy 5 para o galaxy s7. Por hora estou gostando muito, exceto a bateria pois não vi melhoria.O material parece de qualidade, apesar de ser um ímã para impressão digital e ser um pouco pesado.A câmera esta me surpreendendo a cada dia. As fotos noturnas ficam boas e as funcionalidades e opções de personalização são muito uteis para o dia a dia.O always on é uma inovação no aparelho, mas poderia exibir os ícones de outros apps como facebook, whatsapp, instagram...O leitor de digital é outro fator positivo, pois ele é rápido e prático.A certificação de resistência à agua eu não testei, pois no S5 essa resistência, seguindo todas as recomendações e verificações, não funcionou. Excluindo o valor e a bateria, estou satisfeita com o aparelho."
    # },
    # "11.199": {
    #     "opinions": [
    #         [
    #             "A câmera e suas funcionalidades estão me surpreendendo.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "A rapidez do leitor de digital também é um ponto positivo.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Always On é uma função inovadora e muito util, uma vez que não precisamos mais acender a tela do dispositivo para ver as horas.",
    #             "OUTRO",
    #             "+"
    #         ],
    #         [
    #             "Uma sugestão para o Always On seria exibir o ícone de outros apps, como o whatsapp, facebook e instagram.",
    #             "OUTRO",
    #             "-"
    #         ],
    #         [
    #             "Achei o aparelho um pouco pesado.",
    #             "PESO",
    #             "-"
    #         ],
    #         [
    #             "Produto de qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Realizei a troca do galaxy s5 para o galaxy s7. Tirando a bateria que para mim não melhorou, por hora estou amando.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O material parece de qualidade.",
    #             "RESISTÊNCIA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto de qualidade. Realizei a troca do galaxy s5 para o galaxy s7. Tirando a bateria que para mim não melhorou, por hora estou amando. Achei o aparelho um pouco pesado, porem, o material parece de qualidade. A câmera e suas funcionalidades estão me surpreendendo. A rapidez do leitor de digital também é um ponto positivo. Always On é uma função inovadora e muito util, uma vez que não precisamos mais acender a tela do dispositivo para ver as horas. Uma sugestão para o Always On seria exibir o ícone de outros apps, como o whatsapp, facebook e instagram."
    # },
    # "11.200": {
    #     "opinions": [
    #         [
    #             "Otimo celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aprovei e recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo celular. Aprovei e recomendo."
    # },
    # "11.201": {
    #     "opinions": [
    #         [
    #             "Produto maravilhoso.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho excelente!!!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Pra quem reclama da fragilidade recomendo que use uma pelicula de vidro nele e uma capa, pois todo aparelho é quebravel, o moto force se sobressai, mas é feio, então pelicula nele, vale a pena.",
    #             "RESISTÊNCIA",
    #             "-."
    #         ]
    #     ],
    #     "review": "Aparelho excelente!!! Produto maravilhoso, pra quem reclama da fragilidade recomendo que use uma pelicula de vidro nele e uma capa, pois todo aparelho é quebravel, o moto force se sobressai, mas é feio, então pelicula nele, vale a pena."
    # },
    # "11.202": {
    #     "opinions": [
    #         [
    #             "Dislpay quebra-fácil. Trincou todo o display na 1a queda.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Dislpay quebra-fácil. Trincou todo o display na 1a. Queda."
    # },
    # "11.203": {
    #     "opinions": [
    #         [
    #             "Bateria dura muito!",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Muito rápido! Não trava!",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Excelente! Recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente! Recomendo! Muito rápido! Não trava! Bateria dura muito!"
    # },
    # "11.204": {
    #     "opinions": [
    #         [
    #             "Tira fotos com qualidade.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Com ótima performance.",
    #             "DESEMPENHO",
    #             "+"
    #         ],
    #         [
    #             "Smartphone bonito e elegante.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Ótima aquisição.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótima aquisição. Smartphone bonito, elegante, com ótima performance e que tira fotos com qualidade."
    # },
    # "11.205": {
    #     "opinions": [
    #         [
    #             "O melhor da samsung, em qualidade e funcionalidade de imagem e recursos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Trincou fácio o display.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "Câmera na traseina apesar de mais interna, continua sujeita a danos.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "O melhor da samsung, em qualidade e funcionalidade de imagem e recursos. Trincou fácio o display e câmera na traseina apesar de mais interna, continua sujeita a danos."
    # },
    # "11.206": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ainda não usei todas as funções que possui, mas já percebi que o aparelho é excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Ainda não usei todas as funções que possui, mas já percebi que o aparelho é excelente."
    # },
    # "11.207": {
    #     "opinions": [
    #         [
    #             "Otima.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Aparelho otimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Aparelho otimo. Otima."
    # },
    # "11.208": {
    #     "opinions": [
    #         [
    #             "Me direcionei a assistência técnica (Anatech em Porto Alegre-RS) e me informaram que não poderiam dar entrada na garantia, uma vez que a garantia não cobre o reparo da tela.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Prática abusiva de preços de manutenção e celular que quebra na primeira queda. Efetuei a compra de um celular samsung galaxy s7 SM-G930F no dia 08/01/18 na loja pontofrio (online). Recebi o produto no dia 12/01/18 com aparencia de estar intacto e sem nenhum problema. Liguei o mesmo e funcionou corretamente.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Além disso, solicitei para a atendente um orçamento para troca da tela e a mesma me informou que o valor seria de 980R$, além de 35R$ de orçamento, totalizando 1015R$.O preço que paguei pelo produto foi de 1661,59R$.Sendo assim, o valor para um reparo custaria mais de 60% do valor do aparelho.Além disso, no próprio site da empresa samsung, é informado que o reparo de tela custaria 439R$ nos centros de Reparo vide link: www.samsung.com/br/support/valorreparo/. Essa prática, de vender um produto de baixa qualidade, que escorrega e que quebra facilmente e depois cobrar valores surreais de reparo, na minha opinião se caracteriza como uma prática abusiva de preços e uma maneira de tentar extorquir os clientes.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "Em menos de 24horas, no dia 13/01/18, ocorreu a primeira queda do aparelho do meu bolso (o mesmo é muito liso e escorrega do bolso ao se sentar) e o aparelho trincou a tela. Possuia um celular da motorola moto G5 a cerca de 1 ano, que teve quedas muito piores e que ainda funciona perfeitamente e está com minha namorada.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Prática abusiva de preços de manutenção e celular que quebra na primeira queda. Efetuei a compra de um celular samsung galaxy s7 SM-G930F no dia 08/01/18 na loja pontofrio (online Recebi o produto no dia 12/01/18 com aparencia de estar intacto e sem nenhum problema. Liguei o mesmo e funcionou corretamente. Em menos de 24horas, no dia 13/01/18, ocorreu a primeira queda do aparelho do meu bolso (o mesmo é muito liso e escorrega do bolso ao se sentar e o aparelho trincou a tela. Me direcionei a assistência técnica (Anatech em Porto Alegre-RS e me informaram que não poderiam dar entrada na garantia, uma vez que a garantia não cobre o reparo da tela. Além disso, solicitei para a atendente um orçamento para troca da tela e a mesma me informou que o valor seria de 980R$, além de 35R$ de orçamento, totalizando 1015R$.O preço que paguei pelo produto foi de 1661,59R$.Sendo assim, o valor para um reparo custaria mais de 60% do valor do aparelho.Além disso, no próprio site da empresa samsung, é informado que o reparo de tela custaria 439R$ nos centros de Reparo vide link: www.samsung.com/br/support/valorreparo/. Essa prática, de vender um produto de baixa qualidade, que escorrega e que quebra facilmente e depois cobrar valores surreais de reparo, na minha opinião se caracteriza como uma prática abusiva de preços e uma maneira de tentar extorquir os clientes. Possuia um celular da motorola moto G5 a cerca de 1 ano, que teve quedas muito piores e que ainda funciona perfeitamente e está com minha namorada. Não há explicações para a fragilidade de um produto qu."
    # },
    # "11.209": {
    #     "opinions": [
    #         [
    #             "Boas funções mas pouco resistente.",
    #             "PRODUTO",
    #             "-."
    #         ],
    #         [
    #             "O Celular é alérgico a agua, já vi celulares sem proteção resistir melhor. Das duas vezes que o meu entrou em contato com a agua ele foi parar na assistência, sendo que da segunda vez deu PT.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Boas funções mas pouco resistente. O Celular é alérgico a agua, já vi celulares sem proteção resistir melhor. Das duas vezes que o meu entrou em contato com a agua ele foi parar na assistência, sendo que da segunda vez deu PT."
    # },
    # "11.210": {
    #     "opinions": [
    #         [
    #             "Falso anuncio.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "O Bondfaro me alertou que o preço do produto havia caído para 948,00. A loja com o melhor preço é o Carrefour. Mas quando entramos na loja para efetuar a compra, o preço consta como 2298,00.",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Falso anuncio. O Bondfaro me alertou que o preço do produto havia caído para 948,00. A loja com o melhor preço é o Carrefour. Mas quando entramos na loja para efetuar a compra, o preço consta como 2298,00."
    # },
    # "11.211": {
    #     "opinions": [
    #         [
    #             "Pecou na bateria que não se apresentaram tão bem no uso...",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Boa qualidade da câmera.",
    #             "CÂMERA",
    #             "+"
    #         ],
    #         [
    #             "Ótima configuração do celular.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Sempre adquiri celulares dessa marca, pela confiança e qualidade e dessa vez o aparelho de mostrou muito bom, com grande performance e muitos pontos positivos.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Esperava mais.....",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Acabei devolvendo o aparelho para tentar adquirir outro.",
    #             "PRODUTO",
    #             "--"
    #         ],
    #         [
    #             "Pecou no touchscreen que não se apresentaram tão bem no uso...",
    #             "TELA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Esperava mais..... Sempre adquiri celulares dessa marca, pela confiança e qualidade e dessa vez o aparelho de mostrou muito bom, com grande performance e muitos pontos positivos como qualidade da câmera, ótima configuração do celular, mas pecou na bateria e no touchscreen que não se apresentaram tão bem no uso... Por isso acabei devolvendo o aparelho para tentar adquirir outro."
    # },
    # "11.212": {
    #     "opinions": [
    #         [
    #             "S7 razoavel. Pouco tempo mas caro para o que oferece.",
    #             "PRODUTO",
    #             "-"
    #         ]
    #     ],
    #     "review": "S7 razoavel. Pouco tempo mas caro para o que oferece."
    # },
    # "11.214": {
    #     "opinions": [
    #         [
    #             "Ótima tecnologia.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Este modelo da Samsung deixou muito a desejar comparado a outros aparelhos que tive.",
    #             "PRODUTO",
    #             "-"
    #         ],
    #         [
    #             "Péssima resistência.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "Recentemente comprei um Galaxy S7, em 3 dias, numa pequena queda trincou parte do display (falo pequena queda porque os outros modelos que tive, sofreram quedas piores e permaneceram intactos). Um dos chamativos desse modelo da Samsung é justamente a tela Gorilla Glass 4, mas que não tem a menor resistência e, pior, o pequeno reparo da tela ficou orçado em quase R$ 2000,00 pela assistência técnica, R$ 85,00 mais barato que o preço do aparelho novo.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Ótima tecnologia, péssima resistência. Sempre preferi smartphones aos modelos da Apple, primeiramente pelo custo benefício, já que as configurações dos itens de primeira linha, na grande maioria das vezes, são compatíveis ou superiores aos Iphones. Depois disso, os modelos que tive foram super resistentes (Motorola Razr Intel e Galaxy Alpha e só os troque cerca de 2,5 anos depois da compra, para ter um celular mais atualizado e não porque tiveram algum tipo de problema. Recentemente comprei um Galaxy S7, em 3 dias, numa pequena queda trincou parte do display (falo pequena queda porque os outros modelos que tive, sofreram quedas piores e permaneceram intactos Um dos chamativos desse modelo da Samsung é justamente a tela Gorilla Glass 4, mas que não tem a menor resistência e, pior, o pequeno reparo da tela ficou orçado em quase R$ 2000,00 pela assistência técnica, R$ 85,00 mais barato que o preço do aparelho novo. Enfim, este modelo da Samsung deixou muito a desejar comparado a outros aparelhos que tive."
    # },
    # "11.217": {
    #     "opinions": [
    #         [
    #             "O anuncio da TIM é uma enganação! O preço só é valido para quem assina um plano. Como em qualquer operadora. Voce entra no site para comprar o celular, escolhe só o celular, sem venda casada, e o preço vai para R$3.499!!!! O Buscapé não deveria permitir esse tipo de engodo!",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "O anuncio da TIM é uma enganação! O preço só é valido para quem assina um plano. Como em qualquer operadora. Voce entra no site para comprar o celular, escolhe só o celular, sem venda casada, e o preço vai para R$3.499!!!! O Buscapé não deveria permitir esse tipo de engodo!"
    # },
    # "11.219": {
    #     "opinions": [
    #         [
    #             "E O CONCERTO É 70% DO PREÇO DO CELULAR E PAGAMENTO NO MÁXIMO DE 2 VEZES, E DIZEM QUE É MAL USO.",
    #             "EMPRESA",
    #             "-"
    #         ],
    #         [
    #             "DEVERIA SE CHAMAR SAMSUNG TRINCA RAPIDO.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ],
    #         [
    #             "PÉSSIMA COM DOIS MESES DE USO TRINCOU O DISPLAY DE LCD DENTRO DA BOLSA.",
    #             "RESISTÊNCIA",
    #             "-"
    #         ]
    #     ],
    #     "review": "DEVERIA SE CHAMAR SAMSUNG TRINCA RAPIDO. PÉSSIMA COM DOIS MESES DE USO TRINCOU O DISPLAY DE LCD DENTRO DA BOLSA. E O CONCERTO É 70% DO PREÇO DO CELULAR E PAGAMENTO NO MÁXIMO DE 2 VEZES, E DIZEM QUE É MAL USO."
    # },
    # "11.220": {
    #     "opinions": [
    #         [
    #             "Achei ruim a tela ter as bordas curvas, pois nao se encontra o protetor de tela, o que é muito complicado.",
    #             "ACESSÓRIO",
    #             "-"
    #         ]
    #     ],
    #     "review": "Geral. Achei ruim a tela ter as bordas curvas, pois nao se encontra o protetor de tela, o que é muito complicado."
    # },
    # "11.221": {
    #     "opinions": [
    #         [
    #             "Bateria horrível.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "A BATERIA dele é horrível, ainda consegue ser pior que o a do Galaxy S6, que já era péssima, comprei 2 e devolvi por causa da bateria, um celular caro desse com uma bateria péssima, se usar acaba rapidinho mesmo.",
    #             "BATERIA",
    #             "--"
    #         ],
    #         [
    #             "O celular é ótimo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bateria horrível. O celular é ótimo, mas a BATERIA dele é horrível, ainda consegue ser pior que o a do Galaxy S6, que já era péssima, comprei 2 e devolvi por causa da bateria, um celular caro desse com uma bateria péssima, se usar acaba rapidinho mesmo."
    # },

    # "30.001": {
    #     "opinions": [
    #         [
    #             "Boa Câmera.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Boa Câmera. Pouca, recém comprada."
    # },
    # "30.002": {
    #     "opinions": [
    #         [
    #             "Acompanha bateria.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "Os tutoriais online Canon ajudam muito.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "O produto vem com correia para evitar quedas.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "O produto vem com duas lentes para fotografia.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "Acompanha bateria tampas de lentes para evitar riscos e manchas ao manusear.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "Poderia vir um software pelo menos trial para poder editar fotos.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Falta uma mochila para transporte, o que daria muito mais segurança, mesmo sabendo da robustez do corpo. Auxilia muito no transporte.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "A abertura de diafragma das lentes do kit não são das melhores, mas pelo preço proposto é satisfatório.",
    #             "ACESSÓRIO",
    #             "-."
    #         ],
    #         [
    #             "Sobre a anatomia, seu desenho é bom.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "O foco automático é ótimo para poses.",
    #             "FOCO",
    #             "+"
    #         ],
    #         [
    #             "O foco automático é um pouco lento, o que não permite muitas fotos em movimento.",
    #             "FOCO",
    #             "-"
    #         ],
    #         [
    #             "A qualidade de fotografia é superior se comparado a prozoomers.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "O peso atrapalha um pouco, mas para este tipo de equipamento é comum, se comparado aos outros modelos de câmera.",
    #             "PESO",
    #             "-."
    #         ],
    #         [
    #             "Só para caráter de comparação: só o corpo da Nikon chega ao preço que paguei no kit inteiro da Canon.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Me sinto satisfeito pelo que paguei, pois pretendo melhorar as fotos com lentes novas com a 50 mm - f 1.4.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Começo com pé direito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A qualidade é muito boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Mas o essencial para ter bons resultados é possível com este produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não posso marcar pontos negativos pelo que paguei.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Para quem nunca teve experiências com câmera DSLR é um bom começo e possível início da arte da fotografia.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "O corpo é resistente.",
    #             "RESISTÊNCIA",
    #             "+"
    #         ],
    #         [
    #             "O tamanho atrapalha um pouco, mas para este tipo de equipamento é comum, se comparado aos outros modelos de câmera.",
    #             "TAMANHO",
    #             "-."
    #         ]
    #     ],
    #     "review": "Começo com pé direito. O produto vem com correia para evitar quedas, duas lentes para fotografia, o corpo é resistente, a qualidade de fotografia é superior se comparado a prozoomers, Acompanha bateria, tampas de lentes para evitar riscos e manchas ao manusear. Os tutoriais online Canon ajudam muito. Sobre a anatomia, seu desenho é bom. O peso e o tamanho atrapalham um pouco, mas para este tipo de equipamento é comum, se comparado aos outros modelos de câmera. Me sinto satisfeito pelo que paguei, pois pretendo melhorar as fotos com lentes novas com a 50 mm - f 1.4. O foco automático é um pouco lento, o que não permite muitas fotos em movimento, mas é ótimo para poses. A abertura de diafragma das lentes do kit não são das melhores, mas pelo preço proposto é satisfatório. Não posso marcar pontos negativos pelo que paguei. A qualidade é muito boa. Só para caráter de comparação. Só o corpo da Nikon chega ao preço que paguei no kit inteiro da Canon. Falta uma mochila para transporte, o que daria muito mais segurança, mesmo sabendo da robustez do corpo. Auxilia muito no transporte. Poderia vir um software pelo menos trial para poder editar fotos. Mas o essencial para ter bons resultados é possível com este produto. Para quem nunca teve experiências com câmera DSLR é um bom começo e possível início da arte da fotografia."
    # },
    # "30.003": {
    #     "opinions": [
    #         [
    #             "Deveria vir com bateria extra.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Atende minhas necessidades.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Deveria vir com bateria extrado demais atende minhas necessidades."
    # },
    # "30.004": {
    #     "opinions": [
    #         [
    #             "Gostei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Esta sendo bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Gostei. Esta sendo bom."
    # },
    # "30.005": {
    #     "opinions": [
    #         [
    #             "Consigo fotos muito bonitas sem muito trabalho de ajuste fino.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Permite fotos com qualidade profissional, desfocadas, com planos bem distintos( adoro! rsrs) e com alta resolução.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Tem ISO relativamente bom, mas apresenta uma limitação em qualidade a partir do ISO 1600. Com ISO acima disso as fotos ficam boas, mas apresentam algumas granulações leves. Até o momento, o ISO 1200 foi o máximo que senti necessidade de usar, então, na prática, esse fator não me incomoda.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo custo-benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Apesar de ter nome parecido, não recomendo que seja feita comparação com a T5i por serem equipamentos beeem diferentes, não só no valor ( cerca de R$1000,00 de diferença), como na destinação do produto, já que a T5 é volta para fotos( apesar de fazer vídeos curtos) e a T5i possui tecnologia para vídeos bem mais avançada, incluindo comando touch( mais rápido para correção durante uma gravação)",
    #             "PRODUTO",
    #             "!"
    #         ],
    #         [
    #             "Recomendo muito a compra!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Para quem quer tirar fotos pessoais com qualidade profissional, essa é uma ótima opção de produto.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Comprei para uso doméstico, pois queria fotos com muita qualidade e uma câmera com mais recursos do que as superzoom. Amei o produto!",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Achei os comandos bem intuitivos.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Uma coisa muito legal é a possibilidade de trocar as lentes, pois o produto é compatível com todas as lentes da marca.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "É uma câmera de entrada no mundo DSLR, com funções pré-programadas e a possibilidade de fazer configurações próprias, à medida que o usuário vai se familiarizando com esse tipo de equipamento.",
    #             "USABILIDADE",
    #             "+."
    #         ]
    #     ],
    #     "review": "Ótimo custo-benefício. Comprei para uso doméstico, pois queria fotos com muita qualidade e uma câmera com mais recursos do que as superzoom. Amei o produto! É uma câmera de entrada no mundo DSLR, com funções pré-programadas e a possibilidade de fazer configurações próprias, à medida que o usuário vai se familiarizando com esse tipo de equipamento. Permite fotos com qualidade profissional, desfocadas, com planos bem distintos( adoro! rsrs e com alta resolução. Tem ISO relativamente bom, mas apresenta uma limitação em qualidade a partir do ISO 1600. Com ISO acima disso as fotos ficam boas, mas apresentam algumas granulações leves. Até o momento, o ISO 1200 foi o máximo que senti necessidade de usar, então, na prática, esse fator não me incomoda. Achei os comandos bem intuitivos e consigo fotos muito bonitas sem muito trabalho de ajuste fino. Recomendo muito a compra! Para quem quer tirar fotos pessoais com qualidade profissional, essa é uma ótima opção de produto. Uma coisa muito legal é a possibilidade de trocar as lentes, pois o produto é compatível com todas as lentes da marca. Apesar de ter nome parecido, não recomendo que seja feita comparação com a T5i por serem equipamentos beeem diferentes, não só no valor ( cerca de R$1000,00 de diferença), como na destinação do produto, já que a T5 é volta para fotos( apesar de fazer vídeos curtos) e a T5i possui tecnologia para vídeos bem mais avançada, incluindo comando touch( mais rápido para correção durante uma gravação"
    # },
    # "30.006": {
    #     "opinions": [
    #         [
    #             "Uma coisa que falta é a utilização de um microfone externo que faz muita falta.",
    #             "ÁUDIO",
    #             "-"
    #         ],
    #         [
    #             "Ótimo Produto!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uma câmera para a introdução a fotografia.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Ótimo Produto! Uma câmera para a introdução a fotografia, uma coisa que falta é a utilização de um microfone externo que faz muita falta."
    # },
    # "30.007": {
    #     "opinions": [
    #         [
    #             "Positivo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Positivo. Ótimo produto."
    # },
    # "30.008": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente."
    # },
    # "30.009": {
    #     "opinions": [
    #         [
    #             "EXCELENTE PRODUTO.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "ÓTIMO PRODUTO PARA SEMI PROFISSIONAIS.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "EXCELENTE PRODUTO. ÓTIMO PRODUTO PARA SEMI PROFISSIONAIS."
    # },
    # "30.010": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom."
    # },
    # "30.011": {
    #     "opinions": [
    #         [
    #             "Quero ter uma Canon- Eos-rebel-t5- 18,0 Megapixels.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tenho Uma Canon Power Shot SX 40 HS, é uma excelente Câmera, mas gostaria muito de ter uma Canon-Eos-rebel- T5 -18.0 megapixels.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Quero ter uma Canon- Eos-rebel-t5- 18,0 Megapixels. Tenho Uma Canon Power Shot SX 40 HS, é uma excelente Câmera, mas gostaria muito de ter uma Canon-Eos-rebel- T5 -18.0 megapixels."
    # },
    # "30.012": {
    #     "opinions": [
    #         [
    #             "Muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Câmera rebel T5. Muito bom!"
    # },
    # "30.013": {
    #     "opinions": [
    #         [
    #             "Ótima.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ela é uma das melhores câmeras que eu já usei.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótima. Ela é uma das melhores câmeras que eu já usei."
    # },
    # "30.014": {
    #     "opinions": [
    #         [
    #             "E o preço esta muito bom.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Custo beneficio excelente.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Excelente. Eu não possuo uma, mas trabalhei com ela no meu emprego, Agencia de Propaganda, e achei excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O display giratório que possui em alguns modelos diferentes não interfere na qualidade do T5!!! Recomendo.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Eu não possuo uma, mas trabalhei com ela no meu emprego, Agencia de Propaganda, e achei excelente. O display giratório que possui em alguns modelos diferentes não interfere na qualidade do T5!!! Recomendo. E o preço esta muito bom. Custo beneficio excelente."
    # },
    # "30.015": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Gostei muito.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Gostei muito."
    # },
    # "30.016": {
    #     "opinions": [
    #         [
    #             "Um ponto negativo é a lente do kit, porem essa pode ser ótima opção para começo e assim q perceber sua necessidade saberá qual tipo de lente é melhor para cada usuário.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "O custo beneficio, é um dos maiores pontos positivos.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Muito Boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uma ótima opção para fotógrafos iniciantes e amadores que querem se profissionalizar.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Claro que para usufruir de todas as funções, de maneira eficaz é necessário estudar e testar, assim é possivel criar imagens com qualidade profissionais, sem deixar nada a desejar.",
    #             "USABILIDADE",
    #             "-."
    #         ]
    #     ],
    #     "review": "Muito Boa. Uma ótima opção para fotógrafos iniciantes e amadores que querem se profissionalizar.O custo beneficio, é um dos maiores pontos positivos. Claro que para usufruir de todas as funções, de maneira aficais é necessário estudar e testar, assim é possivel criar imagens com qualidade profissionais, sem deixar nada a desejar.Um ponto negativo é a lente do kit, porem essa pode ser ótima opção para começo e assim q perceber sua necessidade saberá qual tipo de lente é melhor para cada usuário."
    # },
    # "30.017": {
    #     "opinions": [
    #         [
    #             "Perfeita.",
    #             "PRODUTO",
    #             "++"
    #         ],
    #         [
    #             "Faço freela para fotografia, comprei essa camera faz uns 2 anos ela e perfeita.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Perfeita. Faço freela para fotografia, comprei essa camera faz uns 2 anos ela e perfeita."
    # },
    # "30.018": {
    #     "opinions": [
    #         [
    #             "A qualidade de imagem é incrível!",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Maravilhosa.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhosa. A qualidade de imagem é incrível!"
    # },
    # "30.019": {
    #     "opinions": [
    #         [
    #             "Fantastica.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Me satisfaz em melhores imagens do meu dia a dia.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Fantastica. Me satisfaz em melhores imagens do meu dia a dia."
    # },
    # "30.020": {
    #     "opinions": [
    #         [
    #             "Controle de foco fácil. Manual ou automático.",
    #             "FOCO",
    #             "+"
    #         ],
    #         [
    #             "A qualidade das imagens são muito boas.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Maravilhoso.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Tive uma excelente experiência.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O Display é bem fácil de acessar.",
    #             "TELA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhoso. Tive uma excelente experiência. A qualidade das imagens são muito boas. O Display é bem fácil de acessar, controle de foco fácil. Manual ou automático."
    # },
    # "30.021": {
    #     "opinions": [
    #         [
    #             "Depois que comprei esta câmera minhas fotos melhoraram Muito, Agora tenho fotos a nível profissional, com ela já fiz ate alguns ensaios e adquiri uma renda extra.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Sensacional..",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A três anos fiz um pesquisa aqui no site Buscape sobre câmeras digitais e fui tirando minhas duvidas, enfim escolhi a câmera Canon EOS Rebel T5.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não tenho oque reclamar deste aparelho, simplesmente sensacional.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Sensacional.. A três anos fiz um pesquisa aqui no site Buscape sobre câmeras digitais e fui tirando minhas duvidas, enfim escolhi a câmera Canon EOS Rebel T5. Depois que comprei esta câmera minhas fotos melhoraram Muito, Agora tenho fotos a nível profissional, com ela já fiz ate alguns ensaios e adquiri uma renda extra. Não tenho oque reclamar deste aparelho, simplesmente sensacional."
    # },
    # "30.022": {
    #     "opinions": [
    #         [
    #             "Ótima.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Meu primo tem uma, se eu pudesse compraria uma.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótima. Meu primo tem uma, se eu pudesse compraria uma."
    # },
    # "30.023": {
    #     "opinions": [
    #         [
    #             "Fotos em alta definição.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo custo benefício!",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Sensacional.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "A Câmera tem ótimo desempenho e tem resultados de uma semi professional.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Sensacional. Ótimo custo benefício! Fotos em alta definição. A Câmera tem ótimo desempenho e tem resultados de uma semi professional."
    # },
    # "30.024": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto perfeito muito bom.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Muito bom. Produto perfeito muito bom."
    # },
    # "30.025": {
    #     "opinions": [
    #         [
    #             "Interessante.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo p/ elaborar trabalhos etc.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Interessante. Fácil manuseio, ótimo p/ elaborar trabalhos etc."
    # },
    # "30.026": {
    #     "opinions": [
    #         [
    #             "Gostei muito do produto!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente câmera! Vale a pena.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Quem não é profissional basta dar uma estudada, ler e praticar!",
    #             "USABILIDADE",
    #             "!"
    #         ]
    #     ],
    #     "review": "Gostei muito do produto! Excelente câmera! Vale a pena.Quem não é profissional basta dar uma estudada, ler e praticar!"
    # },
    # "30.027": {
    #     "opinions": [
    #         [
    #             "Sensacional.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom, vale a pena!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Sensacional. Muito bom, vale a pena!"
    # },
    # "30.028": {
    #     "opinions": [
    #         [
    #             "Bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Para quem procura uma câmera de entrada ela é muito boa!",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom! Para quem procura uma câmera de entrada ela é muito boa!"
    # },
    # "30.029": {
    #     "opinions": [
    #         [
    #             "Ótima.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo, recomendo super.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótima. Recomendo, recomendo super."
    # },
    # "30.031": {
    #     "opinions": [
    #         [
    #             "Registre seus melhores momentos em detalhes!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Que tal unir lazer e profissionalismo? Com a Câmera Digital Canon EOS Rebel T5 18.0 Megapixels agora você pode!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Registrei com detalhes os melhores momentos em família, amigos e amores. Mas não para por ai! As fotos ficaram tão bacanas e reconhecidas que fiz desse meu talento que descobri com a Conon EOS Rebel a construção da minha vida profissional! Hoje faço fotos de todos os tipos e para todos os gostos. Só a Conon mesmo para me proporcionar tanta coisa boa! Sou fotógrafa por paixão e Conor de coração!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É super portátil, levo para todos os lugares comigo, viagens longas ou no parque da cidade que fica bem em frente a minha casa.",
    #             "TAMANHO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Registre seus melhores momentos em detalhes! Que tal unir lazer e profissionalismo? Com a Câmera Digital Canon EOS Rebel T5 18.0 Megapixels agora você pode! É super portátil, levo para todos os lugares comigo, viagens longas ou no parque da cidade que fica bem em frente a minha casa. Registrei com detalhes os melhores momentos em família, amigos e amores. Mas não para por ai! As fotos ficaram tão bacanas e reconhecidas que fiz desse meu talento que descobri com a Conon EOS Rebel a construção da minha vida profissional! Hoje faço fotos de todos os tipos e para todos os gostos. Só a Conon mesmo para me proporcionar tanta coisa boa! Sou fotógrafa por paixão e Conor de coração!"
    # },
    # "30.032": {
    #     "opinions": [
    #         [
    #             "O ruim dela é a duração da bateria,acaba rápido.",
    #             "BATERIA",
    #             "-"
    #         ],
    #         [
    #             "Minha paixão.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Amei esse produto,me surpreendi com a ótima qualidade,essa câmera virou minha queridinha,amei ela mesmo,",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "E ela é super fácil de mexer.Recomendo para todos.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Minha paixão. Amei esse produto,me surpreendi com a ótima qualidade,essa câmera virou minha queridinha,amei ela mesmo,só que o ruim dela é a duração da bateria,acaba rápido,mais o respo é ótimo,e ela é super fácil de mexer.Recomendo para todos."
    # },
    # "30.033": {
    #     "opinions": [
    #         [
    #             "Relativamente bom o investimento.",
    #             "PREÇO",
    #             "+."
    #         ],
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O produto apresenta diversas características de uso profissional amador, comprei para uso pessoal e tive bons resultados.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Relativamente bom o investimento, o produto apresenta diversas características de uso profissional amador, comprei para uso pessoal e tive bons resultados."
    # },
    # "30.034": {
    #     "opinions": [
    #         [
    #             "Produto de excelente qualidade ! recomendo a todos .",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Canon t5. Produto de excelente qualidade ! recomendo a todos ."
    # },
    # "30.035": {
    #     "opinions": [
    #         [
    #             "Otimo produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto de qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo a todos os iniciantes que desejam dar um passo a mais no mundo da fotografia.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito intuitiva, fácil de usar.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Otimo produto. Produto de qualidade, muito intuitiva, fácil de usar e qualidade de imagem.Recomendo a todos os iniciantes que desejam dar um passo a mais no mundo da fotografia."
    # },
    # "30.036": {
    #     "opinions": [
    #         [
    #             "Não possuo,mas penso em ser fotográfa e obtê-la um dia!",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Não possuo,mas penso em ser fotográfa e obtê-la um dia!"
    # },
    # "30.037": {
    #     "opinions": [
    #         [
    #             "Maravilhoso.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Faço free lance e está sendo de ótimo benefício!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhoso. Faço free lance e está sendo de ótimo benefício!"
    # },
    # "30.038": {
    #     "opinions": [
    #         [
    #             "Excelente produto para iniciantes em fotografia.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente Produto. Excelente produto para iniciantes em fotografia."
    # },
    # "30.039": {
    #     "opinions": [
    #         [
    #             "Ótimo custo benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto muito bom, ótima qualidade",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom. Produto muito bom, ótima qualidade, fácil manuseio. Ótimo custo benefício."
    # },
    # "30.040": {
    #     "opinions": [
    #         [
    #             "A entrega foi rápida.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "Produto me agradou muito.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo pra quem está começando.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo pra quem está começando. Produto me agradou muito e a entrega foi rápida."
    # },
    # "30.041": {
    #     "opinions": [
    #         [
    #             "E ótima tem um foco excelente.",
    #             "FOCO",
    #             "+"
    #         ],
    #         [
    #             "Perfect.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Perfect. E ótima tem um foco excelente."
    # },
    # "30.042": {
    #     "opinions": [
    #         [
    #             "Uma ótima compra.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Esta câmera é um ótimo produto,estou satisfeito e fazendo muitos registro importante, pode compra esta aprovado.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Uma ótima compra. Esta câmera é um ótimo produto,estou satisfeito e fazendo muitos registro importante, pode compra esta aprovado."
    # },
    # "30.043": {
    #     "opinions": [
    #         [
    #             "Em que pese a lente do kit basico ser de abertura maxima 3,5 nao muito apropriada para ambientes de pouca iluminacao e internos, por ter um sensor grande o ISO pode ir ate 1600 com um minimo de ruido.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "O acabamento e muito bom e da impressao de resistencia.",
    #             "DESIGN",
    #             "+"
    #         ],
    #         [
    #             "Sempre tive as cameras Canon e considero a melhor marca do mundo pela qualidade das lentes e acabamento.",
    #             "EMPRESA",
    #             "+"
    #         ],
    #         [
    #             "O custo beneficio vale a pena.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Comprei recentemente essa camera por um otimo preco em uma grande rede de hipermercados.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Confesso que me surpreendi com ela.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo a sua compra para quem esta comecando a fotografia profissional e laser.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Surpreendente para uma Camera Canon.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Vantajosa no tocante ao uso de outras lentes e de facil troca.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Surpreendente para uma Camera Canon. Confesso que me surpreendi com ela.Comprei recentemente essa camera por um otimo preco em uma grande rede de hipermercados.Em que pese a lente do kit basico ser de abertura maxima 3,5 nao muito apropriada para ambientes de pouca iluminacao e internos, por ter um sensor grande o ISO pode ir ate 1600 com um minimo de ruido.O acabamento e muito bom e da impressao de resistencia.O custo beneficio vale a pena.Vantajosa no tocante ao uso de outras lentes e de facil troca.Sempre tive as cameras Canon e considero a melhor marca do mundo pela qualidade das lentes e acabamento.Recomendo a sua compra para quem esta comecando a fotografia profissional e laser."
    # },
    # "30.044": {
    #     "opinions": [
    #         [
    #             "Encatamento!!!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Adquiri há pouco tempo mas, estou adorando o produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Há tempo queria comprar, dessa forma é, uma realização.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Encatamento!!! Adquiri há pouco tempo mas, estou adorando o produto. Há tempo queria comprar, dessa forma é, uma realização."
    # },
    # "30.045": {
    #     "opinions": [
    #         [
    #             "Maquina excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Boa maquina para quem esta começando a fotografar.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maquina excelente. Boa maquina para quem esta começando a fotografar."
    # },
    # "30.046": {
    #     "opinions": [
    #         [
    #             "Rebel T5 Canon, uma boa opça.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto, confiável e com bom rendimento.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Rebel T5 Canon, uma boa opça. Ótimo produto, confiável e com bom rendimento."
    # },
    # "30.047": {
    #     "opinions": [
    #         [
    #             "Anuncio falso. Vocês indicam que a camera custa 1.349 , quando vou no site fazer a compra lá custa 1.899, anuncio falso.",
    #             "EMPRESA",
    #             "-"
    #         ]
    #     ],
    #     "review": "Anuncio falso. Vocês indicam que a camera custa 1.349 , quando vou no site fazer a compra lá custa 1.899, anuncio falso."
    # },

    #     "31.001": {
    #     "opinions": [
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Pode comprar esse produto tem qualidade.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente produto. Pode comprar esse produto tem qualidade."
    # },
    # "31.002": {
    #     "opinions": [
    #         [
    #             "Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo o produto pela sua qualidade, nota 1000.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente. Recomendo o produto pela sua qualidade, nota 1000."
    # },
    # "31.003": {
    #     "opinions": [
    #         [
    #             "Boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito bom ..estou feliz.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom ..estou feliz. Boa."
    # },
    # "31.004": {
    #     "opinions": [
    #         [
    #             "Excelente custo-benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto pra quem está iniciando no ramo de fotografia.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Excelente custo-benefício. Ótimo produto pra quem está iniciando no ramo de fotografia."
    # },
    # "31.005": {
    #     "opinions": [
    #         [
    #             "Algumas informações não vieram no Manual.",
    #             "ACESSÓRIO",
    #             "-"
    #         ],
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Maravilhoso.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou ainda aprendendo a manusear.",
    #             "USABILIDADE",
    #             "X"
    #         ]
    #     ],
    #     "review": "Maravilhoso. Muito bom. Estou ainda aprendendo a manusear. Algumas informações não viram no Manual."
    # },
    # "31.006": {
    #     "opinions": [
    #         [
    #             "Ótimo, eu recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Correspondente com todas as características citadas.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muito fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo, eu recomendo! Correspondente com todas as características citadas, muito fácil manuseio.."
    # },
    # "31.007": {
    #     "opinions": [
    #         [
    #             "Gostei e recomendo!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É tudo que eu esperava, completamente satisfeito!",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Gostei e recomendo! É tudo que eu esperava, completamente satisfeito!"
    # },
    # "31.008": {
    #     "opinions": [
    #         [
    #             "Amei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Amei super facil de usar.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Amei. Amei super facil de usar."
    # },
    # "31.009": {
    #     "opinions": [
    #         [
    #             "Porém, me incomodou o ruído presente no momento de gravação de videos. A câmera fica com um ruído, como se estivesse se esforçando muito para gravar, e no vídeo pronto, o ruído aparece.",
    #             "ÁUDIO",
    #             "-"
    #         ],
    #         [
    #             "A qualidade de imagem para fotos é incrível.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "A imagem é muito boa.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Bom custo-beneficio.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "É uma boa câmera.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O produto era o que eu esperava, para uma câmera semi-profissional de entrada.",
    #             "PRODUTO",
    #             "+."
    #         ],
    #         [
    #             "Muito fácil de usar.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Não recomento a câmera para quem queira fazer videos profissionais.",
    #             "VÍDEO",
    #             "-."
    #         ]
    #     ],
    #     "review": "Bom custo-beneficio. O produto era o que eu esperava, para uma câmera semi-profissional de entrada. A imagem é muito boa e muito fácil de usar. Porém, me incomodou o ruído presente no momento de gravação de videos. A câmera fica com um ruído, como se estivesse se esforçando muito para gravar, e no vídeo pronto, o ruído aparece. Não recomento a câmera para quem queira fazer videos profissionais, fora isso, é uma boa câmera, e a qualidade de imagem para fotos é incrível."
    # },
    # "31.010": {
    #     "opinions": [
    #         [
    #             "Amei.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Amei, super recomendo a todos camera maravilhosa.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Amei. Amei, super recomendo a todos camera maravilhosa."
    # },
    # "31.011": {
    #     "opinions": [
    #         [
    #             "A bateria é bastante resistente.",
    #             "BATERIA",
    #             "+"
    #         ],
    #         [
    #             "Imagem excelente da pra brincar até de ser fotógrafo!! kkkkkk.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Camera muito boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Uma ótima aquisição!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Já vai fazer 1 ano que tenho ela, nunca tive problema, super recomendo!",
    #             "RESISTÊNCIA",
    #             "+"
    #         ]
    #     ],
    #     "review": "Uma ótima aquisição! Camera muito boa, imagem excelente da pra brincar até de ser fotógrafo!! kkkkkk a bateria é bastante resistente, tem tb diversas funçoes para tirar foto bem interessante. Já vai fazer 1 ano que tenho ela, nunca tive problema, super recomendo!"
    # },
    # "31.012": {
    #     "opinions": [
    #         [
    #             "Otima.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não tenho mas estou encantada.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Otima. Não tenho mas estou encantada."
    # },
    # "31.013": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não é uma câmera profissional, mas dá pra fazer muita coisa boa com ela, sabendo usar.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Bom. Não é uma câmera profissional, mas dá pra fazer muita coisa boa com ela, sabendo usar."
    # },
    # "31.014": {
    #     "opinions": [
    #         [
    #             "Bateria com duração razoável.",
    #             "BATERIA",
    #             "."
    #         ],
    #         [
    #             "Imagem com resolução muito boa.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Ótimo custo-benefício.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Adorei o produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Fácil de manusear.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo custo-benefício. Excelente produto. Imagem com resolução muito boa, bateria com duração razoável, fácil de manusear. Adorei o produto."
    # },
    # "31.015": {
    #     "opinions": [
    #         [
    #             "Maquina de boa resolução das fotos.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Facilidade no uso.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Maquina de fácil utilização.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Facilidade no uso. Maquina de fácil utilização e boa resolução das fotos."
    # },
    # "31.016": {
    #     "opinions": [
    #         [
    #             "Adquiri o produto e avalio ótimo custo-benefício.",
    #             "PREÇO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo custo-benefício. Adquiri o produto e avalio ótimo custo-benefício."
    # },
    # "31.017": {
    #     "opinions": [
    #         [
    #             "Excelente produto.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo zoom.",
    #             "ZOOM",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente produto. Ótimo zoon."
    # },
    # "31.018": {
    #     "opinions": [
    #         [
    #             "Muito boa!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Nossa o zoom dela é incrível, muito boa!",
    #             "ZOOM",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito boa! Nossa o zoom dela é incrível, muito boa!"
    # },
    # "31.019": {
    #     "opinions": [
    #         [
    #             "Uma ótima câmera para quem gosta de fotos.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Ótimo produto, recomendo a todos a compra dessa câmera, para quem gosta de fotos vai suprir todas as necessidades.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Uma ótima câmera para quem gosta de fotos. Ótimo produto, recomendo a todos a compra dessa câmera, para quem gosta de fotos vai suprir todas as necessidades."
    # },
    # "31.020": {
    #     "opinions": [
    #         [
    #             "Qualidade da imagem.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Facilidade no uso.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Maquina Boa utilização.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maquina Boa utilização. Qualidade da imagem, facilidade no uso."
    # },
    # "31.021": {
    #     "opinions": [
    #         [
    #             "Imagem de ótima qualidade.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Para meus hobbies é ideal, tem zoom de longo alcance e perfeito para amador como eu.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Imagem de ótima qualidade. Para meus hobbies é ideal, tem zoom de longo alcance e perfeito para amador como eu."
    # },
    # "31.022": {
    #     "opinions": [
    #         [
    #             "Câmera muito boa!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "O zoom dela é incrível!",
    #             "ZOOM",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito boa! Câmera muito boa! O zoom dela é incrível!"
    # },
    # "31.023": {
    #     "opinions": [
    #         [
    #             "Ótimo produto, superou minhas expectativas, recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Ótimo produto. Ótimo produto, superou minhas expectativas, recomendo."
    # },
    # "31.024": {
    #     "opinions": [
    #         [
    #             "Mto Boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Me surpreendeu o produto.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Mto Boa. Me surpreendeu o produto."
    # },
    # "31.025": {
    #     "opinions": [
    #         [
    #             "Ótimas fotos.",
    #             "FOTO",
    #             "+"
    #         ],
    #         [
    #             "Fotos com várias alternativas...",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Maravilhosa câmera (Canon SX520)",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Estou adorando a experiência com a Canon Powershot SX520! Muito boa, essa câmera!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente zoom (42).",
    #             "ZOOM",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhosa câmera (Canon SX520 Estou adorando a experiência com a Canon Powershot SX520!Muito boa, essa câmera!Excelente zoom (42 e ótimas fotos com várias alternativas..."
    # },
    # "31.026": {
    #     "opinions": [
    #         [
    #             "Vem com um cartão de memória, mas, para uma excelente câmera, faltou a disponibilidade de memória interna. Mas já substituí o cartão de 8gb por um de 32gb.",
    #             "ARMAZENAMENTO",
    #             "-."
    #         ],
    #         [
    #             "Leve.",
    #             "PESO",
    #             "+"
    #         ],
    #         [
    #             "Excelente câmera!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Me agradou muito sua funcionalidade.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Recomendo essa excelente câmera Canon SX520!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Agradável manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ],
    #         [
    #             "Com ótimo zoom.",
    #             "ZOOM",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente câmera! Recomendo essa excelente câmera Canon SX520!Me agradou muito sua funcionalidade, com ótimo zoom, leve e agradável manuseio.Vem com um cartão de memória, mas, para uma excelente câmera, faltou a disponibilidade de memória interna. Mas já substituí o cartão de 8gb por um de 32gb."
    # },
    # "31.027": {
    #     "opinions": [
    #         [
    #             "Excelente custo benefício para um iniciante.",
    #             "PREÇO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Excelente custo benefício para um iniciante. Excelente custo benefício."
    # },
    # "31.028": {
    #     "opinions": [
    #         [
    #             "Muitos recursos!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Excelente zoom.",
    #             "ZOOM",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito boa. Produto muito bom. Excelente zoom e muitos recursos!"
    # },
    # "31.029": {
    #     "opinions": [
    #         [
    #             "Não dá para focar. o flash só acende na hora do disparo.",
    #             "FOCO",
    #             "-"
    #         ],
    #         [
    #             "Foto ruim pouca luminosidade.",
    #             "FOTO",
    #             "-"
    #         ],
    #         [
    #             "Fotograr à noite ou locais com pouca luminosidade é difícil.",
    #             "FOTO",
    #             "-"
    #         ]
    #     ],
    #     "review": "Foto ruim pouca luminosidade. Fotograr à noite ou locais com pouca luminosidade é difícil. Não dá para focar e o flash só acende na hora do disparo."
    # },
    # "31.030": {
    #     "opinions": [
    #         [
    #             "Muito bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Muita qualidade!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Era tudo o que eu esperava.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom! Era tudo o que eu esperava. Muita qualidade!"
    # },
    # "31.031": {
    #     "opinions": [
    #         [
    #             "Maravilhosa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Grava Vídeos.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhosa. Grava Vídeos."
    # },
    # "31.032": {
    #     "opinions": [
    #         [
    #             "Ótima legal de usar.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom legal de usar. Ótima legal de usar."
    # },
    # "31.033": {
    #     "opinions": [
    #         [
    #             "Manual completo.",
    #             "ACESSÓRIO",
    #             "+"
    #         ],
    #         [
    #             "Qualidade das fotos perfeita.",
    #             "FOTO",
    #             "++"
    #         ],
    #         [
    #             "Câmera leve.",
    #             "PESO",
    #             "+"
    #         ],
    #         [
    #             "Adorei!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Maravilhosa!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Display perfeito.",
    #             "TELA",
    #             "++"
    #         ],
    #         [
    #             "Fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Maravilhosa! Câmera leve e fácil manuseio, manual completo, além do display e qualidade das fotos perfeitas. Adorei!"
    # },
    # "31.034": {
    #     "opinions": [
    #         [
    #             "Ótimo!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Um parente meu comprou e me emprestou para que eu pudesse avaliar, eu fiquei completa e absurdamente viciada, meu celular ficou em um canto que eu só usava para fazer ligações. Quando ele me pediu de volta eu disse que o produto ficaria comigo e não devolveria mais em hipótese alguma!",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Ótimo! Um parente meu comprou e me emprestou para que eu pudesse avaliar, eu fiquei completa e absurdamente viciada, meu celular ficou em um canto que eu só usava para fazer ligações. Quando ele me pediu de volta eu disse que o produto ficaria comigo e não devolveria mais em hipótese alguma!"
    # },
    # "31.035": {
    #     "opinions": [
    #         [
    #             "Muito bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito bom."
    # },
    # "31.036": {
    #     "opinions": [
    #         [
    #             "Produto coerente com todas as especificações técnicas.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Produto coerente com todas as especificações técnicas."
    # },
    # "31.037": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom."
    # },
    # "31.039": {
    #     "opinions": [
    #         [
    #             "Produto show de bola.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Ganhei de presente e não usei ainda. Mas, já li a respeito e por isso eu escolhi de presente de aniversario.",
    #             "PRODUTO",
    #             "x"
    #         ]
    #     ],
    #     "review": "Produto show de bola. Ganhei de presente e não usei ainda.Mas, já li a respeito e por isso eu escolhi de presente de aniversario."
    # },
    # "31.040": {
    #     "opinions": [
    #         [
    #             "A câmera atende ao que se propõe. Muito boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "As funções são variadas e sabendo usá-las a câmera é muito boa.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "É necessário aprender a usar as funções. O modo automático não é muito eficiente.",
    #             "USABILIDADE",
    #             "-"
    #         ]
    #     ],
    #     "review": "A câmera atende ao que se propõe. Muito boa. É necessário aprender a usar as funções. O modo automático não é muito eficiente, mas as funções são variadas e sabendo usa-las a câmera é muito boa."
    # },
    # "31.041": {
    #     "opinions": [
    #         [
    #             "Muito Bom!",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Experimentei com um amigo e adorei! Quero uma camera assim.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Não tão grande.",
    #             "TAMANHO",
    #             "+."
    #         ],
    #         [
    #             "Fácil manuseio.",
    #             "USABILIDADE",
    #             "+"
    #         ]
    #     ],
    #     "review": "Muito Bom! Experimentei com um amigo e adorei! Quero uma camera assim. Fácil manuseio e não tão grande."
    # },
    # "31.042": {
    #     "opinions": [
    #         [
    #             "Se você ama registrar momentos noturno essa câmera não deixa a desejar.",
    #             "IMAGEM",
    #             "+"
    #         ],
    #         [
    #             "Está em ótimo custo beneficio garanto que quem adquirir esse produto não vai se arrepender.",
    #             "PREÇO",
    #             "+"
    #         ],
    #         [
    #             "Produto Excelente.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Sabemos que canon é a melhor marca para câmera para qualquer tipo de uso, eu tenho essa câmera e posso afirmar que ela superou as minhas expectativas não só pela qualidade da imagem mais também pela qualidade do vídeo que esse produto é capaz de fazer.",
    #             "PRODUTO",
    #             "++"
    #         ]
    #     ],
    #     "review": "Produto Excelente. Sabemos que canon é a melhor marca para câmera para qualquer tipo de uso, eu tenho essa câmera e posso afirmar que ela superou as minhas expectativas não só pela qualidade da imagem mais também pela qualidade do vídeo que esse produto é capaz de fazer. Está em ótimo custo beneficio garanto que quem adquirir esse produto não vai se arrepender e se você ama registrar momentos noturno essa câmera não deixa a desejar."
    # },
    # "31.043": {
    #     "opinions": [
    #         [
    #             "Mt boa.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "MT bom. Mt boa."
    # },
    # "31.044": {
    #     "opinions": [
    #         [
    #             "Recomendo.",
    #             "PRODUTO",
    #             "+"
    #         ],
    #         [
    #             "Produto muito bom para quem é amador e quer tirar fotos no lazer.",
    #             "PRODUTO",
    #             "+."
    #         ]
    #     ],
    #     "review": "Recomendo. Produto muito bom para quem é amador e quer tirar fotos no lazer."
    # },
    # "31.045": {
    #     "opinions": [
    #         [
    #             "Bom.",
    #             "PRODUTO",
    #             "+"
    #         ]
    #     ],
    #     "review": "Bom. Nenhuma."
    # }

}


with open("tagged_reviews.p", "wb") as f:
    pickle.dump(textos, f)
print("done.")
