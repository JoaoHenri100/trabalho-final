import os
import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

class PDF(FPDF):
    def header(self):
        self.image('kick.png', 150, 10, 33)
        self.set_font('Times', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'PROJETO PYTHON', 0, 0, 'C')
        self.ln(10)
        self.line(75, 20, 135, 20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 20, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

dadosEstado = pd.read_excel(r'Dados-covid-19-estado.xlsx')
casosdia = dadosEstado["Casos por dia"]
obitosdia = dadosEstado["Óbitos por dia"]

pdf = PDF()
pdf.add_page()
texto_1 = 'A CRISE CAUSADO PELO COVID-19 NO ESTADO DE SÃO PAULO.'
pdf.image(name='covid.png', x=83, y=120, w=50)
pdf.cell(w=0, h=120, txt=texto_1, align='C')
pdf.set_font('Times', '', 17)

pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.set_margins(20, 40, 0)
texto2 =  "  Quase 2 anos se passaram desde o dia 31 de dezembro de 2019, quando a Organização Mundial de Saúde (OMS) emitiu o primeiro alerta do novo coronavírus, após autoridades chinesas notificarem casos de uma misteriosa pneumonia na cidade de Wuhan. Mas afinal, o que é esse vírus?\n Os coronavírus são uma grande família de vírus que podem causar doenças em animais e humanos. Em humanos, os coronavírus provocam infecções respiratórias, que variam do resfriado comum a graves doenças, como a Síndrome Respiratória, e seus sintomas mais comuns da são: febre, cansaço e tosse seca. Sua principal via de transmição é o ar, ou seja, quando falamos, espirramos ou tossimos, expelimos diversas partículas que podem carregar o vírus. Porém algumas partículas são mais pesadas e podem cair em superfícies e objetos, acumulando-se em espaços fechados e sem ventilação.\n Somente no município de São Paulo, até a presente data, foram mais de 40.000 vidas perdidas e quase 1 milhão de infectados com a doença. Com a chegada da pandemia, comércios fecharam as portas, aulas presenciais foram suspensas, missas e outras celebrações religiosas foram adiadas, e medidas públicas relacionadas à saúde para contenção e atendimento à doença foram tomadas pelas autoridades. Em 2021, com o início da campanha de imunização, um sentimento de esperança e alívio tomou conta da população. A enfermeira Mônica Calazans, foi a primeira pessoa a tomar a dose da vacina contra a Covid-19 no país.\n Até o dia 31 de dezembro, eram quase 4,5 milhões de casos confirmados no Estado, já hoje, esse número ultrapassa 150 mil mortes confirmadas por Covid-19 desde o início da pandemia. O funcionamento dos espaços culturais no estado de São Paulo e capital paulista já estão liberados para toda ocupação. A regra é válida para museus, cinemas, teatros e espaços de eventos. O avanço da vacinação em São Paulo é decisivo para a queda expressiva de mortes causadas pela Covid-19 no estado. A ampla cobertura vacinal também resultou no total mensal mais baixo de mortes por Covid-19 dos últimos 18 meses.\n\n            A SEGUIR ESTÃO AS REPRESENTAÇÕES EM GRÁFICOS:"

pdf.multi_cell(w=170, h=8, txt=texto2, align='J')

plt.plot(casosdia)
plt.xlabel('Grafico de casos por dia no estado de sp')
plt.savefig("exemplo1.png")
plt.close()
pdf.image(x=20, y=70, w=180, h=80, name='exemplo1.png')

plt.plot(obitosdia)
plt.xlabel('Grafico de óbitos por dia no estado de sp')
plt.savefig("exemplo2.png")
plt.close()
pdf.image(x=20, y=170, w=180, h=80, name='exemplo2.png')

pdf.add_page()
pdf.set_font('Times', '', 15)
pdf.set_margins(20, 40, 0)
texto3 =  "\n\n\nJoão Henrique G. Silva\n\nTurma: B "

pdf.multi_cell(w=170, h=8, txt=texto3, align='J')

pdf.output('Covid.pdf')

os.system("pause")