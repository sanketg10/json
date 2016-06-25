$(document).ready(function() { 

  $.getJSON('data.json',function(info) { 
    var output = ''; 

    for (var i=0; i < info.links.length; i++) { 
      for(key in info.links[i]) { 
          if (info.links[i].hasOwnProperty(key)) { 
              output +='<li>'+'<a href ="' + info.links[i][key] + 
              '">' + key + '</a>' + 
              '</li>'; 
            } //hasOwnProperty check
          } // for each object
    }// for each array element

    var update = document.getElementById('links'); 
    update.innerHTML = output; 

  }); 

}); 

