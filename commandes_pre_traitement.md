# Pré-traitement
- découpage d'un PDF en plusieurs images PNG avec **ghostcript**
`gs  -sDEVICE=png16m  -dNOPAUSE -dBATCH -dSAFER -dFirstPage=1  -dLastPage=30  -dJPEGQ=100 -r500 -sOutputFile=output%03d.png input.pdf`

- mettre en noir et blanc un batch d'images
`for i in $(seq 1 531); do mogrify -colorspace Gray output$i.png; done`

- augmentation du contraste et de la luminosité d'un batch d'images
`for i in $(seq 1 531); do mogrify -brightness-contrast 10x40 output$i.png; done`
