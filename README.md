# PyBresenham
Pythonimplementation of Bresenham Line-Drawing

wikipedia quotes:

'''Bresenham's line algorithm''' is an [[algorithm]] that determines the points of an ''n''-dimensional [[raster graphics|raster]] that should be selected in order to form a close approximation to a straight line between two points. It is commonly used to draw lines on a computer screen, as it uses only integer addition, subtraction and [[Bitwise operation|bit shifting]], all of which are very cheap operations in standard [[computer architecture]]s. It is one of the earliest algorithms developed in the field of [[computer graphics]]. An extension to the original algorithm may be used for drawing circles.

While algorithms such as [[Xiaolin Wu's line algorithm|Wu's algorithm]] are also frequently used in modern computer graphics because they can support [[Spatial anti-aliasing|antialiasing]], the speed and simplicity of Bresenham's line algorithm means that it is still important. The algorithm is used in hardware such as [[plotter]]s and in the [[Graphics processing unit|graphics chips]] of modern [[graphics card]]s. It can also be found in many software [[graphics library|graphics libraries]]. Because the algorithm is very simple, it is often implemented in either the [[firmware]] or the [[graphics hardware]] of modern graphics cards.

The label "Bresenham" is used today for a family of algorithms extending or modifying Bresenham's original algorithm.

==History==
Bresenham's line algorithm is named after [[Jack Elton Bresenham]] who developed it in 1962 at [[International Business Machines|IBM]]. In 2001 Bresenham wrote:<ref name = DADS>Paul E. Black. ''Dictionary of Algorithms and Data Structures,'' [[National Institute of Standards and Technology|NIST]]. http://www.nist.gov/dads/HTML/bresenham.html</ref>
<blockquote>I was working in the computation lab at IBM's San Jose development lab. A [[Calcomp plotter]] had been attached to an [[IBM 1401]] via the 1407 typewriter console. [The algorithm] was in production use by summer 1962, possibly a month or so earlier. Programs in those days were freely exchanged among corporations so Calcomp (Jim Newland and Calvin Hefte) had copies. When I returned to Stanford in Fall 1962, I put a copy in the Stanford comp center library.

A description of the line drawing routine was accepted for presentation at the 1963 [[Association for Computing Machinery|ACM]] national convention in Denver, Colorado. It was a year in which no proceedings were published, only the agenda of speakers and topics in an issue of Communications of the ACM. A person from the IBM Systems Journal asked me after I made my presentation if they could publish the paper. I happily agreed, and they printed it in 1965.</blockquote>

Bresenham's algorithm was later extended to produce circles, the resulting algorithm being sometimes known as either ''Bresenham's circle algorithm'' or [[midpoint circle algorithm]].




# contact

mukesch.shah@uniklinik-freiburg.de
