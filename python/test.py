from TextRepeater import TextRepeater

## Test 1: Plain Text ##
print('Test 1: Plain Text')

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

repeater.to_file('Test1.txt')
print('-'*80)

## Test 2: Transact-SQL ##
print('Test 2: Transact-SQL')

repeater = TextRepeater()

format_options= [
     ('dbo.[tbl_Person]', 'full_name')
    ,('dbo.[tbl_Book]'  , 'author_name')
    ,('dbo.[tbl_Song]'  , 'artist_name')
]
header = "PRINT CONCAT(GETDATE(), '  START');" + '\n'+'-'*80
section_header = "\nPRINT CONCAT(GETDATE(), '  BEGIN UPDATING {0}');\nGO\n"
section_body = """UPDATE {0}
SET [{1}] = UPPER([{1}]);"""
section_footer = "\nPRINT CONCAT(GETDATE(), '  FINISHED UPDATING {0}');\nGO\n"
footer = '-'*80+'\n' + "PRINT CONCAT(GETDATE(), '  END');\nGO\n"
indentation = 2
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

repeater.to_file('Test2.sql')
print('-'*80)