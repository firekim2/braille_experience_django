var num_of_character = $(".character").length;

$(document).ready(function(){
  reactor();
});

function reactor(){
    var length = $(".character").length;
    $(".character").each(function(index, element){
      $(this).mouseenter(function(){
        $("#big_font").text(this.id);
        $(".glass").css('left',this.offsetLeft + 15 + 'px');
        $(".glass").css('top',this.offsetTop + 15 + 'px');
        if(index == length - 1){
          window.location.replace("/audio_clip");
        }
      });
    });
}
