#!/usr/bin/env python
# coding: utf-8

print "This is console module"
import time
import random
import datetime
import sys
from PythonColorize import *
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
#End
reload(sys) 
sys.setdefaultencoding('utf8')
	
## BOT Config
today = datetime.datetime.today()
t = today.strftime("[%H:%M:]")
tm= today.strftime("%H:%M:")
uptime = datetime.datetime.today()
horas = uptime.strftime("%H:%M")
data = uptime.strftime("%d/%m/%Y")
M = uptime.strftime("%m")
D = uptime.strftime("%d")
A = uptime.strftime("%Y")
bot = telepot.Bot('SEU TOKEN API')
NomeBot = "GE"

## BOT LANG
letra = u'*{}*  é a sua letra do alfabeto gerada!  =]'
info_id = u'*Ok! vou te passar suas informações!* 😝\n\nSeu nome é *{}*\nSeu nome de usuário é {}\n Seu ID é `{}`'
dados = "Acabei de gerar o número *{}* =]"
info_sart= u' Olá *{}*, tudo bem? 😌 \nEu sou um *bot simples*, do canal @Aprender!\n\nAqui você irá encontrar de forma fácil e prática todos os canais,bots educativos e mais alguns *extras* para te auxiliar. \n\n👉🏻 *Para usar todos os meus recursos digita* /menu'
blogs = u'*Ok,* *{}*, *aqui está a lista de blogs para seus estudos:*\n\n👉🏻 *Física:* http://fisicamoderna.blog.uol.com.br\n👉🏻 *Química:* http://www.quimicaensinada.blogspot.com.br\n👉🏻 *Biologia:* http://diariodebiologia.com\n👉🏻 *Matemática:* http://professoraju-mat.blogspot.com.br\n👉🏻 *Geografia:* http://geografiaetal.blogspot.com.br\n👉🏻 *História:* http://historiaagora.com.br\n👉🏻 *Português:* http://portugues.com.br'
produtos = u' *{}*, cofira nossos produtos\n 📚| *Produtos e Revistas:*\n\n📏 _GE História_\n📏 _GE Geografia_\n📏 _GE Química_\n📏 _GE Português_\n📏 _GE Biologia_\n📏 _GE Redação_\n📏 _GE Matemática_\n📏 _GE Física_\n📏 _GE Atualidades 1º e 2º semestre_\n📏 _GE Enem_\n📏 _GE Fuvest_\n📏 _GE Profissões_\n📏 _GE EaD_\n📏 _GE Pós & MBA_\n📏 _GE Resumos & Simulados_'
info = u'Ok,  *{}* ! Vou te passar minhas informações'
start = u'Olá  *{}* ,  Vamos Estudar? 😉\n\nEu sou o *Robô GE*, fui criado pra te auxiliar com a interação do site *Guia do Estudante.*\n\n*O que eu posso fazer?*\nBom, eu sou bastante inteligente.  Eu posso te *indicar canais de estudos te enviar dicas para você estudar* e muito mais.'
info_data= "Hoje é dia *{}* do mês *{}* de *{}*, Por sinal é um dia lindo para estudar! 😄 ."
estudo = '*{}*, hoje você está com *{}* de vontade de estudar!!! =]'
total = '*{}*,  temos *{}* mensagens no seu privado!  =]'
hora = 'O meu relógio indica que são *{}*'
def handle(msg):
### BOT PARAMTS
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    from_id = msg['from']['id']
    from_first_name = msg['from']['first_name']
    from_username = "@" + msg['from']['username']
    texto = msg['text']
    txt = msg['text'].split(' ')
    print(colors.lg_green + t +  colors.lg_blue + from_username + colors.nocolor)
    print(colors.lg_green + t + colors.lg_green + "comando: " +colors.lg_yellow + texto + colors.nocolor)
    print(msg)
    

