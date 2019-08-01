# twilioreply-webhook
This webhook gets triggered when a reply is received by twilio <br> 
clone the repository <br> <b> cd twilioreply-webhook </b><br>
Make required adjustments in settings.py for applied hosts <br>
<b> python manage.py runserver </b>
After the API is running : <br>
<ol>
  <li> Open twilio phone numbers console </li>
  <li> Under Messaging, select webhook and enter the URL <b>http://{base_url}/app/webhook</b></li>
</ol>
  
