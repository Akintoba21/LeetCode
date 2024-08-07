class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        if num < 20: return d[num]
        if num < 100:
            if num % 10 == 0: return d[num] 
            return d[(num // 10) * 10] + " " + d[num%10]
        if num < 1000: 
            if num % 100 == 0: return d[num / 100] + " Hundred"
            return d[num // 100] + " Hundred " + self.numberToWords(num%100)
        if num < 1000000: 
            if num % 1000 == 0: return self.numberToWords(num / 1000) + " Thousand"
            return self.numberToWords(num // 1000) + " Thousand " + self.numberToWords(num%1000)
        if num < 1000000000: 
            if num % 1000000 == 0: return self.numberToWords(num / 1000000) + " Million"
            return  self.numberToWords(num // 1000000) + " Million " + self.numberToWords(num % 1000000)
        if num < 1000000000000: 
            if num % 1000000000 == 0: return self.numberToWords(num / 1000000000) + " Billion"
            return self.numberToWords(num // 1000000000) + " Billion " + self.numberToWords(num % 1000000000)