import pygame
import sys
import random

# Pygame の初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("だんごパズル")

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# フォント
font = pygame.font.Font(None, 40)

# 画像のロード
bg = pygame.image.load("G7.png").convert()
cursor = pygame.image.load("cursor.png").convert_alpha()
img_dango = [
    None,
    pygame.image.load("dango1.png").convert_alpha(),
    pygame.image.load("dango2.png").convert_alpha(),
    pygame.image.load("dango3.png").convert_alpha(),
    pygame.image.load("dango4.png").convert_alpha(),
]
title = pygame.image.load("game_title.png").convert_alpha()
click_start = pygame.image.load("click_start.png").convert_alpha()

# ゲームデータ
grid_width = 8
grid_height = 10
block_size = 64
dango = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
score = 0
hisc = 0
next_dango = 0
current_piece = None
fall_speed = 500  # ミリ秒
last_fall_time = 0

# 現在のピースの位置
current_x = grid_width // 2 - 1
current_y = 0

# ゲームオーバー時のフラグ
game_over = False

# だんごのセット
def set_dango():
    global current_piece, next_dango, current_x, current_y
    if next_dango == 0:
        next_dango = random.randint(1, 4)
    current_piece = [[0, next_dango, random.randint(1, 4)]]
    next_dango = random.randint(1, 4)
    current_x = grid_width // 2 - 1
    current_y = 0

# 衝突判定
def check_collision(piece, offset_x, offset_y):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                new_x = current_x + x + offset_x
                new_y = current_y + y + offset_y
                if new_x < 0 or new_x >= grid_width or new_y >= grid_height:
                    return True
                if new_y >= 0 and dango[new_y][new_x] != 0:
                    return True
    return False

# ピースを固定
def lock_piece():
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell != 0:
                dango[current_y + y][current_x + x] = cell

# ピースの回転
def rotate_piece():
    global current_piece
    rotated = list(zip(*current_piece[::-1]))
    if not check_collision(rotated, 0, 0):
        current_piece = rotated

# だんごの落下
def drop_piece():
    global current_y
    if not check_collision(current_piece, 0, 1):
        current_y += 1
    else:
        lock_piece()
        return False
    return True

# だんごの表示
def disp_dango():
    disp_score()  # スコアの表示
    spacing = 20  # 団子間のスペースを設定
    for y, row in enumerate(dango):
        for x, cell in enumerate(row):
            if cell != 0:
                # 描画位置を計算
                adjusted_x = x * (block_size + spacing) + 16
                adjusted_y = y * (block_size + spacing) + 16
                screen.blit(img_dango[cell], (adjusted_x, adjusted_y))
    if current_piece:  # current_pieceが存在する場合のみ描画
        for y, row in enumerate(current_piece):
            for x, cell in enumerate(row):
                if cell != 0:
                    # 描画位置を計算
                    adjusted_x = (current_x + x) * (block_size + spacing) + 16
                    adjusted_y = (current_y + y) * (block_size + spacing) + 16
                    screen.blit(img_dango[cell], (adjusted_x, adjusted_y))

# スコア表示
def disp_score():
    dark_gray = (105, 105, 105)  # 暗めのグレー
    score_text = font.render(f"Score: {score}", True, dark_gray)  # 暗めのグレーの文字色
    hisc_text = font.render(f"High Score: {hisc}", True, dark_gray)  # 同様にハイスコアも暗めのグレー

    # 右寄せから少し左に寄せる
    score_x = SCREEN_WIDTH - score_text.get_width() - 60  # 右から60pxの位置に変更
    hisc_x = SCREEN_WIDTH - hisc_text.get_width() - 60  # 同様にハイスコアも少し左に

    # Y座標を中央付近に配置
    score_y = SCREEN_HEIGHT // 2 - 1
    hisc_y = score_y + 70

    screen.blit(score_text, (score_x, score_y))
    screen.blit(hisc_text, (hisc_x, hisc_y))

