#credits
init python:

    sub = '''danielokondratiev 
kvnihwr
reaaaason
serjik654
_leah_37
hitmen4701
user9837677317959
ggmunez
drillean
mouhkhalkham
sayrawnft
kermichesamir1
zloicrazzi
5h_a07
neurofauna
mangaka.ma
gryphanv2
bebravqvadrate
.fantank
bewwware
kasperky_virus
someone34132
cyber_emo
danisimo_dd
tipsy_ioj
veneziana18
vitaliydriller
klaf_15_2.0
userl2fymeoi3d
miltiad
fl1jens
sge4kyy
anatoliiyerhin
quacktxww
tatianamischcenko
_ronat_
00imnotahuman00
vs1ct0r
shestoper333
mksm.pn
s0wenius
roma_bo1
denzel77777
genshiko
nezerkat
danik_kitov
fileotovia
diluc_5777
kril520
linixi89
dejavu2_0
userjaerkcuvzo
avenits
k4_squad
romarama.06
tochkazapatai
akutxr666
alionmos
askqnnnn
akexswift25
1jodio_jostar1
ashen23853
zeirvs
elvirosh.0
_superbrawlsaser335_
polina24_5
_mark_121
zauatopzcy
grzybowe_planetki
dombi_vip515
darling_uessa
stanititop
marsshoto
fronkley
_vova_gulivatu_
asphyxia.music
drinbinpipipupu
zzeyy_3d
good_games_studio
iamsovvx
dy7m5otfq58e
bulochkazmakom1
abobyc3547
springtrap3454
ss.tttx
danyattok
danji_cg
dmqtrrqy
_wssgws_
winerf1ly
unityrazrabwar
gkeb888
demxlxrd
dividont
_zartrat_
knjflz
_infuz1ja_
yeti_spammer
howsitfeel_
solli_234
_rewdan_
oleksiu_oleksi1
squidward.nose3
___viktori___1
'''

    credits = ('Главный программист', 'Дима Бобровский (dm1trr1y)'), ('Фоны', 'Даня Чипурко'), ('Спрайты и ЦГ', 'Даня Чипурко'), ('GUI', 'Даня Рева'), ('Сценарий', 'Дима Бобровский'), ('Сценарий', 'Виктория Мищенко'), ('Программирование', 'Дима Бобровсикй'), ('Музыка', 'Стас'), ('Музыка', 'Даня Рева')
    credits_s = "{size=80}Над игрой работала команда Tenki and his Tales\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Подпищики\n{size=60}" + sub
    credits_s += "\n{size=40}Движок\n{size=60}" + renpy.version() #Don't forget to set this to your Ren'py version
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5, xalign=0.5)
    image theend = Text("{size=80}Конец{/size}", text_align=0.5)
    image thanks = Text("{size=80}Спасибо за игру!{/size}", text_align=0.5)

    transform ending_transform:
        xalign 0.5
        ypos 1.2
        linear 102.0 ypos -10.2
   
label credits:
    $ renpy.music.stop("ambience")
    $ renpy.music.stop("audio")
    $ renpy.music.stop("music")

    $ _skipping = False

    play music credits 
    $ quick_menu = False
    $ renpy.block_rollback()
    #$ renpy.set_mouse_pos(2560,1440,99999999)
    #$ credits_speed = 60 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3.0, hard=True)
    hide theend with dissolve
    show cred at ending_transform
    $ renpy.pause(80.0, hard=True)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5.0, hard=True)
    hide thanks
    $ renpy.set_mouse_pos(0,0,0.1)
    return