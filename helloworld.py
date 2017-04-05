import webapp2
form = """
<form>
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

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
        
    def post(self):
        user_month = valid_month(self.response.get('month'))
        
        
    def valid_month(month):
        if month:
            short_month = month[:3].lower()
            return month_abbvs.get(short_month)
    
    def valid_day(day):
        if day.isdigit():
            int_day = int(day)
            if int_day >0 and int_day <= 31:
                return int_day
    
    def valid_year(year):
        if year.isdigit():
            int_year = int(year)
            if int_year >= 1900 and int_year <= 2020:
                return int_year  
    

# class TestHandler(webapp2.RequestHandler):
#     def get(self):
#         q = self.request.get("q")
#         self.response.out.write(q)
app = webapp2.WSGIApplication([('/', MainPage),
                               ],
                              debug=True)
