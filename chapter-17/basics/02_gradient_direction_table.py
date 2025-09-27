# Show gradient signs left/right of the minimum for Error = (g - 3)^2
def grad(g): return 2*(g-3)

for g in [0, 1, 2, 3, 4, 5, 6]:
    direction = 'left' if grad(g)>0 else ('right' if grad(g)<0 else 'stop')
    print(f"g={g:>2}  grad={grad(g):>5.1f}  move {direction}")
