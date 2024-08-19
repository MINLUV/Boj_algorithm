import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def findblock (row,col,color):
    global visited_normal
    global display
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    visited_normal[row][col] = True
    for dx,dy in direction:
        x = dx + row
        y = dy + col
        if 0 <= x < len(visited_normal) and 0 <= y <len(visited_normal) and not visited_normal[x][y] and color == display[x][y]:
            findblock(x,y,color)
    
def findblock_colorblind(row,col,color):
    global visited_colorblind
    global display
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    visited_colorblind[row][col] = True
    for dx,dy in direction:
        x = dx + row
        y = dy + col
        if color == 'R':
            if 0 <= x < len(visited_colorblind) and 0 <= y <len(visited_colorblind) and not visited_colorblind[x][y] and ('R' == display[x][y] or 'G' == display[x][y]):
                findblock_colorblind(x,y,color) 
        else:
            if 0 <= x < len(visited_colorblind) and 0 <= y <len(visited_colorblind) and not visited_colorblind[x][y] and color == display[x][y] :
                findblock_colorblind(x,y,color)


if __name__ == "__main__":
    row_length = int(input())
    col_length = row_length
    colorcount_normal = {'R':0,'G':0,'B':0}
    colorcount_colorBlindeness = {'R':0,'B':0}
    display = list()
    visited_normal = [[False for _ in range(row_length)] for _ in range(col_length)]
    visited_colorblind = [[False for _ in range(row_length)] for _ in range(col_length)]
    for _ in range(row_length):
        display.append(list(input()))

    for r in range(row_length):
        for c in range(col_length):
            if not visited_normal[r][c]:
                color = display[r][c]
                colorcount_normal[color] += 1
                findblock(r,c,color)
            if not visited_colorblind[r][c]:
                color = display[r][c]
                if color == 'R' or color == 'G':
                    colorcount_colorBlindeness['R'] += 1
                    findblock_colorblind(r,c,'R')
                else:
                    colorcount_colorBlindeness['B'] += 1
                    findblock_colorblind(r,c,color)

    print(sum(colorcount_normal.values()),sum(colorcount_colorBlindeness.values()))