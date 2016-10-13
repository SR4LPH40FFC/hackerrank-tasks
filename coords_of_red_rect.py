#!/usr/bin/python


def get_coords_single_rect(lst):

    x1 = None
    y1 = None
    x2 = None
    y2 = None

    coords = list()

    y = 0
    for row in lst:

        if(x1 == None):
            # find top left point of rectangle
            x = 0
            for col in row:
                if(x1 == None):
                    if col == 0:
                        x1 = x
                        y1 = y
                        coords.append([x,y])
                else:
                    if col == 0:
                        coords.append([x,y])
                    elif col == 1:
                        x2 = x-1
                        break

                x += 1

            if(x1 != None and x2 == None):
                x2 = len(row)-1
                coords.append([x2,y1])

        else:

            if (row[x1] == 1):
                y2 = y-1
                break
            elif (row[x1] == 0):
                for r in range(x1,x2+1):
                    coords.append([r,y])

        y += 1

    if y1 != None and y2 == None:
        y2 = len(lst)-1

    if(x1 != None and x2 != None and y1 != None and y2 != None):
        return coords
    else:
        return None

class Rectangle:
    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.coords = list()

    def append(self, x, y):
        self.coords.append(x,y)

# 
# def get_coords_multi(lst):
# 
#     x1 = None
#     y1 = None
#     x2 = None
#     y2 = None
# 
#     coords = dict()
# 
#     y = 0
#     for row in lst:
# 
#         if(x1 == None):
#             # find top left point of rectangle
#             x = 0
#             for col in row:
#                 if(x1 == None):
#                     if col == 0:
#                         coords[x1+","+y1].x1 = x
#                         coords[x1+","+y1].y1 = y
#                         coords[x1+","+y1] = Rectangle()
#                         coords[x1+","+y1].append([x,y])
#                 else:
#                     if col == 0:
#                         coords[x1+","+y1].append([x,y])
#                     elif col == 1:
#                         coords[x1+","+y1].x2 = x-1
#                         # break
# 
#                 x += 1
# 
#             for r in coords:
#                 if (r.y2 != None)
#                 if(r.x2 == None):
#                     r.x2 = len(row)-1
#                     coords[r.x1+","+r.y1].append([r.x2,r.y1])
# 
#         else:
# 
#             if (row[x1] == 1):
#                 y2 = y-1
#                 break
#             elif (row[x1] == 0):
#                 for r in range(x1,x2+1):
#                     coords.append([r,y])
# 
#         y += 1
# 
#     if y1 != None and y2 == None:
#         y2 = len(lst)-1
# 
#     if(x1 != None and x2 != None and y1 != None and y2 != None):
#         return coords
#     else:
#         return None


l = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

coords = get_coords_single_rect(l)

if coords:
    print coords
else:
    print "Not found"

