import os

class TextRepeater:
    """
    Parameters:
    -----------
    format_options
        Expected Type: iterable of string tuples
        format_options is an iterable of string tuples. This is iterated over, and each tuple is passed to the format()
        function on the section_body,

    header
        Expected Type: string
        The header is an optional string that is added to the beginning of the output. A single new line is added after
        the header.

    section_header
        Expected Type: string
        The section_header is an optional string that is added to the beginning of each section. A single new line is
        added after the section_header.

    section_body 
        Expected Type: string
        The section_body, as the name implies, is the text block that is repeated in each iteration. Curly brace
        formatting syntax is supported (see format_options below).

    section_footer
        Expected Type: string
        The section_footer is an optional string that is added to the end of each section. A single new line is added
        before the section_header.

    footer
        Expected Type: string
        The header is an optional string that is added to the end of the output. A single new line is added before the
        footer.

    indentation
        Expected Type: int
        The indentation is used to add whitespace before the section_body, section_header, and section_footer strings.
        Specifically, a number of spaces equal to the integer is added to the beginning of these strings. Currently,
        it does not indent inside a multi-line string, which results in only the first line having the desired
        indentation. This is on the backlog. To add indentation in multiline strings, either add it directly in the
        input, or as an item in format_options.
    
    separator
        This string value is added between each element (i.e. section_header, footer, section_body, etc.).
    """
    def __init__(self, 
                format_options=[], 
                header='', 
                section_header='', 
                section_body='', 
                section_footer='', 
                footer='', 
                indentation=0,
                separator='\n'):
        # Set attributes by input
        self.format_options = format_options
        self.header = header
        self.section_header = section_header
        self.section_body = section_body
        self.section_footer = section_footer
        self.footer = footer
        self.indentation = indentation
        self.separator = separator
        
        # Initialize dynamic attributes
        self.text = ''
    
    ## Setters ##
    def set_section_body(self, section_body):
        self.section_body = section_body
        return True

    def set_format_options(self, format_options):
        self.format_options = format_options
        return True

    def set_section_header(self, section_header):
        self.section_header = section_header
        return True

    def set_section_footer(self, section_footer):
        self.section_footer = section_footer
        return True

    def set_header(self, header):
        self.header = header
        return True

    def set_footer(self, footer):
        self.footer = footer
        return True

    ## Getters ##
    def get_section_body(self):
        return self.section_body

    def get_format_options(self):
        return self.format_options

    def get_section_header(self):
        return self.section_header

    def get_section_footer(self):
        return self.section_footer

    def get_header(self):
        return self.header

    def get_footer(self):
        return self.footer
    
    def get_text(self):
        return self.text
    
    ## Behavior ##
    def build_section(self, fopt):
        return self.section_header + self.section_body.format(fopt) + self.section_footer
    
    def build_text(self):
        # This list will be .join()ed into a string later with self.separator
        text_list = []
        # Add the header at the beginning of the list
        if self.header:
            text_list.append(self.header)
        # Iterate over the format options, building a section for each
        for opts in self.format_options:
            # Only add the section header if it exists
            if self.section_header:
                text_list.append(self.section_header)
            # Only add the section body if it exists  
            if self.section_body:
                text_list.append(self.section_body.format(*opts))
            # Only add the section footer if it exists    
            if self.section_footer:
                text_list.append(self.section_footer)
        # Add the footer at the end of the list
        if self.footer:
            text_list.append(self.footer)
        # Check if anything was added
        if text_list:
            # Update text attribute with built text
            self.text = self.separator.join(text_list)
            # If it makes it here, indicate success
            return True
        else:
            # Nothing was added. Indicate failure
            return False
    
    def to_file(self, file_name):
        """
        Writes the text attribute to the current working directory using provided file name.
        """
        file_path = os.path.join(os.path.curdir, file_name)
        with open(file_path, 'w') as f:
            f.write(self.text)
        print('Output written to', file_path)
        return True
    
    def __repr__(self):
        return repr(self.__dict__)
  
    def __str__(self):
        """
        Returns the built text
        """
        # return '%s + i%s' % (self.real, self.imag)
        return self.text


if __name__ == '__main__':
    import inspect
    repeater = TextRepeater()
    
    for i in inspect.getmembers(repeater, inspect.ismethod):
        print(i)