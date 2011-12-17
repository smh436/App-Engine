
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext.db import djangoforms 

import surveyDB
import cgitb
cgitb.enable()

class SurveyForm(djangoforms.ModelForm):                                     
    class Meta:                                                                
        model = surveyDB.FrontPage
        exclude = ['choice','which_user','submit','results', 'q1a1X', 'q1a2X', 'q1a3X' \
                  , 'q2a1X', 'q2a2X', 'q2a3X', 'q3a1X', 'q3a2X', 'q3a3X']

class SurveyInputPage(webapp.RequestHandler):
    def get(self):

        html = template.render('templates/header.html', {})
        html = html + '<div id="wrapper">'
        html = html + template.render('templates/form_start.html', {'action':'/'})
        surveys = db.GqlQuery("SELECT * FROM FrontPage WHERE name != ''")
        html = html +  "<h3>Do you want to take one of these surveys?<br></h3>"

        for survey in surveys:
            x = survey.name
            x = x.replace(" ","_")
            html = html + "<INPUT TYPE=RADIO NAME='choice' VALUE=" + x + "> %s" %survey.name + "<br>"
            
        html = html +  "<h3>Or would you like to make your own survey?<br></h3>"
        html = html + str(SurveyForm(auto_id=False))
        html = html + template.render('templates/form_end.html', {'sub_title': 'Submit'})
        html = html + '</div>'
        html = html + template.render('templates/footer.html', {'links': ''})
        self.response.out.write(html)

    def post(self): 
        
        front_page = surveyDB.FrontPage()
        front_page.name = self.request.get('name')

        front_page.q1 = self.request.get('q1')
        front_page.q1a1 = self.request.get('q1a1')
        front_page.q1a2 = self.request.get('q1a2')
        front_page.q1a3 = self.request.get('q1a3')

        front_page.q2 = self.request.get('q2')
        front_page.q2a1 = self.request.get('q2a1')
        front_page.q2a2 = self.request.get('q2a2')
        front_page.q2a3 = self.request.get('q2a3')

        front_page.q3 = self.request.get('q3')
        front_page.q3a1 = self.request.get('q3a1')
        front_page.q3a2 = self.request.get('q3a2')
        front_page.q3a3 = self.request.get('q3a3')

        y = self.request.get('choice')
        front_page.choice = y
        front_page.which_user = users.get_current_user()
        front_page.put()

        #if the user chose a survey to take
        if y != '':   

            #get all of the surveys in the datastore
            surveys = db.GqlQuery("SELECT * FROM FrontPage WHERE name != ''")
        
            for survey in surveys:
                currentUser = users.get_current_user()
                userAnswered = db.GqlQuery("SELECT * FROM FrontPage WHERE which_user != ''")

                z = survey.name
                z = z.replace(" ","_")

                #take the survey that is chosen by the user
                if y == z:
                    html = template.render('templates/header.html', {})        
                    #html = html + template.render('templates/form_start.html', {'action':'/results'})
                    html = html + template.render('templates/form_start.html', {})
                    
                    #for answer in userAnswered:
                    #    html = html + str(answer.which_user) + " "
                    #    html = html + str(currentUser) + "<br>"
                        
                    #if str(answer.which_user) == str(currentUser):
                    #    html = html + "partyTime"
                    
                    if(survey.q1 != ''):
                        html = html + survey.q1 + "<br>"
                    
                    if(survey.q1a1 != ''):
                        survey.q1a1 = survey.q1a1.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q1a1 == survey.q1a1 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q1a1' VALUE=" + survey.q1a1 + " DISABLED> %s" %survey.q1a1 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q1a1' VALUE=" + survey.q1a1 + "> %s" %survey.q1a1 + "<br>"   

                    if(survey.q1a2 != ''):
                        survey.q1a2 = survey.q1a2.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q1a2 == survey.q1a2 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q1a2' VALUE=" + survey.q1a2 + " DISABLED> %s" %survey.q1a2 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q1a2' VALUE=" + survey.q1a2 + "> %s" %survey.q1a2 + "<br>"   
                
                    if(survey.q1a3 != ''):
                        survey.q1a3 = survey.q1a3.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q1a3 == survey.q1a3 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q1a3' VALUE=" + survey.q1a3 + " DISABLED> %s" %survey.q1a3 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q1a3' VALUE=" + survey.q1a3 + "> %s" %survey.q1a3 + "<br>"   

                    if(survey.q2 != ''):
                        html = html + survey.q2 + "<br>"

                    if(survey.q2a1 != ''):
                        survey.q2a1 = survey.q2a1.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q2a1 == survey.q2a1 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q2a1' VALUE=" + survey.q2a1 + " DISABLED> %s" %survey.q2a1 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q2a1' VALUE=" + survey.q2a1 + "> %s" %survey.q2a1 + "<br>"   
                    
                    if(survey.q2a2 != ''):                        
                        survey.q2a2 = survey.q2a2.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q2a2 == survey.q2a2 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q2a2' VALUE=" + survey.q2a2 + " DISABLED> %s" %survey.q2a2 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q2a2' VALUE=" + survey.q2a2 + "> %s" %survey.q2a2 + "<br>"   

                    if(survey.q2a3 != ''):
                        survey.q2a3 = survey.q2a3.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q2a3 == survey.q2a3 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q2a3' VALUE=" + survey.q2a3 + " DISABLED> %s" %survey.q2a3 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q2a3' VALUE=" + survey.q2a3 + "> %s" %survey.q2a3 + "<br>"   

                    if(survey.q3 != ''):
                        html = html + survey.q3 + "<br>"

                    if(survey.q3a1 != ''):
                        survey.q3a1 = survey.q3a1.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q3a1 == survey.q3a1 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q3a1' VALUE=" + survey.q3a1 + " DISABLED> %s" %survey.q3a1 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q3a1' VALUE=" + survey.q3a1 + "> %s" %survey.q3a1 + "<br>"   

                    if(survey.q3a2 != ''):
                        survey.q3a2 = survey.q3a2.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q3a2 == survey.q3a2 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q3a2' VALUE=" + survey.q3a2 + " DISABLED> %s" %survey.q3a2 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q3a2' VALUE=" + survey.q3a2 + "> %s" %survey.q3a2 + "<br>"   

                    if(survey.q3a3 != ''):
                        survey.q3a3 = survey.q3a3.replace(" ","_")

                        #disable
                        disabled = 0
                        for answer in userAnswered:
                            if(str(answer.which_user) == str(currentUser) and answer.q3a3 == survey.q3a3 and answer.name == '' and answer.choice == '' ):
                                html = html + "<INPUT TYPE=checkbox NAME='q3a3' VALUE=" + survey.q3a3 + " DISABLED> %s" %survey.q3a3 + "<br>"
                                disabled = 1
                        #enable
                        if disabled == 0:
                            html = html + "<INPUT TYPE=checkbox NAME='q3a3' VALUE=" + survey.q3a3 + "> %s" %survey.q3a3 + "<br>"   

                    html = html + template.render('templates/form_pre_end.html', {'name': 'Submit','sub_title': 'Submit'})
                    html = html + template.render('templates/form_end.html', {'name': 'Submit', 'sub_title': 'Results'})

                    html = html + template.render('templates/footer.html',{'links': 'Enter <a href="/">another</a>'})
                    self.response.out.write(html)
                    
        #the user chose to enter a new survey
        else:
            html = template.render('templates/header.html', {})        
            html = html + template.render('templates/footer.html',{'links': 'Enter <a href="/results">results</a>.'})            
            self.response.out.write(html)


