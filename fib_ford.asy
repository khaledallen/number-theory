size(400);
draw( (0.9,0) -- (2.1,0), arrow=Arrows());
real i;
for (i = 1; i <= 2; i = i + 0.125) {
    Label iLabel;
    if ( i == 1 ) 
        iLabel = Label( '1', position=S);
    else if ( i == 2)
        iLabel = Label( '2', position=S);
    else 
        iLabel = "";
    draw( (i,-0.02) -- (i, 0.02), L=iLabel);
}

draw( arc((1,1/2), 1/2, -90, 0));
draw( arc((2,1/2), 1/2, -90, -180));
draw( circle((3/2,1/8), 1/8));
draw( circle((5/3,1/18), 1/18));
draw( circle((8/5,.5*1/25), .5*1/25));
draw( circle((13/8,.5*1/64), .5*1/64));
draw( circle((21/13,.5*1/(13*13)), .5*1/(13*13)));
label("$\frac{1}{1}$", (1.125,1/4));
label("$\frac{1}{2}$", (2-.125,1/4));
label("$\frac{3}{2}$", (3/2,1/8));
label("$\frac{5}{3}$", (5/3,1/18));
