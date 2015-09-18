'''
Bresenham
http://cobrabytes.squeakyduck.co.uk/forum/index.php?topic=1150.0
@author: mukesch.shah@uniklinik-freiburg.de


'''

def draw3DLine (x0, y0, z0, x1, y1, z1):
    # 'steep' xy Line, make longest delta x plane
    swap_xy = abs(y1 - y0) > abs(x1 - x0)
    if (swap_xy) :
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    # do same for xz
    swap_xz = abs(z1 - z0) > abs (x1 - x0)
    if swap_xz :
        x0, z0 = z0, x0
        x1, z1 = z1, x1

    # delta is Length in each plane
    delta_x = abs(x1 - x0)
    delta_y = abs(y1 - y0)
    delta_z = abs(z1 - z0)

    # drift controls when to step in 'shallow' planes
    # starting value keeps Line centred

    drift_xy = (delta_x/2)
    drift_xz = (delta_x/2)

    # direction of line
    step_x = 1
    if (x0 > x1):
        step_x = -1
    step_y = 1
    if (y0 > y1):
        step_y = -1
    step_z = 1
    if (z0 > z1):
        step_z = -1

    # starting point
    y = y0
    z = z0

    # step through longest delta (which we have swapped to x)
    for x in range (x0,x1,step_x):
        # copy position
        cx = x
        cy = y
        cz = z

        # unswap (in reverse)
        if swap_xz:
            cx, cz = cz, cy
        if swap_xy:
            cx, cy = cy, cx

        # passes through this point
        print (":" + str(cx) + ", " + str(cy) + ", " + str(cz))
        a[cx,cy,cz] = 250

        # update progress in other planes
        drift_xy = drift_xy - delta_y
        drift_xz = drift_xz - delta_z

        # step in y plane
        if (drift_xy < 0):
            y = y + step_y
            drift_xy = drift_xy + delta_x
        # same in z
        if (drift_xz < 0):
            z = z + step_z
            drift_xz = drift_xz + delta_x


imageSpacingX = 0.583984375
imageSpacingY = 0.583984375
imageSpacingZ = 1

def mmToPixel (x,y,z):
    px = x/imageSpacingX
    py = y/imageSpacingY
    pz = z/imageSpacingZ

    return [px,py,pz]
