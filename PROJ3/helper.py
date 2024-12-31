from elements import Link, Heading, Image

''' DO NOT CHANGE THIS FILE'''

def get_text(element_dict):
    if 'text' in element_dict['attributes']:
        return element_dict['attributes']['text']
    if 'alt' in element_dict['attributes'] and element_dict['attributes']['alt'] != None :
        return element_dict['attributes']['alt']
    if 'children' in element_dict.keys():
        for child in element_dict['children']:
            return get_text(child)

    return None

def parse_html_string_to_dict(element):
    # Base dictionary with the element name and its attributes
    node = {"tag": element.name}
    #print("ELEMENT CONTENTS:\n",element.contents)
    if element.attrs:
        node["attributes"] = element.attrs
    
    # If there are children, process them recursively
    children = []
    for child in element.children:
        if child.name is not None:  # If it's a tag
            children.append(parse_html_string_to_dict(child))
        elif child.strip():  # If it's a string (text node), include it if non-empty
            if 'attributes' not in node.keys():
                node["attributes"] = {}    
            #print(child)
            node["attributes"]['text']= child.strip()
    
    if children:
        node["children"] = children

    # if inherits text from decendents
    text_tags = Heading.TAGS + Link.TAGS
    if node["tag"] in text_tags and 'text' not in node['attributes'].keys():
        node['attributes']['text'] = get_text(node)
    
    return node