### BOT COMANDOS
    if 'numero' in texto or 'Numero' in texto:
        bot.sendMessage(chat_id, dados.format(random.randint(1,99)), "Markdown")
    elif texto == '/bhora':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif texto == '/start':
       markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='Site', url='http://guiadoestudante.abril.com.br')]+[dict(text='Compartilhe',switch_inline_query='  👉🏻| Tenha todas as dicas e conteúdo do site do Guia do Estudante na palma da sua mão. ')],])
       bot.sendMessage(chat_id, start.format(from_first_name), parse_mode='Markdown', reply_markup=markup)
       time.sleep(2)
       bot.sendMessage(chat_id, 'Vamos combinar um jeito de conversar? Escreva um assunto,  tipo:  *Português*, *Matemática*,  e eu respondo com uma dica para você estudar.', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, 'Ah!  eu também consigo fazer bastante coisas legais!  Como *calcular, Dar dicas* e muito mais.  Você pode usar todos os meus serviços *digitando* /menu que eu te passo!', parse_mode='Markdown')
       
    elif texto == 'MENU DO SITE':
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='📔| ENEM', url='http://guiadoestudante.abril.com.br/enem/')]+[dict(text='📙| Estudo', url='http://guiadoestudante.abril.com.br/estudo/')],[dict(text='📗| Profissões', url='http://guiadoestudante.abril.com.br/profissoes/')]+[dict(text='📘| Vestibulares', url='http://guiadoestudante.abril.com.br/universidades/')],[dict(text='📓| GE Bolsas', url='https://bolsas.guiadoestudante.com.br/')]+[dict(text='📕| FIES ProUni', url='http://guiadoestudante.abril.com.br/fies-prouni/')],[dict(text='📒| Orientação', url='http://guiadoestudante.abril.com.br/orientacao-profissional/')]+[dict(text='📘| Cursos EAD', url='http://guiadoestudante.abril.com.br/cursos-ead/')],[dict(text='📙| Cursos Enem', url='http://guiadoestudante.abril.com.br/curso-enem/')]+[dict(text='📗| Pós Graduação', url='http://guiadoestudante.abril.com.br/pos-graduacao/')],[dict(text='📕| Vídeos', url='http://guiadoestudante.abril.com.br/videos/')],])
        bot.sendMessage(chat_id, "Nesse *tópico* você poderá encontrar todos os conteúdos do site *Guia do Estudante* de forma fácil.\n\n👉🏻 Por favor, escolha entre as opções do *teclado:*", parse_mode='Markdown', reply_markup=markup)
    elif 'eu' in texto or 'EU' in texto:
        bot.sendMessage(chat_id, info_id.format(from_first_name, from_username,  str(from_id)), parse_mode='Markdown')
    elif texto == 'Canais Educativos':
        bot.sendMessage(chat_id, "📢|  @Portugues - *Aulas de Português* 📚\n\n📢|  @ministeriodaeducacao - *Canal do MEC* 📚\n\n📢|  @Inepbr -  *Canal do INEP* 📚\n\n📢|  @HoradoEnem - *Hora do Enem* 📚\n\n📢|  @Onubrasil - *Canal do ONU Brasil* 📚\n\n📢|  @Guiadoestudante - *Notícias sobre Educação* 📚\n\n📢|  @BrasilEscola - *Noticias sobre vestibular* 📚\n\n📢|  @redacao *Dicas de Redação* 📚\n\n📢|  @Planalto - *Canal com a rotina da república* 📚\n\n📢|  @Obrasil - *Notícias do Brasil* 📚\n\n📢|  @Congresso - *Notícias do Congresso* 📚\n\n📢|  @NationalGeographicBrasil - *Canal não oficial da revista* 📚\n\n📢|  @MinisteriodaSaude -  *Canal do ministério da saúde* 📚\n\n📢|  @ReceitaFederal *Canal da Receita Federal* 📚\n\n📢| @G1Educacao  *G1 Educação* 📚", parse_mode='Markdown')
    elif texto == 'Bots Educativos':
        bot.sendMessage(chat_id, "🍎| — @GramaticaBot -  Bot do canal @portugues, Aulas e dicas de gramáticas. ⚡\n\n🎲| — @SoMatematicaBot - Material de apoio de Matemática. ⚡️\n\n🇬🇧| — @SoinglesBot - Material de apoio de Inglês. ⚡️\n\n🐢| — @SoBiologiaBot - Material de apoio de Biologia. ⚡️\n\n🌏| — @SogeografiaBot - Material de apoio de Geografia. ⚡️\n\n📜| — @SoHistoriaBot - Material de Apoio de História ⚡️\n\n🔬| — @SoquimicaBot - Material de apoio de Química ⚡️\n\n✏️| — @RedacaoBot - Dicas para redigir um texto. ⚡️", parse_mode='Markdown')
    elif texto == 'Blogs Educativos':
        bot.sendMessage(chat_id, blogs.format(from_first_name), parse_mode='Markdown')
    elif texto == 'Sobre':
        bot.sendMessage(chat_id, "*APRENDER BOT*\n*VERSÃO:* `1.0.8`\n\n*CRIADO POR* : @JotaDrake\n\n`Aprender bot armazena canais e bots educativos do @aprender`", parse_mode='Markdown')
    elif texto == '/reboot':
        markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Confirm')], [KeyboardButton(text='Cancel')]], one_time_keyboard=True)
        bot.sendMessage(chat_id, 'Reboot?', reply_markup=markup)
    elif texto == 'Idealizador':
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', url='http://t.me/aprender')]])
        bot.sendMessage(chat_id, 'Olá, sou o Jota Drake, idealizador do projeto @Aprender onde contém diversos canais e bots educacionais e de interesse do pessoal da rede social inovadora e bastante proveitosa Telegram.\n\n\nEsse é apenas um dos projetos que tenho por lá.\nDedicar-me-ei a ele com o mesmo carinho e comprometimento que tenho com meus outros projetos.\n\n 📚 Por favor, entre no canal aprender abaixo, para ficar por dentro das atualizações do bot!', reply_markup=markup )    
    elif texto == 'APRENDER':
        markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Canais Educativos')], [KeyboardButton(text='Bots Educativos')], [KeyboardButton(text='Blogs Educativos')], [KeyboardButton(text='Sobre')]+[KeyboardButton(text='Idealizador')],[KeyboardButton(text='VOLTAR')]], one_time_keyboard=True)
        bot.sendMessage(chat_id, '- Por favor,Escolha entre as opções do teclado, temos canais e bots do projeto aprender:', reply_markup=markup)
    elif texto == '/test':
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', callback_data='Sobre')]])
        bot.sendMessage(chat_id, 'Olá, ', reply_markup=markup )
    elif texto == '/my':
        keyboard=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Press me',callback_data='press')],])
        bot.sendMessage(chat_id,'Use inline keyboard',reply_markup=keyboard)
    elif texto == '/ok':
        markup=ReplyKeyboardMarkup(keyboard=[['Plain text', KeyboardButton(text='Text only')],[dict(text='Phone',request_contact=True), KeyboardButton(text='Location',request_location=True)],])
        bot.sendMessage(chat_id,'Custom keyboard with various buttons',reply_markup=markup)
    elif texto == '/hj':
        markup=InlineKeyboardMarkup(inline_keyboard=[[dict(text='Telegram URL',url='https://core.telegram.org/')],[InlineKeyboardButton(text='Callback - show notification',callback_data='notification')],[dict(text='Callback - show alert',callback_data='alert')],[InlineKeyboardButton(text='Callback - edit message',callback_data='edit')],[dict(text='Switch to using bot inline',switch_inline_query='initial query')],])
        bot.sendMessage(chat_id,'Inline keyboard with various buttons',reply_markup=markup)
    elif texto == 'PROJETO APRENDER':
        markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Linguagens e tecnologias')], [KeyboardButton(text='Ciencias Naturais e tecnologias')], [KeyboardButton(text='Ciencias Humanas e tecnologias')], [KeyboardButton(text='Matematica e suas tecnologias')], [KeyboardButton(text='APRENDER')]+[KeyboardButton(text='Geral')],[KeyboardButton(text='VOLTAR')]], one_time_keyboard=True)
        bot.sendMessage(chat_id, '- Escolha entre as áreas do conhecimento que eu enviarei os canais recomendados para você:', reply_markup=markup)
    elif texto == 'Linguagens e tecnologias':
       markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', url='http://t.me/aprender')]])
       bot.sendMessage(chat_id, ' 👉🏻 *Linguagens, códigos e suas tecnologias:*\n\n01: @Portugues\n02: @Antiburrice\n03: @Cafecomletras\n\n04: @Aprendendoingles\n\n05: @English', parse_mode='Markdown', reply_markup=markup)
    elif texto == 'Ciencias Naturais e tecnologias':
       markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', url='http://t.me/aprender')]])
       bot.sendMessage(chat_id, ' 👉🏻 *Ciências da natureza e suas tecnologias:*\n\n01: @Cosmosastronomia\n02: @Biologia1\n03: @Abelhasnativasdobrasil\n04: @Nationalgeographicbrasil', parse_mode='Markdown', reply_markup=markup)
    elif texto == 'Ciencias Humanas e tecnologias':
       markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', url='http://t.me/aprender')]])
       bot.sendMessage(chat_id, ' 👉🏻 *Ciências Humanas e suas tecnologias:*\n\n01: @historiaparalela\n02: @olhovivo\n03: @Animalplanet\n04: @Causaeefeito', parse_mode='Markdown', reply_markup=markup)
    elif texto == 'Matematica e suas tecnologias':
       markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', url='http://t.me/aprender')]])
       bot.sendMessage(chat_id, ' 👉🏻 *Matemática e suas tecnologias:*\n\n01: @Matematica', parse_mode='Markdown', reply_markup=markup)
    elif texto == 'Geral':
       markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='🎓 APRENDER', url='http://t.me/aprender')]])
       bot.sendMessage(chat_id,' 👉🏻 *Geral:*\n\n01: @Conhecimento\n02: @HoradoEnem\n03: @ideiasincriveis\n04: @dicasdavovo', parse_mode='Markdown', reply_markup=markup)
    elif 'Português' in texto or 'português' in texto:
       bot.sendMessage(chat_id, 'Certo!  Vou te passar uma curiosidade sobre *Português*...', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, random.choice(["Sabia que o plural de gravidez e arroz é gravidezes e arrozes?" ,"A única palavra da língua portuguesa que forma o plural no meio é quaisquer. Legal, né?" ,"Saiba que muçarela é um tipo de queijo que se escreve com ç. 😁 ","A forma correta de escrita da palavra é  aerossol. Isso mesmo, com -ss. Não vai errar, OK? ❤️","A língua portuguesa veio dolatim vulgar, devido à época em os conquistadores romanos dominaram a península Ibérica.","A maior palavra da língua portuguesa é pneumoultramicroscopicossilicovulcanoconiótico, sabia?"," A palavra que reúne a maior quantidade de vogais juntas é piauiense."," Sabia que A bota se calça e a calça se bota?"]), "HTML")
    elif 'Geografia' in texto or 'geografia' in texto:
       bot.sendMessage(chat_id, 'Ok!  aguenta aí que já passo a dica de *Geografia...*', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, random.choice(["Batman é uma cidade localizada no sudeste da Turquia."," O Líbano é o único país do Oriente Médio que não tem deserto."," A bandeira do Nepal é a única bandeira (nacional) do mundo que não é retangular ou quadrada."," Nauru – é o único Estado independente do mundo que não tem capital oficial."," Você tem dinheiro? Há caixas eletrônicos na Antártica."," O rio que nunca encontra o mar: este é o apelido do rio Okavango que termina em um delta interior no meio do deserto de Kalahari."," A maioria das ruas do Japão não tem nome.","Vaticano é o menor País do mundo "]), "HTML")
    elif 'Química' in texto or 'quimica' in texto:
       bot.sendMessage(chat_id, 'Beleza!  Lá vai a dica de *Química*...', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, random.choice(["A farinha é o principal ingrediente para a fabricação do pão. E, embora possa ser produzido com diversos cereais, o trigo é o de melhor desempenho na panificação graças aos bons teores de amido e proteína.","A explosão de um grão de pipoca quando aquecido é o resultado da combinação de 3 substâncias"," Há cebola que possuem menos ácidos e outra que possuem mais, por isso que em algumas vezes não choramos ao cortá-las."," Vaga-lumes ou pirilampos são insetos das famílias Elateridae, Fengodidae ou Lampyridae muito conhecidos por sua bioluminescência"]), "HTML")
    elif 'História' in texto or 'história' in texto:
       bot.sendMessage(chat_id, 'Tá certo.  Já estou enviando a dica de *História*', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, random.choice(["O nome completo de D.Pedro I era Pedro de Alcântara Francisco Antônio João Carlos Xavier de Paula Miguel Rafael Joaquim José Gonzaga Pascoal Cipriano Serafim de Bragança e Bourbon."," Dom Pedro I teve oito filhos, sete do primeiro casamento e um do segundo. Além deles, o imperador teve outros seis filhos de relações extraconjugais."," Dom Pedro II foi aclamado Imperador aos 14 anos de idade, permanecendo no poder até os 63 anos."," .O Papa João XII, eleito em 955, foi o mais jovem a assumiro cargo, ele tinha apenas 18 anos."," .O maior palácio do mundo é o do sultão de Brunei. Tem 1.788 cômodos, 275 banheiros, garagem para 153 carros e teveo custo de 480 milhões de dólares."," Segundo Fidel Castro, ele já sobreviveu a mais de 630 tentativas de assassinato."]), "HTML")
    elif 'Biologia' in texto or 'biologia' in texto:
       bot.sendMessage(chat_id, 'Já estou te enviando uma dica de *Biologia*..', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, random.choice(["Ter cera no ouvido nem sempre é sinal de falta de higiene. A cera, ou cerúmen, é produzida porglândulas e serve para proteger a região de poeira e de micro-organismosque podem causar infecções."," Quando você usa tênis por muito tempo, os péstranspiram. Aí, bactérias e fungos que se alimentam de suor e de restos da pele fazem a festa, liberando substâncias fedidas."," O espirro é uma forma de defesa. Ele serve para eliminar do corpo bactérias, vírus e sujeiras que irritam o interior do nariz ou os pulmões."," O sangue é responsável pelo transporte de substâncias (nutrientes, oxigênio e gás carbônico) e pela defesa do organismo."," De repente, o corpo sacode e as cordas vocais produzem um ruído. Lá vem o soluço!"," Nós temos cerca de 100 mil fios de cabelo e cada fio cresce uns 20 centímetros por ano.","O suor é produzido para resfriaro corpo, que precisa ficar com temperatura em torno dos 36,5 graus Celsius, uffa!"]), "HTML")
    elif 'Matemática' in texto or 'matemática' in texto:
      bot.sendMessage(chat_id, 'Ok! Já estou te enviando as dicas de *Matemática*...', parse_mode='Markdown')
      time.sleep(2)
      bot.sendMessage(chat_id, random.choice(["Números amigáveis são pares de números onde um deles é a soma dos divisores do outro.","O maior numero primo conhecido é 232.582.657", " Você sabia que adicionando o número 1 à multiplicação de quatro números consecutivos você obtém um quadrado perfeito?"," Números primossão os números naturais que têmapenas dois divisores diferentes: o 1 e ele mesmo.","O 0 é um número par"]), "HTML")
      
    
    elif u'Humanas'in texto or 'humahnas' in texto:
       bot.sendMesssage(chat_id, random.choice([" Vaticano é o menor País  do mundo"," Pindorama era o nome do Brasil, dado pelos índios. "," A chamada Muralha da China, ou Grande Muralha, é uma impressionante estrutura de arquitetura militar construída durante a China Imperial. "," Os Himalaias são a maior e mais alta cadeia montanhosa do planeta. "," A primeira capital do Brasil foi Salvador. "]), "HTML")
    elif 'Etc.' in texto or 'etc.' in texto:
       bot.sendMessage(chat_id, 'Vou te enviar uma *dica*!  lá vai...', parse_mode='Markdown')
       time.sleep(2)
       bot.sendMessage(chat_id, random.choice(["Sabia que o plural de gravidez e arroz é gravidezes e arrozes?" ,"A única palavra da língua portuguesa que forma o plural no meio é quaisquer. Legal, né?" ,"Saiba que muçarela é um tipo de queijo que se escreve com ç. 😁 ","A forma correta de escrita da palavra é  aerossol. Isso mesmo, com -ss. Não vai errar, OK? ❤️","A língua portuguesa veio dolatim vulgar, devido à época em os conquistadores romanos dominaram a península Ibérica.","A maior palavra da língua portuguesa é pneumoultramicroscopicossilicovulcanoconiótico, sabia?"," A palavra que reúne a maior quantidade de vogais juntas é piauiense."," Sabia que A bota se calça e a calça se bota?", " Vaticano é o menor País  do mundo"," Pindorama era o nome do Brasil, dado pelos índios. "," A chamada Muralha da China, ou Grande Muralha, é uma impressionante estrutura de arquitetura militar construída durante a China Imperial. "," Os Himalaias são a maior e mais alta cadeia montanhosa do planeta. "," A primeira capital do Brasil foi Salvador. " ]), "HTML")
    elif texto == '/guia':
      bot.sendMessage(chat_id, ' 🔎| *Guia do Estudante:*\n\n📌| /menu *Menu do site*\n📌| /categoria *Categorias do site*\n📌| /dicas *Receba uma dica para você estudar*\n📌| /compre *Loja do site*\n📌| /produtos *Produtos do site*\n📌| /sobre *Sobre o Guia do Estudante.*\n📌| /canais *Canais Educativos do Telegram*\n📌| /info *Informações do Robô.*', parse_mode='Markdown')
    elif texto == 'CATEGORIAS':
      markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='📕| Melhores Faculdades', url='http://guiadoestudante.abril.com.br/blog/melhores-faculdades/')],[dict(text='📕| Atualidades', url='http://guiadoestudante.abril.com.br/blog/atualidades-vestibular/')],[dict(text='📕| Carreira', url='http://guiadoestudante.abril.com.br/blog/estante')],[dict(text='📕| Estante', url='http://guiadoestudante.abril.com.br/blog/estante')],])
      bot.sendMessage(chat_id, " Nesse tópico, encontre de forma fácil o conteúdo que mais se *encaixa* com seu perfil, no *Guia do Estudante*.\n👉🏻 Por favor, escolha entre as opções do *teclado:*", parse_mode='Markdown', reply_markup=markup)
    elif texto == 'COMPRE':
      bot.sendMessage(chat_id, "Beleza, vou te passar...")
      time.sleep(2)
      markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='💰 COMPRAR PRODUTOS', url='http://www.saraiva.com.br/guia-do-estudante-especial-fuvest-9348035.html')]])
      bot.sendMessage(chat_id, "Neste tópico você poderá fazer compras de todos os *produtos* de alta qualidade do *Guia do Estudante:*", parse_mode='Markdown', reply_markup=markup)
    elif texto == 'PRODUTOS':
      bot.sendMessage(chat_id, 'Certo!  vou te passar os *produtos...*', parse_mode='Markdown')
      time.sleep(2)
      bot.sendMessage(chat_id, produtos.format(from_first_name), parse_mode='Markdown')
    elif texto == 'SOBRE O GUIA':
      bot.sendMessage(chat_id, ' *O Guia do Estudante* produz conteúdos, em várias plataformas, para quem vive o momento da passagem do Ensino Médio para o Ensino Superior.\n Dividimos esse conteúdo em dois grandes pilares: *material de orientação profissional* e *material de preparação para provas de vestibular.* \n\n Na área de orientação profissional, trazemos informações sobre todos os cursos de nível superior do país, sobre a situação do mercado de trabalho e também dicas que ajudam os estudantes a chegar a uma escolha segura de carreira. Na área de preparação para provas, acompanhamos tudo o que acontece no Enem e nos maiores vestibulares do país, oferecemos testes e simulados para quem quer praticar e ainda apresentamos vários métodos e técnicas para fazer os estudos renderem muito mais.', parse_mode='Markdown')
    elif texto == 'SOBRE':
      bot.sendMessage(chat_id, info.format(from_first_name), parse_mode='Markdown')
      time.sleep(2)
      bot.sendMessage(chat_id, '📕| *ROBÔ GE*\n\n☕️| *Sobre:* _Tenha no Telegram todas as informações do site Guia do Estudante._\n\n📢| *Atualizações:* @aprender\n🇧🇷| *Criado por* @JotaDrake\n\n👉🏻| *Confira o canal:*  @GuiadoEstudante', parse_mode='Markdown')
    elif 'Oi' in texto or 'oi' in texto or 'Olá' in texto:
      bot.sendMessage(chat_id, ola.format(from_first_name), parse_mode='Markdown')
    elif 'Olá' in texto or 'olá' in texto or 'ola' in texto or 'Ola' in texto:
      bot.sendMessage(chat_id, ola.format(from_first_name), parse_mode='Markdown')
    elif texto == '/git':
      bot.sendMessage(chat_id, 'Ok! vou te passar *meu repositório*... =D', parse_mode='Markdown')
      time.sleep(2)
      bot.sendMessage(chat_id, '🎩| O *Robô GE* está completo no Github.\n\n🔥| *Veja o código:*\n👉🏻 https://github.com/drakejota/GE', parse_mode='Markdown')
    elif 'Hoje' in texto or 'hoje' in texto:
       bot.sendMessage(chat_id, info_data.format(D, M, A), parse_mode="Markdown")
    elif 'é hoje' in texto or 'É hoje' in texto:
       bot.sendMessage(chat_id, info_data.format(D, M, A), parse_mode="Markdown")
    elif 'Data' in texto or 'data' in texto or '/data' in texto:
       bot.sendMessage(chat_id, info_data.format(D, M, A), parse_mode="Markdown")
    elif 'seu nome' in texto or 'se chama' in texto:
       bot.sendMessage(chat_id, 'Me chamo *Robô GE*, seu guia!  =]', parse_mode='Markdown')