# メインループ内での更新
def main():
    global current_x, current_y, score, hisc, last_fall_time, game_over
    clock = pygame.time.Clock()
    state = 0  # 0: タイトル画面, 1: ゲーム中

    while True:
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # タイトル画面でスペースキーを検出してゲーム開始
            if state == 0 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 1
                    set_dango()
                    game_over = False  # ゲームオーバー状態をリセット

            # ゲーム中の操作
            if state == 1 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_piece, -1, 0):
                    current_x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(current_piece, 1, 0):
                    current_x += 1
                elif event.key == pygame.K_DOWN:
                    drop_piece()
                elif event.key == pygame.K_RETURN:  # エンターキーで回転
                    rotate_piece()

        if state == 0:
            screen.blit(title, (50, 240))
            screen.blit(click_start, (50, 560))

        elif state == 1:
            current_time = pygame.time.get_ticks()
            if current_time - last_fall_time > fall_speed:
                if not drop_piece():
                    clear_and_fall()  # 消去＆落下処理を呼び出し
                    if any(dango[0]):  # 最上段にブロックがある場合ゲームオーバー
                        if score > hisc:
                            hisc = score  # ハイスコアを更新
                        game_over = True  # ゲームオーバー状態にする
                        state = 0  # タイトル画面に戻る
                    set_dango()  # 新しいピースを生成
                last_fall_time = current_time

            disp_dango()

        if game_over:  # ゲームオーバー画面
            font_large = pygame.font.Font(None, 100)
            game_over_text = font_large.render("Game Over", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

            # コンテニューボタン
            continue_text = font.render("Press SPACE to Continue", True, WHITE)
            screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

        pygame.display.flip()
        clock.tick(60)

# 消去判定と落下処理
def clear_and_fall():
    global score
    # 消去対象を探す
    to_clear = set()

    # 横方向のチェック
    for y in range(grid_height):
        for x in range(grid_width - 2):
            if dango[y][x] != 0 and dango[y][x] == dango[y][x + 1] == dango[y][x + 2]:
                to_clear.update([(y, x), (y, x + 1), (y, x + 2)])

    # 縦方向のチェック
    for x in range(grid_width):
        for y in range(grid_height - 2):
            if dango[y][x] != 0 and dango[y][x] == dango[y + 1][x] == dango[y + 2][x]:
                to_clear.update([(y, x), (y + 1, x), (y + 2, x)])

    # 消去
    for y, x in to_clear:
        dango[y][x] = 0

    # スコア加算
    score += len(to_clear) * 10

    # 落下処理
    for x in range(grid_width):
        column = [dango[y][x] for y in range(grid_height) if dango[y][x] != 0]
        column = [0] * (grid_height - len(column)) + column
        for y in range(grid_height):
            dango[y][x] = column[y]


if __name__ == "__main__":
    main()

import pygame
import sys
import random

# Pygame の初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("だんごパズル")

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# フォント
font = pygame.font.Font(None, 40)

# 画像のロード
bg = pygame.image.load("G7.png").convert()
cursor = pygame.image.load("cursor.png").convert_alpha()
img_dango = [
    None,
    pygame.image.load("dango1.png").convert_alpha(),
    pygame.image.load("dango2.png").convert_alpha(),
    pygame.image.load("dango3.png").convert_alpha(),
    pygame.image.load("dango4.png").convert_alpha(),
]
title = pygame.image.load("game_title.png").convert_alpha()
click_start = pygame.image.load("click_start.png").convert_alpha()

# ゲームデータ
grid_width = 8
grid_height = 10
block_size = 64
dango = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
score = 0
hisc = 0
next_dango = 0
current_piece = None
fall_speed = 500  # ミリ秒
last_fall_time = 0

# 現在のピースの位置
current_x = grid_width // 2 - 1
current_y = 0


# だんごのセット
def set_dango():
    global current_piece, next_dango, current_x, current_y
    if next_dango == 0:
        next_dango = random.randint(1, 4)
    current_piece = [[0, next_dango, random.randint(1, 4)]]
    next_dango = random.randint(1, 4)
    current_x = grid_width // 2 - 1
    current_y = 0


# 衝突判定
def check_collision(piece, offset_x, offset_y):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                new_x = current_x + x + offset_x
                new_y = current_y + y + offset_y
                if new_x < 0 or new_x >= grid_width or new_y >= grid_height:
                    return True
                if new_y >= 0 and dango[new_y][new_x] != 0:
                    return True
    return False


# ピースを固定
def lock_piece():
    for y, row in enumerate(current_piece):
        for x, cell in enumerate(row):
            if cell != 0:
                dango[current_y + y][current_x + x] = cell


# ピースの回転
def rotate_piece():
    global current_piece
    rotated = list(zip(*current_piece[::-1]))
    if not check_collision(rotated, 0, 0):
        current_piece = rotated


# だんごの落下
def drop_piece():
    global current_y
    if not check_collision(current_piece, 0, 1):
        current_y += 1
    else:
        lock_piece()
        return False
    return True


# だんごの表示
def disp_dango():
    disp_score()  # スコアの表示
    spacing = 20  # 団子間のスペースを設定
    for y, row in enumerate(dango):
        for x, cell in enumerate(row):
            if cell != 0:
                # 描画位置を計算
                adjusted_x = x * (block_size + spacing) + 16
                adjusted_y = y * (block_size + spacing) + 16
                screen.blit(img_dango[cell], (adjusted_x, adjusted_y))
    if current_piece:  # current_pieceが存在する場合のみ描画
        for y, row in enumerate(current_piece):
            for x, cell in enumerate(row):
                if cell != 0:
                    # 描画位置を計算
                    adjusted_x = (current_x + x) * (block_size + spacing) + 16
                    adjusted_y = (current_y + y) * (block_size + spacing) + 16
                    screen.blit(img_dango[cell], (adjusted_x, adjusted_y))



# だんごの削除処理
def check_and_clear_lines():
    global score
    full_rows = [y for y in range(grid_height) if all(dango[y])]
    for row in full_rows:
        del dango[row]
        dango.insert(0, [0] * grid_width)
    score += len(full_rows) * 10
    return len(full_rows)

# スコア表示
def disp_score():
    dark_gray = (105, 105, 105)  # 暗めのグレー
    score_text = font.render(f"Score: {score}", True, dark_gray)  # 暗めのグレーの文字色
    hisc_text = font.render(f"High Score: {hisc}", True, dark_gray)  # 同様にハイスコアも暗めのグレー

    # 右寄せから少し左に寄せる
    score_x = SCREEN_WIDTH - score_text.get_width() - 60  # 右から30pxの位置に変更
    hisc_x = SCREEN_WIDTH - hisc_text.get_width() - 60  # 同様にハイスコアも少し左に

    # Y座標を中央付近に配置
    score_y = SCREEN_HEIGHT // 2 - 1
    hisc_y = score_y + 70

    screen.blit(score_text, (score_x, score_y))
    screen.blit(hisc_text, (hisc_x, hisc_y))

# メインループ内での更新
def main():
    global current_x, current_y, score, hisc, last_fall_time
    clock = pygame.time.Clock()
    state = 0  # 0: タイトル画面, 1: ゲーム中

    while True:
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # タイトル画面でスペースキーを検出してゲーム開始
            if state == 0 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 1
                    set_dango()

            # ゲーム中の操作
            if state == 1 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_piece, -1, 0):
                    current_x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(current_piece, 1, 0):
                    current_x += 1
                elif event.key == pygame.K_DOWN:
                    drop_piece()
                elif event.key == pygame.K_RETURN:  # エンターキーで回転
                    rotate_piece()

        if state == 0:
            screen.blit(title, (50, 240))
            screen.blit(click_start, (50, 560))

        elif state == 1:
            current_time = pygame.time.get_ticks()
            if current_time - last_fall_time > fall_speed:
                if not drop_piece():
                    clear_and_fall()  # 消去＆落下処理を呼び出し
                    if any(dango[0]):  # 最上段にブロックがある場合ゲームオーバー
                        if score > hisc:
                            hisc = score  # ハイスコアを更新
                        state = 0
                        break
                    set_dango()  # 新しいピースを生成
                last_fall_time = current_time

            disp_dango()
            disp_score()  # スコアを表示する

        pygame.display.flip()
        clock.tick(60)




