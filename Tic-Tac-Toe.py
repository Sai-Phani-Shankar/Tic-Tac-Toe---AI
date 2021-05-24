from random import randrange


class Neural_Network():
    lists = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    rewards = [0,0,0,0,0,0,0,0,0]

    def board():
        m = -1
        for i in range(0, 9):
            m += 1
            if m == 3 or m == 6:
                print("\n")
            print(Neural_Network.lists[i], end=" ")

    def clear_board():
        Neural_Network.lists = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        Neural_Network.board()

    def check(index):
        if Neural_Network.rewards[index] == 1 or Neural_Network.rewards[index] == -1:
            return False
        else:
            return True

    def fit():
        k1 = 2
        for i1 in range(13):
            a = False
            b = False
            c = False
            d = False
            e = False
            f = False
            g = False
            h = False

            i = False
            j = False
            k = False
            l = False
            m = False
            n = False
            o = False
            p = False

            val = False
            val1 = False
            val2 = False

            k1 += 1
            if k1 % 2 == 0:
                if Neural_Network.rewards[0] + Neural_Network.rewards[1] + Neural_Network.rewards[2] == -2:
                    i = True
                elif (Neural_Network.rewards[3] + Neural_Network.rewards[4] + Neural_Network.rewards[5] == -2):
                    j = True
                elif (Neural_Network.rewards[6] + Neural_Network.rewards[7] + Neural_Network.rewards[8] == -2):
                    k = True
                elif (Neural_Network.rewards[0] + Neural_Network.rewards[3] + Neural_Network.rewards[6] == -2):
                    l = True
                elif (Neural_Network.rewards[1] + Neural_Network.rewards[4] + Neural_Network.rewards[7] == -2):
                    m = True
                elif (Neural_Network.rewards[2] + Neural_Network.rewards[5] + Neural_Network.rewards[8] == -2):
                    n = True
                elif (Neural_Network.rewards[0] + Neural_Network.rewards[4] + Neural_Network.rewards[8] == -2):
                    o = True
                elif (Neural_Network.rewards[2] + Neural_Network.rewards[4] + Neural_Network.rewards[6] == -2):
                    p = True

                elif Neural_Network.rewards[0] + Neural_Network.rewards[1] + Neural_Network.rewards[2] == 2:
                    a = True
                elif Neural_Network.rewards[3] + Neural_Network.rewards[4] + Neural_Network.rewards[5] == 2:
                    b = True
                elif Neural_Network.rewards[6] + Neural_Network.rewards[7] + Neural_Network.rewards[8] == 2:
                    c = True
                elif Neural_Network.rewards[0] + Neural_Network.rewards[3] + Neural_Network.rewards[6] == 2:
                    d = True
                elif Neural_Network.rewards[1] + Neural_Network.rewards[4] + Neural_Network.rewards[7] == 2:
                    e = True
                elif Neural_Network.rewards[2] + Neural_Network.rewards[5] + Neural_Network.rewards[8] == 2:
                    f = True
                elif Neural_Network.rewards[0] + Neural_Network.rewards[4] + Neural_Network.rewards[8] == 2:
                    g = True
                elif Neural_Network.rewards[2] + Neural_Network.rewards[4] + Neural_Network.rewards[6] == 2:
                    h = True

                else:
                    x = randrange(9)
                    check = Neural_Network.check(x)

                if a:
                    val = Neural_Network.check(0)
                    val1 = Neural_Network.check(1)
                    val2 = Neural_Network.check(2)

                    if val:
                        x = 0
                    if val1:
                        x = 1
                    if val2:
                        x = 2

                if b:
                    val = Neural_Network.check(3)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(5)

                    if val:
                        x = 3
                    if val1:
                        x = 4
                    if val2:
                        x = 5

                if c:
                    val = Neural_Network.check(6)
                    val1 = Neural_Network.check(7)
                    val2 = Neural_Network.check(8)

                    if val:
                        x = 6
                    if val1:
                        x = 7
                    if val2:
                        x = 8

                if d:
                    val = Neural_Network.check(0)
                    val1 = Neural_Network.check(3)
                    val2 = Neural_Network.check(6)

                    if val:
                        x = 0
                    if val1:
                        x = 3
                    if val2:
                        x = 6

                if e:
                    val = Neural_Network.check(1)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(7)

                    if val:
                        x = 1
                    if val1:
                        x = 4
                    if val2:
                        x = 7

                if f:
                    val = Neural_Network.check(2)
                    val1 = Neural_Network.check(5)
                    val2 = Neural_Network.check(8)

                    if val:
                        x = 2
                    if val1:
                        x = 5
                    if val2:
                        x = 8

                if g:
                    val = Neural_Network.check(0)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(8)

                    if val:
                        x = 0
                    if val1:
                        x = 4
                    if val2:
                        x = 8

                if h:
                    val = Neural_Network.check(2)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(6)

                    if val:
                        x = 2
                    if val1:
                        x = 4
                    if val2:
                        x = 6

                if i:
                    val = Neural_Network.check(0)
                    val1 = Neural_Network.check(1)
                    val2 = Neural_Network.check(2)

                    if val:
                        x = 0
                    if val1:
                        x = 1
                    if val2:
                        x = 2

                if j:
                    val = Neural_Network.check(3)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(5)

                    if val:
                        x = 3
                    if val1:
                        x = 4
                    if val2:
                        x = 5

                if k:
                    val = Neural_Network.check(6)
                    val1 = Neural_Network.check(7)
                    val2 = Neural_Network.check(8)

                    if val:
                        x = 6
                    if val1:
                        x = 7
                    if val2:
                        x = 8

                if l:
                    val = Neural_Network.check(0)
                    val1 = Neural_Network.check(3)
                    val2 = Neural_Network.check(6)

                    if val:
                        x = 0
                    if val1:
                        x = 3
                    if val2:
                        x = 6

                if m:
                    val = Neural_Network.check(1)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(7)

                    if val:
                        x = 1
                    if val1:
                        x = 4
                    if val2:
                        x = 7

                if n:
                    val = Neural_Network.check(2)
                    val1 = Neural_Network.check(5)
                    val2 = Neural_Network.check(8)

                    if val:
                        x = 2
                    if val1:
                        x = 5
                    if val2:
                        x = 8

                if o:
                    val = Neural_Network.check(0)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(8)

                    if val:
                        x = 0
                    if val1:
                        x = 4
                    if val2:
                        x = 8

                if p:
                    val = Neural_Network.check(2)
                    val1 = Neural_Network.check(4)
                    val2 = Neural_Network.check(6)

                    if val:
                        x = 2
                    if val1:
                        x = 4
                    if val2:
                        x = 6

                else:
                    if check:
                        Neural_Network.lists[x] = 'O'
                        Neural_Network.rewards[x] = -1
                        Neural_Network.board()
                        print("\n")
                        print("next iteration")
                    else:
                        k1 -= 1

            else:
                y = int(input())
                va = Neural_Network.check(y)
                if va:
                    Neural_Network.lists[y] = 'X'
                    Neural_Network.rewards[y] = 1
                    Neural_Network.board()
                    print("\n")
                    print("AI is thinking")

            if (Neural_Network.lists[0] == 'O' and Neural_Network.lists[1] == 'O' and Neural_Network.lists[
                2] == 'O') or (
                    Neural_Network.lists[3] == 'O' and Neural_Network.lists[4] == 'O' and Neural_Network.lists[
                5] == 'O') or (
                    Neural_Network.lists[6] == 'O' and Neural_Network.lists[7] == 'O' and Neural_Network.lists[
                8] == 'O') or (
                    Neural_Network.lists[0] == 'O' and Neural_Network.lists[3] == 'O' and Neural_Network.lists[
                6] == 'O') or (
                    Neural_Network.lists[1] == 'O' and Neural_Network.lists[4] == 'O' and Neural_Network.lists[
                7] == 'O') or (
                    Neural_Network.lists[2] == 'O' and Neural_Network.lists[5] == 'O' and Neural_Network.lists[
                8] == 'O') or (
                    Neural_Network.lists[0] == 'O' and Neural_Network.lists[4] == 'O' and Neural_Network.lists[
                8] == 'O') or (
                    Neural_Network.lists[2] == 'O' and Neural_Network.lists[4] == 'O' and Neural_Network.lists[
                6] == 'O'):
                Neural_Network.clear_board()
                print("AI has Won")
                break
            if (Neural_Network.lists[0] == 'X' and Neural_Network.lists[1] == 'X' and Neural_Network.lists[
                2] == 'X') or (
                    Neural_Network.lists[3] == 'X' and Neural_Network.lists[4] == 'X' and Neural_Network.lists[
                5] == 'X') or (
                    Neural_Network.lists[6] == 'X' and Neural_Network.lists[7] == 'X' and Neural_Network.lists[
                8] == 'X') or (
                    Neural_Network.lists[0] == 'X' and Neural_Network.lists[3] == 'X' and Neural_Network.lists[
                6] == 'X') or (
                    Neural_Network.lists[1] == 'X' and Neural_Network.lists[4] == 'X' and Neural_Network.lists[
                7] == 'X') or (
                    Neural_Network.lists[2] == 'X' and Neural_Network.lists[5] == 'X' and Neural_Network.lists[
                8] == 'X') or (
                    Neural_Network.lists[0] == 'X' and Neural_Network.lists[4] == 'X' and Neural_Network.lists[
                8] == 'X') or (
                    Neural_Network.lists[2] == 'X' and Neural_Network.lists[4] == 'X' and Neural_Network.lists[
                6] == 'X'):
                Neural_Network.clear_board()
                print("Player 1 has won")
                break


if __name__ == '__main__':
    Neural_Network.fit()


