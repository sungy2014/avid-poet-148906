import webapp2
form = """
<form>
    <label> Month
    <input type="text" name="year">
</form>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(form)
        
    def post(selt):
        user_month = valid_month(self.response.get('month'))

# class TestHandler(webapp2.RequestHandler):
#     def get(self):
#         q = self.request.get("q")
#         self.response.out.write(q)
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testform', TestHandler)],
                              debug=True)