# 消去判定と落下処理
def clear_and_fall():
    global score
    # 消去対象を探す
    to_clear = set()

    # 横方向のチェック
    for y in range(grid_height):
        for x in range(grid_width - 2):
            if dango[y][x] != 0 and dango[y][x] == dango[y][x + 1] == dango[y][x + 2]:
                to_clear.update([(y, x), (y, x + 1), (y, x + 2)])

    # 縦方向のチェック
    for x in range(grid_width):
        for y in range(grid_height - 2):
            if dango[y][x] != 0 and dango[y][x] == dango[y + 1][x] == dango[y + 2][x]:
                to_clear.update([(y, x), (y + 1, x), (y + 2, x)])

    # 消去
    for y, x in to_clear:
        dango[y][x] = 0

    # スコア加算
    score += len(to_clear) * 10

    # 落下処理
    for x in range(grid_width):
        column = [dango[y][x] for y in range(grid_height) if dango[y][x] != 0]
        column = [0] * (grid_height - len(column)) + column
        for y in range(grid_height):
            dango[y][x] = column[y]


def main():
    global current_x, current_y, score, hisc, last_fall_time
    clock = pygame.time.Clock()
    state = 0  # 0: タイトル画面, 1: ゲーム中

    while True:
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # タイトル画面でスペースキーを検出してゲーム開始
            if state == 0 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 1
                    set_dango()

            # ゲーム中の操作
            if state == 1 and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(current_piece, -1, 0):
                    current_x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(current_piece, 1, 0):
                    current_x += 1
                elif event.key == pygame.K_DOWN:
                    drop_piece()
                elif event.key == pygame.K_RETURN:  # エンターキーで回転
                    rotate_piece()

        if state == 0:
            screen.blit(title, (50, 240))
            screen.blit(click_start, (50, 560))

        elif state == 1:
            current_time = pygame.time.get_ticks()
            if current_time - last_fall_time > fall_speed:
                if not drop_piece():
                    clear_and_fall()  # 消去＆落下処理を呼び出し
                    if any(dango[0]):  # 最上段にブロックがある場合ゲームオーバー
                        if score > hisc:
                            hisc = score  # ハイスコアを更新
                        state = 0
                        break
                    set_dango()  # 新しいピースを生成
                last_fall_time = current_time

            disp_dango()

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()

