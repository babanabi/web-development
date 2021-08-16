class convert:

    def fah_to_cel(self,n):
        f = float(n)
        c = (f - 32) * 5/9
        return round(c,1)

    def cel_to_fah(self,n):
        c = float(n)
        f = (c * 9/5) + 32
        return round(f,1)
