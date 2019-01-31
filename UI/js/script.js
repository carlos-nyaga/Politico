function openTab(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tabulinks");
  for (i = 0; i < tabcontent.length; i++) {
      tablinks[i].classList.remove("active");
  }

  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.classList.add("active");
}    







var app = new function() {
    this.el = document.getElementById('countries');
    this.countries = ['Republicans', 'Democrats', 'Jubilee', 'NASA', 'Political Bash', 'The people', 'Power to you', 'We Go', 'Luxembourg'];
    this.Count = function(data) {
      var el   = document.getElementById('counter');
      var name = 'country';
      if (data) {
        if (data > 1) {
          name = 'parties';
        }
        el.innerHTML = data + ' ' + name ;
      } else {
        el.innerHTML = 'No ' + name;
      }
    };
    
    this.FetchAll = function() {
      var data = '';
      if (this.countries.length > 0) {
        for (i = 0; i < this.countries.length; i++) {
          data += '<tr>';
          data += '<td>' + this.countries[i] + '</td>';
          data += '<td><button onclick="app.Edit(' + i + ')">Edit</button></td>';
          data += '<td><button onclick="app.Delete(' + i + ')">Delete</button></td>';
          data += '</tr>';
        }
      }
      this.Count(this.countries.length);
      return this.el.innerHTML = data;
    };
    this.Add = function () {
      el = document.getElementById('add-name');
      // Get the value
      var country = el.value;
      if (country) {
        // Add the new value
        this.countries.push(country.trim());
        // Reset input value
        el.value = '';
        // Dislay the new list
        this.FetchAll();
      }
    };
    this.Edit = function (item) {
      var el = document.getElementById('edit-name');
      // Display value in the field
      el.value = this.countries[item];
      // Display fields
      document.getElementById('spoiler').style.display = 'block';
      self = this;
      document.getElementById('saveEdit').onsubmit = function() {
        // Get value
        var country = el.value;
        if (country) {
          // Edit value
          self.countries.splice(item, 1, country.trim());
          // Display the new list
          self.FetchAll();
          // Hide fields
          CloseInput();
        }
      }
    };
    this.Delete = function (item) {
      // Delete the current row
      this.countries.splice(item, 1);
      // Display the new list
      this.FetchAll();
    };
    
  }
  app.FetchAll();
  function CloseInput() {
    document.getElementById('spoiler').style.display = 'none';
  }