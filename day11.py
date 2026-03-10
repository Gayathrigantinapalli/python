# class markapuram:
#     def __init__(self,chicken,mutton):
#         self.chicken=chicken
#         self.mutton=mutton
#     def chickenfry(self):
#         print(F"I CAN MAKE CHICKENFRY USING{self.chicken}")
#     def muttoncurry(self):
#         print(f"I AM PREPARE FOR MUTTONCURRY USING{self.mutton}")
# class chirrikurapadu(markapuram):
#     def __init__(self, chicken, mutton,curd):
#          super().__init__(chicken, mutton,)
#          self.curd=curd
#     def curdrice(self):
#         print(f"I MAKE A CURDRICE USING{self.curd}")
# class khambam(chirrikurapadu):
#     def __init__(self,chicken,mutton,curd,milk):
#         super().__init__(chicken, mutton,curd) 
#         self.milk=milk
#     def palakova(self):
#         print(f"i can make palakova using{self.milk}")
# a=khambam("chicken","mutton","curd","milk") 
# a.chickenfry()
# a.muttoncurry()
# a.curdrice()
# a.palakova()




# class tangutur:
#     def __init__(self,rice):
#         self.rice=rice
#     def biriyani(self):
#         print(f"i am prepare for a biriyani{self.rice}")
# class chirrikurapadu(tangutur):
#     def __init__(self, rice,greendol):
#         super().__init__(rice)
#         self.greendol=greendol
#     def pappu(self):
#         print(f"i am making a pappu{self.greendol}")
# class kanigiri(chirrikurapadu):
#     def __init__(self, rice, greendol,mushroom):
#         super().__init__(rice, greendol)
#         self.mushroom=mushroom
#     def vegbiriyani(self):
#         print("vegbiriyani is completed")
# class thirupathi(kanigiri):
#     def __init__(self, rice, greendol, mushroom,jagerry):
#         super().__init__(rice, greendol, mushroom)
#         self.jagerry=jagerry
#     def laddu(self):
#         print(f"this is making a laddu{self.jagerry}")
# a=thirupathi("rice","greendol"," mushroom","jagerry")
# a.biriyani()
# a.pappu()
# a.vegbiriyani()
# a.laddu()



# class tangutur:
#     def __init__(self,chicken):
#         self.chicken=chicken
#     def legpiece(self):
#         print(f"i am making a legpiece biriyani and{self.chicken}")
# class kandukuru(tangutur):
#     def __init__(self, chicken,fish):
#         super().__init__(chicken)
#         self.fish=fish
#     def fishfry(self):
#         print(f"you eat fishfry{self.fish}")
# class singarayakonda(tangutur):
#     def __init__(self,chicken,mutton):
#         super().__init__(chicken)
#         self.mutton=mutton
#     def muttonkima(self):
#         print(f"muttonkima is very nice and{self.mutton}")
# a=singarayakonda("chicken lollypop ","mutton fry")
# a.legpiece()
# a.muttonkima() 
        


# class chirrikurapadu:
#     def __init__(self,milk,curd)
#         self.milk=milk
#         self.curd=curd
#     def milk(self):
#         print(f"i like milk{self.milk}")
#     def curd(self):
#         print(f"i eat curd{self.curd}")
# class kandukuru(chirrikurapadu):
#     def __init__(self,milk,curd,fruits)
#         super("")




# class america:
#     def __init__(self,dosa,biriyani):
#         self.dosa=dosa
#         self.biriyani=biriyani
#     def tiffin(self):
#         print("i eat dosa in morning")
#     def lunch(self):
#         print("i like biriyani")
# class chirrikurapadu(america):
#     def __init__(self,dosa,biriyani,chapathi):
#         super().__init__(dosa,biriyani)
#         self.chapathi=chapathi
#     def dinner(self):
#         print("i am making a chapathi") 
# class tangutur(america):
#     def __init__(self,dosa,biriyani,chapathi,pulav):
#         super().__init__(dosa,biriyani)
#         self.pulav=pulav
#     def snacks(self):
#         print("that is a vegpulav")
# a=tangutur("dosa"," biriyani","chapathi","pulav")
# a.tiffin()
# a.lunch()
# a.snacks()