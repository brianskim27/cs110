class StringUtility:
    def __init__(self, string):
        """
        Initialize the variable that will be used (string). 
        args: string (str) An inputted string via the parameter string.
        return: None
        """
        self.string = string

    def __str__(self):
        """
        Creates a copy of the original inputted string and returns it.
        args: str_string (str) A copy of the original inputted string, self.string.
        return: str_string (str) The copy of the original inputted string, self.string.
        """
        str_string = self.string
        return str_string

    def vowels(self):
        """
        Counts the number of vowels in the inputted string.
        args: string_vowels (str) A copy of the original inputted string, self.string.
        vowels (str) All the vowels, both lowercase and uppercase, set in one variable.
        count (int) Variable that keeps track of the number of vowels in string_vowels (str).
        return: str(count) (str) The number of vowels in the string, 'many' if greater than 4.
        """
        string_vowels = self.string
        vowels = "aeiouAEIOU"
        count = 0
        
        for ch in string_vowels:
            if ch in vowels:
                count += 1
        
        if count > 4:
            count = 'many'

        return str(count)

    def bothEnds(self):
        """
        Creates a new string with the first 2 and last 2 characters of the original inputted string, self.string.
        args: string_bothEnds (str) A copy of the original inputted string, self.string.
        count (int) Variable that keeps track of the number of iterations.
        newString_bothEnds (str) String that will contain the first 2 and last 2 characters of the original inputted string, self.string.
        return: newString_bothEnds (str) The first 2 and last 2 characters of the copy of the original inputted string, self.string.
        """
        string_bothEnds = self.string
        count = 0

        if len(string_bothEnds) <= 2:
            newString_bothEnds = ""
        
        else:
            for ch in string_bothEnds:
                count += 1
                newString_bothEnds = string_bothEnds[0:2] + string_bothEnds[count - 2:count]
        
        return newString_bothEnds

    def fixStart(self):
        """
        Replaces repeated characters of the first character in the original inputted string, self.string, with "*", excluding the first character itself.
        args: string_fixStart (str) Copy of the original inputted string, self.string.
        return: string_fixStart (str) The new copy of the original inputted string, self.string, that has repeated characters of the first character in the string replaced as "*" (excluding the first character itself).
        """
        string_fixStart = self.string
        
        if len(self.string) <= 1:
            return self.string
        
        else:
            string_fixStart = string_fixStart[0] + string_fixStart[1:].replace(string_fixStart[0], "*")
        
        return string_fixStart

    def asciiSum(self):
        """
        Adds all the ASCII values of the characters in the original inputted string, self.string.
        args: string_asciiSum (str) A copy of the original inputted string, self.string.
        sum (int) The accumulated value of the ASCII values of the characters in the copy of the original inputted string, self.string.
        return: sum (int) The integer sum of all the ASCII values in the copy of the original inputted string, self.string.
        """
        string_asciiSum = self.string
        sum = 0

        for ch in string_asciiSum:
            sum += ord(ch)

        return sum

    def cipher(self):
        """
        Increments all letters in the original inputted string, self.string, by the length of the string.
        args: length (int) The length of the original inputted string, self.string. 
        string_cipher (str) The new encoded string with the incremented letters.
        cipher (int) Calculates the new ASCII value for ch, including case sensitivity.
        return: str(string_cipher) (str) The new encoded string with the incremented letters from the original inputted string, self.string.
        """
        string_cipher = ""

        for ch in self.string:     
            if ord(ch) > 64 and ord(ch) < 91:
                cipher = (ord(ch) - 65 + len(self.string)) % 26
                string_cipher += chr(cipher + 65)
            
            elif ord(ch) > 96 and ord(ch) < 123:
                cipher = (ord(ch) - 97 + len(self.string)) % 26
                string_cipher += chr(cipher + 97)

            else:
                string_cipher += ch
        
        return str(string_cipher)

