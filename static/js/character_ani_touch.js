var num_of_character = $(".character").length;
var index_now;

$(document).ready(function(){
  finish = 0;
  $("body").on("click touchmove", function(e){
    triggerReactor(e);
  });
  $(".explain-container").on("click touchmove", function(e){
    $(this).css('display','none');
    $(".category").css('display','block');
  })
});

function triggerReactor(e){
  if (e.originalEvent.type == "touchmove"){
    e = e.originalEvent.changedTouches[0];
  }
  else {
    e = e.originalEvent;
  }
  var characters = $(".character");

  for (var i = 0; i < num_of_character; i++) {
    var left = characters[i].offsetLeft;
    var right = left + characters[i].offsetWidth;
    var top = characters[i].offsetTop;
    var bottom = top + characters[i].offsetHeight;
    if (e.clientX > left && e.clientX < right && e.clientY > top && e.clientY < bottom && index_now !== i) {
      index_now = i;
      $("#big_font").text(characters[i].id);
      $("#category").text(characters[i].getAttribute('category'));
      characters.css("color","#000000");
      $(".character:eq("+i+")").css("color","#ff0000");
      if (i == num_of_character - 1){
        if (finish == 1){
          window.location.replace("/audio_clip");
          break;
        }
        $(".explain-container").css('display','block');
        finish = 1;
      }
      window.navigator.vibrate([10]);
    }
  }
}
