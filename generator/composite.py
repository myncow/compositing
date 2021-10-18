from wand.image import Image

def composite(filenames,count):
    with Image(filename=filenames[0]) as l1:
        with Image(filename=filenames[1]) as l2:
            with Image(filename=filenames[2]) as l3:
                with Image(filename=filenames[3]) as l4:
                        with Image(filename=filenames[4]) as l5:
                            with Image(filename=filenames[5]) as l6:
                                with Image(filename=filenames[6]) as l7:
                                    with Image(filename=filenames[7]) as l8:
                                        with Image(filename=filenames[8]) as l9:
                                            l1.composite(l2)
                                            l1.composite(l3)
                                            l1.composite(l4)
                                            l1.composite(l5)
                                            l1.composite(l6)
                                            l1.composite(l7)
                                            l1.composite(l8)
                                            l1.composite(l9)
                                            l1.save(filename=f'output/img/{count}.png')

def pil_composite(filenames,j):
    n=len(filenames)
    img=PImage.open(filenames[0]).convert('RGBA')
    for i in range(1,n):
        new_img=PImage.open(filenames[i]).convert('RGBA')
        img.alpha_composite(new_img,(0,0),(0,0))

    img.save(f"quality_test/pillow_{j}.png")





  