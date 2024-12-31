''' DO NOT CHANGE THIS FILE'''

class Heading:
    '''
    Instance Attributes:
            order; int; page order
            level; int; heading level 1-6
            text; str; 
    '''
    # HTML tags associated with Headings
    TAGS = ["h1","h2","h3","h4","h5","h6"]
    ELEM_TYPE = "heading"

    def __init__(self, odr, lv, text):
        self.order = odr
        self.level = lv
        self.text=text

    def __str__(self):
        return str(self.order)+" h"+str(self.level)+": "+str(self.text)
    
    def get_table_str(self):
        # return string formatted for AccessHTML table
        text_str = self.text
        if not text_str is None:
            text_str = text_str[:30]
        s = f"| {str(self.order):>10} | {self.ELEM_TYPE:<15} | {str(text_str):<30} |"
        return s
    
    def get_spoken_str(self):
        # return string to be spoken by screen reader
        return self.ELEM_TYPE + " "+str(self.level) + " " + self.text

class Image:
    '''
    Instance Attributes:
            order; int; page order
            src; str; url of image
            alt; str; alternative text for image
    '''

    # Class Attributes / Class Constants
    TAGS = ["img"] #html tags associated with images
    ELEM_TYPE = "image" # string identifying image type
    def __init__(self, odr, source, label):
        ''' 
        Parameters:
            self; instance of Image class
            odr; int; page order
            source; str; url of image 
            label; str; alternative text for image
        '''
        self.order = odr
        self.src = source
        self.alt=label
    
    def get_table_str(self):
        # return string formatted for table for AccessHTML
        alt_str = self.alt
        if not alt_str is None:
            alt_str = alt_str[:30]
        s = f"| {str(self.order):>10} | {self.ELEM_TYPE:<15} | {str(alt_str):<30} |"
        return s

    def __str__(self):
        return str(self.order)+" img: "+str(self.alt)
    
    def get_spoken_str(self):
        # return string formatted for screen reader
        s = self.ELEM_TYPE + " "
        if self.alt == None:
            s+= "Unlabeled"
        else:
            s += self.alt
        return s

class Link:
    '''
    Instance Attributes:
            order; int; page order
            src; str; link url
            text; str; text of link
    '''

    TAGS = ["a"]
    SRC_ATTR = "href"
    ELEM_TYPE = "link"
    def __init__(self, order, source, txt):
        self.src = source
        self.text=txt
        self.order = order
    def __str__(self):
        return str(self.order) + " link: "+str(self.text)

    def get_table_str(self):
        text_str = self.text
        if not text_str is None:
            text_str = text_str[:30]
        s = f"| {str(self.order):>10} | {self.ELEM_TYPE:<15} | {str(text_str):<30} |"
        return s

    def get_spoken_str(self):
        s = self.ELEM_TYPE + " "
        if self.text == None:
            s+= "No text"
        else:
            s += self.text
        return s