import pygame
import sys

# Pygame の初期化
pygame.init()

#ゲームメイン処理
def main():
    cursor_x=0
    cursor_y=0
    global score,hisc

    #ゲーム進行状態(0:初回画面/1:ゲーム開始待ち/2:だんご落下中/3:だんご判定/4:スコア判定（だんご消す）/5:カーソル入力待ち/6:ゲームオーバー)
    state = 0   # 初期化(0:初回画面)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_x,mouse_y = pygame.mouse.get_pos()    #マウス位置
        mouse_click = pygame.mouse.get_pressed()    #マウスクリック
        mouse_c = mouse_click[0]       
        pygame.init()
    pygame.display.set_caption("だんごパズル(pygame ver)")
    screen = pygame.display.set_mode((912,768))
    font = pygame.font.Font(None,60)
    clock = pygame.time.Clock()
 
    bg = pygame.image.load("dango_back.png")    #背景画像をロード
    cursor = pygame.image.load("cursor.png")    #カーソル画像をロード
    img_dango = [                               #だんご画像をロード
        None,
        pygame.image.load("dango1.png"),
        pygame.image.load("dango2.png"),
        pygame.image.load("dango3.png"),
        pygame.image.load("dango4.png"),
        pygame.image.load("dango_kushi.png")
    ]
    title = pygame.image.load("game_title.png")
    click_start = pygame.image.load("click_start.png")
 
    #ゲームメイン処理
    main()
    def main():
        cursor_x=0
    cursor_y=0
    global score,hisc
 
    #ゲーム進行状態(0:初回画面/1:ゲーム開始待ち/2:だんご落下中/3:だんご判定/4:スコア判定（だんご消す）/5:カーソル入力待ち/6:ゲームオーバー)
    state = 0   # 初期化(0:初回画面)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_x,mouse_y = pygame.mouse.get_pos()    #マウス位置
        mouse_click = pygame.mouse.get_pressed()    #マウスクリック
        mouse_c = mouse_click[0]                    #マウス左クリック状態を設定
 
        #　-------ゲーム進行状態0:初回画面----------
        if state==0:
            screen.blit(bg,[0,0])               #背景画像描画
            screen.blit(title,[50,240])         #タイトル描画
            screen.blit(click_start,[50,560])   #クリックスタート描画
            state = 1
            mouse_c = False
            def main():
                cursor_x=0
    cursor_y=0
    global score,hisc
 
    #ゲーム進行状態(0:初回画面/1:ゲーム開始待ち/2:だんご落下中/3:だんご判定/4:スコア判定（だんご消す）/5:カーソル入力待ち/6:ゲームオーバー)
    state = 0   # 初期化(0:初回画面)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_x,mouse_y = pygame.mouse.get_pos()    #マウス位置
        mouse_click = pygame.mouse.get_pressed()    #マウスクリック
        mouse_c = mouse_click[0]                    #マウス左クリック状態を設定
 
        #　-------ゲーム進行状態0:初回画面----------
        if state==0:
            screen.blit(bg,[0,0])               #背景画像描画
            screen.blit(title,[50,240])         #タイトル描画
            screen.blit(click_start,[50,560])   #クリックスタート描画
            state = 1
            mouse_c = False
        #　-------ゲーム進行状態1:ゲーム開始待ち----------
        elif state==1:
            if mouse_c == True:                 #マウスクリックされたとき
                for y in range(10):
                    for x in range(8):
                        dango[y][x] = 0         #マス目の配列初期化
                mouse_c = False
                score = 0
                next_dango = 0
                cursor_x = 0
                cursor_y = 0
                set_dango()             #最上位にだんごセット
                state = 2
                def drop_dango():
                    flg = False
    for y in range(8,-1,-1):
        for x in range(8):
            if dango[y][x] !=0 and dango[y+1][x] == 0:
                dango[y+1][x] = dango[y][x]
                dango[y][x] = 0
                flg = True
    return flg
