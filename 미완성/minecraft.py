# size  108 x 92
global f # 전역변수 f로 지정 (콜로세움 틀을 사용하여 다른 건축 요소를 쉽게 만들기 위해)


def Ground(x,y,z)
    blocks.fill(blocks.block_with_data(1, 0),world(x+3,y-1,z-46), world(x+111,y-1,z+46))

def Road(x,y,z) # 콜로세움 길
    n = blocks.block_with_data(0, 0)
    a = blocks.block_with_data(1, 6)
    b = blocks.block_with_data(97, 5)

    start_z = z # 처음 입력받은 좌표 저장

    r = [
    [a,b,b,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,b,b,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,b,b,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,b,b,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,a,a,a],
    [a,b,b,a]
    ]

    for i_1 in range(28,55) # 나머지 공백은 공기(블럭코드0) 으로 채우기
        r.insert_at(i_1, [n,n,n,n])

    for h in range(2):
        for i in r: # i = [a,a]
            for j in i:
                blocks.place(j, world(x+3,y,z-1))
                z += 1
            z = start_z
            x += 1

        r.reverse()   # 배열을 반전 시켜 한번더 실행

def Frame(x,y,z) # 콜로세움 틀
    b1 = blocks.block_with_data(1, 6)
    b2 = blocks.block_with_data(1, 5)
    b3 =
    start_z = z
    start_x = x
    start_y = y

    f =
        [
            [ n, p, e, e, p, e, e, p, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n, n, n, n, n, n, n, n, e, e, p, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ l, l, l, l, l, l, l, l, l, n, n, n, e, p, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ k, k, k, k, k, k, k, k, k, l, l, l, n, n, n, e, p, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ k, k, k, k, k, k, k, k, k, k, k, k, l, l, l, n, n, e, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, l, l, l, n, p, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, l, n, n, n, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n, d, d, d, d, d, d, d, k, k, k, k, k, k, k, k, k, k, l, l, l, n, p, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,c4,c4,c4,c4,c4,c4,c4, d, d, d, k, k, k, k, k, k, k, k, k, l, n, n, n, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,c3,c3,c3,c3,c3,c3,c3,c4,c4,c4, d, d, d, k, k, k, k, k, k, k, l, l, l, n, p, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,c2,c2,c2,c2,c2,c2,c2,c3,c3,c3,c4,c4,c4, d, d, k, k, k, k, k, k, k, l, n, n, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,c0,c0,c0,c0,c0,c0,c0,c2,c2,c2,c3,c3,c3,c4,c4, d, k, k, k, k, k, k, k, l, l, l, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,c0,c0,c0,c0,c0,c0,c0,c0,c0,c0,c2,c2,c2,c3,c3,c4, d, d, k, k, k, k, k, k, k, l, n, p, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,c0,c0,c0,c0,c0,c0,c0,c0,c0,c0,c0,c0,c0,c2,c2,c3,c4,c4, d, k, k, k, k, k, k, l, n, n, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n, c, c, c, c, c, c,c0,c0,c0,c0,c0,c0,c0,c0,c0,c2,c3,c3,c4, d, d, k, k, k, k, k, l, l, l, e, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,b4,b4,b4,b4,b4,b4, c, c, c,c0,c0,c0,c0,c0,c0,c0,c2,c2,c3,c4,c4, d, k, k, k, k, k, k, l, n, p, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,b3,b3,b3,b3,b3,b3,b4,b4,b4, c, c, c,c0,c0,c0,c0,c0,c0,c2,c3,c3,c4, d, k, k, k, k, k, l, n, n, e, n, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,b2,b2,b2,b2,b2,b2,b3,b3,b3,b4,b4,b4, c, c,c0,c0,c0,c0,c0,c2,c2,c3,c4, d, k, k, k, k, k, l, l, l, e, n, n, n, n, n, n, n, n, n, n, n, n],
            [ n,b1,b1,b1,b1,b1,b1,b2,b2,b2,b3,b3,b3,b4,b4, c,c0,c0,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, k, k, l, n, p, n, n, n, n, n, n, n, n, n, n, n],
            [ n, b, b, b, b, b,b0,b1,b1,b1,b2,b2,b2,b3,b3,b4, c, c,c0,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, k, l, n, e, n, n, n, n, n, n, n, n, n, n, n],
            [ n,a5,a5,a5,a5,a5, b, b, b,b0,b1,b1,b1,b2,b2,b3,b4,b4, c,c0,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, k, l, l, e, n, n, n, n, n, n, n, n, n, n],
            [ n,a4,a4,a4,a4,a4,a5,a5,a5, b,b0,b0,b0,b1,b1,b2,b3,b3,b4, c,c0,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, k, l, n, p, n, n, n, n, n, n, n, n, n],
            [ n,a3,a3,a3,a3,a3,a4,a4,a4,a5, b, b,b0,b0,b0,b1,b2,b2,b3,b4, c,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, k, l, n, e, n, n, n, n, n, n, n, n, n],
            [ n,a2,a2,a2,a2,a2,a3,a3,a3,a4,a5,a5, b,b0,b0,b0,b1,b1,b2,b3,b4, c,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, k, l, n, e, n, n, n, n, n, n, n, n],
            [ n,a0,a0,a0,a0,a0,a2,a2,a2,a3,a4,a4,a5, b,b0,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n, n, n, n, n, n, n, n],
            [ n,a0,a0,a0,a0,a0,a0,a0,a0,a2,a3,a3,a4,a5, b, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, n, e, n, n, n, n, n, n, n],
            [ n, a, a, a,a0,a0,a0,a0,a0,a0,a2,a2,a3,a4,a5,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c0,c2,c3,c4, d, k, k, k, k, l, l, e, n, n, n, n, n, n, n],
            [ n, n, n, n, a, a,a0,a0,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, k, l, n, p, n, n, n, n, n, n],
            [ n, n, n, n, n, n, a, a,a0,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n, n, n, n, n, n],
            [ n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n, n, n, n, n],
            [ n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n, n, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, n, e, n, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c3,c4, d, k, k, k, l, n, n, e, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, l, n, n, e, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p, n],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c0,c2,c3,c4, d, k, k, k, l, n, n, e],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, e],
            [ n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, a,a0,a0,a0,a0,a2,a3,a4,a5, b,b0,b0,b0,b1,b2,b3,b4, c,c0,c2,c3,c4, d, k, k, k, k, l, n, p]
        ]

    for h in range(4) # 콜로세움 바닥,벽 틀 건설
        for i in f
            for j in i
                if j == a
                    blocks.fill(b1, world(x+3, y, z), world(x+3, y+6, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+4, z), world(x+3, y+4, z), FillOperation.REPLACE)
                    blocks.fill(BLOCK_OF_NETHERITE, world(x+3, y+7, z), world(x+3, y+7, z), FillOperation.REPLACE)
                elif j == b
                    blocks.fill(b1, world(x+3, y, z), world(x+3, y+12, z), FillOperation.REPLACE)
                    blocks.fill(BLOCK_OF_NETHERITE, world(x+3, y+13, z), world(x+3, y+13, z), FillOperation.REPLACE)
                elif j == c
                    blocks.fill(b1, world(x+3, y, z), world(x+3, y+18, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+17, z), world(x+3, y+17, z), FillOperation.REPLACE)
                    blocks.fill(BLOCK_OF_NETHERITE, world(x+3, y+19, z), world(x+3, y+19, z), FillOperation.REPLACE)
                elif j == d
                    blocks.fill(b1, world(x+3, y, z), world(x+3, y+24, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+25, z), world(x+3, y+25, z), FillOperation.REPLACE)
                    blocks.fill(BLOCK_OF_NETHERITE, world(x+3, y+26, z), world(x+3, y+26, z), FillOperation.REPLACE)
                elif j == e
                    blocks.fill(b1, world(x+3, y, z), world(x+3, y, z), FillOperation.REPLACE)

                elif j == a0
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)

                elif j == a2
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+7, z), FillOperation.REPLACE)

                elif j == a3
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+8, z), FillOperation.REPLACE)

                elif j == a4
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+9, z), FillOperation.REPLACE)

                elif j == a5
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+8, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+6, z), world(x+3, y+9, z), FillOperation.REPLACE)
                    blocks.fill(blocks.block_with_data(44, 8), world(x+3, y+10, z), world(x+3, y+10, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y-1, z), world(x+3, y-1, z), FillOperation.REPLACE)

                elif j == b0
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+12, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                elif j == b1
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+12, z), FillOperation.REPLACE)
                    blocks.fill(STONE_SLAB,world(x+3, y+13, z), world(x+3, y+13, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                elif j == b2
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+13, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                elif j == b3
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+14, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                elif j == b4
                    blocks.fill(b2, world(x+3, y+15, z), world(x+3, y+15, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y-1, z), world(x+3, y-1, z), FillOperation.REPLACE)

                elif j == c0
                    blocks.fill(b2, world(x+3, y+18, z), world(x+3, y+18, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+12, z), FillOperation.REPLACE)
                elif j == c2
                    blocks.fill(b2, world(x+3, y+18, z), world(x+3, y+19, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+12, z), FillOperation.REPLACE)
                elif j == c3
                    blocks.fill(b2, world(x+3, y+18, z), world(x+3, y+20, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                    blocks.fill(b2, world(x+3, y+12, z), world(x+3, y+12, z), FillOperation.REPLACE)
                elif j == c4
                    blocks.fill(b2, world(x+3, y+18, z), world(x+3, y+21, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+6, z), world(x+3, y+6, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y+12, z), world(x+3, y+12, z), FillOperation.REPLACE)
                    blocks.fill(SHROOMLIGHT, world(x+3, y-1, z), world(x+3, y-1, z), FillOperation.REPLACE)

                elif j == p
                    Pillar(x,y,z)

                elif j == l
                    blocks.place(SHROOMLIGHT, world(x+3, y-1, z))
                    blocks.place(SHROOMLIGHT, world(x+3, y+5, z))
                    blocks.place(SHROOMLIGHT, world(x+3, y+12, z))
                    blocks.place(SHROOMLIGHT, world(x+3, y+18, z))
                    blocks.fill(blocks.block_with_data(35, 8), world(x+3, y+19, z), world(x+3, y+27, z), FillOperation.REPLACE)
                    blocks.place(SHROOMLIGHT, world(x+3, y+28, z))
                    blocks.place(BLOCK_OF_NETHERITE, world(x+3, y+29, z))

                elif j == k
                    blocks.place(1, world(x+3, y+5, z))
                    blocks.place(1, world(x+3, y+12, z))
                    blocks.place(1, world(x+3, y+18, z))

                z -= 1
            z = start_z
            x += 1


        if h == 0
            f.reverse() # 배열을 반전 시키는 함수

        elif h == 1
            start_z += 46
            x -= 54
            z += 46
            for i1 in range(54)
                    f[i1].reverse()

        elif h == 2
            x = start_x
            f.reverse()

def Pillar(x,y,z)

    start_z = z
    start_y = y
    start_x = x

    # 기둥 층

    # 석재 반들럭 [1층]
    blocks.fill(blocks.block_with_data(STONE_BRICKS_SLAB, 8), world(x+2, y+5, z-1), world(x+4, y+5, z+1), FillOperation.REPLACE)

    # 안산암 [2층]
    blocks.fill(blocks.block_with_data(1, 6), world(x+2, y+12, z-1), world(x+4, y+12, z+1), FillOperation.REPLACE)

    # 조약돌 반블럭  회백색 양털 [3층]
    blocks.fill(blocks.block_with_data(COBBLESTONE_SLAB, 8), world(x+2, y+17, z-1), world(x+4, y+17, z+1), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(35, 8), world(x+2, y+18, z-1), world(x+4, y+18, z+1), FillOperation.REPLACE)

    # 조약돌 반블럭 [4층]
    blocks.fill(blocks.block_with_data(COBBLESTONE_SLAB, 0), world(x+2, y+29, z-1), world(x+4, y+29, z+1), FillOperation.REPLACE)

    # 석재 계단 [1층]
    blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 4), world(x+2, y+5, z), world(x+2, y+5, z), FillOperation.REPLACE) # 앞
    blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 5), world(x+4, y+5, z), world(x+4, y+5, z), FillOperation.REPLACE) # 뒤
    blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 6), world(x+3, y+5, z-1), world(x+3, y+5, z-1), FillOperation.REPLACE) # 왼
    blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 7), world(x+3, y+5, z+1), world(x+3, y+5, z+1), FillOperation.REPLACE) # 오

    # 석재 계단  조각된 석재 [2층]
    blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 4), world(x+2, y+11, z), world(x+2, y+11, z), FillOperation.REPLACE) # 앞
    blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 5), world(x+4, y+11, z), world(x+4, y+11, z), FillOperation.REPLACE) # 뒤
    blocks.fill(blocks.block_with_data(STONE_BRICKS, 3), world(x+3, y+11, z-1), world(x+3, y+11, z-1), FillOperation.REPLACE) # 왼
    blocks.fill(blocks.block_with_data(STONE_BRICKS, 3), world(x+3, y+11, z+1), world(x+3, y+11, z+1), FillOperation.REPLACE) # 오

    # 석재 계단  조각된 석재 [3층]
    blocks.fill(blocks.block_with_data(COBBLESTONE_STAIRS, 4), world(x+2, y+17, z), world(x+2, y+17, z), FillOperation.REPLACE) # 앞
    blocks.fill(blocks.block_with_data(COBBLESTONE_STAIRS, 5), world(x+4, y+17, z), world(x+4, y+17, z), FillOperation.REPLACE) # 뒤
    blocks.fill(blocks.block_with_data(COBBLESTONE_STAIRS, 6), world(x+3, y+17, z-1), world(x+3, y+17, z-1), FillOperation.REPLACE) # 왼
    blocks.fill(blocks.block_with_data(COBBLESTONE_STAIRS, 7), world(x+3, y+17, z+1), world(x+3, y+17, z+1), FillOperation.REPLACE) # 오

    # 쉬룸 라이트  조약돌 계단 [4층]
    blocks.fill(SHROOMLIGHT, world(x+3, y+28, z-1), world(x+3, y+28, z+1), FillOperation.REPLACE) # 양옆
    blocks.fill(blocks.block_with_data(COBBLESTONE_STAIRS, 4), world(x+2, y+28, z), world(x+3, y+28, z), FillOperation.REPLACE) # 앞
    blocks.fill(blocks.block_with_data(COBBLESTONE_STAIRS, 5), world(x+4, y+28, z), world(x+3, y+28, z), FillOperation.REPLACE) # 뒤

    # 기둥
    blocks.fill(blocks.block_with_data(1, 6), world(x+3, y, z), world(x+3, y+28, z), FillOperation.REPLACE)


