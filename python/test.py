from TextRepeater import TextRepeater

if __name__ == '__main__':
    """
    This isn't the best way to actually use this class. This is for testing, not an example of proper use.
    """
    items = ['format_options'
            ,'indentation'
            ,'header'
            ,'format_options'
            ,'section_header'
            ,'section_body'
            ,'section_footer'
            ,'footer'
            ,'text']

    repeater = TextRepeater()
    
    body = 'def {0}{1}(self, {1}):\n    self.{1} = {1}\n    return True\n'
    # body = 'def {0}{1}(self, {1}):\n    return self.{1}\n'
    
    format_options = [('set_',x) for x in items]
    for i in format_options:
        print(i)
    
    # Set repeater attributes
    repeater.set_format_options(format_options)

    repeater.set_header('## Setters ##')
    
    repeater.set_section_body(body)
    repeater.set_section_footer = '\n'
    
    # repeater.set_footer('')
    
    
    repeater.build_text()
    
    # print('repeater.get_format_options()\n',repeater.get_format_options())
    # print('repeater.get_header()\n',repeater.get_header())
    # print('repeater.get_section_header()\n',repeater.get_section_header())
    # print('repeater.get_section_body()\n',repeater.get_section_body())
    # print('repeater.get_section_footer()\n',repeater.get_section_footer())
    # print('repeater.get_footer()\n',repeater.get_footer())
    # print('repeater.get_text()\n',repeater.get_text())
    
    repeater.to_file('test.txt')