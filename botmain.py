import os
token=''
phy='database//phy'
chem='database//chem'
math='database//math'
phydpp='database//phydpp'
chemdpp='database//chemdpp'
mathdpp='database//mathdpp'
botvar=''
template='''<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body, h1,h2,h3,h4,h5,h6 {font-family: "Montserrat", sans-serif}
.w3-row-padding img {margin-bottom: 12px}
/* Set the width of the sidebar to 120px */
.w3-sidebar {width: 120px;background: #222;}
/* Add a left margin to the "page content" that matches the width of the sidebar (120px) */
#main {margin-left: 120px}
/* Remove margins from "page content" on small screens */
@media only screen and (max-width: 600px) {#main {margin-left: 0}}
</style>
<body class="w3-black">

</div>

<!-- Page Content -->
<div class="w3-padding-large" id="main">
  <!-- Header/Home -->
  <header class="w3-container w3-padding-32 w3-center w3-black" id="home">
    <h1 class="w3-jumbo"><span class="w3-hide-small">Pryaas Batch 2021</h1>
    <p>Time To Rule the World.</p>

  </header>

  <!-- About Section -->
  <div class="w3-content w3-justify w3-text-grey w3-padding-64" id="about">

'''
endtemplate='</body></html>'
datastructure=['','','','']

def read_data(sub):
    di='database//'+sub
    with open(di,'r') as f:
        ##|lecture1|[lecture1]\n[lecture2]
        data=f.read()
        data=data.split('|')
        try:
            data.remove('')
        except:
            a=True
        #print(data)
        #['lecture1','[lecture1]\n[lecture2]\n','lecture 2']
        chapters=[]
        chaptersdata=[]
        for i in range(len(data)//2):
            chapters.append(data[i*2])
            chaptersdata.append(data[(i*2)+1])
        chpterdatalist=[]
        try:
            chaptersdata.remove('')
        except:
            a=True
        #print(chaptersdata)
        #print(chapters)
        chaptersdata1=chaptersdata[0].split('\n')
        #print(chaptersdata1)
        try:
            chaptersdata1.remove('')
        except:
            tt=True
        #print(chaptersdata1)
        chapterdatalist=[]
        for j in chaptersdata1:
            #print(j)
            #print(eval(j))
            chapterdatalist.append(eval(j))
            #[[lec1],[lec2]]
        print('#done')
        return (chapters,chapterdatalist)
    
def newchapter(data):
    #phy|chaptername
    data=data.split('|')
    with open('database//'+data[0],'a') as f:
        wdata="|"+data[1]+"|"
        f.write(wdata)
def write_data(lecturedata):
    #phy|lectureno|link
    data=lecturedata.split('|')
    with open('database//'+data[0],'a') as f:
        wdata=str([data[1],data[2]])+'\n'
        f.write(wdata)
        #|lecture1|[lecture1]\n[lecture2]

def html_maker():
    mainhtml=template+'<hr><H1>Lectures</h1><hr>'
    data_lectures=[read_data('phy'),read_data('chem'),read_data('math'),read_data('phydpp'),read_data('chemdpp'),read_data('mathdpp')]
    name=['PHYSICS LECTURES','CHEMISTRY LECTURES','MATH LECTURES','PHYSICS DPPs','CHEMISTRY DPPs','MATH DPPs']
    bb=0
    #data_dpp= []
    for sub in data_lectures:
        #i=([chapters],[chaptersdata])

        ch=sub[0]
        chd=sub[1]
        #print(ch)
        #print(len(ch))
        mainhtml+='<h2><hr>'+name[bb]+'</h2>'
        bb+=1
        for i in range(len(ch)):
            #print(i)
            #print(mainhtml)
            #print(ch)
            #for cha in ch:
                #print(cha)
                mainhtml+='<h3>'+ch[i]+'</h3>'
                mainhtml+='<ul>'
                #print(chd)
                for lec in chd:
                    syntx1='<button class="w3-button w3-light-grey w3-padding-large w3-section"><i class="fa fa-download"></i><a href='
                    syntax2='</a>'
                    syn3='</button>'
                    #print(lec)
                    gg=syntx1+lec[1]+'>'+lec[0]+syntax2+syn3
                    #print(gg)
                    mainhtml+=gg
                    
                mainhtml+='</ul>'
                #print(mainhtml)
    mainhtml+=endtemplate
    with open('index.html','w') as f:
         f.write(mainhtml)
                    
html_maker()               
            
            
        
    
def handle(msg):
    chat_id = msg['chat']['id']
    try:
        text =  msg['text']
    except:
        text = ''
    sender = msg['from']['id']
    msgid=['message_id']
