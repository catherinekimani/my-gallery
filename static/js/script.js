function myFunction() {
  var copyText = document.getElementById("image_link");

  copyText.select();
  copyText.setSelectionRange(0, 99999);

  navigator.clipboard.writeText(copyText.value);
  
  /* Alert the copied link */
  alert("Copied the link: " + copyText.value);
}