#!/usr/bin/env python3
# This class 'shelves' a dictionary of random strings I obtained online while logging each step
# Future implementation can be automation of importing strings via webscraping

import shelve, logging, os

logging.basicConfig(level = logging.DEBUG, format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-8s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(os.getcwd(), os.path.basename(__file__))),
        logging.StreamHandler()
        ])

class bookshelf(object):

    def placeOnShelf(dictionary):    
        """This function serves as a way to shelf a dictionary input to a separate 'database' that serves as a way to maintain object persistence
        for future random text string entries for the typing test"""
        
        shelfFile = shelve.open('randomTextTypingTestShelf', 'c')
        logging.info("Inside placeOnShelf function")
        with shelfFile as randomText:
            randomText['setOne'] = dictionary
            logging.info("Placed on Shelf with this text file name: {}".format(type(shelfFile)))
            logging.info("Shelf contains these keys: {}".format(list(shelfFile.keys())))
       


    #setOne of random text found online. Future implementation would include at least 9 more sets to randomize the cycle of texts to type out
    setOne = {'s1':"""Perhaps far exposed age effects. Now distrusts you her delivered applauded affection out sincerity.
         As tolerably recommend shameless unfeeling he objection consisted. She although cheerful perceive screened
         throwing met not eat distance. Viewing hastily or written dearest elderly up weather it as. So direction so
         sweetness or extremity at daughters. Provided put unpacked now but bringing. """,
    's2' : """New the her nor case that lady paid read. Invitation friendship travelling eat everything the out two. Shy you who scarcely expenses debating hastened resolved. Always polite moment on is warmth spirit it to hearts. Downs those still witty an balls so chief so. Moment an little remain no up lively no. Way brought may off our regular country towards adapted cheered. """,
    's3' : """In up so discovery my middleton eagerness dejection explained. Estimating excellence ye contrasted insensible as. Oh up unsatiable advantages decisively as at interested. Present suppose in esteems in demesne colonel it to. End horrible she landlord screened stanhill. Repeated offended you opinions off dissuade ask packages screened. She alteration everything sympathize impossible his get compliment. Collected few extremity suffering met had sportsman. """,
    's4' : """Him boisterous invitation dispatched had connection inhabiting projection. By mutual an mr danger garret edward an. Diverted as strictly exertion addition no disposal by stanhill. This call wife do so sigh no gate felt. You and abode spite order get. Procuring far belonging our ourselves and certainly own perpetual continual. It elsewhere of sometimes or my certainty. Lain no as five or at high. Everything travelling set how law literature. """,
    's5' : """Dependent certainty off discovery him his tolerably offending. Ham for attention remainder sometimes additions recommend fat our. Direction has strangers now believing. Respect enjoyed gay far exposed parlors towards. Enjoyment use tolerably dependent listening men. No peculiar in handsome together unlocked do by. Article concern joy anxious did picture sir her. Although desirous not recurred disposed off shy you numerous securing. """,
    's6' : """Unpacked reserved sir offering bed judgment may and quitting speaking. Is do be improved raptures offering required in replying raillery. Stairs ladies friend by in mutual an no. Mr hence chief he cause. Whole no doors on hoped. Mile tell if help they ye full name. """,
    's7' : """Over fact all son tell this any his. No insisted confined of weddings to returned to debating rendered. Keeps order fully so do party means young. Table nay him jokes quick. In felicity up to graceful mistaken horrible consider. Abode never think to at. So additions necessary concluded it happiness do on certainly propriety. On in green taken do offer witty of. """,
    's8' : """Luckily friends do ashamed to do suppose. Tried meant mr smile so. Exquisite behaviour as to middleton perfectly. Chicken no wishing waiting am. Say concerns dwelling graceful six humoured. Whether mr up savings talking an. Active mutual nor father mother exeter change six did all. """,
    's9' : """You vexed shy mirth now noise. Talked him people valley add use her depend letter. Allowance too applauded now way something recommend. Mrs age men and trees jokes fancy. Gay pretended engrossed eagerness continued ten. Admitting day him contained unfeeling attention mrs out. """,
    's10': """Its had resolving otherwise she contented therefore. Afford relied warmth out sir hearts sister use garden. Men day warmth formed admire former simple. Humanity declared vicinity continue supplied no an. He hastened am no property exercise of. Dissimilar comparison no terminated devonshire no literature on. Say most yet head room such just easy. """
    }
    
    placeOnShelf(setOne)
    logging.info("Executing placeOnShelf function on first set of random strings")
    logging.info("Program Terminated")