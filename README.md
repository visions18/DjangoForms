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
<div>
 <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Submit">
 </form> 
</div>

Django renders it like this:

![django](https://user-images.githubusercontent.com/82320729/116766408-00a34780-aa48-11eb-98d7-d8401bbda9e7.PNG") 

Demonstration:
We will manually render the form below and add CSS in it:

![django](https://user-images.githubusercontent.com/82320729/116766308-69d68b00-aa47-11eb-8d69-71df68dfd94e.PNG")

