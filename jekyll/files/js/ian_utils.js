function igbOpenWindow(winURL,winName,features) {
	var newWindow = window.open(winURL,winName,features);
	newWindow.focus();
}

function igbswapImage(id, imgsrc) {
  if (document.getElementById)
  {   document.getElementById(id).setAttribute('src', imgsrc);
  }
}