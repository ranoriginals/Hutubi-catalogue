PS=2010-2012.ps
R=0.5/37.5/0/60
J=X12.95c/6c

gmt set FORMAT_DATE_MAP=-o FONT_ANNOT_PRIMARY +9p
gmt psxy -R$R -J$J -T -P -K > $PS

year=2010
filename=./${year}/fre_10_day_${year}.txt
cat $filename | gmt psxy -R$R -J$J -By20+l'Number' -BWen+t${year} -Sb0.35c -W0.5p,black -Ggray -K -O >> $PS
gmt psxy -R -J -A -W0.5p,- -D0.175c/0c -K -O >> $PS << EOF
12 0 
12 60
EOF
gmt psxy -R -J -A -W0.5p,- -D0.175c/0c -K -O >> $PS << EOF
28 0 
28 60
EOF
echo 2 55 | gmt psxy -R -J -Sa0.5c -Gblack -K -O >> $PS
echo 2.5 55 | gmt psxy -R -J -Sa0.5c -Gblack -K -O >> $PS
gmt psbasemap -R0.5/12.5/0/60 -J$J -Bxa1+l"Month" -BS -K -O >> $PS

year=2011
filename=./${year}/fre_10_day_${year}.txt
cat $filename | gmt psxy -R$R -J$J -By20+l'Number' -BWen+t${year} -Sb0.35c -W0.5p,black -Ggray -Y9c -K -O >> $PS
gmt psxy -R -J -A -W0.5p,- -D0.175c/0c -K -O >> $PS << EOF
12 0 
12 60
EOF
gmt psxy -R -J -A -W0.5p,- -D0.175c/0c -K -O >> $PS << EOF
28 0 
28 60
EOF
echo 7 55 | gmt psxy -R -J -Sa0.5c -Gblack -K -O >> $PS
gmt psbasemap -R0.5/12.5/0/60 -J$J -Bxa1+l"Month" -BS -K -O >> $PS

year=2012
filename=./${year}/fre_10_day_${year}.txt
cat $filename | gmt psxy -R$R -J$J -By20+l'Number' -BWen+t${year} -Sb0.35c -W0.5p,black -Ggray -Y9c -K -O >> $PS
gmt psxy -R -J -A -W0.5p,- -D0.175c/0c -K -O >> $PS << EOF
12 0 
12 60
EOF
gmt psxy -R -J -A -W0.5p,- -D0.175c/0c -K -O >> $PS << EOF
28 0 
28 60
EOF
echo 30 55 | gmt psxy -R -J -Sa0.5c -Gblack -K -O >> $PS
echo 30.5 55 | gmt psxy -R -J -Sa0.5c -Gblack -K -O >> $PS
echo 12 55 | gmt psxy -R -J -Sa0.5c -Gblack -K -O >> $PS
gmt psbasemap -R0.5/12.5/0/60 -J$J -Bxa1+l"Month" -BS -K -O >> $PS

gmt psxy -R -J -T  -O >> $PS 

rm gmt.*
gmt psconvert -A2c -Tf $PS
open 2010-2012.pdf
