'''
Bresenham
http://cobrabytes.squeakyduck.co.uk/forum/index.php?topic=1150.0



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


## fuer das umrechnen
imageSpacingX = 0.583984375
imageSpacingY = 0.583984375
imageSpacingZ = 1

def mmToPixel (x,y,z):
    px = x/imageSpacingX
    py = y/imageSpacingY
    pz = z/imageSpacingZ
    return [px,py,pz]

'''
http://stackoverflow.com/questions/9084189/draw-a-sphere-using-3d-pixels-voxels
'''

def draw3DCircle (x0, y0, z0, y1, radius, error0):
    x = radius
    z = 0
    radiusError = error0 ## Initial error state passed in, NOT 1-x

    while (x >= z):
        # draw the 32 points here.
        '''
        Draw the standard circle algorithm points at
        y0 + y1 and y0 - y1: x0 +/- x, z0 +/- z, y0 +/- y1, x0 +/- z, z0 +/- x, y0 +/- y1,
        total 16 points. This forms the bulk of the vertical of the sphere. octant
        '''
        a[x0+x,y0+y1,z0+z]=250 # 1, 1, 1
        a[x0-x,y0+y1,z0+z]=250 # -1, 1, 1
        a[x0-x,y0-y1,z0+z]=250 # -1, -1, 1
        a[x0+x,y0-y1,z0+z]=250 # 1, -1, 1
        a[x0+x,y0+y1,z0-z]=250 # 1, 1, -1
        a[x0-x,y0+y1,z0-z]=250 # -1, 1, -1
        a[x0-x,y0-y1,z0-z]=250 # -1, -1, -1
        a[x0+x,y0-y1,z0-z]=250 # 1, -1, -1

        a[x0+z,y0+y1,z0+x]=250 # 1, 1, 1
        a[x0-z,y0+y1,z0+x]=250 # -1, 1, 1
        a[x0-z,y0-y1,z0+x]=250 # -1, -1, 1
        a[x0+z,y0-y1,z0+x]=250 # 1, -1, 1
        a[x0+z,y0+y1,z0-x]=250 # 1, 1, -1
        a[x0-z,y0+y1,z0-x]=250 # -1, 1, -1
        a[x0-z,y0-y1,z0-x]=250 # -1, -1, -1
        a[x0+z,y0-y1,z0-x]=250 # 1, -1, -1

        ## aditional points

        a[x0+y1,y0+z,z0+x]=250 # 1, 1, 1
        a[x0-y1,y0+z,z0+x]=250 # -1, 1, 1
        a[x0-y1,y0-z,z0+x]=250 # -1, -1, 1
        a[x0+y1,y0-z,z0+x]=250 # 1, -1, 1
        a[x0+y1,y0+z,z0-x]=250 # 1, 1, -1
        a[x0-y1,y0+z,z0-x]=250 # -1, 1, -1
        a[x0-y1,y0-z,z0-x]=250 # -1, -1, -1
        a[x0+y1,y0-z,z0-x]=250 # 1, -1, -1

        a[x0+x,y0+z,z0+y1]=250 # 1, 1, 1
        a[x0-x,y0+z,z0+y1]=250 # -1, 1, 1
        a[x0-x,y0-z,z0+y1]=250 # -1, -1, 1
        a[x0+x,y0-z,z0+y1]=250 # 1, -1, 1
        a[x0+x,y0+z,z0-y1]=250 # 1, 1, -1
        a[x0-x,y0+z,z0-y1]=250 # -1, 1, -1
        a[x0-x,y0-z,z0-y1]=250 # -1, -1, -1
        a[x0+x,y0-z,z0-y1]=250 # 1, -1, -1

        z +=1
        if(radiusError<0):
            radiusError+=2*z+1
        else:
            x-=1
            radiusError+=2*(z-x+1)

def draw3DSphere(x0, y0, z0, radius):
    x = radius/2  # otherweise radius was diameter
    y = 0
    radiusError = 1-x

    while (x >= y):
        # pass in base point (x0,y0,z0), this algorithm's y as y1,
        # this algorithm's x as the radius, and pass along radius error.
        draw3DCircle(x0, y0, z0, y, x, radiusError)
        y+=1
        if(radiusError<0):
            radiusError+=2*y+1
        else:
            x-=1
            radiusError+=2*(y-x+1)
