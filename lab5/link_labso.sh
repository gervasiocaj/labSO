GERVA=~/workspace/labSO/lab5
MANEL=~/workspace/manel-labso/lab5/python

rm -f $MANEL/phymem.py.bak
mv    $MANEL/phymem.py          $MANEL/phymem.py.bak

ln -s $GERVA/fifo.py            $MANEL
ln -s $GERVA/second_chance.py   $MANEL
ln -s $GERVA/nru.py             $MANEL
ln -s $GERVA/aging.py           $MANEL
ln -s $GERVA/main.py            $MANEL/phymem.py
