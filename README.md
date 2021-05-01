# DjangoForms
## How to manually render forms in Django

Let us first know how Django actually renders forms.

Django handles three distinct parts of the work involved in forms:
* Preparing and restructuring data to make it ready for rendering
* Creating HTML forms for the data
* Receiving and processing submitted forms and data from the client


*Django can take care of it all for you*

### Form rendering options: 

**{{ form.as_table }}** will render field as table cells wrapped in < tr > tags
  
**{{ form.as_p }}** will render fields wrapped in < p > tags
  
**{{ form.as_ul }}** will render fields wrapped in < li > tags
  
Here where we are using {{ form.as_p }} to render a form:
```html
<div>
 <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
 </form> 
</div>
```
Django renders it like this:

<img src="images/form.PNG" width="300" height="300" border="4">

Not so beautiful right! So let's see how we can beautify it with CSS.

Demonstration:
We will manually render the form below and add CSS in it:

<img src="images/Capture.PNG" width="400" height="300" border="4">

Here are the steps:
1. Created a Django project, myproject
2. Created an app, main
3. Connected the templates folder and added form.html
4. Connected static folder and added style.css to it
5. added a view for form.html
6. connected the the template to view via url

