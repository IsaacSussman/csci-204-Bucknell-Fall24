# student submission
from bs4 import BeautifulSoup
from elements import *
import json
from helper import parse_html_string_to_dict

# name: 
class AccessHTML:
    '''
    Attributes:
        elements: list of Heading, Link, and/or Image objects
        num_elements: int
    '''
 
    def __init__(self, html_file):
        ### DO NOT CHANGE THIS METHOD ###
        '''
        Parameters:
            self; instance of AccessHTML
            html_file; string, file path to .html file
        '''

        html_string = ''
        # read all of html file into string 
        with open(html_file, "r") as f:
            html_string = f.read()
        # parse html string into dictionary
        soup = BeautifulSoup(html_string, 'html.parser')
        html_dict = parse_html_string_to_dict(soup)
        
        # save html dictionary to file for easier viewing
        with open(html_file[:-5]+".json", "w") as json_file:
            json_file.write(json.dumps(html_dict,indent=2))

        # define attributes
        self.elements = []
        self.num_elements = 0
        # parse the dictionary to fill self.elements
        self.parse_site(html_dict)

    def parse_site(self, html_element_dict):
        '''
        Parses a dictionary created from an HTML file into a list of 
        Heading, Image, and Link objects. Saves this list to self.elements.

        Parameters:
            html_element_dict; dictionary, of the form presented in the write-up
        Return: none
        '''
        # get the tag from the base dictionary object
        tag = html_element_dict['tag']

        # check if it is a tag of interest
        # use self.num_elements to capture the order of elements on the page
        if tag in Heading.TAGS:
            # check if the Heading hastext
            txt = None
            if 'text' in html_element_dict['attributes'].keys(): 
                txt = html_element_dict['attributes']['text']
            # create new Heading object
            self.elements.append(Heading(self.num_elements,
                                            int(html_element_dict['tag'][-1]), 
                                            txt))
            # increment the number of elements
            self.num_elements += 1

        elif tag in Image.TAGS:
            '''TODO: complete'''
            # if an Image
            # if it has an alt attribute, use that value, otherwise alt is None
            if "alt" in html_element_dict["attributes"].keys():
                alt = html_element_dict["attributes"]["alt"]
            else:
                alt = None
            src_img = html_element_dict["attributes"]["src"]
            i = Image(self.num_elements, src_img, alt)
            self.elements.append(i)
            # get the image source from the 'src' attribute key
            # create an Image object using alt and src, use num_elements as its order 
            # append it to self.elements
            # increment the number of elements
            self.num_elements+=1
            pass

        # if the tag is in Link's TAGs
        elif tag in Link.TAGS:
            ''' TODO: complete'''
            # get the src from the html_element_dict attributes
            src = html_element_dict["attributes"]["href"]
            # get the text from the html_element_dict attributes
            t = html_element_dict["attributes"]["text"]
            # create a new Link object, using num_elements as its order
            l = Link(self.num_elements, src, t)
            self.elements.append(l)
            # increment num_elements by 1
            self.num_elements+=1
            pass

        '''!!! START HERE !!!!'''
        ''' TODO: complete the recursive call'''
        # Recursively search through child tags
        if "children" in html_element_dict.keys():
            for i in html_element_dict["children"]:
                self.parse_site(i)
            # for every child dictionary in the children list
            # call parse site, passing in the child dictionary
        

    def __str__(self):

        ''' DO NOT CHANGE'''
        header = f"| {'Page Order':<10} | {'Element Type':<15} | {'Text or Alt':<30} |\n"

        s=header
        s += "-"*len(header)+'\n'
        for element in self.elements:
            s+=element.get_table_str()
            s+='\n'
        return s
    
    def get_elements(self, elem_type):
        ''' DO NOT CHANGE'''
        # sort by element type
        self.sort_by("TYPE")

        # use binary search to search for starting and ending index        
        start_idx = self._find_idx(elem_type,"FIRST")        
        stop_idx_inc = self._find_idx(elem_type, "LAST")
        # return sublist
        return self.elements[start_idx:stop_idx_inc+1]
    
     
    def _find_idx(self, elem_type, loc = "FIRST"):
        '''
        Find FIRST or LAST index in elements 
        for elements of a given type
        
        Prerequisite: self.elements must be sorted by TYPE before calling
        
        Parameters:
            self; AccessHTML object. self.elements must be sorted by TYPE
            elem_type; string; must the element type of objects in elements
            loc; string. "FIRST" to return index of first instance, 
                        "LAST" to return index of last instance
        Return;
            int; index of first or last element of elem_type in self.elements. 
                return -1 if no elements of elem_type in self.elements
        '''

        # TODO: Implement using BINARY SEARCH
        if len(self.elements) == 0: return -1
        low = 0
        high = len(self.elements)
        mid=0
        while self.elements[mid].ELEM_TYPE != elem_type and high >= low:
            mid = low + (high-low)//2
            if not self.elements[mid].ELEM_TYPE > elem_type:
                low = mid+1
            else:
                high = mid-1
        if self.elements[mid].ELEM_TYPE == elem_type:
            if loc == "FIRST":
                if mid != 0:
                    while mid != 0 and self.elements[mid-1].ELEM_TYPE == elem_type:
                        mid-=1
                return mid
            elif loc=="LAST":
                if mid != len(self.elements)-1:
                    while mid != len(self.elements)-1 and self.elements[mid+1].ELEM_TYPE == elem_type:
                        mid+=1
                return mid
        else:
            return -1
            
    
    def sort_by(self, sort_by="TYPE"):
        '''
        Sorts self.elements based on given criteria.
        "TYPE" is a 2-level sort. It will sort by type, alphabetically, then by page order
        So all elements of a single type will be together in the list and ordered.
        "PAGE_ORDER" is a single-level sort. It will sort all types of elements by page order alone

        Parameter:
            self; AccessHTML object whose elements are being sorted
            sort_by: string. sorting technique used. must be "TYPE" or "PAGE_ORDER"
        Return:
            No return.
        '''
        # it must first sort by elements, then ensure those elements are in page order
        # see project instructions for an example
        if sort_by == "TYPE": 
            # TODO: Implement using INSERTION SORT
            for i in range(len(self.elements)):
                x=i
                for j in range(i-1,-1,-1):
                    if self.elements[x].ELEM_TYPE<self.elements[j].ELEM_TYPE or (self.elements[x].ELEM_TYPE==self.elements[j].ELEM_TYPE and self.elements[x].order<self.elements[j].order):
                        temp=self.elements[x]
                        self.elements[x]=self.elements[j]
                        self.elements[j]=temp
                        x=j
                    else:
                        break            
        
        elif sort_by=="PAGE_ORDER":
            # TODO implement using Merge Sort
            a = self.merge_sort(self.elements)
            self.elements = a
 
    def merge_sort(self, arr):
      """! Perform merge sort to sort the input array of integers."""
      ### Implement the algorithm below
      # Feel free to add any helper functions as needed
      # Note that: array MUST BE sorted by the end of this function!
      """ PSEUDOCODE:
            if array length <= 1: return array
            else:
            middle = you calculate it
            # Warning: unlike Python lists, 
            # Array does not allow slicing.
            left array = copy array[0:middle]
            right array = copy array[middle+1:end]
            left array = mergesort(left array)
            right array = mergesort(right array)
            merge(array, left array, right array)
            return array
      """
      if len(arr)<= 1:
            return arr
            
      else:
            #mid = (len(array)-1)//2
            left = []
            right = []
            for i in range(len(arr)//2):
                  left.insert(i, arr[i])
            for i in range(len(arr)-(len(left))):
                   right.insert(i, arr[len(left)+i])

            left = self.merge_sort(left)
            right = self.merge_sort(right)

            a = self.merge(arr, left, right)

            return a

    def merge(self, array, left, right):
      ### Implement the algorithm below
      # Feel free to add any helper functions as needed
      # Note that: array MUST CONTAIN the merged array! This function DOES NOT return anything.
      """ PSEUDOCODE:
            # overwrite array while merging
            li = ri = ai = 0
            while both lists have contents
                  if left[li] < right[ri]:
                        array[ai] = left[li]
                        li += 1
                  else:
                        array[ai] = right[ri]
                        ri += 1
                  ai += 1

            while left has contents
            array[ai] = left[li]
            li += 1
            ai += 1

            while right has contents
            array[ai] = right[ri]
            ri += 1
            ai += 1
      """
      li = 0
      ri = 0 
      ai = 0
      while li< len(left) and ri < len(right):
            if left[li].order < right[ri].order:
                  array[ai] = left[li]
                  li +=1
            else:
                  array[ai] = right[ri]
                  ri += 1
            ai+=1
            
      while li < len(left):
            array[ai] = left[li]
            li += 1
            ai += 1

      while ri < len(right):
            array[ai] = right[ri]
            ri += 1
            ai += 1
      return array


    

if __name__ == "__main__":
    print("hi")
    site_file = "partialwebsite.html"
    p = AccessHTML(site_file)
    p.sort_by("TYPE")
    p.sort_by("PAGE_ORDER")
    print(p)

    ## ADD MORE TEST CODE HERE
    
    
    
