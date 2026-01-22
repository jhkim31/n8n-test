n = int(input())


routes = []
for _ in range(6):
    route = list(map(int, input().split()))
    routes.append(route)

routes.append(routes[0])

sub = 0
before = -1
_type = -1
for route in routes:
    if before == 3 and route[0] == 2:      
        _type = 1
        sub *= route[1]
        break
    if before == 2 and route[0] == 4:
        _type = 2
        sub *= route[1]
        break
    if before == 4 and route[0] == 1:
        _type = 3
        sub *= route[1]
        break
    if before == 1 and route[0] == 3:
        _type = 4
        sub *= route[1]
        break
    before = route[0]
    sub = route[1]

if _type == 1:
    a = 0
    b = 0  
    for route in routes:
        if route[0] == 1:
            a = route[1]
        if route[0] == 4:
            b = route[1]
    total = a * b
    print((total - sub) * n)


if _type == 2:
    a = 0
    b = 0
    for route in routes:
        if route[0] == 3:
            a = route[1]
        if route[0] == 1:
            b = route[1]
    total = a * b
  
    print((total - sub) * n)
            

if _type == 3:
    a = 0
    b = 0
    for route in routes:
        if route[0] == 2:
            a = route[1]
        if route[0] == 3:
            b = route[1]
    total = a * b
    print((total - sub) * n)

if _type == 4:
    a = 0
    b = 0
    for route in routes:
        if route[0] == 4:
            a = route[1]
        if route[0] == 2:
            b = route[1]
    total = a * b
    print((total - sub) * n)