def Entrance(x,y,z)

    # 1층 입구
    blocks.fill(blocks.block_with_data(1, 6), world(x+10, y+6, z-1), world(x+29, y+6, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+29, y+7, z), world(x+29, y+7, z+1), FillOperation.REPLACE)
    for i in [4,3,2,1,0]
        blocks.fill(blocks.block_with_data(1, 6), world(x+23, y+7+i, z+2), world(x+27-i, y+7+i, z+2), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(1, 6), world(x+23, y+7+i, z-1), world(x+27-i, y+7+i, z-1), FillOperation.REPLACE)

    # 2층 입구
    blocks.fill(blocks.block_with_data(1, 6), world(x+10, y+12, z-1), world(x+23, y+12, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+23, y+13, z-1), world(x+23, y+13, z+2), FillOperation.REPLACE)

    jj = 0
    for j in [2,1,0,0,0]

        blocks.fill(blocks.block_with_data(1, 6), world(x+18, y+17-jj, z+2), world(x+20-j, y+17-jj, z+2), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(1, 6), world(x+18, y+17-jj, z-1), world(x+20-j, y+17-jj, z-1), FillOperation.REPLACE)
        jj += 1

    # 3층 입구
    blocks.fill(blocks.block_with_data(1, 6), world(x+10, y+18, z-1), world(x+18, y+18, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+18, y+19, z-1), world(x+18, y+19, z+2), FillOperation.REPLACE)

    for k in [3,2,1,0]
        blocks.fill(blocks.block_with_data(1, 6), world(x+11, y+19+k, z+2), world(x+14-k, y+19+k, z+2), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(1, 6), world(x+11, y+19+k, z-1), world(x+14-k, y+19+k, z-1), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(1, 6), world(x+11, y+23, z-1), world(x+11, y+23, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+11, y+24, z-1), world(x+11, y+24, z+2), FillOperation.REPLACE)
    blocks.fill(SHROOMLIGHT, world(x+10, y+25, z-1), world(x+10, y+25, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+10, y+26, z-1), world(x+10, y+26, z+2), FillOperation.REPLACE)