###DICAs
    elif 'DICAS' in texto or '/dicas' in texto:
      markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Português')]+[KeyboardButton(text='Matemática')], [KeyboardButton(text='Geografia')]+[KeyboardButton(text='Biologia')], [KeyboardButton(text='Química')]+[KeyboardButton(text='História')]+[KeyboardButton(text='Etc.')],[KeyboardButton(text='VOLTAR')]], one_time_keyboard=True)
      bot.sendMessage(chat_id, 'Oba!  Aqui poderemos estudar juntinhos.\nEu envio *dicas* para você de qualquer assunto abaixo! Vai,  *Escolha: *', parse_mode='Markdown', reply_markup=markup)
        

 #NovosComandos
 
    elif texto == u'/menu':
      bot.sendMessage(chat_id, 'Beleza! vou te enviar nosso *menu*...', parse_mode='Markdown')
      time.sleep(2)
      markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='GUIA DO ESTUDANTE')],[KeyboardButton(text='DICAS')]+[KeyboardButton(text='SOBRE')],[KeyboardButton(text='AJUDA')]+[KeyboardButton(text='EXTRAS')],[KeyboardButton(text='PROJETO APRENDER')]], one_time_keyboard=True)
      bot.sendMessage(chat_id, u'Aqui está nosso *Menu* interativo. Por favor, escolha entre as opções do *teclado*', parse_mode='Markdown', reply_markup=markup)
    elif texto == u'GUIA DO ESTUDANTE':
      markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='MENU DO SITE')],[KeyboardButton(text='CATEGORIAS')],[KeyboardButton(text='COMPRE')]+[KeyboardButton(text='PRODUTOS')],[KeyboardButton(text='SOBRE O GUIA')],[KeyboardButton(text='VOLTAR')]], one_time_keyboard=True)
      bot.sendMessage(chat_id, u'Aqui você encontra de forma *rápida e fácil* o conteúdo do site *Guia do Estudante*. Escolha entre as *opções*:', parse_mode='Markdown', reply_markup=markup)
    elif texto == u'VOLTAR':
      bot.sendMessage(chat_id, '*Espera um pouco*...', parse_mode='Markdown')
      time.sleep(2)
      markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='GUIA DO ESTUDANTE')],[KeyboardButton(text='DICAS')]+[KeyboardButton(text='SOBRE')],[KeyboardButton(text='AJUDA')]+[KeyboardButton(text='EXTRAS')],[KeyboardButton(text='PROJETO APRENDER')]], one_time_keyboard=True)      
      bot.sendMessage(chat_id, 'De volta ao *menu*!', parse_mode='Markdown', reply_markup=markup)
    elif 'EXTRAS' in texto or 'extras' in texto:
      bot.sendMessage(chat_id, 'Blz! já estou te passando meus comandos *Extras*... =]', parse_mode='Markdown')
      time.sleep(2)
      bot.sendMessage(chat_id, '💭| *Comandos Extras Disponíveis:* \n\n/hora Hora de acordo com o relógio do GE.\n\n/data Data de Hoje.\n\n/calcule Calcular uma expressão matemática.\n\n/estudometro Estudometro.\n\n/total Total de mensagens comigo.\n\n/letras Gera uma letra do Alfabeto.\n\n/numero Gera um número qualquer.\n\n/eu suas informações', parse_mode='Markdown')
    elif 'AJUDA' in texto or 'ajuda' in texto:
      bot.sendMessage(chat_id, '| *Funções do Bot:*\n\n• *Guia do Estudante* - Conteúdo do Site Guia do Estudante.\n• *Dicas* - Dicas para Estudar.\n• *Aprender* - Canais e Bots Educativos\n\n*Desenvolvedores:*\n[Jσтα](Telegram.me/jotadrake)\n\n*Suporte:*\n[APRENDER](Telegram.me/aprender) \n\n*Source no GitHub:*\n📦 [Source GitHub](http://GitHub.com/drakejota)\n\n *Última Atualização: 15/02/17*', parse_mode='Markdown', disable_web_page_preview='Yes')
    