class Counter(object):
    def __init__(self, name=None):
        self.name = name
        self.q1a1 = 0
        self.q1a2 = 0
        self.q1a3 = 0
        self.q2a1 = 0
        self.q2a2 = 0
        self.q2a3 = 0
        self.q3a1 = 0
        self.q3a2 = 0
        self.q3a3 = 0

 
class ResultsPage(webapp.RequestHandler):
    def get(self):
        surveys = db.GqlQuery("SELECT * FROM FrontPage WHERE name != ''")        
        responses = db.GqlQuery("SELECT * FROM FrontPage WHERE name = '' AND choice = ''")
        #html = template.render('templates/header.html', {})
        html = """
<html>
<head>
<title></title>
<link type="text/css" rel="stylesheet" href="/static/survey.css" />
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">

      // Load the Visualization API and the piechart package.
      google.load('visualization', '1.0', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Topping');
      data.addColumn('number', 'Slices');
      data.addRows([
        ['"""
        html = html + "Carrots"
        html = html + "', 3],['"
        html = html + "Candy"
        html = html + """', 1],
        ['Olives', 1],
        ['Zucchini', 1],
        ['Pepperoni', 2]
      ]);

      // Set chart options
      var options = {'title':'Results',
                     'width':400,
                     'height':300};

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
    </script>
</head>"""        

        html = html + "<body>"

        html = html + '<div id="chart_div"></div>'

        counterList = []

        for survey in surveys:

            counterList.append(Counter(survey.name))

            for response in responses:
                survey.q1a1 = survey.q1a1.replace(" ","_")
                response.q1a1 = response.q1a1.replace(" ","_")
                if survey.q1a1 == response.q1a1 and survey.q1a1 != '' and response.q1a1 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q1a1 = counter.q1a1 + 1

                survey.q1a2 = survey.q1a2.replace(" ","_")
                response.q1a2 = response.q1a2.replace(" ","_")
                if survey.q1a2 == response.q1a2 and survey.q1a2 != '' and response.q1a2 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q1a2 = counter.q1a2 + 1

                survey.q1a3 = survey.q1a3.replace(" ","_")
                response.q1a3 = response.q1a3.replace(" ","_")
                if survey.q1a3 == response.q1a3 and survey.q1a3 != '' and response.q1a3 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q1a3 = counter.q1a3 + 1

                survey.q2a1 = survey.q2a1.replace(" ","_")
                response.q2a1 = response.q2a1.replace(" ","_")
                if survey.q2a1 == response.q2a1 and survey.q2a1 != '' and response.q2a1 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q2a1 = counter.q2a1 + 1

                survey.q2a2 = survey.q2a2.replace(" ","_")
                response.q2a2 = response.q2a2.replace(" ","_")
                if survey.q2a2 == response.q2a2 and survey.q2a2 != '' and response.q2a2 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q2a2 = counter.q2a2 + 1

                survey.q2a3 = survey.q2a3.replace(" ","_")
                response.q2a3 = response.q2a3.replace(" ","_")
                if survey.q2a3 == response.q2a3 and survey.q2a3 != '' and response.q2a3 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q2a3 = counter.q2a3 + 1

                survey.q3a1 = survey.q3a1.replace(" ","_")
                response.q3a1 = response.q3a1.replace(" ","_")
                if survey.q3a1 == response.q3a1 and survey.q3a1 != '' and response.q3a1 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q3a1 = counter.q3a1 + 1

                survey.q3a2 = survey.q3a2.replace(" ","_")
                response.q3a2 = response.q3a2.replace(" ","_")
                if survey.q3a2 == response.q3a2 and survey.q3a2 != '' and response.q3a2 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q3a2 = counter.q3a2 + 1

                survey.q3a3 = survey.q3a3.replace(" ","_")
                response.q3a3 = response.q3a3.replace(" ","_")
                if survey.q3a3 == response.q3a3 and survey.q3a3 != '' and response.q3a3 != '' :
                    for counter in counterList:
                        if counter.name == survey.name:
                            counter.q3a3 = counter.q3a3 + 1

        for survey in surveys:
 
            if (survey.q1a1 != '') or (survey.q1a2 != '') or (survey.q1a3 != '') \
            or (survey.q2a1 != '') or (survey.q2a2 != '') or (survey.q2a3 != '') \
            or (survey.q3a1 != '') or (survey.q3a2 != '') or (survey.q3a3 != '') :
                html = html + survey.name + "<br>"

            if (survey.q1a1 != '') or (survey.q1a2 != '') or (survey.q1a3 != ''):
                html = html + survey.q1 + "<br>"

            if (survey.q1a1 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q1a1 + " " + str(counter.q1a1) + "<br>"

            if (survey.q1a2 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q1a2 + " " + str(counter.q1a2) + "<br>"

            if (survey.q1a3 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q1a3 + " " + str(counter.q1a3) + "<br>"

            if (survey.q2a1 != '') or (survey.q2a2 != '') or (survey.q2a3 != ''):
                html = html + survey.q2 + "<br>"

            if (survey.q2a1 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q2a1 + " " + str(counter.q2a1) + "<br>"

            if (survey.q2a2 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q2a2 + " " + str(counter.q2a2) + "<br>"

            if (survey.q2a3 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q2a3 + " " + str(counter.q2a3) + "<br>"

            if (survey.q3a1 != '') or (survey.q3a2 != '') or (survey.q3a3 != ''):
                html = html + survey.q3 + "<br>"

            if (survey.q3a1 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q3a1 + " " + str(counter.q3a1) + "<br>"

            if (survey.q3a2 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q3a2 + " " + str(counter.q3a2) + "<br>"

            if (survey.q3a3 != ''):
                for counter in counterList:
                    if counter.name == survey.name:
                        html = html + survey.q3a3 + " " + str(counter.q3a3) + "<br>"

        #for counter in counterList:
        #html = html + counter.name

        html = html + "</body></html>"
        self.response.out.write(html)

app = webapp.WSGIApplication([('/', SurveyInputPage),('/results',ResultsPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