## 반대편

    # 1층 입구
    blocks.fill(blocks.block_with_data(1, 6), world(x+84, y+6, z-1), world(x+103, y+6, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+84, y+7, z), world(x+84, y+7, z+1), FillOperation.REPLACE)
    for i1 in [4,3,2,1,0]
        blocks.fill(blocks.block_with_data(1, 6), world(x+90, y+7+i1, z+2), world(x+86+i1, y+7+i1, z+2), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(1, 6), world(x+90, y+7+i1, z-1), world(x+86+i1, y+7+i1, z-1), FillOperation.REPLACE)

    # # 2층 입구
    blocks.fill(blocks.block_with_data(1, 6), world(x+90, y+12, z-1), world(x+103, y+12, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+90, y+13, z-1), world(x+90, y+13, z+2), FillOperation.REPLACE)

    jj = 0
    for j1 in [2,1,0,0,0]

        blocks.fill(blocks.block_with_data(1, 6), world(x+95, y+17-jj, z+2), world(x+93+j1, y+17-jj, z+2), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(1, 6), world(x+95, y+17-jj, z-1), world(x+93+j1, y+17-jj, z-1), FillOperation.REPLACE)
        jj += 1

    # # 3층 입구
    blocks.fill(blocks.block_with_data(1, 6), world(x+95, y+18, z-1), world(x+103, y+18, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+95, y+19, z-1), world(x+95, y+19, z+2), FillOperation.REPLACE)

    for k1 in [0,1,2,3]
        blocks.fill(blocks.block_with_data(1, 6), world(x+102, y+19+k1, z+2), world(x+99+k1, y+19+k1, z+2), FillOperation.REPLACE)
        blocks.fill(blocks.block_with_data(1, 6), world(x+102, y+19+k1, z-1), world(x+99+k1, y+19+k1, z-1), FillOperation.REPLACE)
    blocks.fill(blocks.block_with_data(1, 6), world(x+102, y+23, z-1), world(x+102, y+23, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+102, y+24, z-1), world(x+102, y+24, z+2), FillOperation.REPLACE)
    blocks.fill(SHROOMLIGHT, world(x+103, y+25, z-1), world(x+103, y+25, z+2), FillOperation.REPLACE)
    blocks.fill(BLOCK_OF_NETHERITE, world(x+103, y+26, z-1), world(x+103, y+26, z+2), FillOperation.REPLACE)

