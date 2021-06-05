<!DOCTYPE html>
<html>
<head>
     <title></title>
</head>
      <p id="output">Default text</p>
      <input id="user_number">
      <button onclick="update_user()">submit</button>
      <script type="text/javascript">
          function update_user(){
              user_number = document.getElementById("user_number").value;
              httpRequest = new XMLHttpRequest();
              httpRequest.open("Get,"https://reqres.in/api/users/"+user_number);
              httpRequest.send();
              httpRequest.onreadystatechange = function(){
                   if(this.readystate == 4 && this.status ===200)
                        {
                       user_data = JSON.parse(this.responseText);
                       document.getElementById("output").innerHTML = user_data.data.first_name;
                     }
                    }
                   }
         </script>
 </body>