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
    
    def set_format_options_from_list(self, format_options):
        self.format_options = [(x,) for x in format_options]
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
    
    def set_indentation(self, indentation):
        self.indentation = indentation
        return True

    def set_separator(self, separator):
        self.separator = separator
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
    
    def get_indentation(self):
        return self.indentation

    def get_separator(self):
        return self.separator
    
    def get_text(self):
        return self.text
    
    ## Behavior ##
    def build_section(self, fopt):
        section_list = []
        # Only add the section header if it exists
        if self.section_header:
            section_header = self.section_header.format(*fopt)
            section_list.append(section_header)
        # Only add the section body if it exists  
        if self.section_body:
            section_body = self.section_body.format(*fopt)
            section_list.append(section_body)
        # Only add the section footer if it exists    
        if self.section_footer:
            section_footer = self.section_footer.format(*fopt)
            section_list.append(section_footer)
        if section_list:
            section = '\n'.join(section_list)
            return self.indent(section)
        else:
            return ''
    
    def indent(self, s):
        return ' '*self.indentation + s.replace('\n', '\n'+' '*self.indentation)
    
    def build_text(self):
        # This list will be .join()ed into a string later with self.separator
        text_list = []
        # Add the header at the beginning of the list
        if self.header:
            text_list.append(self.header)
        # Iterate over the format options, building a section for each
        for opts in self.format_options:
            section = self.build_section(opts)
            if section:
                text_list.append(section)
        # Add the footer at the end of the list
        if self.footer:
            text_list.append(self.footer)
        # Check if anything was added
        if text_list:
            # Update text attribute with built text
            self.text = self.separator.join(text_list)
            # text = self.separator.join(text_list)
            # self.text = text.replace('\n', '\n'+' '*self.indentation)
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
        return self.text


if __name__ == '__main__':
    ## Tests ##
    repeater = TextRepeater()

    # format_options = [('format_options'.upper(),) for i in range(10)]
    format_options = [(str(i),) for i in range(10)]
    header = 'header'.upper()+'\n'+'-'*80
    section_header = 'section_header {}'.upper()
    section_body = 'section_body {}'.upper()
    section_footer = 'section_footer {}'.upper()
    footer = '-'*80+'\n'+'footer'.upper()
    indentation = 4
    separator = '\n'

    repeater.set_format_options(format_options)
    repeater.set_header(header)
    repeater.set_section_header(section_header)
    repeater.set_section_body(section_body)
    repeater.set_section_footer(section_footer)
    repeater.set_footer(footer)
    repeater.set_indentation(indentation)
    repeater.set_separator(separator)
    
    repeater.build_text()
    
    print(repeater)