def Stair(x,y,z)

    # 1 ~ 2층 계단
    blocks.fill(AIR, world(x+6, y, z-2), world(x+9, y+6, z-6), FillOperation.REPLACE) # 계단 자리 구멍 뚫기

    for i in range(1,4)
        blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 3), world(x+8, y+i, z-1-i), world(x+9, y+i, z-1-i), FillOperation.REPLACE) # 계단 오른쪽 1층
        blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 2), world(x+6, y+i+3, z-5+i), world(x+7, y+i+3, z-5+i), FillOperation.REPLACE) # 계단 왼쪽 1층

    blocks.fill(blocks.block_with_data(STONE_BRICKS, 0), world(x+6, y+3, z-5), world(x+9, y+3, z-6), FillOperation.REPLACE) # 계단창 1.5층
    blocks.fill(blocks.block_with_data(STONE_BRICKS, 0), world(x+6, y+6, z-1), world(x+7, y+6, z-1), FillOperation.REPLACE) # 계단창 2층

    # 2 ~ 3층 계단
    blocks.fill(AIR, world(x+6, y+6, z+2), world(x+9, y+12, z+6), FillOperation.REPLACE) # 계단 자리 구멍 뚫기
    for j in range(1,4)
        blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 2), world(x+8, y+i+7, z-5+i), world(x+9, y+i+7, z-5+i), FillOperation.REPLACE) # 계단 왼쪽 1층
        blocks.fill(blocks.block_with_data(STONE_BRICK_STAIRS, 3), world(x+6, y+i+10, z-1-i), world(x+7, y+i+10, z-1-i), FillOperation.REPLACE) # 계단 오른쪽 1층






def Colosseum(x,y,z) #콜로세움 건설
    # Ground(x,y,z)
    # Road(x, y, z)
    # Frame(x, y, z)
    # Entrance(x,y,z)
    Stair(x,y,z)


def Clear(x,y,z) #  건축물 삭제
    for ii in range(-1,41)
        blocks.fill(0, world(x, y+ii, z-48), world(x+111, y+ii+1,z+48))


def ts(x)

    a = blocks.block_with_data(STONE_BRICKS, 3) # 조각된 석재재
    blocks.place(a, pos(0, -1, 0))

player.on_chat(Colosseum,Colosseum)
player.on_chat(Clear, Clear)
player.on_chat(ts, Pillar)