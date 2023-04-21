import pygame as pg
pg.init()
width,height = 600,600
cir = lambda pos,color,radi:pg.draw.circle(window,C_BWRGBYCM[color],(int(pos[0]),int(pos[1])),radi,0)
window = pg.display.set_mode((width, height))
pg.display.set_caption("RAJ's Chess Game")
rect = lambda color,x,y,w,h:pg.draw.rect(window,color,(int(x),int(y),int(w),int(h)))
dis = lambda a,b:((b[0]-a[0])**2+(b[1]-a[1])**2)**0.5
C_BWRGBYCM = ((0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255))
R = pg.image.load('rook_w.png')
N = pg.image.load('knight_w.png')
B = pg.image.load('bishio_w.png')
K = pg.image.load('king_w.png')
Q = pg.image.load('queen_w.png')
P = pg.image.load('pawn_w.png')
r = pg.image.load('rook_b.png')
n = pg.image.load('knight_b.png')
b = pg.image.load('biship_b.png')
k = pg.image.load('king_b.png')
q = pg.image.load('queen_b.png')
p = pg.image.load('pawn_b.png')
wallpaper = pg.transform.scale(pg.image.load("wallpaper.png"), (width, height))
def button(color,hover_color,n,m,v,b,text='',size=3,off_x=5,off_y=2):
    n,m,v,b=int(n),int(m),int(v),int(b)
    front = pg.font.SysFont(None, int(size*10))
    text = front.render(text, True, C_BWRGBYCM[0])
    q,w=pg.mouse.get_pos()
    if n<q<n+v and m<w<m+b:
        pg.draw.rect(window,hover_color,(n,m,v,b))
        if pg.mouse.get_pressed()[0]==1:return True
    else:pg.draw.rect(window,color,(n,m,v,b))
    window.blit(text,(n+off_x,m+off_y))
    return False
def write(text,x,y,color,size=3):
    front = pg.font.SysFont(None, int(size*10))
    text = front.render(text, True, C_BWRGBYCM[color])
    window.blit(text,(int(x),int(y)))
def exit():
    while 1:
        window.fill(C_BWRGBYCM[0])
        for event in pg.event.get():
            if event.type==pg.QUIT:exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:quit()
        rect(C_BWRGBYCM[1],(width/2)-(width/4),(height/2)-(height/4),width/2,(height/3)-50)
        write("do you really want ",(width/2)-(width/4)+10,(height/2)-(height/4)+10,0,4.5)
        write("          to quit ?",(width/2)-(width/4),(height/2)-(height/4)+50,0,4.5)
        if button((0,190,0),C_BWRGBYCM[3],(width/2)+20,(height/2)-50,100,30," yes quit",3,5,4):quit()
        if button((190,0,0),C_BWRGBYCM[2],(width/2)-120,(height/2)-50,100,30," No don't",3,5,6):return
        pg.display.update()
def welcome_screen():
    while 1:
        for event in pg.event.get():
            if event.type==pg.QUIT:exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:quit()
        window.blit(wallpaper, (0, 0))
        if button((190,190,190),C_BWRGBYCM[1],380,450,200,50,"play......!",5,10,10):game()
        if button((190,190,190),C_BWRGBYCM[1],380,530,200,50,"quit......!",5,10,10):exit()
        pg.display.update()
def stringToObject(pice):
    '''returns objects from string use before pice on'''
    if pice=='R':return R
    elif pice=='N':return N
    elif pice=='B':return B
    elif pice=='K':return K
    elif pice=='Q':return Q
    elif pice=='P':return P
    elif pice=='r':return r
    elif pice=='n':return n
    elif pice=='b':return b
    elif pice=='k':return k
    elif pice=='q':return q
    elif pice=='p':return p
def board():
    '''creats board grig'''
    lis=[]
    x,y=0,0
    w,h = (width/8)/2,(height/8)/2
    for i in range(1,9):
        for j in range(1,9):
            if (i+j)%2==0:lis.append(((x+w,y+h),1)) 
            else:lis.append(((x+w,y+h),0))
            x+=width/8
        y+=height/8
        x=0
    return lis