def main():
    cursor_x=0
    cursor_y=0
    global score,hisc
 
    #ゲーム進行状態(0:初回画面/1:ゲーム開始待ち/2:だんご落下中/3:だんご判定/4:スコア判定（だんご消す）/5:カーソル入力待ち/6:ゲームオーバー)
    state = 0   # 初期化(0:初回画面)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_x,mouse_y = pygame.mouse.get_pos()    #マウス位置
        mouse_click = pygame.mouse.get_pressed()    #マウスクリック
        mouse_c = mouse_click[0]                    #マウス左クリック状態を設定
 
        #　-------ゲーム進行状態0:初回画面----------
        if state==0:
            screen.blit(bg,[0,0])               #背景画像描画
            screen.blit(title,[50,240])         #タイトル描画
            screen.blit(click_start,[50,560])   #クリックスタート描画
            state = 1
            mouse_c = False
        #　-------ゲーム進行状態1:ゲーム開始待ち----------
        elif state==1:
            if mouse_c == True:                 #マウスクリックされたとき
                for y in range(10):
                    for x in range(8):
                        dango[y][x] = 0         #マス目の配列初期化
                mouse_c = False
                score = 0
                next_dango = 0
                cursor_x = 0
                cursor_y = 0
                set_dango()             #最上位にだんごセット
                state = 2
        #　-------ゲーム進行状態2:だんご落下中----------
        elif state==2:
            if drop_dango() == False:           #だんごを落下させる
                state = 3                       #落下が終わったら、state=3へ
            disp_dango()    # だんご表示 
            def main():
                cursor_x=0
    cursor_y=0
    global score,hisc
 
    #ゲーム進行状態(0:初回画面/1:ゲーム開始待ち/2:だんご落下中/3:だんご判定/4:スコア判定（だんご消す）/5:カーソル入力待ち/6:ゲームオーバー)
    state = 0   # 初期化(0:初回画面)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_x,mouse_y = pygame.mouse.get_pos()    #マウス位置
        mouse_click = pygame.mouse.get_pressed()    #マウスクリック
        mouse_c = mouse_click[0]                    #マウス左クリック状態を設定

        if state==0:
            screen.blit(bg,[0,0])               
            screen.blit(title,[50,240])         
            screen.blit(click_start,[50,560])   
            state = 1
            mouse_c = False
        elif state==1:
            if mouse_c == True:                 
                for y in range(10):
                    for x in range(8):
                        dango[y][x] = 0        
                mouse_c = False
                score = 0
                next_dango = 0
                cursor_x = 0
                cursor_y = 0
                set_dango()             
                state = 2
        
        elif state==2:
            if drop_dango() == False:        
                state = 3                     
            disp_dango()                
        elif state==3:
            check_dango()                      
            state = 4
            disp_dango()   
            def main():
                cursor_x=0
    cursor_y=0
    global score,hisc
 
    #ゲーム進行状態(0:初回画面/1:ゲーム開始待ち/2:だんご落下中/3:だんご判定/4:スコア判定（だんご消す）/5:カーソル入力待ち/6:ゲームオーバー)
    state = 0   # 初期化(0:初回画面)
    next_dango = 0   #次にセットするだんご
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_x,mouse_y = pygame.mouse.get_pos()    #マウス位置
        mouse_click = pygame.mouse.get_pressed()    #マウスクリック
        mouse_c = mouse_click[0]                    #マウス左クリック状態を設定
 
        #　-------ゲーム進行状態0:初回画面----------
        if state==0:
            screen.blit(bg,[0,0])               #背景画像描画
            screen.blit(title,[50,240])         #タイトル描画
            screen.blit(click_start,[50,560])   #クリックスタート描画
            state = 1
            mouse_c = False
        #　-------ゲーム進行状態1:ゲーム開始待ち----------
        elif state==1:
            if mouse_c == True:                 #マウスクリックされたとき
                for y in range(10):
                    for x in range(8):
                        dango[y][x] = 0         #マス目の配列初期化
                mouse_c = False
                score = 0
                next_dango = 0
                cursor_x = 0
                cursor_y = 0
                set_dango()             #最上位にだんごセット
                state = 2
        #　-------ゲーム進行状態2:だんご落下中----------
        elif state==2:
            if drop_dango() == False:           #だんごを落下させる
                state = 3                       #落下が終わったら、state=3へ
            disp_dango()    # だんご表示                
        #　-------ゲーム進行状態3:だんご判定----------
        elif state==3:
            check_dango()                       #だんごが揃ったか判定
            state = 4
            disp_dango()    # だんご表示
        #　-------ゲーム進行状態4:スコア判定（だんご消す）----------
        elif state==4:
            sc = delete_dango()
            score = score + sc*10
            if score > hisc:
                hisc = score
            if sc > 0:
                state=2
            else:
                if over_dango() == False:       #だんごが最上位になかったら
                    next_dango = random.randint(1,4)    #次のだんごを決める
                    state = 5
                else:
                    state = 6
                    timer = 0
            disp_dango() 