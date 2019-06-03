function myFunctionCopy() {

  /* Get the text field */
  var copyText = document.getElementById("myShortUrl");

  /* Select the text field */
  copyText.select();

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Change the text inside <h3> */
  document.getElementById("x").innerHTML = "Copied";
}
