function validateForm() {
    var x = document.forms["myForm"]["f_name"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
    }
  } 