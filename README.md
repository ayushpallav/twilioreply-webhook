# twilioreply-webhook
This webhook gets triggered when a reply is received by twilio <br> 
<h4> clone the repository </h4> <br> 
<b> cd twilioreply-webhook </b><br>
<h4> Make required adjustments in settings.py for applied hosts </h4><br>
vim app/views.py <br>
<h4> Enter the URL for the workflow </h4><br>
<b> python manage.py runserver </b><br>
After the API is running : <br>
<ol>
  <li> Open twilio phone numbers console </li>
  <li> Under Messaging, select webhook and enter the URL <b>http://{base_url}/app/webhook</b></li>
</ol>
  
