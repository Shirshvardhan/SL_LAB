window.onload = function() {
  var authors = [
  {
      name: "John",
      country: "USA",
      story: "The Lost World",
      year: "1999"
    },
    {
      name: "Green",
      country: "Australia",
      story: "Fault in our Stars",
      year: "2010"
    },
    {
      name: "Paulo",
      country: "USA",
      story: "Alchemist",
      year: "1999"
    },
    {
      name: "Khalid",
      country: "Afghanistan",
      story: "The Kite Runner",
      year: "2005"
    }];

    authors.forEach(function(item,index) {
      if(index<2)
      {
        listelement = document.createElement("tr");
        la = document.createElement("td");
        la.innerHTML = item.name;
        listelement.appendChild(la);

        la = document.createElement("td");
        la.innerHTML = item.country;
        listelement.appendChild(la);
      
        la = document.createElement("td");
        la.innerHTML = item.story;
        listelement.appendChild(la);
      
        la = document.createElement("td");
        la.innerHTML = item.year;
        listelement.appendChild(la);
        document.getElementById("menu").appendChild(listelement);
      
      }


      else {
        ab = document.createElement("div")
        ab.innerHTML = item.name + "  " + item.country + "  " + item.story + "  " + item.year;
        document.getElementById('d').appendChild(ab);
      }
    })
}