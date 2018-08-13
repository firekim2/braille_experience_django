var _t = 0;
$(window).scroll(function() {
  var _n = $(window).scrollTop();
  if (_n > _t + 20 && _n > 0) {
    $("#header").fadeOut(100);
    _t = _n;
  } else if (_n < _t - 20) {
    $("#header").fadeIn(100);
    _t = _n;
  }

});
