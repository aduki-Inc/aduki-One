class stime:
    def __init__(self, h, m):
        self.h = h
        self.m = m
        self.add = h + 1

        if self.h > 12:
            self.nh = h - 12
        else:
            self.nh = h

    def time(self):

        time = str(self.nh) + ":" + str(self.m)

        if self.h == 12 and self.m == 0:
            tme = "It's 12 Noon"
        elif self.h >= 12:
            if self.m == 45:

                if self.add == 24:
                    tme = "It's a quater to Midnight"
                else:
                    tme = "It's a quater to " + str(self.nh + 1) + " PM"

            elif m == 15:
                tme = "It's a quater past " + str(self.nh) + " PM"
            elif m == 30:
                tme = "It's half past " + str(self.nh) + " PM"
            else:
                tme = "The time is " + time + " PM"

        elif self.h < 12:
            if self.m == 45:

                if self.add == 12:
                    tme = "It's a quater to Noon"
                else:
                    tme = "It's a quater to " + str(self.nh + 1) + " AM"

            elif m == 15:
                tme = "It's a quater past " + str(self.nh) + " AM"

            elif m == 30:
                tme = "It's half past " + str(self.nh) + " AM"

            else:
                tme = "The time is " + time + " AM"

        return tme
#BY Fredrick Femar Ochieng
