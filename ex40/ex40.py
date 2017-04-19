class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
        print '\n'
    
    def number_of_lines(self):
        print len(self.lyrics)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

dna_lyrics = ["I got, I got, I got, I got",
              "Loyalty, got royalty inside my DNA"]

dna = Song(dna_lyrics)

dna.sing_me_a_song()
dna.number_of_lines()