#EXTRAS    
    elif txt [0] == 'Calcule' in txt or 'calcule' in txt or '/calcule' in txt:
        bot.sendMessage(chat_id, 'Um momento, estou *resolvendo o cálculo* 🤓 ...', parse_mode='Markdown')
        time.sleep(1)
        try:bot.sendMessage(chat_id, "pelos meus cálculos o resultado é: {} ".format(eval(txt[1])))
        except:bot.sendMessage(chat_id, "por favor verifique os paramêtros do código, algo não está certo...", )
    elif texto == '/letras':
        bot.sendMessage(chat_id, letra.format(random.choice(['A','B','C','D','E','J','Z','H','M','K','Y','X']),"HTML"), "Markdown")
    elif texto == '/estudometro':
        bot.sendMessage(chat_id, estudo.format(from_first_name, random.choice(['20%','40%','50%','60%','70%','80%','90%','100%']),"HTML"), "Markdown")
    elif texto== "/total":
        bot.sendMessage(chat_id, total.format(from_first_name, msg['message_id']), "Markdown")
    elif 'hora' in texto or 'Hora' in texto:
        bot.sendMessage(chat_id, hora.format(horas), parse_mode='Markdown')
    else:
        bot.sendMessage(chat_id, 'Opa! Eu não entendi...🤔\n\nEu só sei falar sobre matérias educativas, tenta digitar *Português* ou *Matemática*! =]', parse_mode='Markdown')    
 ### Executando
print(colors.lg_blue + t + colors.lg_cyan + NomeBot + " Já está rodando...")
time.sleep(2)
bot.message_loop(handle)
while 1:
    time.sleep(10)
