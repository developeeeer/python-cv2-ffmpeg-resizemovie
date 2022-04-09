from resize import resize, resizes

if __name__ == '__main__':
    mode = input("resize or resizes : ")
    if mode == "resize":
        filename = input("filename : files/")
        is_audio = input("is_audio [Y/n] : ")
        resize(
            None if filename == "" else fr"files/{filename}",
            True if is_audio == "" or is_audio == "y" or is_audio == "Y" else False)
    elif mode == "resizes":
        filenames = input("filenames(xxx,yyy) : ")
        is_audio = input("is_audio [Y/n] : ")
        resizes(
            None if len(filenames) < 1 else filenames.split(","),
            True if is_audio == "" or is_audio == "y" or is_audio == "Y" else False
        )
    else:
        print("resizeまたはresizesを指定してください")


