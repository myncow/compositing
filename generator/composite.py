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












  