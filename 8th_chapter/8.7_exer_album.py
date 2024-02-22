def make_album(singer, album_name, amount_waves=None):
    if amount_waves:
        album = {'singer_name': singer.title(), 'album_name': album_name.title(), 'amount_waves': amount_waves}
    else:
        album = {'singer_name': singer.title(), 'album_name': album_name.title()}
    return album

while True:
    singer = input('Please enter singer name \n (print "q" to quit) \n')
    if singer == 'q':
        break
    else:
        album_name = input('Please enter album name \n (print "q" to quit) \n')
        if album_name == 'q':
            break
        else:
            amount_waves = input('Please enter amount waves or press enter to skip \n (print "q" to quit) \n')
            if amount_waves == 'q':
                break
            else:
                print(make_album(singer, album_name, amount_waves))
