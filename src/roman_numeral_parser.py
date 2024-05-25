class parser:
    alphabet : dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    valid : bool = True

    def __init__(self, input : str):
        self.input = input
        self.parsed_input = []
        self.translation = []

    def go(self):
        self.format()
        self.parse()
        self.grammar_check()
        self.translate()

    def reset(self):
        parser.valid = True
        self.parsed_input = []
        self.translation = []

    def format(self):
        self.input = self.input.strip()
        self.input = self.input.upper()
        self.input = self.input.replace(',', ' ')
        self.input = self.input.replace('.', ' ')
        self.input = self.input.replace(':', ' ')
        self.input = self.input.replace(';', ' ')

    def parse(self):
        self.parsed_input = self.input.split()
    
    def translate(self):
        for element in self.parsed_input:
            # Convert to Hindu-Arabic numerals
            hindu_arabic_numeral = self.numeral_math(element)
            self.translation += [str(hindu_arabic_numeral)]
            
    def numeral_math(self, numeral : str):
        result = 0
        n = 0
        while n < len(numeral):
            if n == len(numeral) - 1:
                result += parser.alphabet[numeral[n]]
                break
            # If all numerals cascade to lesser values e.g. LXXVIII = 78
            # Just keep looking to the next value and add them all together
            # if the values are not in decending order we must do subtraction
            # E.g. XLIV = 44; XL -> 50-10 : IV -> 5-1
            # Perform the operation from left to right adding the next value in the string to the previous sum
            # Along the way we must compare the following value (i.e. i+1) to see if it is greater than the current value
            if parser.alphabet[numeral[n+1]] > parser.alphabet[numeral[n]]:
                result += parser.alphabet[numeral[n+1]] - parser.alphabet[numeral[n]]
                n += 2
                continue
            if parser.alphabet[numeral[n+1]] <= parser.alphabet[numeral[n]]:
                result += parser.alphabet[numeral[n]]
            n += 1
        return result
    
    def grammar_check(self):
        for element in self.parsed_input:
            n = 0
            error = 0
            while n < len(element) - 1:
                # Illegal to have more than three of the same numerals in a row
                if element[n] == element[n+1]:
                    error += 1
                else:
                    error = 0
                if error > 2:
                    parser.valid = False
                    break
                n += 1
            # if parser.valid == False:
            #     raise Exception(f"Invalid Roman Numeral : {element}")
            