from PIL import Image, ImageFilter

def applyFilter(background):

    # For background wallpaper
    filter_ = Image.open('src/filter.png')
    background_image = Image.open(background)
    filtered = Image.blend(background_image, filter_, 0.6)

    filtered.save('filtered.png')

    # For lockscreen
    filter_ = Image.open('src/lock-filter.png')
    filtered = filtered.filter(ImageFilter.GaussianBlur(radius=10))
    filtered.paste(filter_, (0,0), filter_)

    filtered.save('filtered-lock.png')