import webapp2
form = """
<form method="post">
    <label> Month
    <input type="text" name="month">
    </label>
    <label> Day
    <input type="text" name="day">
    </label>
    <label> Year
    <input type="text" name="year">
    </label>
    
    <br>
    <br>
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def valid_month(self, month):
        months = ['January',
                  'February',
                  'March',
                  'April',
                  'May',
                  'June',
                  'July',
                  'August',
                  'September',
                  'October',
                  'November',
                  'December']

        month_abbvs = dict((m[:3].lower(), m) for m in months)
        if month:
            short_month = month[:3].lower()
            return month_abbvs.get(short_month)

    def valid_day(self, day):
        if day.isdigit():
            int_day = int(day)
            if int_day >0 and int_day <= 31:
                return int_day
    
    def valid_year(self, year):
        if year.isdigit():
            int_year = int(year)
            if int_year >= 1900 and int_year <= 2020:
                return int_year  

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
        
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))
        
        if not (user_month and user_day and user_year):
            self.response.out.write(user_month, user_day, user_year)
        else:
            self.response.out.write("Thanks! That's a totally valid day!")
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug=True)