def color_board(lis):
    '''color's the board'''
    w,h = (width/8)/2,(height/8)/2
    for i in lis:
        if i[1]==0:rect((0,162,232),i[0][0]-w,i[0][1]-h,width/8,height/8)
        elif i[1]==1:rect((153,217,234),i[0][0]-w,i[0][1]-h,width/8,height/8)
        elif i[1]==2:rect((150,0,0),i[0][0]-w,i[0][1]-h,width/8,height/8)
        elif i[1]==3:rect((0,150,0),i[0][0]-w,i[0][1]-h,width/8,height/8)
    return
def piece_on(board_cor,pice,on):
    if pice==None:return
    window.blit(pice, (int(board_cor[on][0][0]-30),int(board_cor[on][0][1]-30)))
    return
def value(val):
    if type(val)==str:
        if val=='r':return -5
        elif val=='n':return -4
        elif val=='b':return -3
        elif val=='q':return -9
        elif val=='k':return -200
        elif val=='p':return -1
        elif val=='R':return 5
        elif val=='N':return 4
        elif val=='B':return 3
        elif val=='Q':return 9
        elif val=='K':return 200
        elif val=='P':return 1
    elif type(val)==int:
        if val==-5:return 'r'
        elif val==-4:return 'n'
        elif val==-3:return 'b'
        elif val==-9:return 'q'
        elif val==-200:return 'k'
        elif val==-1:return 'p'
        elif val==5:return 'R'
        elif val==4:return 'N'
        elif val==3:return 'B'
        elif val==9:return 'Q'
        elif val==200:return 'K'
        elif val==1:return 'P'
    return
def set_board(fen):
    board_state = []
    val=1
    files,rank=0,7
    for dig in fen:
        if dig=='/':
            rank-=1
            files=0
        else:
            try:
                if type(2)==type(int(dig)):
                    for i in range(int(dig)):
                        board_state.append([val,0])
                        val+=1
                    files+=(int(dig))
            except Exception:
                board_state.append([val,value(dig)])
                files+=1
                val+=1
    return board_state
def show_pice(board_cor):
    for block in board_cor:
        piece_on(board_cor,stringToObject(value(block[3])),block[2]-1)
    return
def combine(board_cor,board_state):
    lis=[]
    for no,i in enumerate(board_cor):
        lis.append([i[0],i[1],board_state[no][0],board_state[no][1]])
    return lis
def on_block(board_cor):
    pos=pg.mouse.get_pos()
    smallest_dis,indx=100,0
    for no,cod_block in enumerate(board_cor):
        current_dis = dis(cod_block[0],pos)
        if current_dis<smallest_dis:
            smallest_dis=current_dis
            indx=no
    return indx
def rook(pos):
    pos2=pos
    lis=[]
    try:
        for i in range(-7,8):
            if 0<pos2+i-1<64:lis.append(pos2+i-1)
            pos2=pos
        # for i in range(-56,57,8):
        #     if 0<pos2+i-1<64:lis.append(pos2+i-1)
        #     pos2=pos
    except Exception:
        pass
    return lis
def check_ligall_moves(board_cor,no):
    if board_cor[no][3]==-5:return rook(board_cor[no][2])
    return
def update_board(board_cor):
    no=on_block(board_cor)
    if board_cor[no][3]!=0:
        board_cor[no][1]=3
        to_paint=check_ligall_moves(board_cor,no)
        print(to_paint)
        for i in to_paint:
            board_cor[i][1]=2
    return board_cor
def game():
    press=False
    board_cor=combine(board(),set_board(f'{fen}'))
    # [(x,y),1,62,-5]
    while 1:
        window.fill(C_BWRGBYCM[0])
        for event in pg.event.get():
            if pg.mouse.get_pressed()[0]==1:press=True
            if event.type==pg.QUIT:exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:welcome_screen()
                if event.key == pg.K_ESCAPE:quit()
        color_board(board_cor)
        if press:
            update_board(board_cor)
            press=False
        show_pice(board_cor)
        pg.display.update()
fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
fen2='8/3r4/8/8/8/8/8/8'
game()
