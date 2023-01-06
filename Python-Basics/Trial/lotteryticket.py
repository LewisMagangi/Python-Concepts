ticket = [ [ 'ABC', 65 ], [ 'HGR', 66 ], [ 'BYHT', 67 ] ]

def bingo(ticket,win):
     if ((sum(chr(x) in l for l, x in ticket)) >= win):
          print('Winner!')
          return(None)
     print("Loser!")
bingo(ticket,2)
