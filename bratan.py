import webbrowser

def open_url(url):
    webbrowser.open(url)


pelmen = input('вы любите хабиба').lower()
if pelmen == 'да':
    open_url("https://scontent.ffru1-4.fna.fbcdn.net/v/t1.6435-9/43405780_2091235000907539_4200379450283524096_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=9eae26&_nc_ohc=GVtqVwbr2R0Q7kNvwFBkoiC&_nc_oc=AdmZ8weCkFzRZTNDxNv2KsXcaRA070b8fzPIqQoH48dnyq_ABkzdtjvx2hJl6c7Pm-E&_nc_zt=23&_nc_ht=scontent.ffru1-4.fna&_nc_gid=JGYfdIAIhVMXCfu3uo2-Ew&oh=00_AfYSJpf5Vc92tUG04erVKxmZA3GeEwQl58wBdY79YYw3Pw&oe=68F70C06")
else:
    open_url('https://masterpiecer-images.s3.yandex.net/a202e9866e5b11eebd65b646b2a0ffc1:upscaled')