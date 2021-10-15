from wand.image import Image
from PIL import Image as PImage

def wand_composite(filenames,i):
    with Image(filename=filenames[0]) as l1:
        with Image(filename=filenames[1]) as l2:
            with Image(filename=filenames[2]) as l3:
                with Image(filename=filenames[3]) as l4:
                        with Image(filename=filenames[4]) as l5:
                            with Image(filename=filenames[5]) as l6:
                                with Image(filename=filenames[6]) as l7:
                                    l1.composite(l2)
                                    l1.composite(l3)
                                    l1.composite(l4)
                                    l1.composite(l5)
                                    l1.composite(l6)
                                    l1.composite(l7)
                                    l1.save(filename=f'quality_test/wand_{i}.png')

def pil_composite(filenames,j):
    n=len(filenames)
    img=PImage.open(filenames[0]).convert('RGBA')
    for i in range(1,n):
        new_img=PImage.open(filenames[i]).convert('RGBA')
        img.alpha_composite(new_img,(0,0),(0,0))

    img.save(f"quality_test/pillow_{j}.png")

fn_arr=[['layers/layer_1/bg_1.png', 'layers/layer_2/mg_5.png', 'layers/layer_3/f_1.png', 'layers/layer_4/ac_2.png', 'layers/layer_5/r_2.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_7.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_5.png', 'layers/layer_2/mg_2.png', 'layers/layer_3/f_1.png', 'layers/layer_4/ac_2.png', 'layers/layer_5/r_2.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_4.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_1.png', 'layers/layer_2/mg_6.png', 'layers/layer_3/f_3.png', 'layers/layer_4/ac_2.png', 'layers/layer_5/r_8.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_1.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_3.png', 'layers/layer_2/mg_4.png', 'layers/layer_3/f_1.png', 'layers/layer_4/ac_3.png', 'layers/layer_5/r_11.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_7.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_4.png', 'layers/layer_2/mg_3.png', 'layers/layer_3/f_2.png', 'layers/layer_4/ac_3.png', 'layers/layer_5/r_10.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_2.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_5.png', 'layers/layer_2/mg_4.png', 'layers/layer_3/f_1.png', 'layers/layer_4/ac_4.png', 'layers/layer_5/r_4.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_7.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_5.png', 'layers/layer_2/mg_5.png', 'layers/layer_3/f_3.png', 'layers/layer_4/ac_1.png', 'layers/layer_5/r_2.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_3.png', 'layers/layer_8/fg_2.png'],
['layers/layer_1/bg_1.png', 'layers/layer_2/mg_1.png', 'layers/layer_3/f_2.png', 'layers/layer_4/ac_2.png', 'layers/layer_5/r_2.png', 'layers/layer_6/f_4.png', 'layers/layer_7/c_4.png', 'layers/layer_8/fg_2.png']]

for i,filenames in enumerate(fn_arr):
    wand_composite(filenames,i)

print(fn_arr)
for i,filenames in enumerate(fn_arr):
    pil_composite(filenames,i)

    
